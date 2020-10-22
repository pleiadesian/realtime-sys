# Simulated Realtime System
## Usage
Scheduler should be implemented in scheduler directory, please look at `abstract_class.py` and `dummy.py` for reference.
```
# replace RHS with any scheduler implementations
scheduler = dummy.DummyScheduler()
```
Replace dummy scheduler with customized scheduler, then run `python main.py`, enter some workloads, e.g. [(0, 5, 2, 1), (0, 10, 3, 2), (0, 20, 1, 3)]
## Output
Output format is as follows:
```
input format: [(start time, deadline, computation time, priority),...]
warning: fallback to use [(1, 5, 2, 1), (2, 10, 5, 2), (3, 20, 10, 3)] as inputs
Workloads:
        [(0, 5, 2, 1), (0, 10, 3, 2), (0, 20, 1, 3)]
sched result:
        [0, 0, 1, 1, 1, 2]
Detailed performance:
        Workloads: 0
                Start time: 0
                Deadline: 5
                Computation time: 2
                Priority: 1
                Response time: 0
                Complete time: 2
                Expired: False
        Workloads: 1
                Start time: 0
                Deadline: 10
                Computation time: 3
                Priority: 2
                Response time: 2
                Complete time: 5
                Expired: True
        Workloads: 2
                Start time: 0
                Deadline: 20
                Computation time: 1
                Priority: 3
                Response time: 5
                Complete time: 6
                Expired: True
Total switches: 2
```