#!/bin/bash

# Generate long flows
declare -a workload=("sparksql" "graphlab" "memcached" "hadoop" "spark")
for dir in "${workload[@]}"; do
    mkdir -p "$dir"
done
bandwidth=100
load=0.4
for workload in "${workload[@]}"; do
    echo "python3 config_traces.py ${workload} ${bandwidth} ${load}"
    python3 config_traces.py ${workload} ${bandwidth} ${load}
    fname="${workload}-${bandwidth}G-${load}.csv"
    echo "../simulator 2 ${workload}/conf-trace-${bandwidth}G-${load}.txt > ${fname}"
    ../simulator 2 ${workload}/conf-trace-${bandwidth}G-${load}.txt > ${workload}/${fname}
    echo "python3 preprocess.py -b ${bandwidth} -fi  ${workload}/${fname} 
                                                -fo ${workload}/proced_${fname}"
    python3 preprocess.py -b ${bandwidth} -fi  ${workload}/${fname} \
                                                -fo ${workload}/proced_${fname}
done

# Generate short flows
mkdir -p "shortflow"
workload="shortflow"
declare -a loadMap=( ["4"]="0.2" ["9"]="0.4" ["13"]="0.6" ["18"]="0.8" ["19"]="0.9" )
for load in 4 9 13 18 19; do #8blk=512bit 
    echo "python3 config_traces.py ${workload} ${bandwidth} ${load}"
    python3 config_traces.py ${workload} ${bandwidth} ${load}
    fname="${workload}-${bandwidth}G-${loadMap[$load]}.csv"
    echo "../simulator 2 ${workload}/conf-trace-${bandwidth}G-${loadMap[$load]}.txt > ${workload}/${fname}"
    ../simulator 2 ${workload}/conf-trace-${bandwidth}G-${load}.txt >${workload}/${fname}
    
    # Gen WREQ
    echo "python3 preprocess.py -b ${bandwidth} -ratio 1 -fi  ${workload}/${fname} 
                                                -fo ${workload}/wonly_${fname}"
    python3 preprocess.py -b ${bandwidth} -ratio 1 -fi  ${workload}/${fname} \
                                                -fo ${workload}/wonly_${fname}
    # Gen RREQ
    echo "python3 preprocess.py -b ${bandwidth} -ratio 0 -fi  ${workload}/${fname} 
                                                -fo ${workload}/ronly_${fname}"
    python3 preprocess.py -b ${bandwidth} -ratio 0 -fi  ${workload}/${fname} \
                                                -fo ${workload}/ronly_${fname}
    # Gen 0.8-mixed
    if [[ ${load} == 18 ]]; then
        for rate in 0.2 0.5 0.8; do
            echo "python3 preprocess.py -b ${bandwidth} -ratio ${rate} -fi  ${workload}/${fname} 
                                                -fo ${workload}/mix${rate}_${fname}"
            python3 preprocess.py -b ${bandwidth} -ratio ${rate} -fi  ${workload}/${fname} \
                                                -fo ${workload}/mix${rate}_${fname}
        done
    fi
done
# 1460/8 =182.5
# 182.5*0.8 = 146
# 109.5~110 for 0.6
# 90～0.5
# 82～0.45
# 73~0.4
# 55~0.3
# 36~0.2
# 18~0.1
# 9~0.05
# 5~0.027 ~ 1/34
# 2~0.01
# 1~0.005
