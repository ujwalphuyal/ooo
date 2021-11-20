print("Marks shhet of the student")
sc=int(input("Enter marks in physics :"))
if sc>100 or sc<0:
    exit("Invalid option")
math=int(input("Enter marks in math :"))
if math>100 or math<0:
    exit("Invalid option")
social=int(input("Enter marks in chemistry :"))
if social>100 or social<0:
    exit("Invalid option")
nepali=int(input("Enter marks in nepali :"))
if nepali>100 or nepali<0:
    exit("Invalid option")
eng=int(input("Enter marks in english :"))
if eng>100 or eng<0:
    exit("Invalid option")
computer=int(input("Enter marks in computer :"))
if computer>100 or computer<0:
    exit("Invalid option")
total_marks=float(sc+math+nepali+computer+eng+social)
total_percent=(total_marks*100)/600
print(f"Total percentage : {total_percent}%")
if(total_percent>=90):
    print("You got A+")
elif(total_percent>=80):
    print("You got A")
elif(total_percent>=70):
    print("You got B+")
elif(total_percent>=60):
    print("You got B")
elif(total_percent>=50):
    print("You got C")
else:
    print("Fail")    