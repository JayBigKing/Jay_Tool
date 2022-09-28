import matplotlib.pyplot as plt
import numpy as np

class CoorDiagram:
    def __init__(self):
        pass
    def drawOneLine(self,x,y):
        plt.plot(x,y)
        plt.show()
    def drawManyLines(self,xList,yList):
        if xList is None or yList is None:
            return
        for i in range(0,len(xList)):
            x = xList[i]
            y = yList[i]
            plt.figure()
            plt.plot(x, y)
        plt.show()

    def drawOneScatter(self,scatter):
        # plt.figure(figsize=(10, 10), dpi=100)
        scatter = np.array(scatter)
        x = scatter[:, 0]
        y = scatter[:, 1]
        plt.figure()
        plt.scatter(x,y)
        plt.show()

    def drwaManyScatters(self,scattersList,colorList = None):
        if scattersList is None:
            return
        for scatter in scattersList:
            scatter = np.array(scatter)
            x = scatter[:, 0]
            y = scatter[:, 1]
            plt.figure()
            if colorList is not None:
                plt.scatter(x, y,c=colorList[i])
                plt.plot(x,y)
            else:
                plt.scatter(x, y)
                plt.plot(x, y)
        plt.show()

    def drwaManyScattersInOnePlane(self,scattersList, nameList = None, theS = 30):
        if scattersList is None :
            return
        for scatter in scattersList:
            scatter = np.array(scatter)
            minVal = np.min(scatter[:, 0])
            maxVal = np.max(scatter[:, 0])

        theX = range(int(minVal - 1),int(maxVal + 1))
        for index, scatter in enumerate(scattersList):
            scatter = np.array(scatter)
            x = scatter[:, 0]
            y = scatter[:, 1]
            # plt.figure()

            plt.scatter(x, y)
            plt.plot(x, y)
            if nameList is None:
                plt.text(x[0],y[0],"orgin",ha='center',va='bottom')
            else:
                plt.text(x[0], y[0], r"%s orgin"%nameList[index], ha='center', va='bottom')
        plt.xticks(theX)
        plt.show()
