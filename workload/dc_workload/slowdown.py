import sys

workload = sys.argv[1]
bandwidth = sys.argv[2]
delay = sys.argv[3]
load = sys.argv[4]
protocol = sys.argv[5]

folder = "workload/dc_workload/all-to-all-144-"+workload
inpfilename = protocol+"-"+bandwidth+"G-"+delay+"ns-"+load+".stats"
outfilename = protocol+"-"+bandwidth+"G-"+delay+"ns-"+load+".out"

f = open(folder+"/"+inpfilename, "r")

out = open(folder+"/"+outfilename, "w")
out.write("Flow ID,"+"Src,"+"Dst,"+"Flow Size(bytes),"+"Flow Completion Time(secs),"+"Slowdown,"+"Throughput(Gbps)")
out.write("\n")

for line in f:
    tokens = line.split()
    if (tokens[0] != '##'):
        flowid = int(tokens[0])
        src = int(tokens[2])
        dst = int(tokens[3])
        flowsize = int(tokens[1])
        fct = float(tokens[6])*1e-6
        slowdown = float(tokens[8])
        rate = (flowsize*8.0) / (fct*1e9)
        if (slowdown < 1.0):
            out.write("Problem,")
        out.write(str(flowid)+","+str(src)+","+str(dst)+","+str(flowsize)+","+str(fct)+","+str(slowdown)+","+str(rate)+"\n")
f.close()
out.close()
