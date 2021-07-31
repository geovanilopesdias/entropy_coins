from random import randint
from time import sleep
from gld_method_library.interface import conc_num_simples as cns
from gld_method_library.interface import cor

tamcol = 60
cor('='*tamcol, 'AM', False)
cor('ANÁLISE DE SORTEIO DE DUAS MOEDAS'.center(tamcol), 'AZ', False)
cor('='*tamcol, 'AM', False)
m = int(input('Insira o número de moedas para lançar: '))
l = int(input('Insira o número de lançamentos desejados: '))
cor('-'*tamcol, 'AM', False)

sgeral = []  # lista permanente para compilação dos lançamentos de cada moeda; recebe a lista smoeda como elemento
smoeda = []  # lista interna para lançamentos de uma moeda
tradutor = 0  # transforma sorteio de 1 ou 2 para cara ou coroa respectivamente
conferencia = (m ** 2 - m)/2  # número de conferências por lançamento
total = conferencia * l  # número total de conferências

try:
    for x in range(0, m):  # iteração para número de moedas
        for y in range(0, l):  # iteração para número de lançamentos
            tradutor = randint(1, 2)
            if tradutor == 1:
                smoeda.append('§§')  # cara
            else:
                smoeda.append('50')  # coroa
        sgeral.append(smoeda[:])
        smoeda.clear()
except Exception as erro:
    print(f'Erro no cadastro de moedas. Causa: {repr(erro)}')
else:
    cor('-' * tamcol, 'VD', False)
    print(f'Foram realizados {l} lançamentos para {m} moedas')
    print(f'Conferiu-se {int(total)} vezes para detectar jogos concordantes')
    cor('-' * tamcol, 'VD', False)

# EXIBIÇÃO DOS RESULTADOS, PARA NO MÁXIMO 10 MOEDAS E 10 LANÇAMENTOS
if m <= 10 and l <= 10:
    for moeda in range(0, m):
        print(f'Os resultados da {moeda+1}ª moeda foram {sgeral[moeda]}.')
        sleep(.5)

# ANÁLISE DE REPETIÇÕES (TODAS CARAS OU TODAS COROAS)
try:
    repet_par = repet_global = a = 0
    b = a + 1
    for lancamento in range(0, l):
        while True:
            while True:
                if sgeral[a][lancamento] == sgeral[b][lancamento]:
                    repet_par += 1
                if repet_par == conferencia:
                    repet_global += 1
                if b == (m - 1):
                    break
                else:
                    b += 1
                    continue
            if a == (m - 2):
                repet_par = 0
                a = 0
                b = a + 1
                break
            else:
                a += 1
                b = a + 1
except Exception as erro:
    print(f'\033[31mErro na análise das repetições\033[m. Causa: {repr(erro)}')
else:
    print(f'As {m} moedas caíram todas iguais {repet_global} ', end='')
    print(cns(repet_par, "vez", "es"))
    probabilidade_todas = 2 / (2 ** m)  # prob. de todas caírem iguais
    #probabilidade_ocorrido += probabilidade_todas
    cor(f'A probabilidade de caírem todas iguais, uma vez, é de uma em {int(probabilidade_todas ** -1)}!', 'AM', False)
    #if repet_global >= 2:
        #cor(f'A probabilidade de acontecer o que ocorreu é {probabilidade_ocorrido * 100}%!', 'VM', False)
