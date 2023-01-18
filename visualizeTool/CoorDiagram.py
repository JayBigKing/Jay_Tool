import os
import matplotlib.pyplot as plt
import numpy as np
import time


class CoorDiagram:
    def __init__(self, storePath="./"):
        self.setStorePath(storePath)

    def setStorePath(self, storePath: str):
        self.storePath = storePath
        if self.storePath[-1] != '/':
            self.storePath = self.storePath + "/"

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

    def drawManyScattersInOnePlane(self, scattersList, nameList=None, labelNames=None, titleName=None,
                                   ifDrawFig=True, ifSaveFig=False, saveFigName=None, showOriginPoint=True):
        if scattersList is None:
            return
        if labelNames is None:
            labelNames = ["x", "y"]

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        for index, scatter in enumerate(scattersList):
            scatter = np.array(scatter)
            x = scatter[:, 0]
            y = scatter[:, 1]

            ax.scatter(x, y)

            if nameList is None:
                ax.plot(x, y)
                if showOriginPoint is True:
                    ax.text(x[0], y[0], "orgin", ha='center', va='bottom')
            else:
                ax.plot(x, y, label=nameList[index])
                if showOriginPoint is True:
                    plt.text(x[0], y[0], r"%s orgin" % nameList[index], ha='center', va='bottom')
                ax.legend()

        if titleName is not None:
            ax.set_title(titleName)

        ax.set_xlabel(labelNames[0])
        ax.set_ylabel(labelNames[1])

        self.saveFigure(fig, ifSaveFig, saveFigName)
        if ifDrawFig is True:
            fig.show()
        # plt.clf()


    def figureFileNameGenerate(self):
        return time.strftime("figure%Y%m%d_%H%M%S.png", time.localtime())

    def saveFigure(self, fig, ifSaveFig, saveFigName):
        if ifSaveFig is True:
            if saveFigName is None:
                saveFigName = self.figureFileNameGenerate()
            if os.path.exists(self.storePath) is False:
                os.mkdir(self.storePath)

            fig.savefig("{:}{:}".format(self.storePath, saveFigName))