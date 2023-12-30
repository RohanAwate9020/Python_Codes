import time
timestamp=time.strftime('%H')
currenttime=time.strftime('%I/%M/%S/%a')


if (int(timestamp)> 6 and int(timestamp)<12):
    print("Good Morning, have a good day a head.")
elif(int(timestamp)>13 and int(timestamp)<18):
    print("Good Afternoon Sir, How is your day")
else:
    print("Good Night Sir, I hope only sweet dreams meet you in sleep")

print("Current Time(hh:mm:ss):", currenttime)