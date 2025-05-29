from batalha5 import narrativa_final, iniciar_batalhafinal


def menu_batalha1(vida_sandubinha, inventario_global):

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Iniciar jornada")
        print("2. Enfrentar Glozium agora")
        print("3. Sair do jogo")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            return False
        
        elif escolha == "2":
            narrativa_final(inventario_global)
            venceu_final, _ = iniciar_batalhafinal(vida_sandubinha, inventario_global)
            if venceu_final:
                print("Você venceu Glozium muito antes do esperado, parabéns! Final alternativo conquistado!")
            else:
                print("Você deveria ter se preparado melhor para enfrentar Glozium. O mundo foi destruído.")
            return True

        elif escolha == "3":
            print("Saindo do jogo. Até logo!")
            return True

        else:
            print("Opção inválida. Tente novamente.")

def menu_batalha(vida_sandubinha, inventario_global):
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Continuar jornada")
        print("2. Enfrentar Glozium agora")
        print("3. Sair do jogo")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            return False
        
        elif escolha == "2":
            narrativa_final(inventario_global)
            venceu_final, _ = iniciar_batalhafinal(vida_sandubinha, inventario_global)
            if venceu_final:
                print("Você venceu Glozium muito antes do esperado, parabéns! Final alternativo conquistado!")
            else:
                print("Você deveria ter se preparado melhor para enfrentar Glozium. O mundo foi destruído.")
            return True

        elif escolha == "3":
            print("Saindo do jogo. Até logo!")
            return True
        else:
            print("Opção inválida. Tente novamente.")
