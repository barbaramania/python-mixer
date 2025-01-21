# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Billi", 456.98, "01/01")

import time

#default argument should follow non-default argument
def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")

count(20) #starts from 0, but still can say 10, 5
