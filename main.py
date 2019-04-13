# coding: utf-8

from entidades_eletrizadas import *
from entidades_auxiliares import *
import math

def posicao(objeto):
    print("\nInsira as coordenadas d%s no espaco tridimensional no formato: " % objeto)
    x, y, z = map(float, input("X, Y, Z: ").split())
    return (x, y, z)

def _carga_pontual():
    carga = float(input("\nDigite o valor da Carga: "))
    ponto = posicao("a Carga")
    return CargaPontual(carga, ponto)

def _esfera():
    carga_total = float(input("\nDigite o valor da Carga Total da Casca: "))
    raio = float(input("\nDigite a medida do Raio da Esfera: "))
    centro = posicao("o Centro da Esfera")
    return Esfera(carga_total, raio, centro)

def _barra():
    carga_total = float(input("\nDigite o valor da Carga Total da Barra: "))
    ponto_i = posicao("o Ponto Inicial da Barra")
    ponto_f = posicao("o Ponto Final da Barra")
    return Barra(carga_total, ponto_i, ponto_f)

def _disco():
    carga_total = float(input("\nDigite o valor da Carga Total do Disco: "))
    centro = posicao("o Centro do Disco")
    raio = float(input("\nDigite a medida do Raio do Disco: "))
    return Disco(carga_total, centro, raio)

def _anel():
    carga_total = float(input("\nDigite o valor da Carga Total do Anel: "))
    centro = posicao("o Centro do Anel")
    raio = float(input("\nDigite a medida do Raio do Anel: "))
    return Anel(carga_total, centro, raio)

if __name__ == '__main__':
    n = 200
    #Texto de Introducao
    print ("O programa calcula no espaco tridimesional o pontecial eletrico de um dado ponto P(x,y,z)"
           "\nem relacao a um objeto de referencia (Anel, Barra, Carga Pontual, Disco ou Esfera)."
           "\nO metodo numerico utilizado para a integracao no Anel, na Barra e no Disco foi a regra do 1/3 de Simpson\n")    
    
    while True:
        print("Selecione um objeto carregado:")
        print("(A)nel\n(B)arra\n(C)arga Pontual\n(D)isco\n(E)sfera\n(S)air")
        opcao = input("\nDigite a Opcao: ")

        if opcao.upper() == "A":
            anel = _anel()
            while True:
                ponto = posicao("o Ponto desejado")
                try:
                    potencial = anel.potencial_no_ponto(ponto, n)
                    print("\nO potencial eletrico do ponto %s eh de:\n%e\n" % (ponto, potencial))
                except Exception as e:
                    print(str(e), end="\n\n")

                continuar = input("Voce deseja calcular com outro ponto para esse anel? (s/n)\n")
                if continuar == "n":
                    break

        elif opcao.upper() == "B":
            barra = _barra()
            while True:
                ponto = posicao("o Ponto desejado")
                try:
                    potencial = barra.potencial_no_ponto(ponto, n)
                    print("\nO potencial eletrico do ponto %s eh de:\n%e\n" % (ponto, potencial))
                except Exception as e:
                    print(str(e), end="\n\n")

                continuar = input("Voce deseja calcular com outro ponto para essa barra? (s/n)\n")
                if continuar == "n":
                    break

        elif opcao.upper() == "C":
            carga_pontual = _carga_pontual()
            while True:
                ponto = posicao("o Ponto desejado")
                try:
                    potencial = carga_pontual.potencial_no_ponto(ponto)
                    print("\nO potencial eletrico no ponto %s eh:\n%e\n" % (ponto, potencial))
                except Exception as e:
                    print(str(e), end="\n\n")

                continuar = input("Voce deseja calcular com outro ponto para essa carga? (s/n)\n")
                if continuar == "n":
                    break

        elif opcao.upper() == "D":
            disco = _disco()
            while True:
                ponto = posicao("o Ponto desejado")
                try:
                    potencial = disco.potencial_no_ponto(ponto, n)
                    print("\nO potencial eletrico do ponto %s eh de:\n%e\n" % (ponto, potencial))
                except Exception as e:
                    print(str(e), end="\n\n")

                continuar = input("Voce deseja calcular com outro ponto para esse disco? (s/n)\n")
                if continuar == "n":
                    break


        elif opcao.upper() == "E":
            casca_esferica = _esfera()
            while True:
                ponto = posicao("o Ponto desejado")

                try:
                    potencial = casca_esferica.potencial_no_ponto(ponto)
                    print("\nO potencial eletrico do ponto %s é de:\ne\n" % (ponto, potencial))
                except Exception as e:
                    print(str(e), end="\n\n")

                continuar = input("Voce deseja calcular com outro ponto para essa esfera? (s/n)\n")
                if continuar == "n":
                    break

        elif opcao.upper() == "S":
            print ("Sessao Encerrada")
            break

        else:
            print("\nEntrada invalida \n")

