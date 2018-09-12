#Завдання 3. Створити файл c.xml (згідно з стандартами), записати в нього
#всі унікальні слова та кількість їх вживання у тексті, використовуючи файл а.txt
#із завдання 2.
import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root,"doc")

with open("a.txt", "r") as f:
	all_words = dict()
	for line in f:
		words = line.split()
		for word in words:
			if ',' in word:
				word = word.replace(',','')				
			elif '.' in word:
				word = word.replace('.','')				
			if word not in list(all_words):
				all_words[word] = 1
			else:
				all_words[word]+=1
				
n = 0
for x in all_words:
	ET.SubElement(doc, "field%s"%n, name = x).text = str(all_words.get(x))
	n+=1

tree = ET.ElementTree(root)
tree.write("c.xml")	
