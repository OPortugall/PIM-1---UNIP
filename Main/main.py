#Gera um 'atraso' no sistema, é um efeito legal, parece que o sistema ta carregando
from time import sleep 

#Funçao para definir cores que vou utilizar no sistema inteiro
def color(text, color_name):
    colors = {
        'clear': '\033[m',
        'yellow': '\033[1;33m',
        'red': '\033[1;31m',
        'green': '\033[1;32m',
        'blue': '\033[1;34m',
        'cian': '\033[1;36m'
    }
    return colors.get(color_name, colors['clear']) + text + colors['clear']

#Linha de separação do título
line = ('-' * 40)

#Título em si
def title(txt):
    print(color(line, 'yellow'))
    print(color(txt.center(len(line)), 'cian'))
    print(color(line, 'yellow'))

#Defini o 'login' do admin, mais pra frente vai ter verificação disso
admin = {
    'username': 'admin',
    'email': 'admin.system@gmail.com',
    'password': '123456'
}

#Função para validar
def is_user_valid(user, email, password):
    return (user == admin['username'] and
            email == admin['email'] and 
            password == admin['password'])
     
#Login
def login(lgn):
    print(color(line, 'yellow'))
    print(color(lgn.center(len(line)), 'cian'))
    print(color(line, 'yellow'))

login('Faça seu login para continuar')

user = str( input(color('Usuário: ', 'green')))
email = str( input(color('Email: ', 'green')))
password = input(color('Senha: ', 'green'))

#Validação
if is_user_valid(user, email, password):
    sleep(1)
    print(color(line, 'yellow'))
    print(color('Seja bem-vindo!'.center(len(line)), 'cian'))
    print(color(line, 'yellow'))
else:
    sleep(1)
    print(color(line, 'yellow'))
    print(color('Usuário não encontrado!'.center(len(line)), 'red'))
    print(color(line, 'yellow'))
    exit()

sleep(2)
title('DJE - Engenharia')
sleep(2)

#menu de opções
def menu(options):
    title('MENU PRINCIPAL')
    for i, option in enumerate(options, 1):
        print(color(f'{i} - {option}', 'blue'))
    print(color(line, 'yellow'))

    while True:
        try:
            choose = int( input(color('Escolha uma opção: ', 'green')))
            if 1 <= choose <= len(options):
                return choose
            else:
                print(color('Opção inválida', 'red'))
        except:
            print(color('Digite uma opção válida!', 'red'))

options = ['Gastos',
           'Margem de lucro',
           'Materiais',
           'Desperdício',
           'Equipamentos eletrônicos',
           'Funcinários',
           'Sair',
           ]

