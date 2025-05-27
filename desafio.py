import random

vida_sandubinha = 5
batalhas_vencidas = 0
inventario_global = []

def narrativa_inicial():
    print("Sandubinha - Então você é meu primeiro desafio nessa floresta encantada?\n")
    input("Pressione Enter para continuar...\n")

    print("Monstro - Bem vindo, vejo que você é um dos escolhidos para enfraquecer Glozium,")
    print("meu nome é *Processus Ministerii*, sou o ser mágico que atende as almas feridas,")
    print("envio os informativos disso às cavernas de *Faturamentus*.\n") 
    input("Pressione Enter para continuar...\n")

    print("Processus - Você não irá lutar comigo, mas sim contra esse ser criado por Glozium.")
    print("Seres mágicos do meu tipo não podem ser afetados por Glozium,")
    print("mas também não podem lutar contra ele. Glozium me atrapalha,")
    print("me desconcentra e provoca erros.\n")
    input("Pressione Enter para continuar...\n")

    print("Surge entre as pernas do grande monstro um ser humanóide, da altura de Sandubinha.\n")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Primeiro, não é 'enfraquecer', vou dar um fim total em Glozium...")
    print("Venha monstro!\n")
    input("Pressione Enter para começar a batalha!\n")

def iniciar_batalha(vida_sandubinha, inventario):
    vida_monstro = 3
    vida_atual = vida_sandubinha
    numeros_sorteados_por_rodada = 1
    numero_secreto_monstro = random.randint(1, 3)
    numero_secreto_sandubinha = random.randint(1, vida_sandubinha)
    historico_batalha = []

    def rodada_sandubinha():
        nonlocal vida_monstro
        n = numeros_sorteados_por_rodada
        numeros = [random.randint(1, 3) for _ in range(n)]
        dano = numero_secreto_monstro * numeros.count(numero_secreto_monstro)
        vida_monstro -= dano
        return ("Sandubinha", numeros, dano, numero_secreto_monstro)

    def rodada_monstro():
        nonlocal vida_atual
        numeros = [random.randint(1, 5) for _ in range(numeros_sorteados_por_rodada)]
        dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)
        vida_atual -= dano
        return ("Monstro", numeros, dano, numero_secreto_sandubinha)

    turno = 0

    while vida_monstro > 0 and vida_atual > 0:
        print("\n--- STATUS ---")
        print(f"Vida do Sandubinha: {vida_atual}")
        print(f"Vida do Monstro: {vida_monstro}")

        if turno == 0:
            print("\n--- Sua vez ---")
            print("1. Atacar\n2. Desistir")
            escolha = input("Escolha sua acao: ")

            if escolha == "1":
                resultado = rodada_sandubinha()
                historico_batalha.append(resultado)
                turno = 1
            elif escolha == "2":
                print("Você desistiu da batalha!")
                print("\nHistórico da batalha:")
                for personagem, numeros, dano, numero_secreto in historico_batalha:
                    print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                return False, vida_atual
                
            else:
                print("Opção inválida!")
                continue
        else:
            print("\n--- Turno do Monstro ---")
            resultado = rodada_monstro()
            historico_batalha.append(resultado)
            turno = 0

    if vida_monstro <= 0:
        print("\nVocê venceu! O Monstro foi derrotado!\n")
        print("Histórico da batalha:\n")
        for personagem, numeros, dano, numero_secreto in historico_batalha:
            print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
        input("Pressione Enter para continuar...\n")
        if "Guia de atendimento" not in inventario:
            print("Formato: Pergaminho")
            print("\nProcessus Ministerii - Muito Obrigado, tome o artefato [Guia de atendimento] e vá para o próximo desafio\n")
            
            print("Esse artefato permite que você sorteie dois números por rodada, ao invés de um")
            inventario.append("Guia de atendimento")
        
        return True, vida_atual
    else:
        print("Você foi derrotado pelo Monstro...")
        input("Pressione Enter para continuar...\n")
        print("Histórico da batalha:\n")
        for personagem, numeros, dano, numero_secreto in historico_batalha:
            print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
        print("\nProcessus Ministerii - Oh não, o mundo será mais uma vez destruído por Glozium")
        print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
        
        return False, vida_atual
    
    

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

