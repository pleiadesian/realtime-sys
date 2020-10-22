#!/bin/python3

from abc import abstractmethod

class Scheduler():
    @abstractmethod
    def schedule(self, workloads):
        """
        Please implement scheduling algorithm in scheduler directory
        @ workloads: list of (start time, deadline, computation time, priority)
        @ return:    scheduled indexes, e.g. [0, 2, 2, 1, 1, 1]
        """
        pass