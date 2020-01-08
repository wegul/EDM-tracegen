import sys
import numpy as np

dirname = sys.argv[1]

#protocols = ['fastpass', 'pfabric', 'phost']
protocols = ['pfabric']
load_val = [20, 40, 60, 80]

for protocol in protocols:
    slowdown_all_val = 0.0
    slowdown_all_count = 0
    slowdown_all_list = []
    slowdown_bins = [10000, 100000, 1000000]
    #slowdown_bins = [100000, 5000000]
    slowdown_list = [[] for i in range(len(slowdown_bins)+1)]
    slowdown_val = [0.0 for i in range(len(slowdown_bins)+1)]
    slowdown_count = [0 for i in range(len(slowdown_bins)+1)]
    slowdown_avg = [0.0 for i in range(len(slowdown_bins)+1)]
    for i in load_val:
        f = open(dirname+"/"+protocol+"-"+str(i)+".txt.out", "r")
        for line in f:
            tokens = line.split()
            if (tokens[0] != '##' and tokens[1] != 'Simulator'):
                flow_size = int(tokens[1])
                slowdown = float(tokens[8])
                slowdown_all_val += slowdown
                slowdown_all_count += 1
                slowdown_all_list.append(slowdown)
                for k in range(len(slowdown_bins)):
                    if (flow_size <= slowdown_bins[k]):
                        slowdown_list[k].append(slowdown)
                        slowdown_val[k] = slowdown_val[k] + slowdown
                        slowdown_count[k] = slowdown_count[k] + 1
                        break
                if (flow_size > slowdown_bins[len(slowdown_bins)-1]):
                    slowdown_list[len(slowdown_bins)].append(slowdown)
                    slowdown_val[len(slowdown_bins)] = slowdown_val[len(slowdown_bins)] + slowdown
                    slowdown_count[len(slowdown_bins)] = slowdown_count[len(slowdown_bins)] + 1
        f.close()

        out = open(dirname+"/"+protocol+"-"+str(i)+".txt.out.slowdown.bin.mean", "w")
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

        out = open(dirname+"/"+protocol+"-"+str(i)+".txt.out.slowdown.bin.99", "w")
        for j in range(len(slowdown_list)):
            if len(slowdown_list[j]) != 0:
                slowdown_list[j].sort()
                if j < len(slowdown_bins):
                    out.write(str(slowdown_bins[j])+","+str(np.percentile(slowdown_list[j], 99)))
                else:
                    out.write("infinity"+","+str(np.percentile(slowdown_list[j], 99)))
                out.write("\n")
        out.close()

        out = open(dirname+"/"+protocol+"-"+str(i)+".txt.out.slowdown.all.mean", "w")
        mean_slowdown = slowdown_all_val / slowdown_all_count
        out.write(str(mean_slowdown))
        out.close()

        out = open(dirname+"/"+protocol+"-"+str(i)+".txt.out.slowdown.all.99", "w")
        slowdown_all_list.sort()
        p99_slowdown = np.percentile(slowdown_all_list, 99)
        out.write(str(p99_slowdown))
        out.close()
