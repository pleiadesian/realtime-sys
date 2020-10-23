from scheduler.abstract_class import Scheduler

class FIFOScheduler(Scheduler):
    def schedule(self, workloads):
        seq = []
        for i in range(0, len(workloads)):
            task = workloads[i]
            compute_time = task[2]
            while compute_time != 0:
                compute_time -= 1
                seq.append(i)
        return seq


