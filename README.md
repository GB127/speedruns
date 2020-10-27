# Speedrun.com statistics fetcher

The entire script is written by Niamek. Current version : 1.0

It's a python script that fetches data from speedrun.com's API to plot graphs (histograms or simple plot) or to display tables.

The program divides the stats into the following categories:
+ PBs
    + Category that covers all PBs and compares them to the leaderboard and WR.
+ Systems
    + Category that covers all systems stats of the said user.
+ Saves
    + Category that covers runs improvements.

The details of each categories will be covered further in the README.

# How to use the script:
First you must have python 3.8 installed in your computer. To run the program, you need to learn how to run a script from a command line (the black windows stuffs). In the future I will try to make it more user friendly, but I have other projects I'm interested in working on.

Running the script will first ask you which user you wish to analyse.
> Which sr user?

Type the speedrun username you want to analyse, then hit "enter".
> Which sr user? niamek

The script will then be fetching data and can't accept commands during the process.**The more runs the user have, the longer the process will be.**
> Fetching data...

**Note:


**



Once the process is done, you will be asked an option from the "main menu".
> What do you want to do?
> [PBs, systems, saves, sort, end]

Type down the category you want to display data. **The commands are case sensitives**.
> What do you want to do?
> [PBs, systems, saves, sort, end] PBs

# PBs
This category will analyse stats of the PBs and compare them to the WR and the leaderboard.

Selecting this option will display a table. It will ask you which run you want to analyse, or select all of them.
>[0 - 7, all]
## The table
The following information are displayed:
+ Sys : System of the run
+ Game : Game of the run
+ Category of the run
    + A current issue with my table is that it doesn't display the differences of two PBs of a game that has a same category, but a different subcategory. They will have all the same category, but, in the background, the script makes a distinction between all of them.
    + Example : https://www.speedrun.com/alttp
        + All runs of the No Major Glitches will be listed as the same category "No Major Glitches".
+ Time : Time of the PB
+ Delta WR : Time behind the WR
    + Example : +0:05:00 => 5 minutes behind WR
+ %WR : Percentage off the WR
    + Example : 200% => The time is double the WR.
+ Rank (%): Rank on the leaderboard, and percentage of people you beat.
    Example: 8/10 (20.0 %) : You are placed 8th on the leaderboard and you are ranked higher than 20% of the runners.

At the foot of the table:
+ the total of all PBs and the total of time behind the WR are displayed.
+ The average of all PBs and the average of time behind the WR and the percentage off the WR are displayed.

## The PB place on leaderboard plot
This plot shows where the runner is on the leaderboard.

The rank is shown on the x axis, and the time is on the y axis. The analysed runner's rank is shown with an arrow.

NOTE : The plot removes some entries that have a way too high time compared to the WR. This is to avoid an entirely crushed plot. Currently, the cut off is 6 times the WR. In other words : if an entry's time is 6 times higher the WR or higher, it won't be displayed on the plot.

## All PBs:
### The histograms of PBs vs. WR:
The histogram combines two histograms : The histogram of all the PBs and the histogram of all the WRs. The histograms represent the frequency of times.

Title of the graphic is the runner and the number of PBs.

gold histogram : Represent all the WRs.
Green histogram : Represent all the current PBs.

Overall, the gold bars should be more to the left than the green bars. The closer the green histogram is to the gold histogram, the closer to WR the user is.

Note that if runs with smaller improvements will have a good chance to appear on the same time bar and not shift to a different time bar.

### The histograms of PBs:
Selecting all PBs will display 4 histograms gathering the infos of all PBs.
On the top left : Histogram of all the runs time frequency.
On the top right : Histogram of all the PBs time frequency.
On the bottom left : Histogram of all the times behind WR frequency.
On the bottom right : Histogram of all the percentages off the WR frequency.

# saves
This category of data will show statistics regarding the improvements of your PBs. For this category, all runs that have only one attempt are omitted. A table will be listed, and then you will be asked to select an entry of the table or all of them.

