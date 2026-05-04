import json 
arquivo = "clientes.json"
clientes = []
def carregar_dados():
    global clientes
    try:
        with open (arquivo, "r", encoding= "utf-8") as arquivo:
            clientes = json.load(arquivo)
        print("Dados carregados com sucesso")

    except FileNotFoundError:
        def carregar_dados():
            print("Arquivo não encontrado. Criaando uma base vazia")
            clientes=[]

        def cadastrar():
            nome = input("Digite o nome do cliente:")
            email = input ("Digite o e-mail do clienet")
            cliente = {
                "nome"= nome
                "email":email
            } 
            clientes.append (cliente)
            salvar_dados()
        def salvar_dados():
            with open (arquivo, "w",encoding= "utf-8") as arquivo:
                json.dump(clientes, arquivo, ident=4)
                print("Dados salvos com sucesso")
        def menu():
            while True:
                print ("\n ====MENU====")
                print("1- Cadastrar Cliente")
                print("2- Listas Cliente")
                print("3- Buscar Cliente")
                print("4- Remover Cliente")
                print("5- Total de  Cliente")
                print("6- Sair")
                op = input ("Escolha uma opção")
                match op:
                    case "1":
                        cadastrar()
                    case "2":
                        listar()
                    case "3":
                        buscar()
                    case "4":
                        remover()
                    case "5":
                        total_clientes()
                    case "6":
                        print ("Encerrando o sistema")
                        break
                    case _:
                        print ("Opção inválida")
        carregat_dados()
        menu()


    