import csv
# import json
# import xml.etree.ElementTree as Et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def func_csv(file):
    data = csv.DictReader(file)
    return [row for row in data]


def read(path):
    with open(path) as file:
        if path.endswith(".csv"):
            return func_csv(file)


class Inventory:
    @staticmethod
    def import_data(path, type):
        data = read(path)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
