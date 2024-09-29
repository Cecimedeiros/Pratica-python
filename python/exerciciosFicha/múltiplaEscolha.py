print(" 1- cadastro", "\n", "2- excluir", "\n", "3- exibicao", "\n", "4- atualizar", "\n", "5-buscar")

opcao=str(input("O que você deseja fazer?"))

match str (opcao):
    case 1:
        print("Cadastrando um cliente")
    case 2:
        print("Excluindo um cliente")
    case 3:
        print("Exibindo todos os clientes")
    case 4:
        print(" Atualizando o sistema")
    case 5:
        print("Buscando cliente no sistema...")

