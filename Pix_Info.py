info =input()
padrao_cnpj = re.compile(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$')
padrao_numero_completo = re.compile(r'^\+55\(\d{2}\)\d{4,5}-\d{4}$')
padrao_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
padrao_chave_rapida = re.compile(r'^\d{2}\.[A-F0-9]{2}\.\d{2}\.[A-F0-9]{2}$')
padrao_data = re.compile(r'^\d{2}/\d{2}/\d{4}$')
padrao_hora = re.compile(r'^([01][0-9]|2[0-3]):[0-5][0-9]$')

chaves = []
while True:
  