> [0 - 19, all]

Selecting a single entry will make a plot of the progression of the PBs.
Selecting all of them will combine every plots into a single plot.

## The table
Selecting this category will print a table with all runs you have submitted to speedrun.com that have more than 1 attempt. The following infos are displayed in culumns in the table:
+ game : Game of the run
+ Category : category of the run
    + A current issue with my table is that it doesn't display the differences of two PBs of a game that has a same category, but a different subcategory. They will have all the same category, but, in the background, the script makes a distinction between all of them.
    + Example : https://www.speedrun.com/alttp
        + All runs of the No Major Glitches will be listed as the same category "No Major Glitches".
+ Number : This is the number of personal bests you have in this category.
+ First PB : This is the first PB of the category.
+ Current PB : This is the current PB of the category.
+ Saved (%) : Amount of time saved and the percentage saved.
    + - 0:05:00 (5.00 %) => 5 minutes saved since first PB, representing 5.00 % of First PB.

At the foot of the table:
+ The total time of the first runs, and the total of time saved is displayed.
+ The average time of the first runs, and the average of time saved is displayed.
+ the total of runs that don't have more than one attempt will be displayed, as well as the total of time.

## The single plot:
Title of the plot is the username of the runner as well as the selected game and category.

The plot is the progression of your times (y axis) over the number of PBs (x axis). The yellow line at the bottom is the **current** WR.

Legend is the current WR.

Notice : The WR does change over time, making the gap between PB and WR not always consistent. Making the changes in the plot will increase the data fetching time. I opted to not consider it in the plot.


## The combined plots
Two plots will be drawn. One appearing at a time. First an histogram will be created.

### The histogram:
The histogram combines two histograms : The histogram of all the first PBs and the histogram of all the current PBs. The histograms represent the frequency of a time.

Title of the graphic is the runner and the number of PBs that has saves.

Red histogram : Represent all the first PBs together.
Green histogram : Represent all the current PBs together.

Overall, the green bars should be more to the left than the red bars, showing the improvements. Note that if runs with smaller improvements will have a good chance to appear on the same time bar and not shift to a different time bar.

### The combined PB progressions plot
The runs with saves are divided in four plots with different time frames to minimize a crushed look. This plot combines all the single plots.

# sort
This option allows you to change the sorting method of the PBs, effectively influencing the tables displayed of all the others options.

Sorting options:
+ game : Sort the PBs by game name.
+ PB# : Sort the PBs by the number of PBs.
+ system : sort the PBs by system.
+ Time : Sort the PBs by time.
+ deltaWR : Sort the PBs by time behind the WR.
+ %WR : Sort the PBs by the percentage of WR
    + Example : 200 %, WR is 1:00:00, => your time is 2:00:00
+ %LB : Sort the PBs by the leaderboard percentage.
    + Example : leaderboard has 10 runners => you are 8th on the leaderboard. You are better than 20% of the runners. Then your leaderboard percentage is 20%.


# systems
This category will analyse stats of systems.
Selecting this option will display a table of the system, and will ask you which system you want to select. Enter the number wanted, or select all of them by typing all.
> [0 - 7, all]




## The table:
The table will display the times splitted by system (displayed on the first column. Total time of all the runs on the said system and the average under it on the second column. The same infos are displayed on the right. The following infos are added: the times behind the WR and the average percentage of the WR.

## Single system
Selecting a single system will display 4 histogram of the said system.
On the top left : Histogram of all the runs time frequency of the said system.
On the top right : Histogram of all the PBs time frequency of the said system.
On the bottom left : Histogram of all the times behind WR frequency of the said system.
On the bottom right : Histogram of all the percentages off the WR frequency of the said system.

## All systems pie:
Selecting all the systems will display a pie system deciphering the percentage of each system. On the left, it's the PBs, on the right it's all the runs. On the top, the percentages of the number of runs per system. On the bottom, the percentages of times per system.

# end
This command ends the script.