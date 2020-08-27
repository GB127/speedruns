import matplotlib.pyplot as plot
import datetime
from tools import *
from api import *
from classe import *

def plot_systems(user):
    """Generate 4 pies that tells the proportions of systems.

        PB#     |   run#
        -------------------
        PB time | run time

        Args:
            user (object): User object.
        """
    fig, axs = plot.subplots(2, 2)

    fig.suptitle(f'{user.username}\n{len(user.all_systems)} systems')

    axs[0,0].set_title("PB #")
    axs[0,0].pie([user.systems_PBs[system]["count"] for system in user.all_systems], labels=[system for system in user.all_systems], autopct='%1.1f%%', startangle=90)


    axs[0,1].set_title("run #")
    axs[0,1].pie([user.systems_runs[system]["count"] for system in user.all_systems], labels=[system for system in user.all_systems], autopct='%1.1f%%', startangle=90)

    axs[1,0].set_title("PB total time")
    axs[1,0].pie([user.systems_PBs[system]["time"] for system in user.all_systems], labels=[system for system in user.all_systems], autopct='%1.1f%%', startangle=90)

    axs[1,1].set_title("run total time")
    axs[1,1].pie([user.systems_runs[system]["time"] for system in user.all_systems], labels=[system for system in user.all_systems], autopct='%1.1f%%', startangle=90)



    plot.show()


def plot_runs(PB,user):  #FIXME : Rework on it.
    runs = user.fetch_runs_PB(PB)
    runs.sort(reverse=True)

    plot.title(f'{get_game(PB.gameID)}\n{get_category(PB.categID)}\nWR:{str_time(PB.WR)}')
    plot.axhline(y=PB.WR, c="gold")

    if len(runs) == 1:
        plot.plot([run.time for run in runs], marker="o")
    else:
        plot.plot([run.time for run in runs])
    plot.xlabel("PB #")
    plot.ylabel("Time")
    plot.yticks(plot.yticks()[0],[datetime.timedelta(seconds=x) for x in plot.yticks()[0]])
    plot.show()


def plot_PB_leaderboard(PB, user):
    leaderboard = get_leaderboard(PB.gameID,PB.categID, PB.vari)

    rank_toremove = []
    for rank in leaderboard:
        if rank[1] > (6 * PB.WR):
            rank_toremove.append(rank)

    for rank in rank_toremove:
        leaderboard.remove(rank)


    plot.plot([time[0] for time in leaderboard], [rank[1] for rank in leaderboard])

    plot.title(f'{get_game(PB.gameID)}\n{get_category(PB.categID)}')


    plot.ylabel("Time")
    plot.yticks(plot.yticks()[0],[datetime.timedelta(seconds=x) for x in plot.yticks()[0]])

    plot.xlabel("Rank")
    ax = plot.gca()
    ax.set_xlim(ax.get_xlim()[::-1])
    plot.annotate(f"{user.username}", xy=(PB.place, PB.time), xytext=(0.65,0.65), textcoords="figure fraction",
                    arrowprops={"arrowstyle":"->"}
                    )



    plot.show()

def plot_leaderboard(PB):
    leaderboards = get_leaderboards(PB.gameID,PB.categID, PB.vari)

    for year in leaderboards.keys():
        if len(leaderboards[year]) == 1:
            plot.plot([time[0] for time in leaderboards[year]], [rank[1] for rank in leaderboards[year]], label=year, marker="*")
        else:
            plot.plot([time[0] for time in leaderboards[year]], [rank[1] for rank in leaderboards[year]], label=year)

    plot.title(f'{get_game(PB.gameID)}\n{get_category(PB.categID)}')


    plot.ylabel("Time")
    plot.yticks(plot.yticks()[0],[datetime.timedelta(seconds=x) for x in plot.yticks()[0]])

    plot.xlabel("Rank")
    ax = plot.gca()
    ax.set_xlim(ax.get_xlim()[::-1])
    


    plot.show()




def plot_system(user, system):
    """Generate 4 histograms about the system times.

        runs times | PB times
        ---------------------
        PB delta   | PB %WR

        Args:
            user (object): User object
            system (string): System to analyse.

        """

    fig, axs = plot.subplots(2, 2)

    fig.suptitle(f"{user}\n{system}")

    data = user.fetch_runs_system(system)
    data_2 = [run.time for run in data]
    axs[0,0].hist(data_2)
    axs[0,0].set_title("Runs")
    plot.sca(axs[0,0])
    plot.xlim(left=0)
    plot.xticks(plot.xticks()[0], [str_time(tick) for tick in plot.xticks()[0]])


    data = user.fetch_runs_system(system, PB=True)
    data_2 = [run.time for run in data]
    axs[0,1].hist(data_2)
    axs[0,1].set_title("PBs")
    plot.sca(axs[0,1])
    plot.xlim(left=0)
    plot.xticks(plot.xticks()[0], [str_time(tick) for tick in plot.xticks()[0]])


    data_2 = [run.delta for run in data]
    axs[1,0].hist(data_2)
    axs[1,0].set_title("delta WR")
    plot.sca(axs[1,0])
    plot.xlim(left=0)
    plot.xticks(plot.xticks()[0], [str_time(tick) for tick in plot.xticks()[0]])

    data_2 = [run.percWR for run in data]
    axs[1,1].hist(data_2)
    axs[1,1].set_title("%WR")
    plot.sca(axs[1,1])
    plot.xlim(left=100)
    plot.xticks(plot.xticks()[0], [str(tick) + " %" for tick in plot.xticks()[0]])






    plot.show()


if __name__ == "__main__":
    testing = user("niamek")
    testing.table_PBs()
    plot_leaderboard(testing.PBs[6])