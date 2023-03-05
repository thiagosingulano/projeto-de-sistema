#A idea desse sistema é facilitar o controle das atividades cotidianas da empresa, começando pelo setor financeiro

#Esse primeiro arquivo cuidará das entradas e saídas e do controle do fluxo de caixa

from datetime import datetime
import locale
import os
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

continuarRodando = False;

#Estabelece a condição para o programa continuar sendo executado 

valoresEntrada = []
categorias = {
"vendas_a_prazo": 0,
"vendas_a_vista": 0,
"despesas_fixas": 0,
"despesas_variaveis": 0
}

#cria uma lista para armazenar as entradas futuras e um dicionário para categorizar cada entrada

def get_prazo_positivo():
    while True:
        prazo = int(input("Primeiramente, insira o total de vendas realizadas à prazo no mês atual: "))
        if prazo > 0:
            return prazo
        print("Desculpe, o valor precisa ser positivo. Tente novamente.")

vendasPrazo = get_prazo_positivo()

#recebe um valor POSISTIVO para as vendas à prazo e armazena 

def get_vista_positivo():
    while True:
        vista = int(input("Agora, insira o total das vendas a vista: "))
        if vista > 0:
            return vista
        print("Desculpe, o valor precisa ser positivo. Tente novamente.")

vendasVista = get_vista_positivo()

#recebe um valor POSISTIVO para as vendas à vista e armazena 

def get_despesas_fixas():
    while True:
        fixas = int(input("Vamos as despesas, primeiro, insira o total das despesas fixas: "))
        if fixas > 0:
            return fixas
        print("Desculpe, o valor precisa ser positivo. Tente novamente.")

despesasFixas =  get_despesas_fixas()

#recebe um valor POSISTIVO para as despesas fixas e armazena 

def get_despesas_variaveis():
    while True:
        variaveis = int(input("Agora, insira o total das despesas variáveis: "))
        if variaveis > 0:
            return variaveis
        print("Desculpe, o valor precisa ser positivo. Tente novamente")

despesasVariaveis = get_despesas_variaveis()

#recebe um valor POSISTIVO para as despesas variáveis e armazena 

print("Total de vendas à prazo: ", vendasPrazo)
print("Total de vendas à vista: ", vendasVista)
print("Total das despesas fixas: ", despesasFixas)
print("Total das despesas variáveis: ", despesasVariaveis)

#armazena e mostra ao usuário o valor das despesas variáveis

resultado_operacional = float((vendasPrazo + vendasVista) - (despesasFixas + despesasVariaveis))
mes_atual = datetime.now().strftime("%B").capitalize()
print(f"O resultado operacional no mês de {mes_atual} foi de R$ {resultado_operacional}")





