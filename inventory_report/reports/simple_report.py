from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        old_date = min(i["data_de_fabricacao"] for i in data)
        prox_validate = min(
            (i["data_de_validade"] for i in data if i
                ["data_de_validade"] >= datetime.now().strftime("%Y-%m-%d"))
        )

        company = [i["nome_da_empresa"] for i in data]
        more_products = Counter(company).most_common(1)[0][0]

        report = (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {prox_validate}\n"
            f"Empresa com mais produtos: {more_products}"
        )

        return report
