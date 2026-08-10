dados = "Ana;Notebook;4500"
print(type(dados))
campos = dados.split(";")
print(campos)
print(type(campos))
nome = "      Ana       "
nome.strip() #o strip ele retira os espaços em branco
nome.strip.lower() # os espaços em branco e letras minúsculas 

print(nome)
print(nome.strip())
print(nome.strip().lower())
dados = """
ana@gmail.com.br;Notebook;4500
calo@gmail.com.br;Mouse;80
ana@gmail.com;Monitor;250
maria@gmail.com:Monitor;350
joao@gmail.com;Noebok;4500
"""

dados= dados.strip()
linhas= dados.splitlines()
print(linhas)
print(len(linhas))
linha = linhas [0]
print(linha)
campos = linha.split(";")
print (campos)
email = campos[0].strip().lower()
produto= campos[1].stip().lower()
preco= float (campos[2].strip())
print(type(preco))
print(type(campos[2]))