import re
aprovado = True
info =input()
padrao_cnpj = re.compile(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$')
padrao_numero_completo = re.compile(r'^\+55\(\d{2}\)\d{4,5}-\d{4}$')
padrao_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
padrao_chaves_rapidas = re.compile(r'^[0-9A-Fa-f]{2}\.[0-9A-Fa-f&&[^0-9A-Fa-f]]{2}\.[0-9A-Fa-f]{2}\.[0-9A-Fa-f&&[^0-9A-Fa-f]]{2}$')
padrao_data = re.compile(r'^\d{2}/\d{2}/\d{4}$')
padrao_hora = re.compile(r'^([01][0-9]|2[0-3]):[0-5][0-9]$')
padrao_email = re.compile(r'.+@.+')
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

cpf_encontrado=padrao_cpf.findall(inicio)
chaves+=cpf_encontrado
cnpj_encontrado=padrao_cnpj.findall(inicio)
chaves+=cnpj_encontrado
telefone_encontrado=padrao_numero_completo.findall(inicio)
chaves+=telefone_encontrado
email_encontrado=padrao_email.findall(inicio)
chaves+=email_encontrado
chave_encontrado=padrao_chaves_rapidas.findall(inicio)
chaves+=chave_encontrado

