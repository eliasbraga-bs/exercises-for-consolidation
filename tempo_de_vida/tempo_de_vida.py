 # Exercício de Tempo de Viagem

# Entrada de dados: Pergunta a quantidade de cigarros fumados por dia e os anos de fumo
cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite há quantos anos você fuma: "))

# Cálculo do total de cigarros fumados
total_cigarros = cigarros_por_dia * anos_fumando * 365

# Cálculo do tempo perdido em minutos (10 minutos por cigarro)
tempo_perdido_minutos = total_cigarros * 10

# Cálculo do tempo perdido em dias
tempo_perdido_dias = tempo_perdido_minutos / (24 * 60)

# Saída de dados: Exibe o total de dias de vida perdidos
print(f"O tempo de vida perdido é de aproximadamente {tempo_perdido_dias:.2f} dias.")
