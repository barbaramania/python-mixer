import time

my_time = int(input("Enter a time for your timer in sec.: "))
for x in reversed(range(0,my_time)): 
# for x in range(my_time,0,-1):
    seconds = x % 60 # 70%60 = 10 sec 1 min
    minutes = int(x / 60) % 60 # 3601/60 = 60 min % 60 = 0 while 1 is 1 sec
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") #counter
    #the programm will sleep for 1 sec
    time.sleep(1)
#output 10 9 8 7 6 5 4 3 2 1 Time's up!
print("Time's up!")