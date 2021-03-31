print("Calculadora")
n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segundo numero:"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é : {} A multiplicação é : {} A divisão é: {:.3f}".format(s ,m ,d, end))
print("O resto da divisão é:{} a potencia é:{}".format(di ,e))