Gastos = {
'Contrato: 25146 - Condomínio Estúdio Uno' : 
['Demolição de concreto - superior e inferior | tipo: M.Obra | Unitário: R$ 300,00 | Total: R$ 4.063,50', 
'Locação de rompedor | tipo: Mat. | Unitário: R$ 750,00 | Total: R$ 750,00',
'Madeirit plastificado | tipo: Mat. | Unitário: R$ 220,00 | Total: R$ 5.500,00',
'Pontalete eucalipto | tipo: Mat. | Unitário: R$ 15,40 | Total: R$ 154,00',
'Tábua bruta pinus | tipo: Mat. | Unitário: R$ 25,00 | Total: R$ 250,00',
'Tábua bruta pinus | tipo: Mat. | Unitário: R$ 40,00 | Total: R$ 400,00',
'Preço com cabeça | tipo: Mat. | Unitário: R$ 16,00 | Total: R$ 160,00',
'Arame recozido | tipo: Mat. | Unitário: R$ 15,00 | Total: R$ 450,00',
'Repara estruturas 20Kg cinza Quartzolit | tipo: Mat. | Unitário: R$ 123,16 | Total: R$ 12.316,00',
'Concreto usinado | tipo: Mat. | Unitário: R$ 500,00 | Total: R$ 4.966,50',
'Imprevistos | tipo: Mat. | Unitário: R$ 2.674,13 | Total: R$ 2.674,13',
'Concretagem | tipo: M.Obra | Unitário: R$ 50,00 | Total: R$ 2.257,50',
'Locação de vibrador | tipo: Mat. | Unitário: R$ 750,00 | Total: R$ 750,00',
'Manta geotextil Bidim | tipo: Mat. | Unitário: R$ 4,00 | Total: R$ 200,00',
'Ensaio de corpo de prova de concreto | tipo: Mat. | Unitário: R$ 120,00 | Total: R$ 720,00',
'Montagem de formas	| tipo: M.Obra | Unitário: R$ 1.200,00 | Total: R$ 1.200,00',
'Limpeza de armadura e aplicação de massa | tipo: M.Obra | Unitário: R$ 2.500,00 | Total: R$ 2.500,00',
'Aplicação de mata asfáltica | tipo: M.Obra | Unitário: R$ 30,00 | Total: R$ 1.350,00',
'Primer Adeflex Viapol	| tipo: Mat. | Unitário: R$ 395,00 | Total: R$ 790,00',
'Manta asfáltica - 4,00 mm | tipo: Mat. | Unitário: R$ 47,00 | Total: R$ 2.749,50',
'Cimento CPIII | tipo: Mat. | Unitário: R$ 32,00 | Total: R$ 512,00',
'Areia Média | tipo: Mat. | Unitário: R$ 195,00 | Total: R$ 390,00',
'Vedacit | tipo: Mat. | Unitário: R$ 115,00 | Total: R$ 230,00',
'Execução de contrapiso FINAL | tipo: M.Obra M.Obra | Unitário: R$ 60,00 | Total: R$ 2.700,00'],

'Contrato: 25149 - Jardinatti' :
['Elaboração de APR | tipo: M.Obra | Unitário:  R$ 120,00 | Total:  R$ 120,00', 
'Tela de proteção | tipo: Mat. | Unitário:  R$ 5,65 | Total:  R$ 339,00', 
'Viga bruta eucalípto | tipo: Mat. | Unitário:  R$ 68,90 | Total:  R$ 137,80', 
'Fechamento de proteção | tipo: M.Obra | Unitário:  R$ 150,00 | Total:  R$ 150,00', 
'Demolição de caixas existentes | tipo: M.Obra | Unitário:  R$ 150,00 | Total:  R$ 300,00', 
'Caixa de passagem | tipo: Mat. | Unitário:  R$ 297,00 | Total:  R$ 594,00', 
'Tampa para caixa de concreto | tipo: Mat. | Unitário:  R$ 118,00 | Total:  R$ 236,00', 
'Mão de obra de instalação | tipo: M.Obra | Unitário:  R$ 500,00 | Total:  R$ 500,00', 
'Imprevistos | tipo: Mat. | Unitário:  R$ 300,00 | Total:  R$ 300,00', 
'Projeto estrutural | tipo: M.Obra | Unitário:  R$ 150,00 | Total:  R$ 150,00', 
'Execução de estacas | tipo: M.Obra | Unitário:  R$ 300,00 | Total:  R$ 600,00', 
'Coluna de aço (armadura pronta) | tipo: Mat. | Unitário:  R$ 110,00 | Total:  R$ 220,00', 
'Tábua bruta pinus | tipo: Mat. | Unitário:  R$ 36,00 | Total:  R$ 180,00', 
'Prego com cabeça | tipo: Mat. | Unitário:  R$ 40,00 | Total:  R$ 80,00', 
'Arame recozido | tipo: Mat. | Unitário:  R$ 15,00 | Total:  R$ 30,00', 
'Cimento | tipo: Mat. | Unitário:  R$ 32,00 | Total:  R$ 320,00', 
'Areia Grossa | tipo: Mat. | Unitário:  R$ 190,00 | Total:  R$ 190,00', 
'Brita #1 | tipo: Mat. | Unitário:  R$ 190,00 | Total:  R$ 190,00', 
'Acabamentos diversos | tipo: M.Obra | Unitário:  R$ 500,00 | Total:  R$ 500,00', 
'Adequações de pota | tipo: Mat. | Unitário:  R$ 500,00 | Total:  R$ 500,00', 
'Diversos | tipo: Mat. | Unitário:  R$ 1.200,00 | Total:  R$ 1.200,00'],

'Contrato: 25147 - Garden' :
['Mão de obra execução | tipo: M.Obra | Unitário: R$ 300,00 | Total: R$ 300,00',
'Massa pronta | tipo: Mat. | Unitário: R$ 7,00 | Total: R$ 21,00',
'Argamassa Aciii | tipo: Mat. | Unitário: R$ 30,00 | Total: R$ 30,00',
'Revestimento padrão | tipo: Mat. | Unitário: R$ 39,90 | Total: R$ 79,80',
'Conserto tubo | tipo: Mat. | Unitário: R$ 200,00 | Total: R$ 200,00',
'Reparo forro de gesso | tipo: M.Obra | Unitário: R$ 150,00 | Total: R$ 150,00' 
]

}

