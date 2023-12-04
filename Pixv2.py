import re
aprovado = True
info="""04.280.196/0001-76 uea@uea.edu.br +55(92)3348-7601

09.628.825/0001-20 03.A4.2B.F8

==========

uea@uea.edu.br 09.628.825/0001-20 R$ 1.000.000,00 09/01/2023 09:03 ABC@@1234abc

03.A4.2B.F8 +55(92)3348-7601 R$ 2.000.000,00 08/01/2022 10:10 FG@H*12ab34c"""

padrao_cnpj = re.compile(r'^\d{2,3}\.\d{3}\.\d{3}/\d{4}-\d{2}$')
padrao_telefone= re.compile(r'^\+55\(\d{2}\)\d{4,5}-\d{4}$')
padrao_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
padrao_chaves_rapidas = re.compile(r"^(?!.*[A-Za-z]{2})(?!.*([0-9A-Fa-f])\1)[0-9A-Fa-f]([0-9A-Fa-f](?![A-Za-z]))?\.[0-9A-Fa-f]{2}(\.[0-9A-Fa-f]{2}){2}$")
padrao_data = re.compile(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$")
padrao_hora = re.compile(r'^([01][0-9]|2[0-3]):[0-5][0-9]$')
padrao_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
padrao_codigo = re.compile(r"^(?=(?:.*[A-Z]){3})(?=(?:.*[a-z]){3})(?=(?:.*[$%@(,[*]){2})(?=(?:.*\d){4}).{12}$")
padrao_dinheiro = re.compile(r'^R\$\s\d{1,3}(?:\.\d{3})*(?:,\d{2})?$')
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
        chave_encontrado = padrao_chaves_rapidas.match(inicio[z])
        if chave_encontrado:
            chaves.append(chave_encontrado.group())
    

    if final:
        linhas_final = final.split('\n')

        for i in range(1, len(linhas_final)): 
            partes_linha = linhas_final[i].split()
            
            
            dinheiro_valida = padrao_dinheiro.match(partes_linha[2]+" "+partes_linha[3])
            data_valida = padrao_data.match(partes_linha[4])
            hora_valida = padrao_hora.match(partes_linha[5])
            codigo_valida = padrao_codigo.match(partes_linha[6])
            
         
            if ((len(partes_linha) >= 2) and (partes_linha[0] in chaves) and (partes_linha[1] in chaves) and (dinheiro_valida) and (data_valida) and(hora_valida) and(codigo_valida)):
                continue  
            else:
                aprovado = False
                break
           
    else:
        aprovado=False           
else:
    aprovado=False

if aprovado==True:
    print("True",end="")
else:
    print("False",end="")
    
