import  numpy as np


a=int(input("Enter the number of rows:"))
b=int(input("Enter the number of column:"))
if a<0 or b<=0:
    print("Both n and m must be postive integers:")
else:
    U=[]
    print(f"Enter {a+b} values for the matrix")
    for i in range(a):
        row=[]
        for j in range(b):
            val=int(input(f"Enter value for U[{i}][{j}]:"))
            row.append(val)
            U.append(row)

            print("\nMatrix U:")
            for row in U:
             print(row )

