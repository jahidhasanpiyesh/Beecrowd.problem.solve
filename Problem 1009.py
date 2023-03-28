'''
Make a program that reads a seller's name, his/her fixed salary and the sale's total made by
 himself/herself in the month (in money). Considering that this seller receives 15% over all products sold,
  write the final salary (total) of this seller at the end of the month , with two decimal places.

- Don’t forget to print the line's end after the result, otherwise you will receive “Presentation Error”.

- Don’t forget the blank spaces.

Input
The input file contains a text (employee's first name), and two double precision values,
that are the seller's salary and the total value sold by him/her.

JOAO-------------input
500.00-----------input
1230.30----------input

Output
Print the seller's total salary, according to the given example.

TOTAL = R$ 684.54     ----------output
'''

name = input()  # enter this any name
salary = float(input()) # enter this floating point salary
bonus = (float(input())*15)/100 # enter this floating point bonus and equal 15%
total = salary + bonus # sum salary and bonus
print(f"TOTAL = R$ {total:.2f}") # output .2 and free space
