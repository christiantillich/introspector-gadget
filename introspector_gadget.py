import inspect
import pandas as pd
import re

def GoGoGadget(obj):
    """
    Pass in a module, class, or other object. GoGoGadget returns a human readable
    printout of the different subcomponents of the object.
    """
    def GetType(thing):
        try:
            type_string = re.search('^<\\w+', str(thing)).group(0)
            type_string = re.sub('<','',type_string)
            return(type_string.upper())
        except:
            return('Unknown')

    comp_list = inspect.getmembers(obj)
    names = [x[0] for x in comp_list]
    types = [GetType(x[1]) for x in comp_list]

    comp_DF = pd.DataFrame({'names': names, 'types': types})

    for type, df in comp_DF.groupby('types'):
        print("\t" + type)
        [print("\t\t" + x) for x in df['names']]
        print("\n")

