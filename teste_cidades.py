regiao = 0
while regiao != 1 and regiao != 2 and regiao != 3 and regiao != 4 and regiao != 5:
    print("Escolha uma regiao")
    print("[1] Norte")
    print("[2] Nordeste")
    print("[3] Centro-Oeste")
    print("[4] Sudeste")
    print("[5] Sul")
    regiao = int(input("Digite a regiao: "))
    match regiao:
        case 1:
            print("Voce escolheu a regiao Norte")
            print("Escolha o estado")
            print("[1] Acre")
            print("[2] Amapa")
            print("[3] Amazonas")
            print("[4] Para")
            print("[5] Rondonia")
            print("[6] Roraima")
            print("[7] Tocantins")
            estado = int(input("Digite o estado: "))
            match estado:
                case 1:
                    print("Voce escolheu o estado do Acre")
                case 2:
                    print("Voce escolheu o estado do Amapa")
                case 3:
                    print("Voce escolheu o estado do Amazonas")
                case 4:
                    print("Voce escolheu o estado do Para")
                case 5:
                    print("Voce escolheu o estado de Rondonia")
                case 6:
                    print("Voce escolheu o estado de Roraima")
                case 7:
                    print("Voce escolheu o estado de Tocantins")
                case _:
                    print("Estado invalido")
        case 2:
            print("Voce escolheu a regiao Nordeste")
            print("Escolha o estado")
        case 3:
            print("Voce escolheu a regiao Centro-Oeste")
            print("Escolha o estado")
        case 4:
            print("Voce escolheu a regiao Sudeste")
            print("Escolha o estado")
        case 5:
            print("Voce escolheu a regiao Sul")
            print("Escolha o estado")
        case _:
            print("Regiao invalida")            