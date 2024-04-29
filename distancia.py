# Recebe a distância e a velocidade do usuário
distancia = float(input("Digite a distância da viagem em quilômetros: "))
velocidade = float(input("Digite a velocidade média da viagem em km/h: "))

# Calcula o tempo de viagem
tempo = distancia / velocidade

# Exibe o tempo de viagem na tela
print(f"O tempo estimado de viagem é de {tempo:.2f} horas.")