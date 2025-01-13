principle =0
rate = 0
time = 0

#Adds a variation of 0 in variable
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        principle = float(input("The principle amount should be more than zero: "))
    else:
        break

while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        rate = float(input("The rate amount should be more than zero: "))

while time <= 0:
    time = float(input("Enter the time in yers: "))
    if time <= 0:
        time = float(input("Time should be more than zero: "))

total = principle * pow((1 + rate / 100),time)
print(f"BALANCE AFTER {time} year/s: ${total:.2f}")
