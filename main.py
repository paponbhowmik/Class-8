# Loop To Multiply
num = int(input("Enter your number: "))
a = 1
while a<= 10:
    b = num*a
    print(f"{num}x{a}={b}")
    a+=1
# Q1: write a program to print first 10 integers and their squares using while loop
a = 1
print("number\t\tsquares")   # -----> \t meaning TAB ba spaces
while a<=10:
    b = a**2
    print(f"{a}\t=\t{b}")    # -----> \t meaning TAB ba spaces
    a+=1
# Q2: write a while loop statement to print the following series 105,98,91.........7.
a = 105
while a>=1:
    print(a)
    a-=7
# Q3: write a program to print first 10 natural number in reverse order using while loop
a = 10
while a>=1:
    print(a)
    a-=1
# Q4: write a program to print sum of first 10 even numbers
a = 2
b = 0
print("Even-Number\tEven-Sum-Number")   # -----> \t meaning TAB ba spaces
while a<=20:
    print(f"{a}\t=\t{b+a}")   # -----> \t meaning TAB ba spaces
    a+=2
# Q5 : 1
#      12
#      123
#      1234
#      12345
#      123456
#      1234567
#      12345678
a = 1
while a<=8:
    b = 1
    while b<=a:
        print(b,end="")
        b+=1
    print()
    a+=1
# Q6 : 1
#      12
#      123
#      1234
#      12345
#      123456 -------> break
#      1234567
#      12345678
a = 1
while a<=8:
    b = 1
    while b<=a:
        print(b,end="")
        b+=1
    print()
    if a==6:
         break
    a+=1
