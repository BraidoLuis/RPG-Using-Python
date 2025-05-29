import random

def narrativa_segundoato():
    print("\nVocê avançou para as Cavernas de Faturamentus...")
    input("Pressione Enter para continuar...\n")
    print("\nExiste sempre um preço a se pagar pela cura do corpo e da alma, após a floresta do atendimentus")
    print("seu preço é calculado de acordo com o tipo de contrato divino que você tem")
    input("Pressione Enter para continuar...\n")

    print("Percorrendo a caverna segurando uma tocha. Sandubinha escuta sons assustadores de grunhidos")
    input("Pressione Enter para continuar...\n")
    print("O cenário é iluminado por minérios misteriosos. Anciões fantasmas anotam diversas coisas em pergaminhos,")
    print("estão todos muito ocupados para falar algo a Sandubinha.")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Que tipo de situação é essa?")
    input("Pressione Enter para continuar...\n")

    print("Um monstro em forma de urso surge e diz a Sandubinha")
    input("Pressione Enter para continuar...\n")

    print("Urso Sangrento - Finalmente diversão, esses anciões só sabem ficar anotando essas coisas inúteis.")
    print("Vamos lutar heroizinho!")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Criatura desagradável, não me deu tempo nem de tomar uma água, então bora nessa!")
    input("Pressione Enter para começar a batalha")

def iniciar_batalha2(vida_sandubinha, inventario):
        vida_urso = 6
        vida_atual = vida_sandubinha
        numeros_sorteados_por_rodada = 1
        numeros_sorteados_por_rodada_urso = 2
        numero_secreto_urso = random.randint(1, 6)
        numero_secreto_sandubinha = random.randint(1, vida_atual)
        guia = False
        historico_batalha = []

        def listar_itens_equipados(): #Função para listar os itens equipados, caso a tag seja True, o item entra na lista
            itens_equipados = []
            if guia: itens_equipados.append("Guia de atendimento")
            
            return itens_equipados

        def rodada_sandubinha():
                nonlocal vida_urso, guia
                
                if guia: #Funcionalidade do item
                    n = 2
                else:
                    n = numeros_sorteados_por_rodada

                numeros = [random.randint(1, 6) for _ in range(n)]
                dano = numero_secreto_urso * numeros.count(numero_secreto_urso)
                vida_urso -= dano

                return ("Sandubinha", numeros, dano, numero_secreto_urso)

        def rodada_urso():
            nonlocal vida_atual
            
            numeros = [random.randint(1, 7) for _ in range(numeros_sorteados_por_rodada_urso)]
            dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)
            vida_atual -= dano
            return ("Urso", numeros, dano, numero_secreto_sandubinha)
        
        turno = 0

        while vida_urso > 0 and vida_atual > 0:
            print("\n--- STATUS ---\n")
            print(f"Vida do Sandubinha: {vida_atual}")
            print(f"Vida do Urso: {vida_urso}")

            if turno == 0:
                print("\n--- Sua vez ---")
                print("1. Atacar\n2. Itens\n3. Desequipar item\n4. Desistir\n")
                escolha = input("Escolha sua ação: ")

                if escolha == "1":
                    resultado = rodada_sandubinha()
                    historico_batalha.append(resultado)
                    personagem, numeros, dano, numero_secreto = resultado
                    print(f"\nVocê atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    if dano > 0:
                        print(f"Você causou {dano} de dano ao Urso!")
                    else:
                        print("Seu ataque não causou dano ao Urso.")
                    turno = 1
                elif escolha == "2":
                    item_usado = False
                    if not inventario:
                        print("Você não tem itens disponíveis agora.")
                        continue
                    print("Seus itens:")
                    for i, item in enumerate(inventario): #Mostra os itens com índice +1, pois por padrão inicia no 0
                        print(f"{i + 1}. {item}")
                    item_escolhido = input("Escolha o número do item para usar (ou pressione Enter para voltar): ")
                    if item_escolhido == "":
                        continue
                    if item_escolhido.isdigit(): #Verifica se somente números estão sendo passados
                        index = int(item_escolhido) - 1 #Retira o 1 que tinha sido somado no índice
                        if 0 <= index < len(inventario): #Confirma o índice do número na lista   
                            item = inventario[index] #Obs: não usar .pop pois exclui totalmente o item do inventario
                            if item == "Guia de atendimento":
                                if guia:
                                    print("Você já usou o Guia de atendimento.")
                                else:
                                    print("Você usou o Guia de atendimento e se fortaleceu!")
                                    guia = True
                                    item_usado = True

                            else:
                                print(f"Você usou {item}, mas nada aconteceu.")
                            if item_usado:
                                turno = 1
                        else:
                            print("Item inválido.")
                    continue
                elif escolha == "3":
                    itens_equipados = listar_itens_equipados()
                    if not itens_equipados:
                        print("Você não tem itens equipados no momento.")
                        continue

                    print("Itens equipados:")
                    
                    for i, item in enumerate(itens_equipados): #Mostra os itens que estão equipados
                        print(f"{i + 1}. {item}")

                    escolha_item = input("Escolha o número do item que deseja desequipar (ou Enter para voltar): ").strip()
                    if escolha_item == "":
                        continue
                    elif escolha_item.isdigit():
                        index = int(escolha_item) - 1
                        if 0 <= index < len(itens_equipados):
                            item = itens_equipados[index]
                            if item == "Guia de atendimento":
                                guia = False                        
                        turno = 1
                    else:
                        print("Escolha inválida.")
                        continue
                elif escolha == "4":
                    print("Você desistiu da batalha!")
                    for personagem, numeros, dano, numero_secreto in historico_batalha:
                        print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    return False
                else:
                    print("Opção inválida!")
                    continue
            else:
                print("\n--- Turno do Urso ---")
                resultado = rodada_urso()
                historico_batalha.append(resultado)
                personagem, numeros, dano, numero_secreto = resultado
                print(f"\nUrso atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                if dano > 0:
                    print(f"{dano} recebido!")
                else:
                    print("Nenhum dano recebido.")
                
                turno = 0

        if vida_urso <= 0:
            print("\nVocê venceu! O Urso foi derrotado!")
            input("Pressione Enter para continuar...\n")
            print("Ancião faturador - Muito obrigado, mas tô ocupado demais para agradecimentos longos, tome o artegato sagrado e siga em frente\n")
            if "Faturamentus" not in inventario:
                print("Sandubinha ganha o artefato [Faturamentus] e o coloca no inventário.\n")
                print("Formato: Placa de pedra")
                print("Esse artefato permite que você sorteie quatro números por rodada, ao invés de um.")
                print("porém, caso você erre o número secreto do oponente, você recebe 2 de dano a mais no próximo ataque do oponente")
                inventario.append("Faturamentus")
            print("Histórico da batalha:")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            
            return True, vida_atual
            
        else:
            print("\nVocê foi derrotado pelo Urso...")
            input("Pressione Enter para continuar...\n")
            print("Ancião faturador - Herói merda, nem para cumprir o trabalho dele, estamos perdidos\n")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!")
            print("Histórico da batalha:")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            return False, vida_atual