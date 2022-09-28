import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from visualize import BasicDiagram
class PearsonDiagram(BasicDiagram.BasicDiagram):
    def __init__(self):
        super().__init__()
        pass
    def show(self,dataSrc = './iris.csv'):
        data = self._BasicDiagram__getData(dataSrc)
        corr = data.corr()
        sns.heatmap(corr, annot=True)
        plt.show()

pd = PearsonDiagram()
pd.show()