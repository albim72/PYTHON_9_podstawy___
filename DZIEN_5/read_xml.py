import xml.etree.ElementTree as ET

try:
    tree=ET.parse("kraj.xml")
    root = tree.getroot()

    for child in root:
        print(f'tag: {child.tag}, atrybyuty: {child.attrib}')

except Exception as exc:
    print(exc)
