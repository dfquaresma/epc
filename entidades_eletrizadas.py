from entidades_auxiliares import *
import math

""" Modulo responsavel por agrupar as classes que representam entidades eletrizadas """

class CargaPontual(object):
    """ Classe representando uma carga pontual """
    
    def __init__(self, carga, posicao):
        """ Metodo construtor da classe. Assume que o parametro carga recebe um inteiro ou float
        e que o parametro posicao eh uma tupla no formato (x, y, z), onde x, y e z sao as coordenadas do ponto 
        nos eixos x, y e z, respectivamente."""
        self._carga = carga
        self._posicao = posicao

    def potencial_no_ponto(self, ponto):
        """ Retorna o potencial eletrico no ponto recebido como parametro. Assume que o formato
        do parametro posicao eh o mesmo que o utilizado no metodo __init__()."""
        if ponto == self._posicao:
            raise Exception("O ponto pertence a carga pontual!") # levantamos uma excecao pois nesse ponto a distancia entre pontos eh zero.
        return Calculadora.potencial_eletrico(self._carga, self._posicao, ponto)

    @property
    def carga(self):
        return self._carga

    @property
    def posicao(self):
        return self._posicao

class Esfera(object):
    """ Classe representando uma esfera carregada com cargas estaticas na casca. """

    def __init__(self, carga_total, raio, centro):
        """ Metodo construtor da classe. Assume que o parametro carga_total e raio recebem um inteiro ou float
        e que o parametro centro eh uma tupla no formato (x, y, z), onde x, y e z sao as coordenadas do ponto
        nos eixos x, y e z, respectivamente."""
        self._carga_pontual = CargaPontual(carga_total, centro)
        self._potencial_eletrico_ate_a_casca = self._carga_pontual.potencial_no_ponto((centro[0] + raio, centro[1], centro[2]))
        self._densidade_de_carga = carga_total / (4 * math.pi * (raio ** 2))
        self._raio = raio

    def potencial_no_ponto(self, ponto):
        """ Retorna o potencial eletrico no ponto recebido como parametro. Assume que o formato
            do parametro posicao eh o mesmo que o utilizado no parametro centro do metodo __init__()."""
        if Calculadora.distancia_entre(self._carga_pontual.posicao, ponto) == self._raio:
            raise Exception("O ponto pertence a casca da esfera!") # levantamos uma excecao pois nesse ponto a distancia entre pontos eh zero.
        if Calculadora.distancia_entre(self._carga_pontual.posicao, ponto) < self._raio:
            return self._potencial_eletrico_ate_a_casca
        else:
            return self._carga_pontual.potencial_no_ponto(ponto)

    @property
    def carga_total(self):
        return self._carga_pontual.carga

    @property
    def centro_da_esfera(self):
        return self._carga_pontual.posicao

    @property
    def densidade_de_carga(self):
        return self._densidade_de_carga

    @property
    def raio(self):
        return self._raio
 
