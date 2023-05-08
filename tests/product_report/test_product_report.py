from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Processador",
        "exotech",
        "07/07/1995",
        "01/01/2010",
        "1234567",
        "Local seguro",
    )

    assert product.__repr__() == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
