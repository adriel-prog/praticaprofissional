# modular.py

# Cadastro de produtos
def cadastrar_produto(estoque, codigo, nome, preco, quantidade):
    if codigo in estoque:
        print("Código já cadastrado!")
    else:
        estoque[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
        print("Produto cadastrado com sucesso!")

# Movimento de estoque
def movimentar_estoque(estoque, codigo, quantidade):
    if codigo in estoque:
        estoque[codigo]["quantidade"] += quantidade
        print("Movimento realizado com sucesso!")
    else:
        print("Produto não encontrado!")

# Relatórios
def gerar_relatorio(estoque):
    print("\nRelatório de Estoque:")
    print(f"{'Código':<10}{'Nome':<20}{'Preço':<10}{'Quantidade':<10}")
    print("-" * 50)
    for codigo, dados in estoque.items():
        print(f"{codigo:<10}{dados['nome']:<20}{dados['preco']:<10.2f}{dados['quantidade']:<10}")
    print("-" * 50)

# Programa principal
if __name__ == "__main__":
    estoque = {}
    while True:
        print("\nMenu:")
        print("1. Cadastrar Produto")
        print("2. Movimentar Estoque")
        print("3. Gerar Relatório")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade inicial: "))
            cadastrar_produto(estoque, codigo, nome, preco, quantidade)
        elif opcao == "2":
            codigo = input("Código do produto: ")
            quantidade = int(input("Quantidade a movimentar (use negativo para saída): "))
            movimentar_estoque(estoque, codigo, quantidade)
        elif opcao == "3":
            gerar_relatorio(estoque)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")