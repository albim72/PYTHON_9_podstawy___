from xml.dom.minidom import parse

dom = parse("dane_kody.xml")
name = dom.getElementsByTagName('name')
kod = dom.getElementsByTagName('kod')
url = dom.getElementsByTagName('url')
ds = dom.getElementsByTagName('opis')[0]

ds_atrybut = ds.getAttribute('desc')

print("  ".join(t.nodeValue for t in name[0].childNodes if t.nodeType == t.TEXT_NODE))
print("  ".join(t.nodeValue for t in kod[0].childNodes if t.nodeType == t.TEXT_NODE))
print("  ".join(t.nodeValue for t in kod[1].childNodes if t.nodeType == t.TEXT_NODE))
print("  ".join(t.nodeValue for t in url[0].childNodes if t.nodeType == t.TEXT_NODE))
print("  ".join(t.nodeValue for t in url[1].childNodes if t.nodeType == t.TEXT_NODE))
# print("  ".join(t.nodeValue for t in ds[0].childNodes if t.nodeType == t.TEXT_NODE))
print(f"atrybut taga opis: {ds_atrybut}")
