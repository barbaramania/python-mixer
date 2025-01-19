# print a shipping lable using function wirh args and **kwargs
# **kwargs can be only after *args
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    # for value in kwargs.values():
    #     print(value, end =" ")

    # if the is no apt skip this key:
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('zip')}")



shipping_label("Dr.", "Bill", "Montersole", "II",
                street = "123 West st", 
                # apt = "100",
                pobox = "10010",
                city = "Seattle",
                zip = 98100)