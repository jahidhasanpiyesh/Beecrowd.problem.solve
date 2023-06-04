# solve this problem ?
x, y = map(int, input().split())
if x == 1 :
    Price = float(4.00*y)
elif x == 2 :
    Price = float(4.50*y)
elif x == 3 :
    Price = float(5.00*y)
elif x == 4 :
    Price = float(2.00*y)
elif x == 5 :
    Price = float(1.50*y)

print(f"Total: R$ {Price:.2f}")
