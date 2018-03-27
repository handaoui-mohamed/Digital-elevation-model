import os
from time import time
import datetime


def printProgressBar(iteration, total, prefix='Progress', suffix='', decimals=1, length=100, fill='█'):
    """
    Print iterations progress
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def printTiming(start):
    """
    timer function, just to check the performance
    """
    end = time()
    duration = end - start
    if duration < 60:
        print("Total Timing: " + str(round(duration, 2)) + "s.", end='\n')
    else:
        mins = int(duration / 60)
        secs = round(duration % 60, 2)
        if mins < 60:
            print("Total Timing: " + str(mins) +
                  "m " + str(secs) + "s.", end='\n')
        else:
            hours = int(duration / 3600)
            mins = mins % 60
            print("Total Timing: " + str(hours) + "h " +
                  str(mins) + "m " + str(secs) + "s.", end='\n')


def printDate(prefix):
    print(prefix + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), end='\n')
