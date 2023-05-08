import csv
import json
import xml.etree.ElementTree as Et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def func_csv(file):
    data = csv.DictReader(file)
    return [row for row in data]


def func_json(file):
    data = file.read()
    return json.loads(data)


def func_xml(file):
    data = []
    root_xml = Et.parse(file).getroot()
    for record in root_xml.findall(".//record"):
        product = {}
        for tag in record:
            product[tag.tag] = tag.text
        data.append(product)
    return data


def read(path):
    with open(path) as file:
        if path.endswith(".csv"):
            return func_csv(file)
        elif path.endswith(".json"):
            return func_json(file)
        elif path.endswith(".xml"):
            return func_xml(file)


class Inventory:
    @staticmethod
    def import_data(path, type):
        data = read(path)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
