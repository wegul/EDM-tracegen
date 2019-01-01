#!/bin/bash

declare -a traffic=("all-to-all-144" "permutation-144")
declare -a workload=("aditya" "dctcp" "datamining")

for i in "${traffic[@]}"
do
    for j in "${workload[@]}"
    do
        echo "scp $i-$j/*.csv vishal@sonic22.cs.cornell.edu:~/NDP/sim/EXAMPLES/dynamic/$i-$j/"
        scp $i-$j/*.csv vishal@sonic22.cs.cornell.edu:~/NDP/sim/EXAMPLES/dynamic/$i-$j/
    done
done
