#####flask 接受请求处理模块,
import xml.etree.ElementTree as ET


###接受xml 处理
def xml_to_dict_wx_msg(web_date):
    return_dict = {}
    if len(web_date) == 0:
        return return_dict
    else:
        tree = ET.parse(web_date)
        for i in tree.getroot():
            return_dict[i.tag] = i.text
    return return_dict


print(xml_to_dict_wx_msg('text.xml'))
