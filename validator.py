from lxml import etree
parser = etree.XMLParser(dtd_validation=True)

try:
    tree = etree.parse("ksiazki.xml", parser)
    print('Validation successful')
except Exception as e:
    print(str(e))
