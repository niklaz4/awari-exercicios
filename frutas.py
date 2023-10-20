# Lista de frutas inicial
frutas = ['bananas', 'maçãs', 'peras', 'uvas', 'laranjas']

# Loop para pedir ao usuário para inserir uma fruta
while True:
    # Pedir ao usuário para inserir uma fruta ou 999 para sair
    entrada = input("Digite o nome da fruta ou 999 para sair: ")
    
    # Verificar se o usuário quer sair
    if entrada == '999':
        break
    
    # Verificar se a fruta já está na lista
    if entrada in frutas:
        print(f"A fruta '{entrada}' já está na lista.")
    else:
        # Adicionar a nova fruta à lista
        frutas.append(entrada)
        print(f"A fruta '{entrada}' foi adicionada à lista.")

# Imprimir a lista final de frutas
print("Lista final de frutas:", frutas)
