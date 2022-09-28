import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from visualize import BasicDiagram
class MatrixDiagram((BasicDiagram.BasicDiagram)):
    def __init__(self):
        super().__init__()
        pass
    def show(self,dataSrc = './iris.csv',theHue  = 'Species'):
        data = self._BasicDiagram__getData(dataSrc)
        sns.pairplot(data, hue=theHue)
        plt.show()
#
# md = MatrixDiagram()
# md.show('./clusters_2021122115818.csv','type')