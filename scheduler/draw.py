import matplotlib.pyplot as plt
import numpy as np


def rindex(l, v):
    return len(l) - l[-1::-1].index(v) - 1


def drawResults(results: list = [], workloads: list = [], title: str = ''):
    """
    @ results: the sequence of schedule algorithm
    @ workloads: the original input, to get the info of start time, deadline, etc.
    @ title: name of schedule algorithm
    e.g. drawResults([0,0,1,1,1,2,2], 'FIFO')
    """
    font_en = 'Times New Roman'

    fig = plt.figure(figsize=(10, 5))
    task_set = list(set(results) - {-1})
    task_num = len(task_set)
    colors = ['c', 'b', 'm', 'r', 'g', 'y', 'k', 'w']
    color_map = {task_set[i]: colors[i] for i in range(0, len(task_set))}

    plt.plot([], [], label='Arrival Time', color='black')
    plt.plot([], [], label='Deadline', color='red')
    plt.plot([], [], label='Finish Time', color='green')

    for i in range(0, len(workloads)):
        work = workloads[i]
        arrival_time, deadline = work[0], work[1]
        finish_time = rindex(results, i) + 1
        plt.annotate("", xy=(arrival_time, i + 1), xytext=(arrival_time, i + 1 + 0.5),
                     arrowprops=dict(arrowstyle="->", color='black'))
        plt.annotate("", xy=(deadline, i + 1), xytext=(deadline, i + 1 + 0.5),
                     arrowprops=dict(arrowstyle="->", color='red'))
        plt.annotate("", xy=(finish_time, i + 1), xytext=(finish_time, i + 1 + 0.5),
                     arrowprops=dict(arrowstyle="->", color='green'))

    for i in range(0, len(results)):
        task = results[i]
        if task == -1:
            continue
        x = np.linspace(i, i + 1, 1000)
        y = (task + 1) + x * 0
        plt.plot(x, y, color=color_map[task], linewidth=3)

    plt.yticks(np.arange(1, task_num + 2, 1))
    plt.xticks(np.arange(0, 25, 1))
    # plt.xticks(np.arange(0, len(results) + 1, 1))

    plt.ylabel('Task', fontproperties=font_en)
    plt.xlabel('Time', fontproperties=font_en)
    plt.title(title)

    plt.grid()
    plt.legend()
    plt.show()
