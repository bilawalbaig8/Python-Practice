"""

Healthy Programmer

9AM to 5PM

Water drink notifier
    Person need to drink 3.5 liter water in the working hours
    Divide required water from working hours
    Play water tone
    Need to give any input to close the alarm
    when close save the log in the document with date and time

Eye Exersice
    Alarm will run after every 30 minutes
    Need to give any input to close the alarm
    when close save the log in the document with date and time

Physical Exersice
    Alarm will run after every 45 minutes
    Need to give any input to close the alarm
    when close save the log in the document with date and time

"""

import time
import datetime
import pygame
import os


def calculate_working_hours(Log_in, Log_out):
    login_time = datetime.datetime.strptime(str(Log_in), '%I%p')
    logout_time = datetime.datetime.strptime(str(Log_out), '%I%p')

    # Calculate the working hours
    working_hours = (logout_time - login_time).total_seconds() / 3600.0

    # Print the working hours
    return working_hours


def playsound(stop):
    pygame.mixer.init()
    pygame.mixer.music.load("AlarmSFX/Alarm.wav")  # Audio file

    pygame.mixer.music.play(-1)  # -1 to make infinite loop

    pygame.mixer.music.set_volume(0.3)  # Controlling volume

    if stop == "Stop":  # Condition to check whether stop or not
        pygame.mixer.music.stop()


def require_water_glass(working_hours):
    water_liter = 3.5  # Liter of water
    water_liter_ml = water_liter * 1000
    time_interval = 20  # Minutes
    num_session = (working_hours * 60) // time_interval
    water_in_session = water_liter_ml // num_session

    return water_in_session


def make_txt_file():
    return


def water_notifier():
    return


def eye_notifier():
    return


def exercise_notifier():
    return


Log_in = "9AM"
Log_out = "6PM"

working_hours = calculate_working_hours("Log_in", "Log_out")
water_in_session = require_water_glass(working_hours)

login_time_obj = datetime.datetime.strptime(Log_in, '%I%p').time()
logout_time_obj = datetime.datetime.strptime(Log_out, '%I%p').time()

while True:

    current_time_obj = datetime.datetime.now().time()

    if login_time_obj <= current_time_obj <= logout_time_obj:
        print(current_time_obj.strftime("%I:%M:%S %p"), " It's to drink {0}ml glass of Water".format(water_in_session))
        snooze = True

        while snooze:
            playsound("Play")
            disable_Alarm = input("Type 'Done' to snooze\n")
            if disable_Alarm.lower() == "done":
                snooze = False
                playsound("Stop")
                break
    time.sleep(5)
