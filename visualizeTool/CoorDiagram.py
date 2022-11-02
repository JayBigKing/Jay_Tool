import os
import matplotlib.pyplot as plt
import numpy as np
import time


class CoorDiagram:
    def __init__(self, storePath = "./"):
        self.storePath = storePath
        print(os.getcwd())
    def setStorePath(self, storePath):
        self.storePath = storePath

    def drawOneLine(self, x, y):
        plt.plot(x, y)
        plt.show()

    def drawManyLines(self, xList, yList):
        if xList is None or yList is None:
            return
        for i in range(0, len(xList)):
            x = xList[i]
            y = yList[i]
            plt.figure()
            plt.plot(x, y)
        plt.show()

    def drawOneScatter(self, scatter):
        # plt.figure(figsize=(10, 10), dpi=100)
        scatter = np.array(scatter)
        x = scatter[:, 0]
        y = scatter[:, 1]
        plt.figure()
        plt.scatter(x, y)
        plt.show()

    def drawManyScatters(self, scattersList, colorList=None):
        if scattersList is None:
            return
        for scatter in scattersList:
            scatter = np.array(scatter)
            x = scatter[:, 0]
            y = scatter[:, 1]
            plt.figure()
            if colorList is not None:
                plt.scatter(x, y, c=colorList[i])
                plt.plot(x, y)
            else:
                plt.scatter(x, y)
                plt.plot(x, y)
        plt.show()

    def drawManyScattersInOnePlane(self, scattersList, nameList=None, labelNames=None, titleName=None, ifSaveFig=False,
                                   saveFigName=None):
        if scattersList is None:
            return
        if labelNames is None:
            labelNames = ["x", "y"]

        for index, scatter in enumerate(scattersList):
            scatter = np.array(scatter)
            x = scatter[:, 0]
            y = scatter[:, 1]

            plt.scatter(x, y)

            if nameList is None:
                plt.plot(x, y)
                plt.text(x[0], y[0], "orgin", ha='center', va='bottom')
            else:
                plt.plot(x, y, label = nameList[index])
                plt.text(x[0], y[0], r"%s orgin" % nameList[index], ha='center', va='bottom')
                plt.legend()

        if titleName is not None:
            plt.title(titleName)

        plt.xlabel(labelNames[0])
        plt.ylabel(labelNames[1])

        self.saveFigure(ifSaveFig, saveFigName)
        plt.show()

    def figureFileNameGenerate(self):
        return time.strftime("figure%Y%m%d_%H%M%S", time.localtime())

    def saveFigure(self, ifSaveFig, saveFigName):
        if ifSaveFig is True:
            if saveFigName is None:
                saveFigName = self.figureFileNameGenerate()
            if os.path.exists(self.storePath) is False:
                os.mkdir(self.storePath)

            plt.savefig("{:}{:}".format(self.storePath, saveFigName))

