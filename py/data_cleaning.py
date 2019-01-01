import sys
import numpy as np

dirname = sys.argv[1]

protocols = ['fastpass', 'pfabric', 'phost']
load_val = [20, 40, 60, 80]

slowdown_bins = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
slowdown_list = [[] for i in range(len(slowdown_bins)+1)]
slowdown_val = [0.0 for i in range(len(slowdown_bins)+1)]
slowdown_count = [0 for i in range(len(slowdown_bins)+1)]
slowdown_avg = [0.0 for i in range(len(slowdown_bins)+1)]

for protocol in protocols:
    for i in load_val:
        f = open(dirname+"/"+protocol+"-"+str(i)+".txt.out", "r")
        for line in f:
            tokens = line.split()
            if (tokens[0] != '##' and tokens[1] != 'Simulator'):
                flow_size = int(tokens[1])
                slowdown = float(tokens[8])
                for k in range(len(slowdown_bins)):
                    if (flow_size <= slowdown_bins[k]):
                        slowdown_list[k].append(slowdown)
                        slowdown_val[k] = slowdown_val[k] + slowdown
                        slowdown_count[k] = slowdown_count[k] + 1
                        break
                if (flow_size > slowdown_bins[len(slowdown_bins)-1]):
                    slowdown_val[len(slowdown_bins)] = slowdown_val[len(slowdown_bins)] + slowdown
                    slowdown_count[len(slowdown_bins)] = slowdown_count[len(slowdown_bins)] + 1
        f.close()

        out = open(dirname+"/"+protocol+"-"+str(i)+".txt.out.slowdown.mean", "w")
        for j in range(len(slowdown_val)):
            if slowdown_val[j] != 0:
                assert(slowdown_count[j] != 0)
                slowdown_avg[j] = slowdown_val[j] / slowdown_count[j]
                if j < len(slowdown_bins):
                    out.write(str(slowdown_bins[j])+","+str(slowdown_avg[j]))
                else:
                    out.write("infinity"+","+str(slowdown_avg[j]))
                out.write("\n")
        out.close()

        out = open(dirname+"/"+protocol+"-"+str(i)+".txt.out.slowdown.99", "w")
        for j in range(len(slowdown_list)):
            if len(slowdown_list[j]) != 0:
                if j < len(slowdown_bins):
                    out.write(str(slowdown_bins[j])+","+str(np.percentile(slowdown_list[j], 99)))
                else:
                    out.write("infinity"+","+str(np.percentile(slowdown_list[j], 99)))
                out.write("\n")
        out.close()
