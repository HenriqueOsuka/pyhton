arquivo = open ("dados.txt","w", encoding ="utf-8")
arquivo.write("Linha 1 -aula de Python")
arquivo.write(" Linha 2 - Segunda-Feira")
arquivo.close()
print("Arquivo criado com sucesso")
#ler arquivo 
arquivo= open ("dados.txt","r",encoding= "utf-8")
conteudo = arquivo.read
print("\n Conteúdo do arquivo")
print (conteudo)
arquivo.close()
#adicionar 
arquivo = open ("dados.txt","a",encoding="utf-8")
arquivo.write("Linha 3 - Amanhã tem mentoria")
print("\n Conteúdo adicionado com suceseso")
arquivo.close()
#Métodos de leitura 
with open("dados.txt","r",encoding="utf-8") as arquivo:
    print ("\n readline ()-lê uma linha")
    print(arquivo.readline())
    linhas = arquivo.readlines () # listas de linhas 
    print (linhas)
with open ("dados.txt","r",encoding="utf-8") as arquivo:
    arquivo.seek (0)
    print("\n Primeiros 10 caracteres")
    print(arquivo.read(20))


    