MargemLucro = {
'Contrato: 25146 - Condomínio Estúdio Uno' : [
'Custo Mão de Obra: R$ 14.071,00',
'Custo Material: R$ 33.962,13',
'Custo Total: R$ 48.033,13',
'Venda Mão de Obra x 1.80: R$ 25.327,80',
'Venda Material x 1.50: R$ 50.943,19',
'Venda total x 1.59(Taxa Mão de Obra/Taxa Material): R$ 76.270,99',
color('Imposto pago: Total x 0,12: R$ 9.152,52', 'red'),
color('Lucro Previsto: R$ 19.085,34', 'blue'),
color(f'Lucro real: Lucro Previsto x 0.05 = R$ {19085.34 * 0.05:.2f}', 'green')
],

'Contrato: 25149 - Jardinatti' : [
'Custo Mão de Obra: R$ 2.320,00',
'Custo Material: R$ 4.516,80',
'Custo Total: R$ 6.836,80',
'Venda Mão de Obra x 1.80: R$ 4.176,00',
'Venda Material x 1.50: R$ 8.130,24',
'Venda total x 1.59(Taxa Mão de Obra/Taxa Material): R$ 12.306,24',
color('Imposto pago: Total x 0,12: R$ 1.476,75', 'red'),
color('Lucro Previsto: R$ 3.992,69', 'blue'),
color(f'Lucro real: Lucro Previsto x 0.05 = R$ {3992.69 * 0.05:.2f}', 'green')
],

'Contrato: 25147 - Garden' :[
'Custo Mão de Obra: R$ 450,00',
'Custo Material: R$ 330,80',
'Custo Total: R$ 780,80',
'Venda Mão de Obra x 1.80: R$ 810,00',
'Venda Material x 1.50: R$ 446,58',
'Venda total x 1.59(Taxa Mão de Obra/Taxa Material): R$ 1.236,57',
color('Imposto pago: Total x 0,12: R$ 148,39', 'red'),
color('Lucro Previsto: R$ 307,38', 'blue'),
color(f'Média do lucro real: Lucro Previsto x 0.05 = R$ {307.38 * 0.05:.2f}', 'green')
]

}

Materiais = {
'Contrato: 25146 - Condomínio Estúdio Uno': [
f'Média de Gasto com materiais : Total gasto com materiais / Custo total de materiais = R$ {33962.13/18:.2f} '
],

'Contrato: 25149 - Jardinatti': [
f'Média de Gasto com materiais : Total gasto com materiais / Custo total de materiais = R$ {4516.80/14:.2f}'
],

'Contrato: 25147 - Garden': [
f'Média de Gasto com materiais : Total gasto com materiais / Custo total de materiais = R$ {330.80/4:.2f}'
]
}

Desperdicio = {
'Contrato: 25146 - Condomínio Estúdio Uno' : [
f'Desperdício previsto: Custo total x 15%: {48033.13 * 0.15:.2f}'
'O desperdício real não pode ser calculado'
],

'Contrato: 25149 - Jardinatti': [
f'Desperdício previsto: Custo total x 15%: {6836.80 * 0.15:.2f}'
'O desperdício real não pode ser calculado'
],

'Contrato: 25147 - Garden': [
f'Desperdício previsto: Custo total x 12%: {780.80 * 0.12:.2f}'
'O desperdício real não pode ser calculado'
]
}

EquipamentosEletronicos = {
'Equipamentos Eletronicos da empresa em geral':[
'2 Notebooks',
'1 Computador',
'4 Impressoras multiuso',
'2 Drones de imagem',
'1 Câmera térmica',
'1 Pacômetro',
'2 Trenas à laser',
'1 Modem',
'3 HDs externos',
'1 Televisão',
'2 Monitores'
]
}   

Funcionarios = {
'Média de Funcionários por obra':[
'Fixos: 2 Engenheiros Civis',
'1 Encarregado de obra',
'2 Pedreiros',
'3 Ajudantes'
]
}

#Retorna o a chave e o valor de cada uma das opções escolhidas
def get_items(case):
    for key, values in case.items():
        sleep(2)
        title(f'{key}')
        for item in values:
            print(f'- {item}')

#Menu de interação 
while True:
    response = menu(options)
    sleep(1)
    match response:
        case 1:
            get_items(Gastos)
        case 2:
            get_items(MargemLucro)
        case 3:
            get_items(Materiais)
        case 4:
            get_items(Desperdicio)
        case 5:
            get_items(EquipamentosEletronicos)
        case 6:
            get_items(Funcionarios)
        case 7:
            break
    sleep(1)
title('Finalizando sistema de consultas...')
sleep(2)