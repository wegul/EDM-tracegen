#!/bin/bash

no_of_nodes=144
nodes_per_rack=16

declare -a workload=("aditya" "dctcp")
protocol="pfabric"

for workload in "${workload[@]}"
do
    for bandwidth in 40 100 400
    do
        for delay in 625.6 #propagation delay per hop (ns)
        do
            for load in 0.2 0.4 0.6 0.8
            do
                echo "python workload/dc_workload/generate_run_files.py ${workload} ${bandwidth} ${delay} ${load}"
                python workload/dc_workload/generate_run_files.py ${workload} ${bandwidth} ${delay} ${load}
                echo "./simulator 1 workload/dc_workload/all-to-all-144-${workload}/conf-run-${bandwidth}G-${delay}ns-${load}.txt > workload/dc_workload/all-to-all-144-${workload}/${protocol}-${bandwidth}G-${delay}ns-${load}.stats"
                ./simulator 1 workload/dc_workload/all-to-all-144-${workload}/conf-run-${bandwidth}G-${delay}ns-${load}.txt > workload/dc_workload/all-to-all-144-${workload}/${protocol}-${bandwidth}G-${delay}ns-${load}.stats
                echo "python workload/dc_workload/slowdown.py ${workload} ${bandwidth} ${delay} ${load} ${protocol}"
                python workload/dc_workload/slowdown.py ${workload} ${bandwidth} ${delay} ${load} ${protocol}
            done
        done
    done
done
