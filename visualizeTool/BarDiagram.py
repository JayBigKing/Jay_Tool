#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : DUAVTracking
@File    : BarDiagram.py
@Author  : jay.zhu
@Time    : 2023/10/17 11:05
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


# TODO: 把CoorDiagram类的保存文件的部分封装出来作为一个基类，现在BarDiagram类暂时继承CoorDiagram类，后续需要改成继承那个基类
class BarDiagram(CoorDiagram):
    def drawManyBarsInOnePlane(self, barsList, labelNames=None, titleName=None, ifDrawFig=True, ifSaveFig=False,
                               saveFigName=None, saveFigNameSuffix="pdf", figureArgs=None):
        if barsList is None:
            print("warning: no barsList input")
            return

        if figureArgs is not None:
            if figureArgs.get("figSize") is not None:
                fig = plt.figure(figsize=figureArgs["figSize"])
            else:
                fig = plt.figure()
        else:
            fig = plt.figure()

        ax = fig.add_subplot(1, 1, 1)

        barX = [bar[0] for bar in barsList]
        barY = [bar[1] for bar in barsList]

        ax.bar(barX, barY)

        if titleName is not None:
            ax.set_title(titleName)

        if labelNames is not None:
            ax.set_xlabel(labelNames[0])
            ax.set_ylabel(labelNames[1])

        self.saveFigure(fig, ifSaveFig, saveFigName, saveFigNameSuffix)
        if ifDrawFig is True:
            fig.show()
        plt.close(fig)
        # plt.clf()
