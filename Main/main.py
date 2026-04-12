#Gera um 'atraso' no sistema, é um efeito legal, parece que o sistema ta carregando
from time import sleep 

#Funçao para definir cores que vou utilizar no sistema inteiro
def color(text, color_name):
    colors = {
        'clear': '\033[m',
        'yellow': '\033[1;33m',
        'red': '\033[1;31m',
        'green': '\033[1;32m',
        'blue': '\033[1;34m'
    }
    return colors.get(color_name, colors['clear']) + text + colors['clear']

#Linha de separação do título
line = ('-' * 40)

#Título em si
def title(txt):
    print(color(line, 'yellow'))
    print(color(txt.center(len(line)), 'blue'))
    print(color(line, 'yellow'))

#Defini o 'login' do admin, mais pra frente vai ter verificação disso
admin = {
    'username': 'admin',
    'email': 'admin.system@gmail.com',
    'password': '123456'
}

#Função para validar
def user_validation(user, email, password):
    if (user == admin['username'] and
        email == admin['email'] and 
        password == admin['password']):
        return True
    return False

#Login
def login(lgn):
    print(color(line, 'yellow'))
    print(color(lgn.center(len(line)), 'blue'))
    print(color(line, 'yellow'))

login('Faça seu login para continuar!')

user = str( input(color('Usuário: ', 'green')))
email = str( input(color('Email: ', 'green')))
password = input(color('Senha: ', 'green'))

#Validação
if user_validation(user, email, password):
    print(color(line, 'yellow'))
    print(color('Seja bem-vindo!'.center(len(line)), 'blue'))
    print(color(line, 'yellow'))
else:
    print(color(line, 'yellow'))
    print(color('Usuário não encontrado!'.center(len(line)), 'red'))
    print(color(line, 'yellow'))

