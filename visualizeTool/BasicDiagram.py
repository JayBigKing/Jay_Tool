import pandas as pd
class BasicDiagram:
    def __init__(self):
        pass
    def __getData(self,dataSrc = './iris.csv'):
        data =None
        if isinstance(dataSrc,str):
            data = pd.read_csv(dataSrc)
        else:
            data = dataSrc
        return data
