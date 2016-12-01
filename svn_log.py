#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path
import os.path
import xml.dom.minidom
import os.path
import xml.etree.ElementTree as ET

path_list = {}

#取所有资源版本号
def log_res_list(file_name):
	os.path.split(os.path.realpath(__file__))[0]
	tree = ET.ElementTree(file = "old_version.xml")
	root = tree.getroot()

	for child in root:
		#print child.tag
		version_id = child.attrib["revision"]
		paths = child.find("paths")
		for path in paths:
			#print path.text

			if path_list.has_key(path.text):
				old_version = 0#int(path_list[path.text].encode("utf-8"))
				now_version = int(version_id.encode("utf-8"))
				if now_version > old_version:
					path_list[path.text] = str(now_version)

			else:
				path_list[path.text] = version_id


			#print path.text,":",version_id,"\n"
		
		#print child.tag

	
	#print path_list
def fomatTree(elem):
 	"""格式化XML的内容,用于输出，保存XML时并不需要"""
 	root_str = ET.tostring(elem, 'UTF-8')
 	reparse = xml.dom.minidom.parseString(root_str)
 	return reparse.toprettyxml(" ")
	

def gen_res_list_xml():
	file = open("new_version.xml","wb+")
	
	doc = xml.dom.minidom.Document()

	root_element = doc.createElement("update")
	doc.appendChild(root_element)
	for x in path_list:
		element = doc.createElement("res")
		
		element.setAttribute("name",x.encode('UTF-8'))
		element.setAttribute("id", path_list[x].encode('UTF-8'))
		root_element.appendChild(element)
		pass
	
	doc.writexml(file,"\t","\t","\n","utf-8")	

	
def main():
	temp_path = os.path.dirname(os.path.realpath(__file__))
	print temp_path
	cmd = "cd " + temp_path
	os.system(cmd)
	print cmd
	
	os.system("svn log -v -r 15510:15594 --xml >>old_version.xml")
	os.system("pause")
	pass

if __name__ == '__main__':
	#main()
	log_res_list("")
	gen_res_list_xml()