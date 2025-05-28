import random

def narrativa_quartoato(vida_sandubinha):
    print("Após derrotar o Dragão, Sandubinha avança para a Torre de Contas a Receber")
    print("Ele tem duas opções:")
    print("1. Usar Azah Transmissão para voar até o topo.")
    print("2. Ir a pé, o que consome 3 pontos de vida.")

    escolha = input("Escolha 1 (Voar) e 2(ir a pé)\n")

    if escolha == "1":
        print("Sandubinha voa até o topo da torre em segurança.")
    elif escolha == "2":
        vida_sandubinha -= 3 # Sandubinha inicia a próxima batalha com -3 de vida do total acumulado das batalhas anteriores
        print("Sandubinha vai a pé e perde 3 pontos de vida.")
    else:
        print("Escolha inválida.")
        
    input("Pressione Enter para continuar...\n")

    print("A terrível torre é onde seres mágicos recebem o pagamento por ser árduo trabalho.")
    print("Dizem que a ruína perto da torre eram a cidade mais próxima do 'grito', terra natal dos Analyticaes di Glosium")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha chega ao primeiro andar da torre. Ele sente uma energia mágica mortífera vindo do topo. Sem dúvidas, Glozium estava lá...")
    print("A parede se abre e sai dela o penúltimo monstro a ser enfrentado!")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Uma estátua na forma do último herói, por que?")
    input("Pressione Enter para começar a batalha")

    return vida_sandubinha

