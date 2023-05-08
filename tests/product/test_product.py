from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Processador",
        "exoshop",
        "07/07/1995",
        "01/01/2010",
        "1234567",
        "Local limpo",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Processador"
    assert product.nome_da_empresa == "exoshop"
    assert product.data_de_fabricacao == "07/07/1995"
    assert product.data_de_validade == "01/01/2010"
    assert product.numero_de_serie == "1234567"
    assert product.instrucoes_de_armazenamento == "Local limpo"
