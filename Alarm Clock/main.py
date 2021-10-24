""" Alarm Clock
----------------------------------------
"""
import datetime
import os
import time
import random
import webbrowser

if not os.path.isfile("youtube_alarm_videos.txt"):
    print('Creating "youtube_alarm_videos.txt"...')
    with open("youtube_alarm_videos.txt", "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=anM6uIZvx74")

def check_alarm_input(alarm_time):
    """Checks to see if the user has entered in a valid alarm time"""
    if len(alarm_time) == 1: 
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: 
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3: 
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0 and \
           alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False
print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
while True:
    alarm_input = input(">> ")
    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: Enter time in HH:MM or HH:MM:SS format")

seconds_hms = [3600, 60, 1] 
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

time_diff_seconds = alarm_seconds - current_time_seconds

if time_diff_seconds < 0:
    time_diff_seconds += 86400 

print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

time.sleep(time_diff_seconds)

print("Wake Up!")

with open("youtube_alarm_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()

webbrowser.open(random.choice(videos))