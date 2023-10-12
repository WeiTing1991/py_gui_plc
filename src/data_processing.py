import xml.dom.minidom as xmldom


domtree = xmldom.parse(".\plc\plc_st_controller\GVL.xml")

group = domtree.documentElement

variables = group.getElementsByTagName("variable")

for variable in variables:
    if "Temperature" in variable.getAttribute("name"):
        print(variable.getAttribute("name"))

#<variable name="f_RED_Status_Temperature_Funnel_inlet">