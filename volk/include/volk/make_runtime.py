from xml.dom import minidom
from emit_omnilog import *
from volk_regexp import *



def make_runtime(funclist, arglist) :
    tempstring = "";
    tempstring = tempstring + '/*this file is auto generated by volk_register.py*/\n';

    tempstring = tempstring + '\n#ifndef INCLUDED_VOLK_RUNTIME';
    tempstring = tempstring + '\n#define INCLUDED_VOLK_RUNTIME';
    tempstring = tempstring + '\n\n#include<volk/volk_typedefs.h>\n';
    tempstring = tempstring + '#include<volk/volk_config_fixed.h>\n';
    tempstring = tempstring + '#include<volk/volk_complex.h>\n';
    tempstring = tempstring + emit_prolog();

    tempstring = tempstring + '\n';

    for i in range(len(funclist)):
        tempstring = tempstring + "extern void (*" + funclist[i] + ")(" + arglist[i] + ");\n"

    tempstring = tempstring + emit_epilog();
    tempstring = tempstring + "#endif /*INCLUDED_VOLK_RUNTIME*/\n";

    return tempstring;
    