class Barra(object):
    """ Classe representando uma barra carregada com cargas estaticas destribuidas uniformemente
    ao longo da barra. A barra eh considerada como uma sequencia de cargas pontuais."""

    def __init__(self, carga_total, pontoi, pontof):
        """ Metodo construtor da classe. Assume que o parametro carga_total recebe um inteiro ou float
        e que os parametros pontoi e pontof sao tuplas no formato (x, y, z), onde x, y e z sao as coordenadas do ponto
        nos eixos x, y e z, respectivamente."""
        self._carga_total = carga_total
        self._pontoi = pontoi
        self._pontof = pontof
        self._vetor_barra = (pontof[0] - pontoi[0], pontof[1] - pontoi[1], pontof[2] - pontoi[2])
        self._comprimento = Calculadora.distancia_entre(pontoi, pontof)
        if self._comprimento != 0:
            self._densidade_de_carga = self._carga_total / self._comprimento
        else:
            self._densidade_de_carga = self._carga_total

    def potencial_no_ponto(self, ponto, n):
        """ Retorna  o potencial eletrico no ponto recebido como parametro. Assume que o formato do parametro
        posicao eh o mesmo que o utilizado nos parametros pontoi e pontof do metodo __init__(). o parametro n
        eh utilizado pela classe Simpson para o calculo a integral numerica."""
        xi, xf = self._get_xi_xf()
        yi, yf = self._get_yi_yf()
        zi, zf = self._get_zi_zf()
        potencial_no_ponto = 0
        if self._vetor_barra[0] != 0:
            potencial_no_ponto += Simpson.integra_barra(xi, xf, "x", self._densidade_de_carga, self._vetor_barra, self._pontoi, ponto, n)

        elif self._vetor_barra[1] != 0:
            potencial_no_ponto += Simpson.integra_barra(yi, yf, "y", self._densidade_de_carga, self._vetor_barra, self._pontoi, ponto, n)

        elif self._vetor_barra[2] != 0:
            potencial_no_ponto += Simpson.integra_barra(zi, zf, "z", self._densidade_de_carga, self._vetor_barra, self._pontoi, ponto, n)

        elif self._pontoi != ponto:
            potencial_no_ponto += Calculadora.potencial_eletrico(self._densidade_de_carga, self._pontoi, ponto)

        else:
            raise Exception("O ponto pertence a barra!") # levantamos uma excecao pois nesse ponto a distancia entre pontos eh zero.

        return potencial_no_ponto

    def _get_xi_xf(self):
        """ Metodo privado para uso interno da classe. Retorna uma tupla com os valores de xi e xf de modo que xf sempre eh maior que xi. """
        if self._pontoi[0] <= self._pontof[0]:
            return self._pontoi[0], self._pontof[0]
        return self._pontof[0], self._pontoi[0]

    def _get_yi_yf(self):
        """ Metodo privado para uso interno da classe. Retorna uma tupla com os valores de yi e yf de modo que yf sempre eh maior que yi. """
        if self._pontoi[1] <= self._pontof[1]:
            return self._pontoi[1], self._pontof[1]
        return self._pontof[1], self._pontoi[1]

    def _get_zi_zf(self):
        """ Metodo privado para uso interno da classe. Retorna uma tupla com os valores de zi e zf de modo que zf sempre eh maior que zi. """
        if self._pontoi[2] <= self._pontof[2]:
            return self._pontoi[2], self._pontof[2]
        return self._pontof[2], self._pontoi[2]

    @property
    def carga_total(self):
        return self._carga_total

    @property
    def comprimento(self):
        return self._comprimento

    @property
    def densidade_de_carga(self):
        return self._densidade_de_carga

    @property
    def extremidades(self):
        return self._pontoi, self._pontof
       
class Anel(object):
    """ Classe representando anel carregado com cargas estaticas destribuidas uniformemente ao longo da anel.
    O anel eh considerado como uma sequencia de cargas pontuais, distribuida de modo a forma um circulo."""

    def __init__(self, carga_total, centro, raio):
        """ Metodo construtor da classe. Assume que o parametro carga_total e raio recebem um inteiro ou float
        e que o parametro centro eh uma tupla no formato (x, y, z), onde x, y e z sao as coordenadas do ponto
        nos eixos x, y e z, respectivamente."""
        self._carga_total = carga_total
        self._centro = centro
        self._raio = raio
        self._densidade_de_carga = self._carga_total / (2 * math.pi * raio)

    def potencial_no_ponto(self, ponto, n):
        """ Retorna  o potencial eletrico no ponto recebido como parametro. Assume que o formato do parametro
        posicao eh o mesmo que o utilizado no parametro centro do metodo __init__().o parametro n
        eh utilizado pela classe Simpson para o calculo a integral numerica."""
        xi = self._centro[0] - self._raio
        xf = self._centro[0] + self._raio
        return Simpson.integra_anel(xi, xf, self._carga_total, self._raio, self._centro, ponto, n)

    @property
    def carga_total(self):
        return self._carga_total

    @property
    def densidade_de_carga(self):
        return self._densidade_de_carga

    @property
    def raio(self):
        return self._raio

    @property
    def centro(self):
        return self.centro

class Disco(object):
    """ Classe representando disco carregado com cargas estaticas destribuidas uniformemente ao longo da disco."""

    def __init__(self, carga_total, centro, raio):
        """ Metodo construtor da classe. Assume que o parametro carga_total e raio recebem um inteiro ou float
        e que o parametro centro eh uma tupla no formato (x, y, z), onde x, y e z sao as coordenadas do ponto
        nos eixos x, y e z, respectivamente."""
        self._carga_total = carga_total
        self._centro = centro
        self._raio = raio
        self._densidade_de_carga = self._carga_total / (math.pi * (raio ** 2))

    def potencial_no_ponto(self, ponto, n):
        """ Retorna  o potencial eletrico no ponto recebido como parametro. Assume que o formato do parametro
        posicao eh o mesmo que o utilizado no parametro centro do metodo __init__().o parametro n
        eh utilizado pela classe Simpson para o calculo a integral numerica."""
        return Simpson.integra_disco(self._raio, self._densidade_de_carga, self._centro, ponto, n)

    @property
    def carga_total(self):
        return self._carga_total

    @property
    def densidade_de_carga(self):
        return self._densidade_de_carga

    @property
    def raio(self):
        return self._raio

    @property
    def centro(self):
        return self.centro
