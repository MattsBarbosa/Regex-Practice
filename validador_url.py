import re

# https://www.bytebank.com.br/cambio
# usando () em vez de [] em RegeEx significa
#[] pode ter qualquer caracter desta lista
#() precisa conter exatamente o mesmo conteudo na mesma ordem

url = "https://www.bytebank.com.br/cambio"
padrao_url = re.compile('(http(s)?://)?(www.)?bybank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")


#search quando queremos buscar um padrão dentro de uma string inteira
#match quando queremos verificar se a nossa string inteira bate com aquele padrão.