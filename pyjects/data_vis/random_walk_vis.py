import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Plot
    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)

    # Color the walk from light -> dark for start -> end
    ax.scatter(rw.x_vals, rw.y_vals, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.set_aspect('equal')
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_vals[-1], rw.y_vals[-1], c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_going = input("Make another walk? (y/n): ")
    if keep_going == 'n':
        break