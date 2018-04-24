# -*- coding: UTF-8 -*-
# 从文件中读取数据
import xml.etree.ElementTree as ET


class BastPage:
    """
    封装读取page.xml
    """

    def __init__(self, filename):
        self.level = 1  # 节点的深度从1开始
        self.result_list=[]
        self.root = ET.parse(filename).getroot()

# 遍历所有的节点
    def walk_data(self, root_node, level, result_list, page_name, locator):
        #global result_list
        if root_node.text.encode('utf-8') == locator:
            temp_list = [level, root_node.tag, root_node.attrib, root_node.text]
            result_list.append(temp_list)
            result_list.append(level)
            result_list.append(root_node.tag)
            result_list.append(root_node.attrib)
            result_list.append(root_node.text)
            #result_list = root_node.text
            return result_list
        else:
            try:
                if root_node.tag == 'map' or root_node.attrib['pageName'] == page_name:
                    children_node = root_node.getchildren()
                    if len(children_node) == 0:
                        pass
                    for child in children_node:
                        self.walk_data(child, level + 1, result_list, page_name, locator)
                    return result_list
            except:
                pass

    def run(self, page_name, locator):
        result = self.walk_data(self.root, self.level, self.result_list,page_name, locator)
        return result

b = BastPage('page.xml')
a = b.run('login', '账号')
c = b.run('login', '密码')
d = b.run('login1', 1 )
print a
# print a['type']
# print c['timeOut']
# print d['value']
