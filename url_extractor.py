import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia.")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        index_question_mark = self.url.find('?')
        url_base = self.url[:index_question_mark]
        return url_base

    def get_url_parametros(self):
        index_question_mark = self.url.find('?')
        url_parametros = self.url[index_question_mark+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print(extrator_url)

valor_dolar = 5.50 # 1 dolar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")
quantidade_float = float(quantidade)

if moeda_origem == "real":
    resultado = quantidade_float * valor_dolar
    print(f"{quantidade_float:.2f} reais equivale a: {resultado}{moeda_destino}")

elif moeda_origem == "dollar":
    resultado = quantidade_float / valor_dolar
    print(f"{quantidade_float:.2f} dólares equivale a: {resultado}{moeda_destino}")

else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")