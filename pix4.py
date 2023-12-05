import re
import sys
aprovado = True

def validar_cpf(cpf):
    cpf = [int(digito) for digito in cpf if digito.isdigit()]
    
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    
    soma1 = sum(x * y for x, y in zip(cpf[:9], range(10, 1, -1)))
    digito1 = (soma1 * 10) % 11 % 10
    
    soma2 = sum(x * y for x, y in zip(cpf[:10], range(11, 1, -1))) + digito1 * 2
    digito2 = (soma2 * 10) % 11 % 10
    
    return digito1 == cpf[9] and digito2 == cpf[10]


def validar_cnpj(cnpj):
    cnpj = [int(digito) for digito in cnpj if digito.isdigit()]
    
    if len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False
    
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(x * y for x, y in zip(cnpj[:12], peso1))
    digito1 = (11 - soma1 % 11) % 11
    
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum(x * y for x, y in zip(cnpj[:13], peso2))
    digito2 = (11 - soma2 % 11) % 11
    
    return digito1 == cnpj[12] and digito2 == cnpj[13]




def finalizar():
    print("False", end="")
    sys.exit()


info="""987.654.321-00 alice@email.com 1A.2B.3C.4D +55(92)8765-4321
11.222.333/0001-44 company@cnpj.com
==========
alice@email.com alice@email.com R$ 500,00 20/09/2022 18:30 P@ssw0rd123!%
1A.2B.3C.4D +55(92)8765-4321 R$ 300,00 20/09/2022 19:00 987654ABCdef"""

fin="""
==========
"""

if info == fin:
    finalizar()

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
        cnpj_encontrado = padrao_cnpj.match(inicio[z])

        if (cnpj_encontrado):
            
            if(validar_cnpj(cnpj_encontrado.group())):
                chaves.append(cnpj_encontrado.group())
                    
    
        cpf_encontrado = padrao_cpf.match(inicio[z])
        if (cpf_encontrado):
            if(validar_cpf(cpf_encontrado.group())):
                chaves.append(cpf_encontrado.group())
                
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
