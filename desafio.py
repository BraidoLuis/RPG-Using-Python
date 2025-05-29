from batalha1 import narrativa_inicial, iniciar_batalha
from batalha2 import narrativa_segundoato, iniciar_batalha2
from batalha3 import narrativa_terceiroato, iniciar_batalha3
from batalha4 import narrativa_quartoato, iniciar_batalha4
from batalha5 import narrativa_final, iniciar_batalhafinal
from menus_batalhas import menu_batalha1, menu_batalha

#Importa todas as narrativas, menus e batalhas dos arquivos

vida_sandubinha = 5
batalhas_vencidas = 0
inventario_global = []

def main():
    global batalhas_vencidas, inventario_global
    while True:
            
            inventario_global = []
            batalhas_vencidas = 0
            vida_total = vida_sandubinha + 2 * batalhas_vencidas
            narrativa_inicial()
            if menu_batalha1(vida_total, inventario_global):
                    break
            venceu_primeira, vida_total = iniciar_batalha(vida_total, inventario_global)

            if venceu_primeira:
                batalhas_vencidas += 1
                vida_total = vida_sandubinha + 2 * batalhas_vencidas
                narrativa_segundoato()
                if menu_batalha(vida_total, inventario_global):
                    break
                venceu_segunda, vida_total = iniciar_batalha2(vida_total, inventario_global)

                if venceu_segunda:
                    batalhas_vencidas += 1
                    vida_total = vida_sandubinha + 2 * batalhas_vencidas
                    narrativa_terceiroato(inventario_global)
                    if menu_batalha(vida_total, inventario_global):
                        break
                    venceu_terceira, vida_total = iniciar_batalha3(vida_total, inventario_global)

                    if venceu_terceira:
                        batalhas_vencidas += 1
                        vida_total = vida_sandubinha + 2 * batalhas_vencidas
                        vida_total = narrativa_quartoato(vida_total)
                        if menu_batalha(vida_total, inventario_global):
                            break
                        venceu_quarta, vida_total = iniciar_batalha4(vida_total, inventario_global)

                        if venceu_quarta:
                            batalhas_vencidas += 1
                            vida_total = vida_sandubinha + 2 * batalhas_vencidas
                            inventario_global = narrativa_final(inventario_global)
                            venceu_final, vida_total = iniciar_batalhafinal(vida_total, inventario_global)                            
                            if venceu_final:
                                break
                            else:
                                print("\nVocê foi derrotado na batalha final...")
                        else:
                            print("\nVocê foi derrotado no quarto ato...")
                    else:
                        print("\nVocê foi derrotado no terceiro ato...")
                else:
                    print("\nVocê foi derrotado no segundo ato...")
            else:
                print("\nVocê foi derrotado no primeiro ato...")

            print("\nDeseja jogar novamente? (s/n)")
            if input("> ").lower() != "s": #.lower garante que seja minúsculo como recebe o código
                print("Fim de jogo. Obrigado por jogar!")
                break

main()