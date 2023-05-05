timeinput = "04:59:59AM"

hours = int(timeinput[:2])
minutes = int(timeinput[3:5])
second = int(timeinput[6:8])
am_pm = timeinput[8:]

if am_pm == "PM" and hours != 12:
    hours += 12
elif am_pm == "AM" and hours == 12:
    hours = 0

print("{:02d}:{:02d}:{:02d}".format(hours,minutes,second))