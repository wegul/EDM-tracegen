import sys

dirname = sys.argv[1]

#protocols = ['fastpass', 'pfabric', 'phost']
protocols = ['pfabric']
load_val = [20, 40, 60, 80]

utilization_val = [0.0 for i in range(len(load_val))]

for protocol in protocols:
    count = 0
    for i in load_val:
        f = open(dirname+"/"+protocol+"-"+str(i)+".txt.out", "r")
        for line in f:
            tokens = line.split()
            if (tokens[0] == '##'):
                started_pkts = float(tokens[9])
                outstanding_pkts = float(tokens[3])
                recvd_pkts = started_pkts - outstanding_pkts
                utilization_val[count] = (recvd_pkts / started_pkts)*100
                assert(utilization_val[count] <= 100.0)
        f.close()
        count += 1
    out = open(dirname+"/"+protocol+".utilization", "w")
    out.write("arch " + "0.2 " + "0.4 " + "0.6 " + "0.8")
    out.write("\n")
    out.write(str(protocol) + " ")
    for i in range(len(utilization_val)):
        out.write(str(utilization_val[i]) + " ")
    out.close()
