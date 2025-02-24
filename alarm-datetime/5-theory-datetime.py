import datetime

date = datetime.date(2025, 1, 9)
print(date) # 2025-01-09

today = datetime.date.today()
print(today) # 2025-02-16

time = datetime.time(10,30, 0)
print(time) #10:30:00

now = datetime.datetime.now()
print(now) #2025-02-16 15:49:33.537742

#format specifiers
now = now.strftime("%H:%M:%S %m-%d-%y")
print(now) #15:51:48 02-16-25

target_datetime = datetime.datetime(2030, 1 ,4, 12,30,9)
current_datetime = datetime.datetime.now()
if target_datetime< current_datetime:
    print("Target date has passed")
else: 
    print("Target date has NOT passed") #