# Calcular aumento de salário

# Entrada de dados
salario = float(input("Digite o valor do salário: "))
porcentagem = float(input("Digite a porcentagem de aumento (%): "))

# Cálculo do valor do aumento
valor_aumento = salario * (porcentagem / 100)

# Cálculo do novo salário
novo_salario = salario + valor_aumento

# Saída de dados
print(f"O valor do aumento é: R${valor_aumento:.2f}")
print(f"O novo salário é: R${novo_salario:.2f}")
