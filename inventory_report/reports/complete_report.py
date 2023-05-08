from .simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    @staticmethod
    def generate(data):
        simple = SimpleReport.generate(data)
        company = [i["nome_da_empresa"] for i in data]
        company_not_duplicate = []
        for i in company:
            if i not in company_not_duplicate:
                company_not_duplicate.append(i)
        company_item = Counter(company)
        report = f"{simple}\nProdutos estocados por empresa:\n"
        for i in company_not_duplicate:
            quanty = company_item[i]
            report += f"- {i}: {quanty}\n"

        return report
