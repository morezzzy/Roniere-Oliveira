p1 = 0
p2 = 0
p3 = 0



print(" Informe o preço de três produtos ")

p1 = int(input("Digite o valor do primeiro produto:"))
p2 = int(input("Digite o valor do segundo produto:"))
p3 = int(input("Digite o valor do terceiro produto:"))

if p1 < p2 and p2 < p3:
    print("você deve compra o primeiro produto:")

elif p2 < p3:
    print("você deve compra o segundo produto")
elif p3 < p1:
    print("você deve compra o terceiro produto")
