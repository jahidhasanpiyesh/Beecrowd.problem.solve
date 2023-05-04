# solve this bee 1019 problem solve :
# input this int numbers
second = int(input())
# second / minutes and int type data not a float data ?
minutes = int(second/60)
# modulus use this float answer not allow so point break
second %= 60
# minutes / 60 and int type data access
hor = int(minutes/60)
minutes %= 60
# use this short way and one line output
print(f"{hor}:{minutes}:{second}")
