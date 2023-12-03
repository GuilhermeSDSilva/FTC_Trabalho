import re
aprovado = True
info ="""04.280.196/0001-76 uea@uea.edu.br +55(92)3348-7601

09.628.825/0001-20 03.A4.2B.F8

==========

uea@uea.edu.br 09.628.825/0001-20 R$ 1.000.000,00 09/01/2023 09:03 ABC@@1234abc

03.A4.2B.F8 +55(92)3348-7601 R$ 2.000.000,00 08/01/2022 10:10 FG@H*12ab34c"""

padrao_cnpj = re.compile(r'^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$')
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

inicio_final=0
for x in range(len(info)):
  if info[x]!="=":
    inicio += info[x]
  else:
    inicio_final=x
    break
    
inicio_final+=10

for y in range(inicio_final,len(info)):
  final+=info[y]

inicio = inicio.split()
for z in range (len(inicio)):
    cnpj_encontrado = padrao_cnpj.findall(inicio[z])
    chaves+=cnpj_encontrado
    cpf_encontrado = padrao_cpf.findall(inicio[z])
    chaves+=cpf_encontrado
    email_encontrado = padrao_email.findall(inicio[z])
    chaves+=email_encontrado
    telefone_encontrado = padrao_telefone.findall(inicio[z])
    chaves+=telefone_encontrado
    chave_encontrado = padrao_chaves_rapidas.findall(inicio[z])
    chaves+=chave_encontrado
    
    

print(chaves)
