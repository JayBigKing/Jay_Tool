import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import andrews_curves
from visualize import BasicDiagram
class AndrewsDiagram(BasicDiagram.BasicDiagram):
    def __init__(self):
        super().__init__()
        pass
    def show(self,dataSrc = './iris.csv',colors = ['blue', 'green', 'orange','red'],title = 'myAndrews'):
        data = self._BasicDiagram__getData(dataSrc)
        plt.figure('多维度-andrews_curves')
        plt.title(title)
        andrews_curves(data, 'Species', color=colors)
        plt.show()

# ad = AndrewsDiagram()
# ad.show()
