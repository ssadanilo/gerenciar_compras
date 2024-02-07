# Criando a lista
lista_produtos = []
# Criando as linhas
linhas = '_' * 100

# Função para adicionar um produto a lista
def adicionar_produto():
    print('Adicionar Produto')
    nome_produto = input('Digite o nome do produto: ').lower().strip()
    preco_com_virgula = input('Digite o valor do produto: ') # Criando uma varável que aceite o caracter vírgula no preço
    preco_com_virgula = preco_com_virgula.replace(',', '.') # Substitui vírgula por ponto
    preco_produto = float(preco_com_virgula) # Variável permanente que substitui a anterior já com erro corrigido         
    qto_produto = int(input('Digite a quantidade do produto: '))
    total_produto = qto_produto * preco_produto # Total da compra a ser apresentada
    composicao_produto = {'produto': nome_produto, 'custo': preco_produto, 'quantidade': qto_produto, 'custo total': total_produto}
    lista_produtos.append(composicao_produto)
    print(linhas)
    print(f'{composicao_produto} Adidionado com sucesso!')
    print(linhas)
          
# Função para visualizar a lista de produtos
def visualizar_produto():
    print('Lista de Produtos')
    for composicao_produto in lista_produtos:
        print(linhas)
        print(f'Nome: {composicao_produto['produto']}, Quantidade: {composicao_produto['quantidade']}, Custo: {composicao_produto['custo']}, custo total: {composicao_produto['custo total']}')
    
    total_compras = sum(composicao_produto['custo total'] for composicao_produto in lista_produtos)
    print(linhas)
    print(f'Total das compras: {total_compras}')
    print(linhas)

# Função para atualizar o produto
def atualizar_produto():
    print('Atualizar Produto')
    nome_produto = input('Digite o nome do produto a ser atualizado: ').lower().strip()
    for composicao_produto in lista_produtos:
        if composicao_produto['produto'] == nome_produto:
            composicao_produto['produto'] = input('Nome do novo produto: ')
            preco_com_virgula = input('Preço do novo produto: ') # Criando uma varável que aceite o caracter vírgula no preço
            preco_com_virgula = preco_com_virgula.replace(',', '.') # Caso o usuário digite o preço com uma vírgula, será substituído por um ponto
            composicao_produto['custo'] = float(preco_com_virgula) # Variável permanente que substitui a anterior já com erro corrigido
            composicao_produto['quantidade'] = int(input('Nova quantidade do produto: '))
            composicao_produto['custo total'] = composicao_produto['quantidade'] * composicao_produto['custo'] # Total da compra a ser apresentada
            print(linhas)
            print('Produto atualizado com sucesso!')
            print(linhas)
            return
    print(linhas)
    print('Produto não encontrado na lista')
    print(linhas)
 
# Função para remover um produto da lista
def remover_produto():
    nome_produto = input('Digite o nome do produto: ')
    for composicao_produto in lista_produtos:
        if composicao_produto['produto'] == nome_produto:
            lista_produtos.remove(composicao_produto)
            print(linhas)
            print(f'Produto {nome_produto} removido com sucesso!')
            print(linhas)
            return
    print(linhas)
    print('Produto não encontrado na lista')
    print(linhas)

