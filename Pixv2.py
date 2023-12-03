import re
aprovado = True
info=input()

padrao_cnpj = re.compile(r'^\d{2,3}\.\d{3}\.\d{3}/\d{4}-\d{2}$')
padrao_telefone= re.compile(r'^\+55\(\d{2}\)\d{4,5}-\d{4}$')
padrao_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
padrao_chaves_rapidas = re.compile(r'\b[0-9A-Fa-f]{2}(?:\.[0-9A-Fa-f]{2}){3}\b')
padrao_data = re.compile(r'^\d{2}/\d{2}/\d{4}$')
padrao_hora = re.compile(r'^([01][0-9]|2[0-3]):[0-5][0-9]$')
padrao_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
chaves = []

inicio=""
meio="=========="
final=""

inicio_final = info.find(meio) + len(meio)

# Separar o início até o ponto onde as igualdades terminam
inicio = info[:inicio_final]

# O final é tudo após o ponto onde as igualdades terminam
final = info[inicio_final:]

# Verificar se 'inicio' não está vazio antes de dividir
if inicio:
    inicio = inicio.split()
    for z in range(len(inicio)):
        cnpj_encontrado = padrao_cnpj.findall(inicio[z])
        chaves += cnpj_encontrado
        cpf_encontrado = padrao_cpf.findall(inicio[z])
        chaves += cpf_encontrado
        email_encontrado = padrao_email.findall(inicio[z])
        chaves += email_encontrado
        telefone_encontrado = padrao_telefone.findall(inicio[z])
        chaves += telefone_encontrado
        chave_encontrado = padrao_chaves_rapidas.findall(inicio[z])
        chaves += chave_encontrado

    

