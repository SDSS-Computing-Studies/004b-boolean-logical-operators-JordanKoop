#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
a = input("Enter a number:  ")
a=float(a)
aa=str(a)
b = input("Enter a number:  ")
b=float(b)
bb=str(b)

if a>b:
    if a/b== int(a/b):
        print(bb+ " is a factor of "+aa)
    else:
        print(bb +" is not a factor of "+ aa)
elif b>a:
    if b/a== int(b/a):
        print(aa+ " is a factor of "+bb)
    else:
        print(aa +" is not a factor of "+ bb)