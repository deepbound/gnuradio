from xml.dom import minidom

def make_environment_init_c(dom) :
    tempstring = "";
    tempstring = tempstring + "/*this file is auto_generated by volk_register.py*/\n\n";
    tempstring = tempstring + "#include<volk/volk_environment_init.h>\n"
    for domarch in dom:
        arch = str(domarch.attributes["name"].value);
        incs = domarch.getElementsByTagName("include");
        for inc in incs:
            my_inc = str(inc.firstChild.data);
            tempstring = tempstring + "#ifdef LV_HAVE_" + arch.swapcase() + "\n";
            tempstring = tempstring + "#include<" + my_inc + ">\n";
            tempstring = tempstring + "#endif\n"
    tempstring = tempstring + '\n\n';
    tempstring = tempstring + "void volk_environment_init(){\n"
    
    for domarch in dom:
        arch = str(domarch.attributes["name"].value);
        envs = domarch.getElementsByTagName("environment");
        for env in envs:
            cmd = str(env.firstChild.data);
            tempstring = tempstring + "#ifdef LV_HAVE_" + arch.swapcase() + "\n";
            tempstring = tempstring + "        " + cmd + "\n";
            tempstring = tempstring + "#endif\n"     
    
    tempstring = tempstring + "}\n";
    return tempstring;
            


    
