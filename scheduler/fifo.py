from scheduler.abstract_class import Scheduler

class FIFOScheduler(Scheduler):
    def schedule(self, workloads):
        seq = []
        # add an order number for each task
        tasks = zip(list(range(0, len(workloads))), workloads)
        # sort by start time
        tasks = sorted(tasks, key=lambda x: x[1][0])
        for i in range(0, len(tasks)):
            task_order, task = tasks[i][0], tasks[i][1]
            compute_time = task[2]
            seq += [task_order] * compute_time
        return seq


