# Exercício de Tempo de Viagem:

# Entrada de dados: Pergunta a distância e a velocidade média
distancia = float(input("Digite a distância a percorrer (Em km): "))
velocidade_media = float(input("Digite a velocidade médoa eperada (em km/h): "))

# Cálculo do tempo de viagem
tempo_viagem = distancia / velocidade_media

# Saída de dados: Exinir o tempo estimado de viagem
print(f"O tempo estimado de viagem é de {tempo_viagem:.2f} horas.")