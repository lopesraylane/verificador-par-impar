# Projeto: Verificador de Número Par ou Ímpar
# Autor: Raylane ✨

print("🔢 Verificador de Número Par ou Ímpar")

# Pede um número ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
