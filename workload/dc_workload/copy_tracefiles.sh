#!/bin/bash

declare -a workload=("aditya" "dctcp" "datamining")

for workload in "${workload[@]}"
do
    cp all-to-all-144-${workload}/trace-* ~/NDP/sim/EXAMPLES/dynamic/workload/dc_workload/all-to-all-144-${workload}/
    cp all-to-all-144-${workload}/trace-* ~/ns-allinone-2.35/ns-2.35/workload/dc_workload/all-to-all-144-${workload}/
    scp all-to-all-144-${workload}/trace-* vishal@compute20.fractus.cs.cornell.edu:~/NDP/sim/EXAMPLES/dynamic/workload/dc_workload/all-to-all-144-${workload}/
    scp all-to-all-144-${workload}/trace-* vishal@sonic22.cs.cornell.edu:~/NDP/sim/EXAMPLES/dynamic/workload/dc_workload/all-to-all-144-${workload}/

    scp all-to-all-144-${workload}/trace-* vishal@compute20.fractus.cs.cornell.edu:~/pNet/simulation/workload/dc_workload/all-to-all-144-${workload}/
done
