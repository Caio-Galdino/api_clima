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
                    url = f"https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true"
                case 2:
                    print("Voce escolheu o estado do Amapa")
                    url = f"https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true"
                case 3:
                    print("Voce escolheu o estado do Amazonas")
                    url = f"https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true"
                case 4:
                    print("Voce escolheu o estado do Para")
                    url = f"https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true"
                case 5:
                    print("Voce escolheu o estado de Rondonia")
                    url = f"https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true"
                case 6:
                    print("Voce escolheu o estado de Roraima")
                    url = f"https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true"
                case 7:
                    print("Voce escolheu o estado de Tocantins")
                    url = f"https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true"
                case _:
                    print("Estado invalido")
        case 2:
            print("Voce escolheu a regiao Nordeste")
            print("Escolha o estado")
            estado = int(input("Digite o estado: "))
            match estado:
                case 1:
                    print("Voce escolheu o estado do Alagoas")
                    print("Escolha a cidade")
                    print("[1] Maceio")
                    print("[2] Arapiraca")
                    print("[3] Palmeira dos Indios")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Maceio")
                        case 2:
                            print("Voce escolheu a cidade de Arapiraca")
                        case 3:
                            print("Voce escolheu a cidade de Palmeira dos Indios")
                        case _:
                            print("Cidade invalida")
                case 2:
                    print("Voce escolheu o estado da Bahia")
                    print("Escolha a cidade")
                    print("[1] Salvador")
                    print("[2] Feira de Santana")
                    print("[3] Vitoria da Conquista")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Salvador")
                        case 2:
                            print("Voce escolheu a cidade de Feira de Santana")
                        case 3:
                            print("Voce escolheu a cidade de Vitoria da Conquista")
                        case _:
                            print("Cidade invalida")  
                case 3:
                    print("Voce escolheu o estado do Ceara")
                    print("Escolha a cidade")
                    print("[1] Fortaleza")
                    print("[2] Juazeiro do Norte")
                    print("[3] Sobral")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Fortaleza")
                        case 2:
                            print("Voce escolheu a cidade de Juazeiro do Norte")
                        case 3:
                            print("Voce escolheu a cidade de Sobral")
                        case _:
                            print("Cidade invalida")
                case 4:
                    print("Voce escolheu o estado do Maranhao")
                    print("Escolha a cidade")
                    print("[1] Sao Luis")
                    print("[2] Imperatriz")
                    print("[3] Caxias")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Sao Luis")
                        case 2:
                            print("Voce escolheu a cidade de Imperatriz")
                        case 3:
                            print("Voce escolheu a cidade de Caxias")
                        case _:
                            print("Cidade invalida")
                case 5:
                    print("Voce escolheu o estado da Paraiba")
                    print("Escolha a cidade")
                    print("[1] Joao Pessoa")
                    print("[2] Campina Grande")
                    print("[3] Patos")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Joao Pessoa")
                        case 2:
                            print("Voce escolheu a cidade de Campina Grande")
                        case 3:
                            print("Voce escolheu a cidade de Patos")
                        case _:
                            print("Cidade invalida")
                case 6:
                    print("Voce escolheu o estado de Pernambuco")
                    print("Escolha a cidade")
                    print("[1] Recife")
                    print("[2] Jaboatao dos Guararapes")
                    print("[3] Olinda")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Recife")
                        case 2:
                            print("Voce escolheu a cidade de Jaboatao dos Guararapes")
                        case 3:
                            print("Voce escolheu a cidade de Olinda")
                        case _:
                            print("Cidade invalida")
                case 7:
                    print("Voce escolheu o estado do Piauí")
                    print("Escolha a cidade")
                    print("[1] Teresina")
                    print("[2] Parnaiba")
                    print("[3] Picos")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Teresina")
                        case 2:
                            print("Voce escolheu a cidade de Parnaiba")
                        case 3:
                            print("Voce escolheu a cidade de Picos")
                        case _:
                            print("Cidade invalida")
                case 8:
                    print("Voce escolheu o estado do Rio Grande do Norte")
                    print("Escolha a cidade")
                    print("[1] Natal")
                    print("[2] Mossoro")
                    print("[3] Parnamirim")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Natal")
                        case 2:
                            print("Voce escolheu a cidade de Mossoro")
                        case 3:
                            print("Voce escolheu a cidade de Parnamirim")
                        case _:
                            print("Cidade invalida")
                case 9:
                    print("Voce escolheu o estado de Sergipe")
                    print("Escolha a cidade")
                    print("[1] Aracaju")
                    print("[2] Nossa Senhora do Socorro")
                    print("[3] Lagarto")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Aracaju")
                        case 2:
                            print("Voce escolheu a cidade de Nossa Senhora do Socorro")
                        case 3:
                            print("Voce escolheu a cidade de Lagarto")
                        case _:
                            print("Cidade invalida")
                case _:
                    print("Estado invalido")
        case 3:
            print("Voce escolheu a regiao Centro-Oeste")
            print("Escolha o estado")
            print("[1] Distrito Federal")
            print("[2] Goias")
            print("[3] Mato Grosso")
            print("[4] Mato Grosso do Sul")
            estado = int(input("Digite o estado: "))
            match estado:
                case 1:
                    print("Voce escolheu o Distrito federal")
                    print("Escolha a cidade")
                    print("[1] Brasilia")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Brasilia")
                        case _:
                            print("Cidade invalida")
                case 2:
                    print("Voce escolheu o estado de Goias")
                    print("Escolha a cidade")
                    print("[1] Goiania")
                    print("[2] Aparecida de Goiania")
                    print("[3] Anapolis")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Goiania")
                        case 2:
                            print("Voce escolheu a cidade de Aparecida de Goiania")
                        case 3:
                            print("Voce escolheu a cidade de Anapolis")
                        case _:
                            print("Cidade invalida")
                case 3:
                    print("Voce escolheu o estado de Mato Grosso")
                    print("Escolha a cidade")
                    print("[1] Cuiaba")
                    print("[2] Várzea Grande")
                    print("[3] Rondonopolis")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Cuiaba")
                        case 2:
                            print("Voce escolheu a cidade de Várzea Grande")
                        case 3:
                            print("Voce escolheu a cidade de Rondonopolis")
                        case _:
                            print("Cidade invalida")
                case 4:
                    print("Voce escolheu o estado de Mato Grosso do Sul")
                    print("Escolha a cidade")
                    print("[1] Campo Grande")
                    print("[2] Dourados")
                    print("[3] Três Lagoas")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Campo Grande")
                        case 2:
                            print("Voce escolheu a cidade de Dourados")
                        case 3:
                            print("Voce escolheu a cidade de Três Lagoas")    
                        case _:
                            print("Cidade invalida")
                case _:
                    print("Estado invalido")
        case 4:
            print("Voce escolheu a regiao Sudeste")
            print("Escolha o estado")
            print("[1] Espirito Santo")
            print("[2] Minas Gerais")
            print("[3] Rio de Janeiro")
            print("[4] Sao Paulo")
            estado = int(input("Digite o estado: "))
            match estado:
                case 1:
                    print("Voce escolheu o estado do Espirito Santo")
                    print("Escolha a cidade")
                    print("[1] Vitoria")
                    print("[2] Vila Velha")
                    print("[3] Serra")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Vitoria")
                        case 2:
                            print("Voce escolheu a cidade de Vila Velha")
                        case 3:
                            print("Voce escolheu a cidade de Serra")
                        case _:
                            print("Cidade invalida")
                case 2:
                    print("Voce escolheu o estado de Minas Gerais")
                    print("Escolha a cidade")
                    print("[1] Belo Horizonte")
                    print("[2] Uberlandia")
                    print("[3] Contagem")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Belo Horizonte")
                        case 2:
                            print("Voce escolheu a cidade de Uberlandia")
                        case 3:
                            print("Voce escolheu a cidade de Contagem")
                        case _:
                            print("Cidade invalida")
                case 3:
                    print("Voce escolheu o estado do Rio de Janeiro")
                    print("Escolha a cidade")
                    print("[1] Rio de Janeiro")
                    print("[2] Sao Goncalo")
                    print("[3] Duque de Caxias")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Rio de Janeiro")
                        case 2:
                            print("Voce escolheu a cidade de Sao Goncalo")
                        case 3:
                            print("Voce escolheu a cidade de Duque de Caxias")
                        case _:
                            print("Cidade invalida")
                case 4:
                    print("Voce escolheu o estado de Sao Paulo")
                    print("Escolha a cidade")
                    print("[1] Sao Paulo")
                    print("[2] Guarulhos")
                    print("[3] Campinas")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Sao Paulo")
                        case 2:
                            print("Voce escolheu a cidade de Guarulhos")
                        case 3:
                            print("Voce escolheu a cidade de Campinas")
                        case _:
                            print("Cidade invalida")
                case _:
                    print("Estado invalido")
        case 5:
            print("Voce escolheu a regiao Sul")
            print("Escolha o estado")
            print("[1] Parana")
            print("[2] Rio Grande do Sul")
            print("[3] Santa Catarina")
            estado = int(input("Digite o estado: "))
            match estado:
                case 1:
                    print("Voce escolheu o estado do Parana")
                    print("Escolha a cidade")
                    print("[1] Curitiba")
                    print("[2] Londrina")
                    print("[3] Maringa")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Curitiba")
                        case 2:
                            print("Voce escolheu a cidade de Londrina")
                        case 3:
                            print("Voce escolheu a cidade de Maringa")
                        case _:
                            print("Cidade invalida")
                case 2:
                    print("Voce escolheu o estado do Rio Grande do Sul")
                    print("Escolha a cidade")
                    print("[1] Porto Alegre")
                    print("[2] Caxias do Sul")
                    print("[3] Pelotas")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Porto Alegre")
                        case 2:
                            print("Voce escolheu a cidade de Caxias do Sul")
                        case 3:
                            print("Voce escolheu a cidade de Pelotas")
                        case _:
                            print("Cidade invalida")  
                case 3:
                    print("Voce escolheu o estado de Santa Catarina")
                    print("Escolha a cidade")
                    print("[1] Florianopolis")
                    print("[2] Joinville")
                    print("[3] Blumenau")
                    cidade = int(input("Digite a cidade: "))
                    match cidade:
                        case 1:
                            print("Voce escolheu a cidade de Florianopolis")
                        case 2:
                            print("Voce escolheu a cidade de Joinville")
                        case 3:
                            print("Voce escolheu a cidade de Blumenau")    
                        case _:
                            print("Cidade invalida")  
                case _:
                    print("Estado invalido")
        case _:
            print("Regiao invalida")
