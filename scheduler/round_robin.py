from scheduler.abstract_class import Scheduler
import math

class RoundRobinScheduler(Scheduler):
    def schedule(self, workloads):
        seq = []
        time_slice = 1
        # add an order number for each task
        tasks = zip(list(range(0, len(workloads))), workloads)
        # sort by start time
        tasks = sorted(tasks, key=lambda x: x[1][0])
        begin_time = tasks[0][1][0]
        seq += ([-1] * time_slice) * math.ceil(begin_time / time_slice)
        while len(tasks) != 0:
            # get the queue front
            task_order, task = tasks[0][0], tasks[0][1]
            start_time, deadline, compute_time, priority = task[0], task[1], task[2], task[3]
            # pop the queue
            tasks = tasks[1:]
            if compute_time < time_slice:
                seq += [task_order] * compute_time
                seq += [-1] * (time_slice - compute_time)
                compute_time = 0
            else:
                seq += [task_order] * time_slice
                compute_time -= time_slice
            if compute_time > 0:
                tasks.append((task_order, (start_time, deadline, compute_time, priority)))
        return seq
        
