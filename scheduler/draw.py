import matplotlib.pyplot as plt
import numpy as np


def drawResults(results: list, title: str):
    """
    @ results: the sequence of schedule algorithm
    @ title: name of schedule algorithm 
    e.g. drawResults([0,0,1,1,1,2,2], 'FIFO')
    """
    font_en = 'Times New Roman'

    plt.figure(figsize=(10, 5))
    task_set = list(set(results) - {-1})
    task_num = len(task_set)
    colors = ['c', 'b', 'm', 'r', 'g', 'y', 'k', 'w']
    color_map = {task_set[i]: colors[i] for i in range(0, len(task_set))}

    for i in range(0, len(results)):
        task = results[i]
        if task == -1:
            continue
        x = np.linspace(i, i + 1, 1000)
        y = (task + 1) + x * 0
        plt.plot(x, y, color=color_map[task], linewidth=3)

    plt.yticks(np.arange(1, task_num + 1, 1))
    plt.xticks(np.arange(0, len(results) + 1, 1))

    plt.ylabel('Task', fontproperties=font_en)
    plt.xlabel('Time', fontproperties=font_en)
    plt.title(title)

    plt.grid()
    plt.legend()
    plt.show()