def iniciar_batalha4(vida_sandubinha, inventario):
        vida_estatua = 25
        vida_atual = vida_sandubinha
        numeros_sorteados_por_rodada = 1
        numeros_sorteados_por_rodada_estatua = 5
        guia = False
        faturamentus = False
        estilingue = False
        azah = False
        penalidade_faturamentus = False
        penalidade_estilingue = False
        penalidade_azah = False
        atordoamento = False
        usoestilingue = 0
        turnos_atordoados = 0
        historico_batalha = []
        numero_secreto_estatua = random.randint(1, 25)
        numero_secreto_sandubinha = random.randint(1, vida_atual)

        def listar_itens_equipados():
                itens_equipados = []
                if guia: itens_equipados.append("Guia de atendimento")
                if faturamentus: itens_equipados.append("Faturamentus")
                if estilingue: itens_equipados.append("Estilingue mágico")
                if azah: itens_equipados.append("Azah Transmissão")
                return itens_equipados
        
        def rodada_sandubinha():
            nonlocal vida_estatua, penalidade_faturamentus, usoestilingue, penalidade_estilingue, atordoamento, penalidade_azah

            n = numeros_sorteados_por_rodada
            if guia: #Funcionalidades dos itens
                n = 2           
            if faturamentus:
                n = 4
            if estilingue:
                n = int(vida_estatua/2) + numeros_sorteados_por_rodada
            if azah:
                n += 10
            else:
                n = numeros_sorteados_por_rodada            

            numeros = [random.randint(1, 25) for _ in range(n)]
            dano = numero_secreto_estatua * numeros.count(numero_secreto_estatua)
            vida_estatua -= dano

            if faturamentus and dano == 0:
                penalidade_faturamentus = True
                
            if estilingue:
                if dano == 0:
                    usoestilingue += 1
                    if usoestilingue > 3:
                        penalidade_estilingue = True
                        print("Você não pode usar o Estilingue mágico mais de 3 vezes, tomou um de dano.")
                        vida_atual -= 1    
                elif dano > 0:
                        atordoamento = True
                        print("Você atordoou a estatua!")
                        print("A estatua não pode atacar nesta rodada!") 
            
            if azah and dano == 0:
                penalidade_azah = True


            return ("Sandubinha", numeros, dano, numero_secreto_estatua)

        def rodada_estatua():
            nonlocal vida_atual, penalidade_faturamentus, penalidade_estilingue, atordoamento, penalidade_azah, turnos_atordoados

            numeros = [random.randint(1, 11) for _ in range(numeros_sorteados_por_rodada_estatua)]
            dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)

            if atordoamento:
                turnos_atordoados += 1
                print("A estátua está atordoada e não pode atacar nesta rodada!")
                if turnos_atordoados > 1:
                    print("A estátua recuperou o fôlego pode atacar nesta rodada!")
                    atordoamento = False
                    turnos_atordoados = 0
                return ("Estátua", numeros, 0, numero_secreto_sandubinha)

            if penalidade_faturamentus and dano > 0:
                print("A Estátua aproveitou do seu erro e te deu mais dano que o normal!")
                dano += 2
                penalidade_faturamentus = False

            if penalidade_estilingue:
                print("A Estátua ri de você após se acertar com o próprio estilingue!")

            if atordoamento:
                print("A Estátua não pode atacar nesta rodada!")
                atordoamento = False
                return ("Estátua", numeros, 0, numero_secreto_sandubinha)
            
            if penalidade_azah:
                dano_azah = max(vida_atual - numero_secreto_estatua, 0)
                vida_atual -= dano_azah
                print("Azah ativada: como Sandubinha errou o número secreto, ele recebe um dano proporcional!")

            vida_atual -= dano
            return ("Estátua", numeros, dano, numero_secreto_sandubinha)
        
        turno = 0

        while vida_estatua > 0 and vida_atual > 0:
            print("\n--- STATUS ---\n")
            print(f"Vida do Sandubinha: {vida_atual}")
            print(f"Vida da Estátua: {vida_estatua}")

            if turno == 0:
                print("\n--- Sua vez ---\n")
                print("1. Atacar\n2. Itens\n3. Desequipar item\n4. Desistir\n")
                escolha = input("Escolha sua acao: ")

                if escolha == "1":
                    resultado = rodada_sandubinha()
                    historico_batalha.append(resultado)
                    personagem, numeros, dano, numero_secreto = resultado
                    print(f"\nVocê atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    if dano > 0:
                        print(f"Você causou {dano} de dano a Estátua!")
                    else:
                        print("Seu ataque não causou dano a Estátua.")
                    turno = 1
                elif escolha == "2":
                    item_usado = False
                    if not inventario:
                        print("Você não tem itens disponíveis agora.")
                        continue
                    print("Seus itens:")
                    for i, item in enumerate(inventario):
                        print(f"{i + 1}. {item}")
                    item_escolhido = input("Escolha o número do item para usar (ou pressione Enter para voltar): ")
                    if item_escolhido == "":
                        continue
                    if item_escolhido.isdigit():
                        index = int(item_escolhido) - 1
                        if 0 <= index < len(inventario):
                            item = inventario[index] 
                            if item == "Guia de atendimento":
                                if guia:
                                    print("Você já usou o Guia de atendimento.\n")
                                else:
                                    print("Você usou o Guia de atendimento e se fortaleceu!\n")
                                    guia = True
                                    item_usado = True
                            
                            if item == "Faturamentus":
                                if faturamentus:
                                    print("Você já usou o Faturamentus.\n")
                                else:
                                    print("Você usou o Faturamentus e se fortaleceu!\n")
                                    faturamentus = True
                                    item_usado = True
                                
                            if item == "Estilingue mágico":
                                if estilingue:
                                    print("Você já usou o Estilingue mágico.\n")
                                else:
                                    print("Você usou o Estilingue mágico e se fortaleceu!\n")
                                    estilingue = True
                                    item_usado = True
                                
                            if item == "Azah Transmissão":
                                if azah:
                                    print("Você já usou o Azah Transmissão.\n")
                                else:
                                    print("Você usou o Azah Transmissão e se fortaleceu!\n")
                                    azah = True
                                    item_usado = True
                                
                            if not any([guia, faturamentus, estilingue, azah]):
                                print(f"Você usou {item}, mas nada aconteceu.\n")
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
                    for i, item in enumerate(itens_equipados):
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
                            elif item == "Faturamentus":
                                faturamentus = False
                            elif item == "Estilingue mágico":
                                estilingue = False
                            elif item == "Azah Transmissão":
                                azah = False
                            print(f"{item} foi desequipado com sucesso!")
                            turno = 1
                        else:
                            print("Escolha inválida.")
                    else:
                        print("Escolha inválida.")
                    continue

                    
                elif escolha == "4":
                    print("Você desistiu da batalha!\n")
                    print("\nHistórico da batalha:")
                    for personagem, numeros, dano, numero_secreto in historico_batalha:
                        print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    return False, vida_atual
                else:
                    print("Opção inválida!")
                    continue
            else:
                print("\n--- Turno da Estátua ---\n")
                resultado = rodada_estatua()
                historico_batalha.append(resultado)
                personagem, numeros, dano, numero_secreto = resultado
                print(f"\nEstátua atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                if dano > 0:
                    print(f"{dano} recebido!")
                else:
                    print("Nenhum dano recebido.")
                turno = 0

        if vida_estatua <= 0:
            print("\nVocê venceu! A estátua foi derrotada!\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            input("Pressione Enter para continuar...\n")
            print("\nEstatua do último herói - ...")
            input("Pressione Enter para continuar...\n")
            print("Sandubinha - É assustador olhar para essa estátua despedaçada e ver a forma do último herói\n")
            if "Colar da estátua sagrada" not in inventario:
                print("\nSandubinha ganha o artefato [Colar da estátua sagrada]\n")
                inventario.append("Colar da estátua sagrada") #Adiciona Colar da estátua sagrada ao inventario
            print("Formato: Colar")
            print("Esse artefato permite que você sorteie 10 números por rodada, ao invés de um.")   
            print("Porém, sempre que utilizado em uma rodada, receberá 3 de dano.\n")
            return True, vida_atual
        else:
            print("Você foi derrotado pela Estátua do último herói...")
            input("Pressione Enter para continuar...\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            print("\nEstatua do último herói - ...")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
            
            return False, vida_atual