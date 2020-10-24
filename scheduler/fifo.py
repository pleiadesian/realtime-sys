from scheduler.abstract_class import Scheduler
from scheduler.draw import drawResults

class FIFOScheduler(Scheduler):
    def schedule(self, workloads):
        seq = []
        # add an order number for each task
        tasks = zip(list(range(0, len(workloads))), workloads)
        # sort by start time
        tasks = sorted(tasks, key=lambda x: x[1][0])
        # maybe an idle before 1st task arrived
        begin_time = tasks[0][1][0]
        seq += begin_time * [-1]
        for i in range(0, len(tasks)):
            task_order, task = tasks[i][0], tasks[i][1]
            compute_time = task[2]
            seq += [task_order] * compute_time
        drawResults(seq, 'FIFO')
        return seq


