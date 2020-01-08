#!/bin/bash

declare -a workload=("aditya" "dctcp" "datamining")

for workload in "${workload[@]}"
do
    for bandwidth in 40 100 400
    do
        for load in 0.2 0.4 0.6 0.8
        do
            echo "python generate_trace_files.py ${workload} ${bandwidth} ${load}"
            python generate_trace_files.py ${workload} ${bandwidth} ${load}
            echo "../../simulator 2 all-to-all-144-${workload}/conf-trace-${bandwidth}G-${load}.txt > all-to-all-144-${workload}/trace-${bandwidth}G-${load}.csv"
            ../../simulator 2 all-to-all-144-${workload}/conf-trace-${bandwidth}G-${load}.txt > all-to-all-144-${workload}/trace-${bandwidth}G-${load}.csv
        done
    done
done