def iniciar_batalha2(vida_sandubinha, inventario):
        vida_urso = 6
        vida_atual = vida_sandubinha
        numeros_sorteados_por_rodada = 1
        numeros_sorteados_por_rodada_urso = 2
        numero_secreto_urso = random.randint(1, 6)
        numero_secreto_sandubinha = random.randint(1, vida_atual)
        guia = False
        historico_batalha = []

        estado_original = {
        "guia": guia,
        }

        def restaurar_estado():
            nonlocal guia
            guia = estado_original["guia"]
            print("\nTodos os efeitos de itens foram removidos. Sandubinha voltou ao estado normal.\n")

        def rodada_sandubinha():
                nonlocal vida_urso, guia
                
                if guia:
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
                    restaurar_estado()
                    print("Você desequipou seus itens.")
                    turno = 1
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
            
            return True
            
        else:
            print("\nVocê foi derrotado pelo Urso...")
            input("Pressione Enter para continuar...\n")
            print("Ancião faturador - Herói merda, nem para cumprir o trabalho dele, estamos perdidos\n")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!")
            print("Histórico da batalha:")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            return False
        
def narrativa_terceiroato(inventario):
    print("\nUma vila mágica que recebe cobranças vindas das cavernas de Faturamentus. Os moradores entregam as mensagens na Torre")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha é bem recebido em sua chegada. Ele é convidado para um jantar ritualístico com comidas típicas")
    input("Pressione Enter para continuar...\n")

    print("Os moradores contam que o monstro a ser enfrentado é um ser que voa. Para atacá-lo, o Sandubinha terá que derrubar o monstro e usar sua espada.")
    print("Então, dão a ele um item, o [Estilingue mágico]")
    if "Estilingue mágico" not in inventario:
            print("\nVocê recebeu o item [Estilingue mágico] dos moradores\n")
            print("Formato: Estilingue")
            print("Esse artefato permite que você atordoe os inimigos por uma rodada, porém,")
            print("caso você erre o número secreto do oponente mais do que 3 vezes, você recebe 1 de dano a cada vez que você utiliza após isso.")
            inventario.append("Estilingue mágico")
    input("Pressione Enter para continuar...\n")

    print("Logo, um monstro em forma de dragão surge voando e diz:")
    print("Dragão da transmissão - Você já tem sua arma...já fui guardião dessas terras e transmitia as mensagens à torre.")
    print("Mas milênios atrás Glozium me tornou seu escravo, sou obrigado a lutar com toda fúria. Livre-me do sofrimento...")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Você também está preso a um destino que não escolheu, vou te libertar!")
    return inventario

