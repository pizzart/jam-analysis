# importing the required module
import matplotlib.pyplot as plt


def make_plot(results: dict):
    x = range(len(results))
    for criteria in results["Rock'n'Rover"].keys():
        y = []
        for game in reversed(results.keys()):
            y.append(results[game][criteria]['place'])
        plt.plot(x, y, label=criteria, linewidth=3)

    plt.xlabel('games')
    plt.ylabel('place')

    plt.title('LD')
    plt.legend()
    plt.grid(True)

    plt.show()
