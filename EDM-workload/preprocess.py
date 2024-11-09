# Process raw trace file:
# Map 512 to 64 nodes
# Give each flow a memType based on -ism
# Randomly pick flows as RREQ or WREQ
# Generate RREQ based on RRESP.

import os
import random
import sys
import re
import argparse
import math
import pandas as pd


def assignFlowType(wr_rate, seed):
    thres = wr_rate*10.01
    if seed >= thres:
        return 1  # RREQ
    else:
        return 3  # WREQ


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fi', required=True)
    parser.add_argument('-b', required=True)  # bandwidth in Gbps
    parser.add_argument('-c', default=8)  # packet size, in bytes
    parser.add_argument('-ratio', default=0.5)  # ratio == wreq/ all
    parser.add_argument('-fo', required=True)
    parser.add_argument('-short', action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    slot_time = (float(args.c) * 8.0) / float(args.b) * 1e-9
    filename = args.fi
    newfilename = args.fo
    isShort = args.short
    wr_rate = float(args.ratio)

    trace = pd.read_csv(filename, header=None, dtype=str)

    # Change second to timeslot_num
    timeslots = []
    start_time_arr = trace.iloc[:, -1].values
    for time in start_time_arr:
        slot = (int)(float(time)/slot_time)
        timeslots.append(str(slot))
    trace.iloc[:, -1] = pd.Series(timeslots)

    # Add flowType
    flowSize = trace.iloc[:, 3].values.copy()
    old_flowSize = trace.iloc[:, 3].values.copy()
    flowType_arr = []
    for i in range(0, trace.shape[0]):
        seed = random.randint(0, 10)
        # 1 is RREQ, 2 is RRES, 3 is WREQ
        flowType = assignFlowType(wr_rate, seed)
        if flowType == 1:  # RREQ
            flowSize[i] = 16
        elif isShort is True:  # this is short flow, change to 64B!
            flowSize[i] = 64
        flowType_arr.append(flowType)

    trace.iloc[:, 3] = pd.Series(flowSize)
    trace.insert(1, column=None, value=flowType_arr)

    # Add ReqLen
    reqLen_arr = []
    for i in range(0, len(flowType_arr)):
        if flowType_arr[i] == 1:
            # For long flow, just append old flow size
            if isShort is True:  # For short flow, fixed 64
                reqLen_arr.append(64)
            else:
                reqLen_arr.append(old_flowSize[i])
        else:
            reqLen_arr.append(-1)
    trace.insert(5, column=None, value=reqLen_arr)
    trace.to_csv(newfilename, header=False, index=False)


if __name__ == '__main__':
    main()
