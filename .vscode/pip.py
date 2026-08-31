import requests

url= "https://jsonplaceholder.typicode.com/users"

try:
    resposta = requests.get(
        url,
        timeout=10
    )

    resposta.raise_for_status()
    usuarios = resposta.json()
    print ("Usuários da API")

    for usuario in usuarios:
        print(
            "ID:", usuario ["ID"],
            "Nome:", usuario["name"],
            "Email", usuario["email"]
        )

    nome_busca = input(
        "\nDigite parte do  nome que deseja buscar"
    ).strip().lower()
    
    
    encontrado = False
    for usuario in usuarios:
        nome = usuario["name"].strip().lower()
        if nome_busca in nome:
            print("\nusuario encontrado")
            print("id", usuario["id"])
            print("nome", usuario["name"])
            print("email", usuario["email"])
            print("telefone", usuario["telefone"])
    if encontrado ==False:
        print("\nNenhum usuário encontrado")
except requests.exceptions.ConnectionError:
    print("\nerro de conexão")
except requests.exceptions.Timeout:
    print("\ndemorou d+")
except requests.exceptions.HTTPError as erro:
    print("erro no http",erro)
except KeyError as erro:
    print("Campo não encontrado",erro)
except ValueError:
    print("Não foi possível interpertrar dados")
        


