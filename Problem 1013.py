'''
Make a program that reads 3 integer values and present the greatest one followed
by the message "eh o maior". Use the following formula:

Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.

Input Samples	Output Samples
7 14 106

                106 eh o maior

217 14 6

                217 eh o maior
'''
# first step
a,b,c=map(int,input().split())
print(max(a,b,c),"eh o maior")

# second step
a,b,c=list(map(int,input().split()))
print(max(a,b,c),"eh o maior")

# third step
a,b,c=list(map(int,input().split()))
print("{} eh o maior".format(max(a,b,c)))