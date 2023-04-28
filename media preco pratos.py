pratos = []
pratoadd = 0
media = 0
escolha = ''
somaprato = 0
nprato = 0

while escolha != 4:
    escolha = int(input("O que você deseja fazer? \n [1] Pesar prato \n [2] Verificar os pratos \n [3] Verificar a média \n [4] Sair \n"))
    
    if escolha == 1:
        pratoadd = float(input("Qual o peso do prato adicionado? \n "))
        somaprato += pratoadd
        nprato += 1
        pratos.append(pratoadd)
        print("Prato adicionado")
    
    elif escolha == 2:
        if nprato > 0:
            print("Os pratos pesados até agora foram: ")
            for x in pratos:
                print(x)
        else:
            print("Nenhum prato foi pesado até agora")
    
    elif escolha == 3:
        if nprato > 0:
            media = somaprato / nprato
            print(f"A média dos pratos foi de: {media}")
            
        else:
            print("Nenhum prato foi pesado até agora")
    
    else:
        print("Escolha inválida")

print("Você escolheu sair do código, volte sempre!")