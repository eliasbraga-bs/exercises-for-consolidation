# Passo 1: Solicitar ao usuário a quantidade de horas
horas = int(input("Digite a quantidade de horas: "))

# Passo 2: Converter horas em dias
dias = horas // 24  # divisão inteira para obter o número de dias

# Passo 3: Obter as horas restantes
horas_restantes = horas % 24  # resto da divisão para obter as horas restantes

# Passo 4: Exibir o resultado
print(f"{horas} horas equivalem a {dias} dias e {horas_restantes} horas.")
