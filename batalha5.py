import random

def narrativa_final(inventario):
    print("Sandubinha sente que no topo da Torre de Contas a Receber reside Glozium, é uma habilidade dos Analyticaes di Glosium.\n")
    print("Você alcançou a maestria necessária para forjar a Espada ZG, você quer forjá-la?\n")

    escolha = input("Digite 'sim' para forjar a espada ou 'não' para continuar sem ela: ").strip().lower() #strip() remove espaços extras e lower() torna tudo minúsculo
    if escolha == "sim":
        itens_necessarios = ["Colar da estátua sagrada", "Faturamentus", "Azah Transmissão", "Estilingue mágico", "Guia de atendimento"]
        if all(item in inventario for item in itens_necessarios):
            inventario.clear()  # Limpa o inventário
            inventario.append("Espada ZG")
            print("Você usou todos seus itens para formar a poderosa Espada ZG!\n")
            print("Formato: Espada")
            print("Essa espada faz com que você possa sortear 40 números de uma só vez a cada ataque.")
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
        espada_zg_usada = False
        penalidade_faturamentus = False
        penalidade_estilingue = False
        penalidade_azah = False
        atordoamento = False
        usoestilingue = 0
        turnos_atordoados = 0
        historico_batalha = []
        numero_secreto_glozium = random.randint(1, 100)
        numero_secreto_sandubinha = random.randint(1, vida_atual)

        def listar_itens_equipados():
            itens_equipados = []
            if guia: itens_equipados.append("Guia de atendimento")
            if faturamentus: itens_equipados.append("Faturamentus")
            if estilingue: itens_equipados.append("Estilingue mágico")
            if azah: itens_equipados.append("Azah Transmissão")
            if colar_estatua_sagrada: itens_equipados.append("Colar da estátua sagrada")
            if espada_zg: itens_equipados.append("Espada ZG")
            return itens_equipados


        def rodada_sandubinha():
            nonlocal vida_glozium, penalidade_faturamentus, usoestilingue, penalidade_estilingue, atordoamento, penalidade_azah, colar_estatua_sagrada, espada_zg

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
                colar_estatua_sagrada = False
            if espada_zg:
                n = 40   
                espada_zg = False    

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
                        vida_atual -= 1    
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
                    personagem, numeros, dano, numero_secreto = resultado
                    print(f"\nVocê atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    if dano > 0:
                        print(f"Você causou {dano} de dano a Glozium!")
                    else:
                        print("Seu ataque não causou dano a Glozium.")
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
                                    espada_zg_usada = True
                                    item_usado = True

                            if not any([guia, faturamentus, estilingue, azah, colar_estatua_sagrada, espada_zg]):
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
                            elif item == "Colar da estátua sagrada":
                                colar_estatua_sagrada = False
                            elif item == "Espada ZG":
                                espada_zg = False
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
                resultado = rodada_glozium()
                historico_batalha.append(resultado)
                personagem, numeros, dano, numero_secreto = resultado
                print(f"\nGlozium atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                if dano > 0:
                    print(f"{dano} recebido!")
                else:
                    print("Nenhum dano recebido.")
                turno = 0

        if vida_glozium <= 0:
            if espada_zg_usada:
                print("\nVocê venceu! Glozium foi derrotado!\n")
                print("Histórico da batalha:\n")
                for personagem, numeros, dano, numero_secreto in historico_batalha:
                    print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                print("\nSandubinha - Finalmente, Glozium está eliminado por completo, irei retomar a minha família\n")
                print("O Herói derrotou Glozium, o mundo agora poderá voltar a seus tempos de alegria. Muito obrigado, herói!\n")
                print("Fim de jogo!")
                return True, vida_atual
            else:
                print("\nVocê venceu! Glozium foi derrotado!\n")
                print("Histórico da batalha:\n")
                for personagem, numeros, dano, numero_secreto in historico_batalha:
                    print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    
                    
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
                return True, vida_atual
            
        else:
            print("Você foi derrotado por Glozium...")
            input("Pressione Enter para continuar...\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            print("\nGlozium - Finalmente! um herói bosta que apenas aumentou meus poderes.")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
            
            return False, vida_atual