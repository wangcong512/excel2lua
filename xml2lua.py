#!/usr/bin/env 
# -*- coding: utf-8 -*-

try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys 
import os.path

reload(sys)
print sys.setdefaultencoding("utf-8")

g_tab = {}
g_cfg_tab = {}

def print_table(table):

	for k,v in table.items():
		print k
		for row in v:
			for colum in row:
				print colum,
				pass
			print

		print
	pass


"""
类型有：
int
string1：用引号的字符串,如:"XXX"
string2：用中括号的字符串,如:[[XXX]]
array1：以 "|" 分割的一维数组(不定长)
array2：以"#", "|" 分割的二维数组(不定长)
array3：以"\n", "|" 分割的二维数组(不定长)
array4：以"\n", "#", "|" 分割的三维数组(不定长)
array5：以"\n" 分割的一维数组(不定长)

"""
def gen_global_config(tab_sheet):
	global g_tab
	global g_cfg_tab
	global_config = g_tab[str("全局配置").decode("utf-8")]
	if global_config == None:
		print "not have global_config"
		return
	#
	g_cfg_tab.clear()
	for index in range(0,len(global_config)):
		if index > 0:

			if global_config[index][1] != None:

				g_cfg_tab[global_config[index][0]] = global_config[index]
				fp = open("%s.lua"%global_config[index][1],"wb+")
				fp.close()
	gen_lua_file()		
				

def gen_lua_file():
	global g_cfg_tab
	global g_tab
	# print "test"
	# print_table(g_cfg_tab)
	for k,v in g_cfg_tab.items():
		# print "test",k
		#print_table(g_tab)
		tab_value = g_tab[k]
		fp = open("%s.lua"%v[1],"wb+")
		fp.write("Config = Config or {}\n")
		fp.write("Config.%s = {\n" %v[1])

		for index in range(0,len(tab_value)):

			if index > 3:
				fp.write("{")
				for colum in range(0,len(tab_value[index])):
					
					fp.write("%s = %s,"%(tab_value[0][colum],tab_value[index][colum]))
				fp.write("}\n")


		fp.write("}\n")




def parseXml(path_name):
	

	dir_name = os.path.dirname(__file__)
	tree = ET.ElementTree(file = "dmap_auto.xml")

	if tree == None:
		print "not has file %s" % path_name
	root = tree.getroot()
	global g_tab
	g_tab = {}
	for child in root:
		#print child.tag
		#print child
		# print child.get("{urn:schemas-microsoft-com:office:spreadsheet}Name")
		
		if child.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Worksheet":
			print "---------------------"
			#if child.get("{urn:schemas-microsoft-com:office:spreadsheet}Name") == "全局配置".decode("utf-8"):
			tab = child.find("{urn:schemas-microsoft-com:office:spreadsheet}Table")
			#表数据
			#print tab
			row_data = []
			x = 0
			y = 0
			for row in tab.findall("{urn:schemas-microsoft-com:office:spreadsheet}Row"):
				#print row
				if row.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Row":
					#print row
					colum_data = []
					
					y = 0
					for cell in row.findall("{urn:schemas-microsoft-com:office:spreadsheet}Cell"):
						#print cell
						text = ""
						if cell.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Cell":
							
							indx = cell.get("{urn:schemas-microsoft-com:office:spreadsheet}Index")
							if indx != None:
								y = int(indx) - 1
							
							for data in cell.findall("{urn:schemas-microsoft-com:office:spreadsheet}Data"):
								#print data.text,"\t",
								text = data.text
						while len(colum_data) < y:
							colum_data.insert(y,text)
							pass
						colum_data.insert(y,text)
						y += 1

					#print "\n",
					row_data.insert(x,colum_data)
					x += 1
					
				#print
			# print sys.getdefaultencoding()
			# print sys.stdout.encoding
			# print sys.stdin.encoding
			g_tab[child.get("{urn:schemas-microsoft-com:office:spreadsheet}Name")] = row_data
			
			# else:
			# 	print "not have global config"
			# 	break


	#print str(g_tab)
	#print_table(g_tab)



def genLua():
	pass


def main():
	parseXml("E:\\export\\old_version.xml")
	global g_tab
	gen_global_config(g_tab)
	pass

if __name__ == '__main__':
	main()