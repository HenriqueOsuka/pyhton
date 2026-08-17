
# ============================================================
# PARTE 1 - LISTA
# ============================================================

# Criamos uma lista representando um aluno.
#
# Cada informação ocupa uma posição (índice).

aluno_lista = [
    "Ana",
    20,
    "Sistemas de Informação"
]


# Os índices começam em 0.
#
# 0 -> nome
# 1 -> idade
# 2 -> curso

print("Nome:", aluno_lista[0])

print("Idade:", aluno_lista[1])

print("Curso:", aluno_lista[2])


# ============================================================
# PARTE 2 - DICIONÁRIO
# ============================================================

# Agora representamos o mesmo aluno utilizando
# um dicionário.
#
# Diferentemente da lista, não precisamos lembrar
# qual é o índice de cada informação.
#
# Utilizamos CHAVE -> VALOR.

aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Sistemas de Informação"
}
# Para acessar uma informação, utilizamos sua chave.
print("\nNome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])


# ============================================================
# PARTE 3 - ADICIONANDO E ALTERANDO INFORMAÇÕES
# ============================================================

# Podemos adicionar uma nova informação ao dicionário.

aluno["email"] = "ana@email.com"


# Podemos alterar uma informação existente.

aluno["idade"] = 21


print("\nAluno atualizado:")

print(aluno)

print("\nChaves:")
print(aluno.keys())

print("\nValores:")
print(aluno.values())

print("\nItens:")
print(aluno.items())


print("\nDados do aluno")
for chave, valor in aluno.items():
    print(chave, ":", valor)

print ("\nConsulta ao dicionário")
#todo try deve terminar com um except pois precisa de um escape caso de erro 
try:
    chave = input(
        "digite a informação que deseja"
    )
    print("resultado:", aluno[chave])
except KeyError:
    print(
        "Erro: essa informação não existe"
    )
print(
    aluno.get(
        "Telefone",
        "Telefone não cadastrado"
    )
)


produto =[
{
    "nome": "Notebook",
    "preco": 4500,
    "quantidade": 10,
    "categoria": "informática"
},
{
    "nome":"Mouse",
    "preco": 80,
    "quantidade":25,
    "categoria": "Periférico",
},
{
    "nome": "Teclado",
    "Preco": 250,
    "quantidade:": 15,
    "categoria": "periférico "

}]

print ("Produto")
print ("=======")
print ("nome:", produto ["nome"])
print ("Preço:", produto ["preco"])
print ("Quantidade:", produto ["quantidade"])
print ("Categoria:", produto["categoria"])



produto_busca = input ("Digite o nome do produt:").strip(),lower()
encontrado = False
for produto in produto:
    #lower() permite comparar sem considerar
    #diferenças entre maiúsculas e minúsculas 
    if produto["nome"].lower() == produto_busca:
        print ("\nProduto encontrado!")
        print("Nome:", produto["nome"])
        print("Preço:", produto["preco"])
        print("Quantidade:", produto["quantidade"])
        print("Categoria:", produto["categoria"])
        encontrado = True

if encontrado == False:
        print("\nProduto não encontrado")


try: 
     #solicitar o nome do produto
     nome = input ("Nome do produto:").strip()
     #verifica se o campo foi preenchido 
     if nome == "":
          raise ValueError ("o nome não pode ser vazio")
     #solicita o preço
     preco = float(input("Preço:"))
     #verifica uma regra de negócio
     if preco <= 0:
          raise ValueError ("O preço deve ser maior que zero")
     #solicita a quantidade
     quantidade = nt(input("Quantidade:"))
     #verifica se a quantidade é válida
     if quantidade <=0:
          raise ValueError ("A quantidade não pode ser negativa")
     #solicitar a categoria
     categoria = input ("categoria:").strp()
     #verifica se a categoria foi preenchida
     if categoria =="":
          raise ValueError("A categoria não pode ser vazia")
     # se todas as informações forem válidas #criamos o novo dicionário
     novo_produto = {
          "nome":nome,
          "preco":preco,
          "quantidade":quantidade,
          "categoria":categoria
     }
     #adicionamo o novo produto à lista
     produto.append(novo_produto)
     print("\nProduto cadastrado com sucesso")
     #trata de erros de conversão e erros
     #de validação criados pelo programa
except ValueError as erro:
     print("\nerro", erro)