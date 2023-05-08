import xml.etree.ElementTree as Et
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        data = []
        with open(path) as file:
            root_xml = Et.parse(file).getroot()
            for rec in root_xml.findall(".//record"):
                product = {}
                for tag in rec:
                    product[tag.tag] = tag.text
                data.append(product)
        return data
