#!/bin/bash

# Generate long flows
testdir="../../simulation/testdir"
mkdir -p "$testdir"
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
    cp ${workload}/proced_${fname} ${testdir}/proced_${fname}
done




# Generate short flows
mkdir -p "shortflow"
workload="shortflow"
declare -A loadMap=( ["3"]="0.2" ["7"]="0.4" ["12"]="0.6" ["19"]="0.8" ["21"]="0.9" )
for load in "${!loadMap[@]}"; do #8blk=512bit 
    echo "python3 config_traces.py ${workload} ${bandwidth} ${load}"
    python3 config_traces.py ${workload} ${bandwidth} ${load}
    fname="${workload}-${bandwidth}G-${loadMap[$load]}.csv"
    echo "../simulator 2 ${workload}/conf-trace-${bandwidth}G-${loadMap[$load]}.txt > ${workload}/${fname}"
    ../simulator 2 ${workload}/conf-trace-${bandwidth}G-${load}.txt >${workload}/${fname}
    
    # Gen WREQ
    echo "python3 preprocess.py -short -b ${bandwidth} -ratio 1 -fi  ${workload}/${fname} 
                                                -fo ${workload}/wonly_${fname}"
    python3 preprocess.py -short -b ${bandwidth} -ratio 1 -fi  ${workload}/${fname} \
                                                -fo ${workload}/wonly_${fname}
    cp ${workload}/wonly_${fname} ${testdir}/wonly_${fname}

    # Gen RREQ
    echo "python3 preprocess.py -short -b ${bandwidth} -ratio 0 -fi  ${workload}/${fname} 
                                                -fo ${workload}/ronly_${fname}"
    python3 preprocess.py -short -b ${bandwidth} -ratio 0 -fi  ${workload}/${fname} \
                                                -fo ${workload}/ronly_${fname}
    cp ${workload}/ronly_${fname} ${testdir}/ronly_${fname}

    # Gen 0.8-mixed
    if [[ ${load} == 19 ]]; then
        for rate in 0.2 0.5 0.8; do
            echo "python3 preprocess.py -short -b ${bandwidth} -ratio ${rate} -fi  ${workload}/${fname} 
                                                -fo ${workload}/mix_w${rate}_0.8.csv"
            python3 preprocess.py -short -b ${bandwidth} -ratio ${rate} -fi  ${workload}/${fname} \
                                                -fo ${workload}/mix_w${rate}_0.8.csv
            cp ${workload}/mix_w${rate}_0.8.csv ${testdir}/mix_w${rate}_0.8.csv
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
