print("welcome to nepal telecome.")
duration=int(input("please dail theduration of the call in a min:"))

if  duration>=10:
    bonus=duration/2
    print(f"Your total bonus is Rs{bonus}")
    print("HAPPY CALLING")
else:
    print("HAPPY CALLING \n you did'nt reach the limit of call to "
    "to make bonus")