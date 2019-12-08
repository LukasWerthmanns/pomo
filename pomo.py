import time
import os
from playsound import playsound
from datetime import datetime
import getch
import subprocess
import math
import sys

# duration for one interval and pause in seconds
duration = 25*60
normal_pause = 5*60
long_pause = 30*60
duration_end_sound = "/home/lukas/python/pomodoro/pling.mp3"
progress_bar_length = 50

try:
    sys.argv[1]
except IndexError:
    interval_number = 0
else:
    if sys.argv[1] == "help" or sys.argv[1] == "h":
        print("This is a simple pomodoro timer")
        print("python pomo.py [1-4]")
        print("give the interval you want to start in as an argument (default 0)")
        print("Intervals will be " + str(duration) + "min with " + str(normal_pause) + "min Pause in between\nand " + str(long_pause) + "min after ther 4th interval")
        print("After an interval finished you will be prompted to continue or quit")
        exit()

    else:
        interval_number = int(sys.argv[1])

        if interval_number > 4:
            print("Interval Number should be <= 4")
            exit()


def interval(durationtime, infostring):
    curr = durationtime
    end_message = infostring + " ended"
    print(infostring + " interval " + str(interval_number) + ": " + str(durationtime/60) + "min")
    for i in range(durationtime):
        progress_bar_string = math.floor(((progress_bar_length/durationtime)*i))*"=" + (progress_bar_length - math.floor(((progress_bar_length/durationtime)*i)))*" " + "]"
        print("[" + progress_bar_string, end="\r")
        curr = curr - 1
        time.sleep(1)
    os.system('clear')
    print(infostring + " ended")
    playsound(duration_end_sound)
    subprocess.Popen(['notify-send', "Pomodoro", end_message])
    os.system('clear')


while True:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    start_time = str(date_time)
    interval(duration, "POMODORO")
    pomolog = open("pomolog.txt", "a")
    pomolog.write(start_time + "\n")
    pomolog.close()
    if interval_number == 4:
        interval(long_pause, "Long Pause")
        interval_number = 0
    else:
        interval(normal_pause, "Pause")
        interval_number += 1
    os.system('clear')

    print("FINISHED - " + date_time + "\n")
    print("Press c to continue or q to quit" + "\n")

    while True:
        input = getch.getch()
        if input == "c":
            os.system('clear')
            break
        if input == "q":
            exit()
