rase = ""
def digitar():
    global frase
    frase = input("Digite sua frase").strip()
   
   
def quantidade():
    palavras = frase.strip()
    print("Quantidade de palavras:",len(palavras))
   
def substituir():
    global frase
    antiga = input("Palavra substituir:")
    nova = input("Nova palavra")
    frase = frase.replace(antiga,nova)
    print ("Frase atualizada",frase)
 
def verificar():
    palavra = input ("Digite a palavra")
    if palavra in frase:
        print("Existe na frase")
    else:
        print("Não existe a palavra")
       
def inverter():
    print("Frase invertida:",frase[::-1])      
                   
while True:
    print ("\n 1 - Digitar \n 2 - Quantidade \n 3 - Substituir \n 4 - Verificar \n 5 - Inverter \n 6 - Sair")
    op = input ("Opção:")
    match op:
        case "1":
            digitar()
        case "2":
            quantidade()
        case "3":
            substituir()
        case "4":
            verificar()
        case "5":
            inverter()
        case "6":
            print("Encerrando")
            break
        case _:
            print ("Opção inválida")