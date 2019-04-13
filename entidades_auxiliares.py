import math

""" Modulo responsavel por agrupar as classes que representam entidades auxiliares """

class Simpson:
    """ Classe responsavel pela aplicacao do metodo numerico. Todos os metodos publicos desta classe
    implementam a integral numerica de Simpson, tambem conhecida como regra do 1/3 de simpson. """

    def integra_anel(xi, xf, carga_total, raio, centro, ponto, n):
        """ Calcula a integral, em relacao a x(dx), do pontecial eletrico em cada ponto do anel cujas informacoes foram recebidas
        nos parametros. Eh assumido que os parametros xi, xf, carga_total e raio, sao inteiros ou floats. Os parametros centro e
        ponto seguem o formato (x, y, z), onde x, y e z sao as coordenadas do ponto nos eixos x, y e z, respectivamente. O parametro
        n eh um numero par e representa o numero de divisoes que o intevalo de integracao recebera."""
        valor_xi, valor_xf = 0, 0
        total_par, total_impar = 0, 0
        x, h = xi, abs(xf - xi) / (2 * n)
        count = 0

        if (h <= 0):
            raise Exception("o parametro n eh grande demais")

        while x <= xf:
            yp = math.sqrt(abs((raio ** 2) - (x ** 2))) + centro[1]
            yn = -math.sqrt(abs((raio ** 2) - (x ** 2))) + centro[1]

            if ( (x, yp, centro[2]), (x, yn, centro[2]) ) != (ponto, ponto):
                potencial = Calculadora.potencial_eletrico(carga_total, (x, yp, centro[2]), ponto)
                potencial += Calculadora.potencial_eletrico(carga_total, (x, yn, centro[2]), ponto)
            else:
                raise Exception("O ponto pertence ao anel!") # levantamos uma excecao pois nesse ponto a distancia entre pontos eh zero.

            if x == xi:
                valor_xi = potencial
            elif x == xf:
                valor_xf = potencial
            elif count % 2 == 0:
                total_par += potencial
            elif count % 2 != 0:
                total_impar += potencial
            count += 1
            x += h

        potencial_resultante = (h/3) * (valor_xi + valor_xf + (4 * total_impar) + (2 * total_par))
        return potencial_resultante

    def integra_disco(raio, densidade_de_carga, centro, ponto, n):
        """ Calcula a integral em relacao a r(dr), o raio, do pontecial eletrico em cada ponto do disco cujas informacoes foram
        recebidas nos parametros. Eh assumido que os parametros raio e densidade_de_carga sao inteiros ou floats. Os parametros
        centro e ponto seguem o formato (x, y, z), onde x, y e z sao as coordenadas do ponto nos eixos x, y e z, respectivamente.
        O parametro n eh um numero par e representa o numero de divisoes que o intevalo de integracao recebera."""
        from entidades_eletrizadas import Anel
        valor_xi, valor_xf = Calculadora.potencial_eletrico(densidade_de_carga, centro, ponto), 0
        total_par, total_impar = 0, 0
        x, h = 0, abs(raio - 0) / (2 * n)
        x += h
        count = 1

        if (h <= 0):
            raise Exception("o parametro n eh grande demais")

        while x <= raio:
            carga_do_anel = densidade_de_carga * 2 * math.pi * x
            anel = Anel(carga_do_anel, centro, x)

            try:
                potencial = anel.potencial_no_ponto(ponto, n)
            except Exception:
                raise Exception("O ponto pertence ao disco!") # levantamos uma excecao pois nesse ponto a distancia entre pontos eh zero.

            if x == raio:
                valor_xf = potencial
            elif count % 2 == 0:
                total_par += potencial
            elif count % 2 != 0:
                total_impar += potencial
            count += 1
            x += h

        potencial_resultante = (h/3) * (valor_xi + valor_xf + (4 * total_impar) + (2 * total_par))
        return potencial_resultante

    def integra_barra(i, f, t, densidade_de_carga, vetor_barra, pontoi, ponto, n):
        """ Calcula e retorna o valor da integral resultante somatorio do potencial eletrico em cada ponto da barra cujas
        informacoes foram recebidas nos parametros. Eh assumido que os parametros i, f e densidade_de_carga sao inteiros ou floats.
        Os parametros vetor_barra, pontoi e ponto seguem o formato (x, y, z), onde x, y e z sao as coordenadas do ponto nos eixos
        x, y e z, respectivamente. O parametro n deve ser um numero positivo par, diferente de zero, e representa o numero de
        divisoes que o intevalo de integracao recebera."""
        valor_i,valor_f = 0, 0
        total_par, total_impar = 0, 0
        c, h = i, abs(f - i) / (2 * n)
        count = 0

        if (h <= 0):
            raise Exception("o parametro n eh grande demais")

        while c <= f:
            x, y, z = Simpson.__coords(c, t, vetor_barra, pontoi)

            if (x, y, z) != ponto:
                potencial = Calculadora.potencial_eletrico(densidade_de_carga, (x, y, z), ponto)
            else:
                raise Exception("O ponto pertence a barra!")

            if c == i:
                valor_i = potencial
            elif c == f:
                valor_f = potencial
            elif count % 2 == 0:
                total_par += potencial
            elif count % 2 != 0:
                total_impar += potencial
            count += 1
            c += h

        potencial_resultante = (h / 3) * (valor_i + valor_f + (4 * total_impar) + (2 * total_par))
        return potencial_resultante

    def __coords(c, t, vetor_barra, pontoi):
        """ Metodo privado para uso interno da classe. Analisa os dados recebidos na entrada a fim de assegurar
        que os valores de x, y e z sao os adequados para a integracao desejada. O parametro c eh o iterador do algoritmo
        de integracao numerica, deve ser float ou inteiro. O parametro t simboliza qual eixo a integral esta percorrendo.
        Os parametros vetor barra e pontoi seguem o mesmo formato (x, y, z) dos metodos anteriores. O parametro x pode
        ser inteiro ou float."""
        if t == "x":
            x = c
            y = Simpson.__coord_y_para_x(vetor_barra, pontoi, c)
            z = Simpson.__coord_z_para_x(vetor_barra, pontoi, c)
            return x, y, z

        if t == "y":
            x = pontoi[0]
            y = c
            z = Simpson.__coord_z_para_y(vetor_barra, pontoi, c)
            return x, y, z

        if t == "z":
            x = pontoi[0]
            y = pontoi[1]
            z = c
            return x, y, z

        raise Exception()

    def __coord_y_para_x(vetor_barra, pontoi, x):
        """ Metodo privado para uso interno da classe. Calcula e retorna a coordenada de y em relacao a um x passado
        como parametro, o vetor da barra em questao e um ponto da mesma. Os parametros vetor barra e pontoi seguem o
        mesmo formato (x, y, z) dos metodos anteriores. O parametro x pode ser inteiro ou float."""
        return (vetor_barra[1] / vetor_barra[0]) * (x - pontoi[0]) + pontoi[1]

    def __coord_z_para_x(vetor_barra, pontoi, x):
        """ Metodo privado para uso interno da classe. Calcula e retorna a coordenada de z em relacao a um x passado
        como parametro, o vetor da barra em questao e um ponto da mesma. Os parametros vetor barra e pontoi seguem o
        mesmo formato (x, y, z) dos metodos anteriores. O parametro x pode ser inteiro ou float."""
        return (vetor_barra[2] / vetor_barra[0]) * (x - pontoi[0]) + pontoi[2]

    def __coord_z_para_y(vetor_barra, pontoi, y):
        """ Metodo privado para uso interno da classe. Calcula e retorna a coordenada de z em relacao a um y passado
        como parametro, o vetor da barra em questao e um ponto da mesma. Os parametros vetor barra e pontoi seguem o
        mesmo formato (x, y, z) dos metodos anteriores. O parametro y pode ser inteiro ou float."""
        return (vetor_barra[2] / vetor_barra[1]) * (y - pontoi[1]) + pontoi[2]

class Calculadora:

    def potencial_eletrico(carga, pontoi, pontof):
        """ Calcula e retorna o potencial eletrico entre os pontos recebidos como parametro. O parametro
         carga eh um inteiro ou float e os parametros pontoi e pontof sao tuplas no formato (x, y, z), onde
         x, y e z sao as coordenadas do ponto nos eixos x, y e z, respectivamente."""
        distancia = Calculadora.distancia_entre(pontoi, pontof)
        return (carga / distancia) * Calculadora.constante_eletrostatica()

    def distancia_entre(pontoi, pontof):
        """ Calcula e retorna a distancia entre os pontos recebidos como parametro. Os parametros
        pontoi e pontof seguem o mesmo formato (x, y, z) utilizado no metodo potencial_eletrico()."""
        xf, xi = pontof[0], pontoi[0]
        yf, yi = pontof[1], pontoi[1]
        zf, zi = pontof[2], pontoi[2]
        vx, vy, vz = xf - xi, yf - yi, zf - zi
        return math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)

    def constante_eletrostatica():
        """ Retorna o valor da constante eletrostatica. """
        return 8.99 * 10 ** 9
