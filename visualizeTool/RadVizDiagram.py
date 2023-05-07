import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import radviz
from visualize import BasicDiagram
class RadVizDiagram(BasicDiagram.BasicDiagram):
    def __init__(self):
        super().__init__()
        pass
    def show(self,dataSrc = './iris.csv',colors = ['blue', 'green', 'red', 'yellow'],title = 'myRadviz'):
        data = self._BasicDiagram__getData(dataSrc)
        plt.figure('多维度-radviz')
        plt.title(title)
        radviz(data, 'Species', color=colors)
        plt.show()

rvd = RadVizDiagram()
rvd.show()






