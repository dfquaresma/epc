from entidades_eletrizadas import *

def integra_barras_exemplo(n):
    print("Barra Carregada")

    barra = Barra(1, (0, 0, 0), (8, 0, 0))
    print("Integrando em relacao a x")
    print("%e" % barra.potencial_no_ponto((0, 0.1, 0), n) + " fora e relativamente perto da barra - (0, 0.1, 0)")
    print("%e" % barra.potencial_no_ponto((0, 0, 0.1), n) + " fora e relativamente perto da barra - (0, 0, 0.1)")
    print("%e" % barra.potencial_no_ponto((0, 0.1, 0.1), n) + " fora e relativamente perto da barra - (0, 0.1, 0.1)")

    print("%e" % barra.potencial_no_ponto((0, 60000, 0), n) + " fora e relativamente longe da barra - (0, 60000, 0)")
    print("%e" % barra.potencial_no_ponto((0, 60000, 60000), n) + " fora e relativamente longe da barra - (0, 60000, 60000)")
    print("%e" % barra.potencial_no_ponto((0, 0, 60000), n) + " fora e relativamente longe da barra - (0, 0, 60000)")


    barra = Barra(1, (0, 0, 0), (0, 7, 0))
    print("Integrando em relacao a y")
    print("%e" % barra.potencial_no_ponto((0, 0, 0.1), n) + " fora e relativamente perto da barra - (0, 0.1, 0)")
    print("%e" % barra.potencial_no_ponto((0.1, 0, 0.1), n) + " fora e relativamente perto da barra - (0.1, 0, 0.1)")
    print("%e" % barra.potencial_no_ponto((0.1, 0, 0), n) + " fora e relativamente perto da barra - (0.1, 0, 0)")

    print("%e" % barra.potencial_no_ponto((60000, 0, 0), n) + " fora e relativamente longe da barra - (60000, 0, 0)")
    print("%e" % barra.potencial_no_ponto((0, 0, 60000), n) + " fora e relativamente longe da barra - (0, 0, 60000)")
    print("%e" % barra.potencial_no_ponto((60000, 0, 60000), n) + " fora e relativamente longe da barra - (60000, 0, 60000)")


    barra = Barra(1, (0, 0, 0), (0, 0, 6))
    print("Integrando em relacao a z")
    print("%e" % barra.potencial_no_ponto((0.1, 0, 0), n) + " fora e relativamente perto da barra - (0.1, 0, 0)")
    print("%e" % barra.potencial_no_ponto((0.1, 0.1, 0), n) + " fora e relativamente perto da barra - (0.1, 0.1, 0)")
    print("%e" % barra.potencial_no_ponto((0, 0.1, 0), n) + " fora e relativamente perto da barra - (0, 0.1, 0)")

    print("%e" % barra.potencial_no_ponto((0, 60000, 0), n) + " fora e relativamente longe da barra - (0, 60000, 0)")
    print("%e" % barra.potencial_no_ponto((60000, 60000, 0), n) + " fora e relativamente longe da barra - (60000, 60000, 0)")
    print("%e" % barra.potencial_no_ponto((60000, 0, 0), n) + " fora e relativamente longe da barra - (60000, 0, 0)")

def integra_aneis_exemplo(n):
    print("Anel Carregado")

    anel = Anel(1, (8, 0, 0), 1)
    print("Integrando em relacao a x")
    print("%e" % anel.potencial_no_ponto((0, 1.1, 0), n) + " fora e relativamente perto do anel - (0, 1.1, 0)")
    print("%e" % anel.potencial_no_ponto((0, 0, 1.1), n) + " fora e relativamente perto do anel - (0, 0, 1.1)")
    print("%e" % anel.potencial_no_ponto((0, 1.1, 1.1), n) + " fora e relativamente perto do anel - (0, 1.1, 1.1)")
    print("%e" % anel.potencial_no_ponto((0, 200000, 0), n) + " fora e relativamente longe do anel - (0, 200000, 0)")
    print("%e" % anel.potencial_no_ponto((0, 0, 200000), n) + " fora e relativamente longe do anel - (0, 0, 200000)")
    print("%e" % anel.potencial_no_ponto((0, 200000, 200000), n) + " fora e relativamente longe do anel - (0, 200000, 200000)")

    anel = Anel(1, (0, 6, 0), 1)
    print("Integrando em relacao a y")
    print("%e" % anel.potencial_no_ponto((1.1, 0, 0), n) + " fora e relativamente perto do anel - (1.1, 0, 0)")
    print("%e" % anel.potencial_no_ponto((0, 0, 1.1), n) + " fora e relativamente perto do anel - (0, 0, 1.1)")
    print("%e" % anel.potencial_no_ponto((1.1, 0, 1.1), n) + " fora e relativamente perto do anel - (1.1, 0, 1.1)")
    print("%e" % anel.potencial_no_ponto((200000, 0, 0), n) + " fora e relativamente longe do anel - (200000, 0, 0)")
    print("%e" % anel.potencial_no_ponto((0, 0, 200000), n) + " fora e relativamente longe do anel - (0, 0, 200000)")
    print("%e" % anel.potencial_no_ponto((200000, 0, 200000), n) + " fora e relativamente longe do anel - (200000, 0, 200000)")

    anel = Anel(1, (0, 0, 7), 1)
    print("Integrando em relacao a z")
    print("%e" % anel.potencial_no_ponto((1.1, 0, 0), n) + " fora e relativamente perto do anel - (1.1, 0, 0)")
    print("%e" % anel.potencial_no_ponto((0, 1.1, 0), n) + " fora e relativamente perto do anel - (0, 1.1, 0)")
    print("%e" % anel.potencial_no_ponto((1.1, 1.1, 0), n) + " fora e relativamente perto do anel - (1.1, 1.1 0)")
    print("%e" % anel.potencial_no_ponto((200000, 0, 0), n) + " fora e relativamente longe do anel - (200000, 0, 0)")
    print("%e" % anel.potencial_no_ponto((0, 200000, 0), n) + " fora e relativamente longe do anel - (0, 200000 0)")
    print("%e" % anel.potencial_no_ponto((200000, 200000, 0), n) + " fora e relativamente longe do anel - (200000, 200000, 0)")

