import sys
import os

workload = sys.argv[1]
bandwidth = int(sys.argv[2])
load = sys.argv[3]

folder = "all-to-all-144-"+workload
f = open(folder+"/"+"conf-trace-"+str(bandwidth)+"G-"+load+".txt", "w")

f.write("init_cwnd: 6\n")
f.write("max_cwnd: 12\n")
f.write("retx_timeout: 45e-06\n")
f.write("queue_size: 36864\n")
f.write("propagation_delay: 0.0000002\n")
f.write("bandwidth: " + str(bandwidth*1000000000.0) + "\n")
f.write("queue_type: 2\n")
f.write("flow_type: 114\n")
f.write("num_flow: 1000000\n")
f.write("flow_trace: ./CDF_"+workload+".txt\n")
f.write("cut_through: 1\n")
f.write("mean_flow_size: 0\n")
f.write("load_balancing: 0\n")
f.write("preemptive_queue: 0\n")
f.write("big_switch: 0\n")
f.write("host_type: 14\n")
f.write("traffic_imbalance: 0\n")
f.write("load: "+load+"\n")
f.write("reauth_limit: 3\n")
f.write("magic_trans_slack: 1.1\n")
f.write("magic_delay_scheduling: 1\n")
f.write("use_flow_trace: 0\n")
f.write("smooth_cdf: 1\n")
f.write("burst_at_beginning: 0\n")
f.write("capability_timeout: 1.5\n")
f.write("capability_resend_timeout: 9\n")
f.write("capability_initial: 8\n")
f.write("capability_window: 8\n")
f.write("capability_window_timeout: 25\n")
f.write("ddc: 0\n")
f.write("ddc_cpu_ratio: 0.33\n")
f.write("ddc_mem_ratio: 0.33\n")
f.write("ddc_disk_ratio: 0.34\n")
f.write("ddc_normalize: 2\n")
f.write("ddc_type: 0\n")
f.write("deadline: 0\n")
f.write("schedule_by_deadline: 0\n")
f.write("avg_deadline: 0.0001\n")
f.write("capability_third_level: 1\n")
f.write("capability_fourth_level: 0\n")
f.write("magic_inflate: 1\n")
f.write("interarrival_cdf: none\n")
f.write("num_host_types: 13")

f.close()