def iniciar_batalha3(vida_sandubinha, inventario):
        vida_dragao = 12
        vida_atual = vida_sandubinha
        numeros_sorteados_por_rodada = 1
        numeros_sorteados_por_rodada_dragao = 3
        guia = False
        faturamentus = False
        estilingue = False
        penalidade_faturamentus = False
        penalidade_estilingue = False
        atordoamento = False
        usoestilingue = 0
        turnos_atordoados = 0
        historico_batalha = []
        numero_secreto_dragao = random.randint(1, 12)
        numero_secreto_sandubinha = random.randint(1, vida_atual)
        
    

        estado_original = {
            "guia": guia, 
            "faturamentus": faturamentus,
            "estilingue": estilingue
        }

        def restaurar_estado():
            nonlocal guia, faturamentus, estilingue
            guia = estado_original["guia"]
            faturamentus = estado_original["faturamentus"]
            estilingue = estado_original["estilingue"]
            print("\nTodos os efeitos de itens foram removidos. Sandubinha voltou ao estado normal.\n")
        
        

        def rodada_sandubinha():
            nonlocal vida_dragao, penalidade_faturamentus, usoestilingue, penalidade_estilingue, atordoamento,vida_atual, turnos_atordoados
            dano = 0
            n = numeros_sorteados_por_rodada
            numeros = [] # Adiciona uma lista vazia para não causar dano, antes de +3 usos

            if guia:
                n = 2
            if faturamentus:
                n = 4
            if estilingue:
                if not atordoamento: #Antes de atordoar, adiciona 1 aos usos
                    usoestilingue += 1
                    n = int(vida_dragao / 2)
                    numeros = [random.randint(1, 12) for _ in range(n)]
                    acertou_pedra = numero_secreto_dragao in numeros

                    if acertou_pedra: #Caso estilingue acerte, atordoa o dragão
                        print("Você acertou o Dragão com a pedra do Estilingue! Ele está atordoado e agora pode ser atingido!")
                        atordoamento = True
                        
                    else:
                        print(f"Você usou o Estilingue ({usoestilingue}/3), mas errou a pedra.") #Quantidade de usos do estilingue

                    if usoestilingue > 3: #Caso passe de 3 usos, perde 1 de vida
                        print("Você usou o Estilingue mais de 3 vezes e se feriu com o recuo! Perdeu 1 de vida.")
                        vida_atual -= 1
                        penalidade_estilingue = True
                        

                    return ("Sandubinha", numeros, 0, numero_secreto_dragao)
                else: #Dragão atordoado, pode receber dano
                    n = numeros_sorteados_por_rodada
                    if guia:
                        n = 2
                    if faturamentus:
                        n = 4
                    numeros = [random.randint(1, 12) for _ in range(n)]
                    dano = numero_secreto_dragao * numeros.count(numero_secreto_dragao)
                    vida_dragao -= dano
                    atordoamento = False
                    
            else:
                    # Sem estilingue — só pode causar dano se dragão já estiver atordoado
                numeros = [random.randint(1, 12) for _ in range(n)]
                if not atordoamento:
                    print("O Dragão está voando e invulnerável. Você precisa acertá-lo com o Estilingue primeiro!")
                    dano = 0
                else:
                    dano = numero_secreto_dragao * numeros.count(numero_secreto_dragao)
                    vida_dragao -= dano
                    atordoamento = False

            if faturamentus and dano == 0:
                penalidade_faturamentus = True

            return ("Sandubinha", numeros, dano, numero_secreto_dragao)

        def rodada_dragao():
            nonlocal vida_atual, penalidade_faturamentus, penalidade_estilingue, atordoamento, turnos_atordoados
            numeros = [random.randint(1, 9) for _ in range(numeros_sorteados_por_rodada_dragao)]
            dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)

            if atordoamento:
                turnos_atordoados += 1
                print("O Dragão está atordoado e não pode atacar nesta rodada!")
                if turnos_atordoados > 1:
                    print("O Dragão recuperou o fôlego pode atacar nesta rodada!")
                    atordoamento = False
                    turnos_atordoados = 0
                return ("Dragão", [], 0, numero_secreto_sandubinha)

            if penalidade_faturamentus and dano > 0:
                print("O dragão aproveitou do seu erro e te deu mais dano que o normal!")
                dano += 2
            penalidade_faturamentus = False

            if penalidade_estilingue:
                print("O dragão ri de você após se acertar com o próprio estilingue!")

            vida_atual -= dano
            return ("Dragão", numeros, dano, numero_secreto_sandubinha)

        turno = 0

        while vida_dragao > 0 and vida_atual > 0:
            print("\n--- STATUS ---\n")
            print(f"Vida do Sandubinha: {vida_atual}")
            print(f"Vida do Dragão: {vida_dragao}")

            if turno == 0:
                print("\n--- Sua vez ---\n")
                print("1. Atacar\n2. Itens\n3. Desequipar item\n4. Desistir\n")
                escolha = input("Escolha sua acao: ")

                if escolha == "1":
                    resultado = rodada_sandubinha()
                    historico_batalha.append(resultado)
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
                                else :
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
                    
                            if not any([guia, faturamentus, estilingue]):
                                print(f"Você usou {item}, mas nada aconteceu.\n")

                            if item_usado:
                                turno = 1
                            
                        else:
                            print("Item inválido.")
                    continue                                                                 
                elif escolha == "3":
                    restaurar_estado()
                    print("Você desequipou seus itens.")
                    turno = 1
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
                print("\n--- Turno do Dragão ---\n")
                resultado = rodada_dragao()
                historico_batalha.append(resultado)
                turno = 0

        if vida_dragao <= 0:
            print("\nVocê venceu! O Dragão foi derrotado!\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            input("Pressione Enter para continuar...\n")
            if "Azah Transmissão" not in inventario:
                print("\nSandubinha ganha o artefato [Azah Transmissão]\n")
                print("Formato: Capa")
                print("Esse artefato permite que você sorteie 10 números por rodada, ao invés de um.")
                print("Porém, se você errar o número secreto do oponente, receberá o proximo dano proporcional do último número sorteado.")
                inventario.append("Azah Transmissão")
            print("\nDragão - Muito obrigado, todo herói evitava essa batalha e seguia para a torre, agora sou livre!")
            input("Pressione Enter para continuar...\n")
            print("Sandubinha - Evitava? E dá pra seguir sem lutar?? Como assim????\n")
            return True, vida_atual
        else:
            print("Você foi derrotado pelo Dragão...")
            input("Pressione Enter para continuar...\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            print("\nDragão - Sinto muito herói, que sua alma seja livre")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
            
            return False, vida_atual

def narrativa_quartoato(vida_sandubinha):
    print("Após derrotar o Dragão, Sandubinha avança para a Torre de Contas a Receber")
    print("Ele tem duas opções:")
    print("1. Usar Azah Transmissão para voar até o topo.")
    print("2. Ir a pé, o que consome 3 pontos de vida.")

    escolha = input("Escolha 1 (Voar) e 2(ir a pé)\n")

    if escolha == "1":
        print("Sandubinha voa até o topo da torre em segurança.")
    elif escolha == "2":
        vida_sandubinha -= 3
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

        estado_original = {
            "guia": guia, 
            "faturamentus": faturamentus,
            "estilingue": estilingue,
            "azah": azah
        }

        def restaurar_estado():
            nonlocal guia, faturamentus, estilingue, azah
            guia = estado_original["guia"]
            faturamentus = estado_original["faturamentus"]
            estilingue = estado_original["estilingue"]
            azah = estado_original["azah"]
            print("\nTodos os efeitos de itens foram removidos. Sandubinha voltou ao estado normal.\n")
        
        def rodada_sandubinha():
            nonlocal vida_estatua, penalidade_faturamentus, usoestilingue, penalidade_estilingue, atordoamento, penalidade_azah

            n = numeros_sorteados_por_rodada
            if guia:
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
                        vida_sandubinha -= 1    
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
                    restaurar_estado()
                    print("Você desequipou seus itens.")
                    turno = 1
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
                print("Formato: Colar")
                print("Esse artefato permite que você sorteie 10 números por rodada, ao invés de um.")   
                print("Porém, sempre que utilizado em uma rodada, receberá 3 de dano.")
                inventario.append("Colar da estátua sagrada")
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
        
def narrativa_final(inventario):
    print("Sandubinha sente que no topo da Torre de Contas a Receber reside Glozium, é uma habilidade dos Analyticaes di Glosium.")
    print("Você alcançou a maestria necessária para forjar a Espada ZG, você quer forjá-la?\n")
    escolha = input("Digite 'sim' para forjar a espada ou 'não' para continuar sem ela: ").strip().lower() #strip() remove espaços extras e lower() torna tudo minúsculo
    if escolha == "sim":
        itens_necessarios = ["Colar da estátua sagrada", "Faturamentus", "Azah Transmissão", "Estilingue mágico", "Guia de Atendimento"]
        if all(item in inventario for item in itens_necessarios):
            print("Você usou todos seus itens para formar a poderosa Espada ZG!")
            print("Formato: Espada")
            print("Essa espada faz com que você possa sortear 40 números de uma só vez a cada ataque.")
            inventario.append("Espada ZG")
        else:
            print("Você não tem todos os itens, não pode forjar a Espada ZG.")
    elif escolha == "não":
        print("Você decidiu não forjar a Espada ZG.")
    else:
        print("Escolha inválida")
    print("Sandubinha entra na sala do chefe e se depara com a presença arrepiante de Glozium sentado no trono.\n")

    pulo = input("Você deseja pular o diálogo entre Sandubinha e Glozium? Digite 'sim' ou 'não'\n").strip().lower()
    if pulo == "sim":
        print("Você pulou o diálogo.")
        return inventario
    elif pulo == "não":
        print("Glozium - Um rato invadiu meu recinto; talvez sirva de alimento para meus escravos\n")
        input("Pressione Enter para continuar...\n")

        print("Sandubinha - Então você é Glozium? Não é mais aterrorizante que as criaturas apodrecidas que encontrei.\n")
        input("Pressione Enter para continuar...\n")


        print("Glozium - ha ha ha ha! que petulante.")
        print("Chegou a época, mas mandaram um pobre coitado; péssima ideia.\n")
        input("Pressione Enter para continuar...\n")

        print("Sandubinha - Vou te destruir, Glozium, e garantir sua aniquilação total e permanente!\n")
        print("E o que um garoto com cabeça de hambúrguer pode fazer contra um monstro milenar, que presenciou eventos tão singulares,")
        print("que caminhou sobre a superfície de vulcões e subjugou a humanidade?\n")
        input("Pressione Enter para continuar...\n")

        print("Sandubinha lança sua espada girando no ar que fere o monstro e retorna a sua mão.\n")

        print("Sandubinha - Não subestime alguém com cabeça de hambúrguer, sou um descendente dos Analycaties di Glosium.")
        print("Te procurei em cada canto do inferno para reduzir você a Zero.\n")
        input("Pressione Enter para continuar...\n")

        print("Glozium - Interessante, aceito seu pedido de batalha!")
        return inventario

def iniciar_batalhafinal(vida_sandubinha, inventario):
        vida_glozium = 100
        vida_atual = vida_sandubinha
        numeros_sorteados_por_rodada = 1
        numeros_sorteados_por_rodada_glozium = 10
        guia = False
        faturamentus = False
        estilingue = False
        azah = False
        colar_estatua_sagrada = False
        espada_zg = False
        penalidade_faturamentus = False
        penalidade_estilingue = False
        penalidade_azah = False
        atordoamento = False
        usoestilingue = 0
        turnos_atordoados = 0
        historico_batalha = []
        numero_secreto_glozium = random.randint(1, 100)
        numero_secreto_sandubinha = random.randint(1, vida_atual)

        estado_original = {
            "guia": guia,
            "faturamentus": faturamentus,
            "estilingue": estilingue,
            "azah": azah,
            "colar_estatua_sagrada": colar_estatua_sagrada,
            "espada_zg": espada_zg
        }

        def restaurar_estado():
            nonlocal guia, faturamentus, estilingue, azah, espada_zg
            guia = estado_original["guia"]
            faturamentus = estado_original["faturamentus"]
            estilingue = estado_original["estilingue"]
            azah = estado_original["azah"]
            espada_zg = estado_original["espada_zg"]
            print("\nTodos os efeitos de itens foram removidos. Sandubinha voltou ao estado normal.\n")


        def rodada_sandubinha():
            nonlocal vida_glozium, penalidade_faturamentus, usoestilingue, penalidade_estilingue, atordoamento, penalidade_azah

            n = numeros_sorteados_por_rodada
            if guia:
                n = 2
            if faturamentus:
                n = 4
            if estilingue:
                n = int(vida_glozium/2) + numeros_sorteados_por_rodada
            if azah:
                n += 10
            if colar_estatua_sagrada:
                n += 10
            if espada_zg:
                n = 40       

            numeros = [random.randint(1, 100) for _ in range(n)]
            dano = numero_secreto_glozium * numeros.count(numero_secreto_glozium)
            vida_glozium -= dano

            if faturamentus and dano == 0:
                penalidade_faturamentus = True
                
            if estilingue:
                if dano == 0:
                    usoestilingue += 1
                    if usoestilingue > 3:
                        penalidade_estilingue = True
                        print("Você não pode usar o Estilingue mágico mais de 3 vezes, tomou um de dano.")
                        vida_sandubinha -= 1    
                elif dano > 0:
                        atordoamento = True
                        print("Você atordoou a estatua!")
                        print("A estatua não pode atacar nesta rodada!") 
            
            if azah and dano == 0:
                penalidade_azah = True

            if colar_estatua_sagrada:
                vida_atual -= 3

            return ("Sandubinha", numeros, dano, numero_secreto_glozium)
        
        def rodada_glozium():
            nonlocal vida_atual, penalidade_faturamentus, penalidade_estilingue, atordoamento, penalidade_azah, turnos_atordoados

            numeros = [random.randint(1, 13) for _ in range(numeros_sorteados_por_rodada_glozium)]
            dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)

            if atordoamento:
                turnos_atordoados += 1
                print("Glozium está atordoado e não pode atacar nesta rodada!")
                if turnos_atordoados > 1:
                    print("Glozium recuperou o fôlego pode atacar nesta rodada!")
                    atordoamento = False
                    turnos_atordoados = 0
                return ("Glozium", numeros, 0, numero_secreto_sandubinha)

            if penalidade_faturamentus and dano > 0:
                print("Glozium aproveitou do seu erro e te deu mais dano que o normal!")
                dano += 2
                penalidade_faturamentus = False

            if penalidade_estilingue:
                print("Glozium ri de você após se acertar com o próprio estilingue!")

            if atordoamento:
                print("Glozium não pode atacar nesta rodada!")
                atordoamento = False
                return ("Glozium", numeros, 0, numero_secreto_sandubinha)
            
            if penalidade_azah:
                dano_azah = max(vida_atual - numero_secreto_glozium, 0)
                vida_atual -= dano_azah
                print("Azah ativada: como Sandubinha errou o número secreto, ele recebe um dano proporcional!")

            vida_atual -= dano
            return ("Glozium", numeros, dano, numero_secreto_sandubinha)
        
        turno = 0

        while vida_glozium > 0 and vida_atual > 0:
            print("\n--- STATUS ---\n")
            print(f"Vida do Sandubinha: {vida_atual}")
            print(f"Vida do Glozium: {vida_glozium}")

            if turno == 0:
                print("\n--- Sua vez ---\n")
                print("1. Atacar\n2. Itens\n3. Desequipar item\n4. Desistir\n")
                escolha = input("Escolha sua acao: ")

                if escolha == "1":
                    resultado = rodada_sandubinha()
                    historico_batalha.append(resultado)
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

                            if item == "Colar da estátua sagrada":
                                if colar_estatua_sagrada:
                                    print("Você já usou o Colar da estátua sagrada.\n")
                                else:
                                    print("Você usou o Colar da estátua sagrada e se fortaleceu!\n")
                                    colar_estatua_sagrada = True
                                    item_usado = True

                            if item == "Espada ZG":
                                if espada_zg:
                                    print("Você já usou a Espada ZG.\n")
                                else:
                                    print("Você usou a Espada ZG e se fortaleceu!\n")
                                    espada_zg = True
                                    item_usado = True

                            if not any([guia, faturamentus, estilingue, azah, colar_estatua_sagrada, espada_zg]):
                                print(f"Você usou {item}, mas nada aconteceu.\n")

                            if item_usado:
                                turno = 1
                            
                        else:
                            print("Item inválido.")
                    continue                                                                 
                elif escolha == "3":
                    restaurar_estado(guia)
                    print("Você desequipou seus itens.")
                    turno = 1
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
                resultado = rodada_glozium()
                historico_batalha.append(resultado)
                turno = 0

        if vida_glozium <= 0:
            if espada_zg:
                print("\nVocê venceu! Glozium foi derrotado!\n")
                print("Histórico da batalha:\n")
                for personagem, numeros, dano, numero_secreto in historico_batalha:
                    print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    input("Pressione Enter para continuar...\n")

                print("Sandubinha - Finalmente, Glozium está eliminado por completo, irei retomar a minha família\n")
                print("O Herói derrotou Glozium, o mundo agora poderá voltar a seus tempos de alegria. Muito obrigado, herói!\n")
                print("Fim de jogo!")
                return True, vida_atual
            else:
                print("\nVocê venceu! Glozium foi derrotado!\n")
                print("Histórico da batalha:\n")
                for personagem, numeros, dano, numero_secreto in historico_batalha:
                    print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    input("Pressione Enter para continuar...\n")
                    
                print("Glozium - Você me derrotou com armas tão simples, impressionante, mas irei retornar no ano seguinte.\n")
                input("Pressione Enter para continuar...\n")

                print("Sandubinha - ... retornarei envergonhado para minha família, mas ao menos serei feliz\n")
                input("Pressione Enter para continuar...\n")

                print("Sandubinha começa a se enrijecer como pedra...\n")
                input("Pressione Enter para continuar...\n")

                print("Glozium - Você me derrotou, mas suguei sua energia vital, você irá se transformar em minha estátua da entrada da torre hahaha")
                input("Pressione Enter para continuar...\n")

                print("Sandubinha - Maldito!...Eu...nunc...ir...[Virou pedra].\n")
                input("Pressione Enter para continuar...\n")

                print("O herói derrotou Glozium ao custo de sua alma, o mundo seguirá normalmente por mais 1 ano...Fim de jogo!\n")
            
        else:
            print("Você foi derrotado por Glozium...")
            input("Pressione Enter para continuar...\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            print("\nGlozium - Finalmente! um herói bosta que apenas aumentou meus poderes.")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
            
            return False, vida_atual

def main():
    global batalhas_vencidas, inventario_global
    while True:
            
            inventario_global = []
            batalhas_vencidas = 0
            vida_total = vida_sandubinha + 2 * batalhas_vencidas
            narrativa_inicial()
            venceu_primeira, vida_total = iniciar_batalha(vida_total, inventario_global)

            if venceu_primeira:
                batalhas_vencidas += 1
                vida_total = vida_sandubinha + 2 * batalhas_vencidas
                narrativa_segundoato()
                venceu_segunda = iniciar_batalha2(vida_total, inventario_global)

                if venceu_segunda:
                    batalhas_vencidas += 1
                    vida_total = vida_sandubinha + 2 * batalhas_vencidas
                    narrativa_terceiroato(inventario_global)
                    venceu_terceira, vida_total = iniciar_batalha3(vida_total, inventario_global)

                    if venceu_terceira:
                        batalhas_vencidas += 1
                        vida_total = vida_sandubinha + 2 * batalhas_vencidas
                        vida_total = narrativa_quartoato(vida_total)
                        venceu_quarta, vida_total = iniciar_batalha4(vida_total, inventario_global)

                        if venceu_quarta:
                            batalhas_vencidas += 1
                            vida_total = vida_sandubinha + 2 * batalhas_vencidas
                            inventario_global = narrativa_final(inventario_global)
                            venceu_final, vida_total = iniciar_batalhafinal(vida_total, inventario_global)
                            
                            if venceu_final:
                                break
                        else:
                            print("Você foi derrotado na batalha final...")
                    else:
                        print("\nVocê foi derrotado no terceiro ato...")
                else:
                    print("\nVocê foi derrotado no segundo ato...")
            else:
                print("\nVocê foi derrotado no primeiro ato...")

            print("\nDeseja jogar novamente? (s/n)")
            if input("> ").lower() != "s":
                print("Fim de jogo. Obrigado por jogar!")
                break
# Início do jogo

main()