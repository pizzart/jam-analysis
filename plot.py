import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

GRADE_TYPES = ['place', 'rating', 'amount']
GRADE_TITLES = {
    'place': 'Place',
    'rating': 'Rating',
    'amount': 'Amount of Ratings'
}
CRITERIAS = ['overall', 'fun', 'innovation',
             'theme', 'graphics', 'audio', 'humor', 'mood']


def make_plot(results: dict, nums: list, proper_username: str, scale: float):
    plt.rc('font', size=24 * scale)
    plt.rc('legend', fontsize=14 * scale)
    plt.style.use('Solarize_Light2')

    fig = plt.figure()
    axs = fig.subplots(2, 2)
    axs = axs.flatten()

    x = np.arange(len(results))
    for i, grade_type in enumerate(GRADE_TYPES):
        lines = []
        for c, criteria in enumerate(CRITERIAS):
            y = []
            for game in reversed(results.keys()):
                criterias = results[game]
                if criteria in criterias.keys():
                    stats = criterias[criteria]
                    y.append(stats[grade_type])
                else:
                    y.append(None)

            line, = axs[i].plot(x, y, label=criteria.capitalize(), linewidth=4 * scale,
                                marker='o', markersize=12 * scale)
            line.set_dashes([4, c, 2, c])
            line.set_dash_capstyle('round')
            lines.append(line)

        axs[i].set_xticks(x, reversed(results.keys()))

        axs[i].tick_params(labelsize=16 * scale, width=2)
        plt.setp(axs[i].get_xticklabels(), rotation=15,
                 horizontalalignment='right')

        ax2 = axs[i].secondary_xaxis('top')
        ax2.set_xticks(x, nums[::-1])
        ax2.tick_params(labelsize=20 * scale)

        axs[i].set_ylabel(GRADE_TITLES[grade_type], fontsize=20 * scale)

        axs[i].grid(True)

        leg = axs[i].legend(fancybox=True, shadow=True)
        lined = {}
        for legline, origline in zip(leg.get_lines(), lines):
            legline.set_picker(True)
            lined[legline] = origline

        if grade_type == 'place':
            axs[i].yaxis.set_major_locator(ticker.MultipleLocator(100))
            axs[i].invert_yaxis()
        elif grade_type == 'rating':
            axs[i].yaxis.set_major_locator(ticker.MultipleLocator(0.25))
            axs[i].set_ylim(top=5)

        def on_pick(event):
            legline = event.artist
            origline = lined[legline]
            visible = not origline.get_visible()
            origline.set_visible(visible)
            legline.set_alpha(1.0 if visible else 0.2)
            fig.canvas.draw()

        fig.canvas.mpl_connect('pick_event', on_pick)

    # place_avg = []
    # rating_avg = []
    # amount_avg = []
    # grade_avgs = [place_avg, rating_avg, amount_avg]

    # places = []
    # ratings = []
    # amounts = []
    # grades_list = [places, ratings, amounts]

    # for criterias in reversed(results.values()):
    #     game_grade_list = [[], [], []]
    #     game_grade_avg_list = [[], [], []]
    #     for criteria in criterias.values():
    #         for i, grade_value in enumerate(criteria.values()):
    #             game_grade_list[i].append(grade_value)
    #     for i, game_grades in enumerate(game_grade_list):
    #         grades_list[i].append(game_grades)
    #         grade_avg = 0
    #         for grade in game_grades:
    #             grade_avg += grade
    #         grade_avg /= len(game_grades)
    #         grade_avgs[i].append(grade_avg)
    #     # for i, game_grade_avgs in enumerate(game_grade_avg_list):
    #         # grade_avgs[i].append(game_grade_avgs)

    # w = 0.2
    # # for i, averages in enumerate(grade_avgs[1:]):
    # axs[3].bar(results.keys(), x, grade_avgs[1], w)

    fig.suptitle(f'{proper_username} - Ludum Dare')
    axs[3].set_visible(False)

    plt.show()
