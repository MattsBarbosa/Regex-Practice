endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression -- RegEx

# 5 digitos + hifen (opcional) + 3 digitos
# se algo é opcional adicionamos o "?" logo apos o parametro

# quantificadores = de 0 a 9 5 vezes. - de 0 a 9 3 vezes.
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco) # Match

if busca: # Se conseguiu encontrar
    cep = busca.group() # O resultado do match
    print(cep)
