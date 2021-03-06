#!/bin/python3

from scheduler import draw
from scheduler import dummy
from scheduler import fifo
from scheduler import round_robin
from scheduler import fixed_priority
from scheduler import EDF

def process_input():
    inputs = []
    try:
        inputs = eval(input())
    except:
        pass
    if not isinstance(inputs, list) or len(inputs) == 0 or \
        not all([isinstance(i, tuple) and len(i) == 4 for i in inputs]):
        # inputs = [(1, 5, 2, 1), (2, 10, 5, 2), (3, 20, 10, 3)]
        inputs = [(5, 17, 5, 1), (4, 15, 10, 1), (7, 10, 1, 1)]
        print("input format: [(start time, deadline, computation time, priority),...]\n"
                "warning: fallback to use " + str(inputs) + " as inputs")
    else:
        print("inputs: " + str(inputs))
    return inputs

def perf(workloads, results):
    # response time, complete time, scheduled times
    # visualize scheduling and plot perf
    # for idx in results:
    #     workload = workloads[idx]
    #     response_time = 
    def rindex(l, v):
        return len(l) - l[-1::-1].index(v) - 1
    print("Workloads:")
    print("\t" + str(workloads))
    print("sched result:")
    print("\t" + str(results))
    print("Detailed performance:")
    for workload, i in zip(workloads, range(len(workloads))):
        response_time = rindex(results, i) + 1 - workload[0]
        complete_time = rindex(results, i) + 1
        expired = (rindex(results, i) + 1) > workload[1]
        print("\tWorkloads: " + str(i))
        print("\t\tStart time: " + str(workload[0]))
        print("\t\tDeadline: " + str(workload[1]))
        print("\t\tComputation time: " + str(workload[2]))
        print("\t\tPriority: " + str(workload[3]))
        print("\t\tResponse time: " + str(response_time))
        print("\t\tComplete time: " + str(complete_time))
        print("\t\tExpired: " + str(bool(expired)))
    sched_times = sum([r0 != r1 for r0, r1 in zip(results, results[1:])])
    print("Total switches: " + str(sched_times))

def main(scheduler, scheduler_name):
    workloads = process_input()
    results = scheduler.schedule(workloads)
    perf(workloads, results)
    draw.drawResults(results, workloads, scheduler_name)

# replace RHS with any scheduler implementations
scheduler = dummy.DummyScheduler()
scheduler = fifo.FIFOScheduler()
scheduler = round_robin.RoundRobinScheduler()
scheduler = fixed_priority.FixedPriorityScheduler()
scheduler = EDF.EDFScheduler()
main(scheduler, 'EDF')
