import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from visualize import BasicDiagram
class ParrallelCoorDiagram(BasicDiagram.BasicDiagram):
    def __init__(self):
        super().__init__()
        pass
    def show(self,dataSrc = './iris.csv',colors = ['blue', 'green', 'red', 'yellow'],title = 'parallel_coordinates'):
        data = self._BasicDiagram__getData(dataSrc)
        plt.figure('多维度-parallel_coordinates')
        plt.title(title)
        parallel_coordinates(data, 'Species', color=colors)
        plt.show()
# pcd = ParrallelCoorDiagram()
# pcd.show()