def integra_discos_exemplo(n):
    print("Disco Carregado")

    disco = Disco(1, (6, 0, 0), 1)
    print("Integrando em relacao a x")
    print("%e" % disco.potencial_no_ponto((0, 1.1, 0), n) + " fora e relativamente perto do anel - (0, 1.1, 0)")
    print("%e" % disco.potencial_no_ponto((0, 0, 1.1), n) + " fora e relativamente perto do anel - (0, 0, 1.1)")
    print("%e" % disco.potencial_no_ponto((0, 1.1, 1.1), n) + " fora e relativamente perto do anel - (0, 1.1, 1.1)")
    print("%e" % disco.potencial_no_ponto((0, 200000, 0), n) + " fora e relativamente longe do anel - (0, 200000, 0)")
    print("%e" % disco.potencial_no_ponto((0, 0, 200000), n) + " fora e relativamente longe do anel - (0, 0, 200000)")
    print("%e" % disco.potencial_no_ponto((0, 200000, 200000), n) + " fora e relativamente longe do anel - (0, 200000, 200000)")

    disco = Disco(1, (0, 7, 0), 1)
    print("Integrando em relacao a y")
    print("%e" % disco.potencial_no_ponto((1.1, 0, 0), n) + " fora e relativamente perto do anel - (1.1, 0, 0)")
    print("%e" % disco.potencial_no_ponto((0, 0, 1.1), n) + " fora e relativamente perto do anel - (0, 0, 1.1)")
    print("%e" % disco.potencial_no_ponto((1.1, 0, 1.1), n) + " fora e relativamente perto do anel - (1.1, 0, 1.1)")
    print("%e" % disco.potencial_no_ponto((200000, 0, 0), n) + " fora e relativamente longe do anel - (200000, 0, 0)")
    print("%e" % disco.potencial_no_ponto((0, 0, 200000), n) + " fora e relativamente longe do anel - (0, 0, 200000)")
    print("%e" % disco.potencial_no_ponto((200000, 0, 200000), n) + " fora e relativamente longe do anel - (200000, 0, 200000)")

    disco = Disco(1, (0, 0, 8), 1)
    print("Integrando em relacao a z")
    print("%e" % disco.potencial_no_ponto((1.1, 0, 0), n) + " fora e relativamente perto do anel - (1.1, 0, 0)")
    print("%e" % disco.potencial_no_ponto((0, 1.1, 0), n) + " fora e relativamente perto do anel - (0, 1.1, 0)")
    print("%e" % disco.potencial_no_ponto((1.1, 1.1, 0), n) + " fora e relativamente perto do anel - (1.1, 1.1 0)")
    print("%e" % disco.potencial_no_ponto((200000, 0, 0), n) + " fora e relativamente longe do anel - (200000, 0, 0)")
    print("%e" % disco.potencial_no_ponto((0, 200000, 0), n) + " fora e relativamente longe do anel - (0, 200000 0)")
    print("%e" % disco.potencial_no_ponto((200000, 200000, 0), n) + " fora e relativamente longe do anel - (200000, 200000, 0)")



if __name__ == '__main__':

    print("ZERO FINALIZA O LOOP!")
    while True:
        opcao = input("Barra, Anel ou disco, CHOOSE YOUR TEST!!!\nyour choice... ")
        n = int(input("N: "))
        if n == 0:
            break
        if n < 0:
            print("N NAO PODE SER NEGATIVO!")
        elif n % 2 != 0:
            print("N DEVE SER PAR!!")
        else:

            if opcao.upper() == "BARRA":
                integra_barras_exemplo(n)
                print()
            elif opcao.upper() == "ANEL":
                integra_aneis_exemplo(n)
                print()

            elif opcao.upper() == "DISCO":
                integra_discos_exemplo(n)
                print()

            else:
                print("CHOOSE A VALID ONE, STUPID!!! lol kk")




    


