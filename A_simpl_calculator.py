# A Simple Calculator

#.......Author.......

#...Riyad Zaigirdar..



print("Enter Operation")
print("1.Addition")
print("2.Substration")
print("3.Multiplication")
print("4.Division")

a = input("What Do Want TO Do ? (1/2/3/4) Ans : ")

b = int(input("Enter First Number : "))
c = int(input("Enter Second Number : "))

if a == "1"  :
    print("Number 1 + Number 2 is :", int(b) + int(c) )

elif a == "2" :
    print("Number 1 - Number 2 is :",int(b)-int(c))

elif a == "3" :
    print("Number 1 * Number 2 is :", int(b) * int(c))

elif a == "4" :
    print("Number 1 / Number 2 is :", int(b) / int(c) )

else:
    print("Invalid Input")    
