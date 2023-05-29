import Pyro4

uri = "PYRO:obj_81ee0fcf8f5d4d158a3cd3279fec6496@192.168.1.114:9090"
servico_remoto = Pyro4.Proxy(uri)

saudacao = servico_remoto.saudacao()

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

resultado = servico_remoto.calcular_bhaskara(a, b, c)

print("Status do servidor:", saudacao)
print("Resultado da fórmula de Bhaskara:", resultado)
