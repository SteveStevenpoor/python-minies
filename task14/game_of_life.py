from copy import deepcopy
from enum import Enum
from functools import partial

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from task14.scripts.timing import timing
from task8.format_table import format_table


class Mode(Enum):
    np_field = 0
    list_field = 1


resources = {
    1: 'materials/fig_1.txt',
    2: 'materials/fig_2.txt',
    3: 'materials/clock1.txt',
    4: 'materials/spaceship1.txt',
    5: 'materials/R-p1.txt'
}


def choose_mode(universe, rows, cols):
    # mode = int(input("Set up mode\n 1 - Gun\n 2 - Star\n 3 - Watch\n 4 - Spaceship\n 5 - Pentamino\n 6 - Random\n"))
    mode = 5
    if mode in resources.keys():
        with open(resources[mode], 'r') as field:
            for line in field:
                i, j = (int(x) for x in line.split())
                universe[i][j] = 1
    elif mode == 6:
        if isinstance(universe, list):
            universe[:] = np.random.choice([0, 1], rows * cols, p=[0.2, 0.8]).reshape(rows, cols).tolist()
        else:
            universe[:] = np.random.choice([0, 1], rows * cols, p=[0.2, 0.8]).reshape(rows, cols)
    else:
        print('Unknown option, try again')


def next_epoch(framedata, mat, universe, rows, cols):
    if isinstance(universe, np.ndarray):
        new_universe = np.copy(universe)
    else:
        new_universe = deepcopy(universe)

    for i in range(rows):
        for j in range(cols):
            alive_neighbours_cnt = (universe[i][(j - 1) % cols] + universe[i][(j + 1) % cols] +
                                    universe[(i - 1) % rows][j] + universe[(i + 1) % rows][j] +
                                    universe[(i - 1) % rows][(j - 1) % cols] +
                                    universe[(i - 1) % rows][(j + 1) % cols] +
                                    universe[(i + 1) % rows][(j - 1) % cols] +
                                    universe[(i + 1) % rows][(j + 1) % cols])
            if not universe[i][j]:
                if alive_neighbours_cnt == 3:
                    new_universe[i][j] = 1
            else:
                if (alive_neighbours_cnt < 2) or (alive_neighbours_cnt > 3):
                    new_universe[i][j] = 0

    universe[:] = new_universe
    if mat: mat.set_data(universe)
    return None


def animate(universe, rows, cols, epoch_num):
    fig, ax = plt.subplots()
    mat = ax.matshow(universe)
    ani = animation.FuncAnimation(fig, partial(next_epoch, mat=mat, universe=universe, rows=rows, cols=cols),
                                  range(epoch_num), interval=50,
                                  cache_frame_data=False, repeat=False)
    plt.show()


@timing
def simulate_life(rows, cols, epoch_num: int, mode, animated=False) -> None:
    universe = None
    if mode == Mode.np_field:
        universe = np.zeros(rows * cols, dtype=np.uint8).reshape(rows, cols)
    else:
        universe = [[0 for _ in range(cols)] for _ in range(rows)]

    choose_mode(universe, rows, cols)

    if not animated:
        for _ in range(epoch_num):
            next_epoch(None, None, universe, rows, cols)
    else:
        animate(universe, rows, cols, epoch_num)


size = 200
format_table(["list field", "np array field"], ["size", "time"],
             [[size, simulate_life(size, size, 128, Mode.list_field)[1]],
              [size, simulate_life(size, size, 128, Mode.np_field)[1]]])
