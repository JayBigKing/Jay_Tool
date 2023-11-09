#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : DUAVTracking
@File    : ErrorShadowDiagram.py
@Author  : jay.zhu
@Time    : 2023/10/12 19:50
"""
import sys
import matplotlib

if sys.platform.startswith('linux'):
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
from Jay_Tool.visualizeTool.CoorDiagram import CoorDiagram


class ErrorShadowDiagram(CoorDiagram):
    class ErrShadowScatterStruct:
        def __init__(self, xList=None, maxYList=None, minYList=None, avgYList=None):
            self.xList = xList
            self.maxYList = maxYList
            self.minYList = minYList
            self.avgYList = avgYList

    def drawManyLines(self, xList, yList):
        pass

    def drawOneScatter(self, scatter):
        pass

    def drawManyScatters(self, scattersList, colorList=None):
        pass

    def drawManyScattersInOnePlane(self, scattersList, nameList=None, labelNames=None, titleName=None,
                                   ifDrawFig=True, ifSaveFig=False, saveFigName=None, showOriginPoint=True,
                                   saveFigNameSuffix="pdf", ifScatterPlotPoint=True, figureArgs=None):

        if scattersList is None:
            return
        if labelNames is None:
            labelNames = ["x(m)", "y(m)"]

        errShadowSctterList = []

        for oneScatterList in scattersList:
            maxYList = [np.max([scatter[index][1] for scatter in oneScatterList]) for index in
                        range(len(oneScatterList[0]))]
            minYList = [np.min([scatter[index][1] for scatter in oneScatterList]) for index in
                        range(len(oneScatterList[0]))]
            avgYList = [np.average([scatter[index][1] for scatter in oneScatterList]) for index in
                        range(len(oneScatterList[0]))]
            errShadowSctterList.append(
                self.ErrShadowScatterStruct(xList=[item[0] for item in oneScatterList[0]], maxYList=maxYList,
                                            minYList=minYList, avgYList=avgYList))

        if figureArgs is not None:
            if figureArgs.get("figSize") is not None:
                fig = plt.figure(figsize=figureArgs["figSize"])
            else:
                fig = plt.figure()
        else:
            fig = plt.figure()

        ax = fig.add_subplot(1, 1, 1)

        for index, scatter in enumerate(errShadowSctterList):

            x = scatter.xList
            y = scatter.avgYList

            if nameList is None:
                ax.plot(x, y)
                # if showOriginPoint is True:
                #     ax.text(x[0], y[0], "orgin", ha='center', va='bottom')
            else:
                ax.plot(x, y, label=nameList[index])

            fillBtwAlpha = 0.5
            if figureArgs is not None:
                if figureArgs.get("fillBtwAlpha") is not None:
                    fillBtwAlpha = figureArgs["figureArgs"]

            ax.fill_between(range(len(scatter.xList)),  scatter.maxYList, scatter.minYList, alpha=fillBtwAlpha)

            if nameList is not None:
                ax.legend()

        if titleName is not None:
            ax.set_title(titleName)

        ax.set_xlabel(labelNames[0])
        ax.set_ylabel(labelNames[1])

        self.saveFigure(fig, ifSaveFig, saveFigName, saveFigNameSuffix)
        if ifDrawFig is True:
            fig.show()
        plt.close(fig)
        # plt.clf()
