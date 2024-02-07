# Importe das funções 
from funcoes import(adicionar_produto, visualizar_produto, atualizar_produto, remover_produto)

def menu():
    while True:
        print('SISTEMA DE CONTROLE DE PRODUTOS')
        print('1 - Adicionar Produto')
        print('2 - Lista de Produtos')
        print('3 - Atualizar Produto')
        print('4 - Remover Produto')
        print('5 - Sair')

        opcao = int(input('Digite a opção desejada: '))

        match opcao:

            case 1:
                adicionar_produto()
            
            case 2:
                visualizar_produto()

            case 3:
                atualizar_produto()

            case 4:
                remover_produto()

            case 5:
                print('Programa Encerrado')
                break
        
if __name__ == '__main__':
    menu()
                


