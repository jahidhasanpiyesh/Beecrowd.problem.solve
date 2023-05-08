# new code solve this code
A = float(input())
N = A
a = N / 100
b = N % 100
c = b / 50
d = b % 50
e = d / 20
f = d % 20
g = f / 10
h = f % 10
i = h / 5
j = h % 5
k = j / 2
l = j % 2

E = A * 100
B = (int(E))
m = B % 100
n = m / 50
o = m % 50
p = o / 25
q = o % 25
r = q / 10
s = q % 10
t = s / 5
u = s % 5
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(a)))
print("{} nota(s) de R$ 50.00".format(int(c)))
print("{} nota(s) de R$ 20.00".format(int(e)))
print("{} nota(s) de R$ 10.00".format(int(g)))
print("{} nota(s) de R$ 5.00".format(int(i)))
print("{} nota(s) de R$ 2.00".format(int(k)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(l)))
print("{} moeda(s) de R$ 0.50".format(int(n)))
print("{} moeda(s) de R$ 0.25".format(int(p)))
print("{} moeda(s) de R$ 0.10".format(int(r)))
print("{} moeda(s) de R$ 0.05".format(int(t)))
print("{} moeda(s) de R$ 0.01".format(int(u)))

# Banknotes and Coins try this code
coins = float(input())
coins1 = int(coins / 100)
coins = coins % 100
coins2 = int(coins / 50)
coins = coins % 50
coins3 = int(coins / 20)
coins = coins % 20
coins4 = int(coins / 10)
coins = coins % 10
coins5 = int(coins / 5)
coins = coins % 5
coins6 = int(coins / 2)
coins = coins % 2

coins7 = int(coins / 1.00)
coins = coins % 1.00
coins8 = int(coins / 0.50)
coins = coins % 0.50
coins9 = int(coins / 0.25)
coins = coins % 0.25
coins10 = int(coins / 0.10)
coins = coins % 0.10
coins11 = int(coins / 0.05)
coins = coins % 0.05
coins12 = int(coins / 0.01)
coins = coins % 0.01
print("NOTAS:")
print(coins1, "nota(s) de R$ 100.00")
print(coins2, "nota(s) de R$ 50.00")
print(coins3, "nota(s) de R$ 20.00")
print(coins4, "nota(s) de R$ 10.00")
print(coins5, "nota(s) de R$ 5.00")
print(coins6, "nota(s) de R$ 2.00")
print("MOEDAS:")
print(coins7, "moeda(s) de R$ 1.00")
print(coins8, "moeda(s) de R$ 0.50")
print(coins9, "moeda(s) de R$ 0.25")
print(coins10, "moeda(s) de R$ 0.10")
print(coins11, "moeda(s) de R$ 0.05")
print(coins12, "moeda(s) de R$ 0.01")

# Banknotes and Coins try this code
value = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for nota in notas:
    nota_value = int(value / nota)
    print("{} nota(s) de R$ {:.2f}".format(nota_value, nota))
    value = value - nota_value * nota
print("MOEDAS:")
for moeda in moedas:
    moeda_value = int(value / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(moeda_value, moeda))
    value = value - moeda_value * moeda
