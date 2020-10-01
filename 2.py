
time_sec = int(input("Write your time there in seconds: "))
sec = int((time_sec % 60))
minute = int((time_sec // 60 % 60))
hour = int((time_sec // 3600 % 24))
print('{0:02}:{1:02}:{2:02}'.format(hour, minute, sec))
