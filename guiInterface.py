import math

from PySide2 import QtGui, QtWidgets, QtCore, QtUiTools
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QToolButton, QFileDialog, \
    QGraphicsView, QDialogButtonBox, QListWidget
from PySide2.QtGui import QIcon, QPainter, QColor
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, Qt
from PySide2.QtGui import QIcon, QMovie
import PySide2
import sys
from PySide2.QtCharts import QtCharts
import re
from RL_brain import QLearningTable
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine
import copy
import glob
import os

import glob
import os

import MySQLdb
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import sqlalchemy
from RL_brain import QLearningTable
import time
import copy

import jsonlines
import json

import numpy as np
import pandas as pd


#
# import Start
# import Stop
# import upload
# import parameters
# import inputQueries

class Mortal():
    def __init__(self):
        # # main interface
        # self.mainWindow = QMainWindow()
        # self.mainWindow.resize(1000, 900)
        # self.mainWindow.move(300, 300)
        # self.mainWindow.setWindowTitle('Mapping Multi-Model to Relational Data with RL')
        #
        # # textbox
        # self.textEdit = QPlainTextEdit(self.mainWindow)
        # self.textEdit.setPlaceholderText("Please input JSON")
        # self.textEdit.resize(100, 100)
        # self.textEdit.move(10, 10)
        #
        # # button
        # self.buttonExecute = QPushButton('Execute', self.mainWindow)
        # self.buttonExecute.move(600, 700)
        # self.buttonExecute.clicked.connect(self.executeLearningButton)

        qfile_mapping = QFile('interface.ui')
        qfile_mapping.open(QFile.ReadOnly)
        qfile_mapping.close()

        # create a window instance from UI definition dynamically
        # note: all the widget objects in this window become the attributes of window instance
        # for example: self.ui.button, self.ui.textEdit

        self.ui = QUiLoader().load(qfile_mapping)
        # self.ui.toolButton_parameter.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # self.cleanJSONAddress = ''
        # self.cleanRDFAddress = ''
        # self.cleanRELATIONAddress = ''
        #
        # self.cleanedJSONAddress = ''
        # self.cleanedRDFAddress = ''
        # self.cleanedRELATIONAddress = ''
        #
        # self.loadJSONDirectory = ''
        # self.loadRDFDirectory = ''
        # self.loadRelationDirectory = ''

        #
        # self.learning_rateSetting = ''
        # self.reward_decaySetting = ''
        # self.e_greedySetting = ''
        # self.episodeSetting = ''

        self.constraintContents = ''
        #
        # self.arangoDBTime = ''
        # self.arangoDBSpace = ''
        # self.competitor = ''

        self.query1 = ''
        self.query2 = ''
        self.query3 = ''
        self.query4 = ''
        self.query5 = ''
        self.query6 = ''
        self.query7 = ''

        self.newSchema = ''

        # for display in main interface
        self.tableData = []


        self.outputExperimentStatisticsFileNo = 1

        self.noToAttributeDict = {}
        self.attributeToNoDict = {}
        self.secondRL = None
        self.randomTab = 0
        self.done = None
        self.removeArrayTable = 0

        # for test
        # clean data
        self.cleanJSONAddress = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/Person_dataset/person.json'
        self.cleanRDFAddress = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/Person_dataset/personGraph.csv'
        self.cleanRELATIONAddress = ''

        self.cleanedJSONAddress = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/JsonInitialTables'
        self.cleanedRDFAddress = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/RDFInitialTables'
        self.cleanedRELATIONAddress = ''

        # load cleaned data
        self.loadJSONDirectory = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/JsonInitialTables'
        self.loadRDFDirectory = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/RDFInitialTables'
        self.loadRelationDirectory = ''

        self.learning_rateSetting = 0.01
        self.reward_decaySetting = 0.9
        self.e_greedySetting = 0.1
        self.episodeSetting = 20
        self.competitor = 'ArangoDB'
        self.arangoDBTime = 14.965
        self.arangoDBSpace = 463.837
        self.constraintContes = '5 = 98'  # constraint

        # char line time
        self.ui.widget_time.setContentsMargins(0, 0, 0, 0)
        self.lay_time = QtWidgets.QVBoxLayout(self.ui.widget_time)
        self.lay_time.setContentsMargins(0, 0, 0, 0)

        self.chartviewTime = QtCharts.QChartView()
        self.chartviewTime.setContentsMargins(0, 0, 0, 0)
        self.lay_time.addWidget(self.chartviewTime)

        # #char line space
        self.ui.widget_space.setContentsMargins(0, 0, 0, 0)
        self.lay_space = QtWidgets.QVBoxLayout(self.ui.widget_space)
        self.lay_space.setContentsMargins(0, 0, 0, 0)

        self.chartviewSpace = QtCharts.QChartView()
        self.chartviewSpace.setContentsMargins(0, 0, 0, 0)
        self.lay_space.addWidget(self.chartviewSpace)




        self.ui.tableWidget_output.cellDoubleClicked.connect(self.openModifyDialog)

        ##################################################################################
        # toolButton_dataClean
        self.ui.toolButton_dataClean.clicked.connect(self.openDataCleanDialog)

        # toolButton_load
        self.ui.toolButton_load.clicked.connect(self.openLoadFilesDialog)

        # toolButton_parameter
        self.ui.toolButton_parameter.clicked.connect(self.openParameterSettingDialog)

        # toolButton_queries
        self.ui.toolButton_queries.clicked.connect(self.openQueriesDialog)

        # toolButton_constraints
        self.ui.toolButton_constraints.clicked.connect(self.openConstraintDialog)

        # toolButton_optimal
        # self.ui.toolButton_optimal.clicked.connect(self.openOptimalDialog)

        # toolButton_start
        self.ui.toolButton_start.clicked.connect(self.buttonStart)

        # toolButton_stop
        self.ui.toolButton_stop.clicked.connect(self.buttonStop)

    def buttonStop(self):

        sys.exit()

    ############################################################################
    #################### start running
    ############################################################################
    def buttonStart(self):

        ####################################################################################################
        #                                   load JSON files
        ###################################################################################################
        filenames_JSON = []
        directoryLocation_JSON = self.loadJSONDirectory
        os.chdir(directoryLocation_JSON)  # The specified directory
        for i in glob.glob("*.csv"):  # take all .csv files in the specified directory
            filenames_JSON.append(i[:-4])  # take file name, but does not include ".csv" suffix

        self.noToAttributeDict = {}
        self.attributeToNoDict = {}
        # currentSchema_Initial i.e., current schema  #{1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}
        currentSchema_Initial = {}

        # {1: objId  ns(tuple)， 2: objId original(tuple), ...}
        currentTableContent_Initial = {}

        ######## i starts from 1
        i = 1
        # iterate files
        for file_name_JSON in filenames_JSON:
            file = open(directoryLocation_JSON + '/' + file_name_JSON + '.csv', encoding='utf8')
            data_csv = pd.read_csv(file, encoding='utf8mb4')  # use pandas to read csv file
            # print(data_csv.head())

            if file_name_JSON == 'arrayTable':
                self.removeArrayTable = i

            self.noToAttributeDict[
                i] = file_name_JSON  # {1: 'ns', 2: 'original', 3: 'pageid', 4: 'arrayTable', 5: 'title', 51: 'subject', 52: 'occupation', 53: 'personFunction', 54: 'birthYear', 55: 'birthPlace', 56: 'birthDate', 57: 'title'}
            self.attributeToNoDict[file_name_JSON] = i
            currentSchema_Initial[i] = [
                i]  # {1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}
            currentTableContent_Initial[i] = data_csv
            i += 1

        ####################################################################################################
        #                                   load RDF files
        ###################################################################################################
        filenames_RDF = []
        directoryLocation_RDF = self.loadRDFDirectory
        # directoryLocation_RDF = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampleInitialTablesRDF'
        os.chdir(directoryLocation_RDF)  # The specified directory

        for i in glob.glob("*.csv"):  # take all .csv files in the specified directory
            filenames_RDF.append(i[:-4])  # take file name, but does not include ".csv" suffix

        # i starts from 51 for RDF files
        i = 51
        # iterate files
        for file_name_RDF in filenames_RDF:
            file = open(directoryLocation_RDF + '/' + file_name_RDF + '.csv', encoding='utf8')
            data_csv = pd.read_csv(file, encoding='utf8mb4')  # use pandas to read csv file
            # print(data_csv.head())

            if file_name_RDF == 'title':
                self.noToAttributeDict[i] = 'title_RDF'
                self.attributeToNoDict['title_RDF'] = i
            else:
                self.noToAttributeDict[i] = file_name_RDF
                self.attributeToNoDict[file_name_RDF] = i

            currentSchema_Initial[i] = [i]
            currentTableContent_Initial[i] = data_csv
            i += 1

        # initial state e.g., [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 51, 0, 52, 0, 53, 0, 54, 0, 55, 0, 56, 0, 57]
        initialState = []
        allAttr = list(self.noToAttributeDict.keys())  # [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
        # print(allAttr)
        for i in range(0, len(allAttr)):
            initialState.append(allAttr[i])
            initialState.append(0)

        initialState.pop()  # remove the last 0

        observation_ini = " ".join('%s' % i for i in initialState)

        print(">> initialState", initialState)

        ####################################################################################################
        #
        ###################################################################################################

        RL = QLearningTable(actions=allAttr)
        self.secondRL = QLearningTable(actions=allAttr)

        #self.randomTab = 0

        for episode in range(self.episodeSetting):

            # fresh

            # initial observation(state) string 1 0 2 0 3 0 4 0 5 0 51 0 52 0 53 0 54 0 55 0 56 0 57
            observation = str(observation_ini)

            # action space [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
            action_space = copy.deepcopy(allAttr)

            # currentSchema_Initial
            currentSchema = copy.deepcopy(currentSchema_Initial)

            print('>>  currentSchema copy:')
            print(currentSchema)

            # currentTableContent_Initia
            currentTableContent = copy.deepcopy(currentTableContent_Initial)

            # print('>>  currentTableContent copy:')
            # print(currentTableContent.keys())

            # we do not consider JSON array to join
            action_space.remove(self.removeArrayTable)

            # record the previous query timee
            previousQueryTime = 0

            while True:

                # RL choose action based on observation
                # In our situation, action space is Real-time changing
                # After choosing one action (one attribute), this action will be removed from action space.
                action, action_space, self.done = RL.choose_action(observation, action_space)

                # # RL take action and current state (observation) to get next observation and reward
                observation_, reward, currentSchema, currentTableContent, currentQueryTime = self.step(observation, action,
                                                                                                  currentSchema,
                                                                                                  currentTableContent,
                                                                                                  previousQueryTime)

                # # RL learn from this transition
                # maxExpectedValue = RL.learn(observation, action, reward, observation_, self.done)
                maxExpectedValue = RL.learn(observation, action, reward, observation_)

                # action is equal to index, randomTab is equal to action in second Q-table
                ## second table
                ##      1  2  3  4  5  6 ...
                ##  1
                ##  2
                ##  3
                ##  :
                ####
                # here using maxExpectedValue in Q-table 1 want to show
                # considering there are two situations: table 1 2 and table 1 4
                # when (action: 3), we choose randomTable: 1,
                # then generate table 1 2, 3 or  1 3 4
                # the second Q-table want to indicate that (In either case, it is reflect the reward for choosing random table 1 under the action 3)
                self.secondRL.secondTableLearn(action, self.randomTab, reward, maxExpectedValue)

                #
                # # swap observation
                observation = observation_

                if reward != 0:
                    previousQueryTime = currentQueryTime
                # currentTableContent = currentTableContent_

                # break while loop when end of this episode
                if self.done:
                    break

            # end of game
            print('>> finish one episode')
            #self.outputExperimentStatisticsFileNo += 1


            #################################################
            #update graph
            ################################################
            newTableTuple = []
            directoryLocation_TXT = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/Results/totalQueryTimeArray' + str(self.outputExperimentStatisticsFileNo) + '.txt'
            file = open(directoryLocation_TXT, encoding='utf8')
            lines = file.readlines()
            localOptimal = [None] * 8
            if (len(lines) > 8):
                localOptimal[0] = lines[0]
                localOptimal[1] = lines[1]
                localOptimal[2] = lines[2]
                localOptimal[3] = lines[3]
                localOptimal[4] = lines[4]
                localOptimal[5] = lines[5]
                localOptimal[6] = lines[6]
                localOptimal[7] = lines[7]

            count = 0
            while (count < len(lines)):
                tempTotalTime = lines[count]
                # print(count)
                if float(tempTotalTime) < float(localOptimal[0]):
                    j = 0
                    while (j < 8):
                        localOptimal[j] = lines[count + j]
                        j += 1
                    count += 8
                else:
                    count += 8
            file.close()

            newTableTuple.append(localOptimal[6])   #schemaString
            newTableTuple.append(localOptimal[0])   #time
            newTableTuple.append(localOptimal[7])   #space

            self.tableData.append(newTableTuple)

            ##################################################################################
            # tablewidge
            rowcnt = len(self.tableData)
            colcnt = len(self.tableData[0])


            self.ui.tableWidget_output.setRowCount(rowcnt)
            self.ui.tableWidget_output.setColumnCount(colcnt)

            for i in range(rowcnt):
                for j in range(colcnt):
                    item = QtWidgets.QTableWidgetItem(str(self.tableData[i][j]))
                    self.ui.tableWidget_output.setItem(i, j, item)



            #################################################################################
            # line chart time
            # Create Chart and set General Chart setting

            series_time = QtCharts.QLineSeries()
            series_time2 = QtCharts.QLineSeries()
            series_space = QtCharts.QLineSeries()
            series_space2 = QtCharts.QLineSeries()

            for i in range(rowcnt):
                # series_time.append(i + 1, float(self.tableData[i][1]))
                series_time << QtCore.QPointF(i + 1, float(self.tableData[i][1]))
                MysqlSpaceMB = float(self.tableData[i][2][9:-3]) / (math.pow(2, 20))
                series_space.append(i + 1, MysqlSpaceMB)

                series_time2.append(i + 1, self.arangoDBTime)
                series_space2.append(i + 1, self.arangoDBSpace)

            series_time.setName('SQL')
            series_time2.setName(self.competitor)

            chart_time = QtCharts.QChart()
            chart_time.addSeries(series_time)
            chart_time.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            # chart_time.legend().hide()

            # X Axis Settings
            axisX = QtCharts.QValueAxis()
            axisX.setTitleText('Episode')
            chart_time.addAxis(axisX, QtCore.Qt.AlignBottom)
            # axisX.setRange(0,20)
            # axisX.setTickCount(10)  # how many of grid
            # axisX.setMinorTickCount(2)      #setting min scalee of each grid
            # axisX.setLabelFormat("%u")        # setting format of scale
            series_time.attachAxis(axisX)

            # Y Axis Settings
            axisY = QtCharts.QValueAxis()
            axisY.setTitleText('Time/s')
            chart_time.addAxis(axisY, QtCore.Qt.AlignLeft)
            axisY.setMin(0)
            # axisY.setRange(0,20)
            series_time.attachAxis(axisY)
            # chartviewTime.setChart(chart_time)

            chart_time.addSeries(series_time2)
            series_time2.setColor(QColor(255, 0, 0))
            series_time2.attachAxis(axisX)
            series_time2.attachAxis(axisY)

            self.chartviewTime.setChart(chart_time)

            ##################################################################################
            # line chart space
            # Create Chart and set General Chart setting

            series_space.setName('SQL')
            series_space2.setName(self.competitor)

            chart_space = QtCharts.QChart()
            chart_space.addSeries(series_space)
            chart_space.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            # chart_space.legend().hide()
            # chart_space.setTitle("Changes in Space")

            # X Axis Settings
            axisX_Space = QtCharts.QValueAxis()
            axisX_Space.setTitleText('Episode')
            chart_space.addAxis(axisX_Space, QtCore.Qt.AlignBottom)
            series_space.attachAxis(axisX_Space)

            # Y Axis Settings
            axisY_Space = QtCharts.QValueAxis()
            axisY_Space.setTitleText('Memory/MB')
            axisY_Space.setRange(390, 480)
            chart_space.addAxis(axisY_Space, QtCore.Qt.AlignLeft)
            series_space.attachAxis(axisY_Space)


            chart_space.addSeries(series_space2)
            series_space2.setColor(QColor(255, 0, 0))
            series_space2.attachAxis(axisX_Space)
            series_space2.attachAxis(axisY_Space)

            self.chartviewSpace.setChart(chart_space)



            self.lay_time.removeWidget(self.chartviewTime)
            self.outputExperimentStatisticsFileNo += 1

    ############################################################################
    #################### modify schema dialog
    ############################################################################
    def openModifyDialog(self, row, column):
        if column == 0:
            item = self.ui.tableWidget_output.item(row, column)
            # print(item.text())

            qfile_Dialog = QFile('modifySchemaDiag.ui')
            qfile_Dialog.open(QFile.ReadOnly)
            qfile_Dialog.close()
            self.modifyui = QUiLoader().load(qfile_Dialog)
            self.modifyui.show()

            self.modifyui.plainTextEdit_currentSchema.setPlainText('{}'.format(item.text()))

            file = open('/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/noToAttributeDict.txt',
                        'r')
            row = 0
            for line in file.readlines():
                line = line.strip()
                lineArray = line.split(' ')
                tempString = lineArray[0] + ': ' + lineArray[1]
                self.modifyui.listWidget_notoAttributes.insertItem(row, tempString)
                row += 1
            file.close()

            # toolButton_Execute
            self.modifyui.toolButton_Execute.clicked.connect(self.executeButton)

            #

    def executeButton(self):
        self.newSchema = self.modifyui.plainTextEdit_newSchema.toPlainText()

        noToAttributeDict = {}
        attributeToNoDict = {}
        currentSchema = {}

        #######################
        ####################### JSON
        filenames_JSON = []
        directoryLocation_JSON = self.loadJSONDirectory
        os.chdir(directoryLocation_JSON)  # The specified directory
        for i in glob.glob("*.csv"):  # take all .csv files in the specified directory
            filenames_JSON.append(i[:-4])  # take file name, but does not include ".csv" suffix

        ######## i starts from 1
        i = 1
        # iterate files
        for file_name_JSON in filenames_JSON:
            noToAttributeDict[
                i] = file_name_JSON  # {1: 'ns', 2: 'original', 3: 'pageid', 4: 'arrayTable', 5: 'title', 51: 'subject', 52: 'occupation', 53: 'personFunction', 54: 'birthYear', 55: 'birthPlace', 56: 'birthDate', 57: 'title'}
            attributeToNoDict[file_name_JSON] = i
            i += 1

        #######################
        ####################### RDF
        filenames_RDF = []
        directoryLocation_RDF = self.loadRDFDirectory
        os.chdir(directoryLocation_RDF)  # The specified directory
        for i in glob.glob("*.csv"):  # take all .csv files in the specified directory
            filenames_RDF.append(i[:-4])  # take file name, but does not include ".csv" suffix

        # i starts from 51 for RDF files
        i = 51
        # iterate files
        for file_name_RDF in filenames_RDF:
            if file_name_RDF == 'title':
                noToAttributeDict[i] = 'title_RDF'
                attributeToNoDict['title_RDF'] = i
            else:
                noToAttributeDict[i] = file_name_RDF
                attributeToNoDict[file_name_RDF] = i
            i += 1

        # currentSchema
        schamaString = self.newSchema
        # schamaString ='1 0 2 0 3 0 4 0 5 0 54 0 56 0 58 0 59 0 53 62 0 63 0 55 61 67 70 0 68 76 0 69 0 72 0 74 86 0 51 71 75 79 0 77 0 81 0 82 0 66 78 83 85 0 84 0 87 0 88 0 89 0 65 73 91 0 52 64 90 92 0 57 93 0 95 0 96 0 60 97 0 80 94 98'

        schemaArray = re.split(r'\s[0]\s', schamaString)
        # ['1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 54 ', ' 56 ', ' 58 ', ' 59 ', ' 53 62 ', ' 63 ', ' 55 61 67 7', ' ', ' 68 76 ', ' 69 ', ' 72 ', ' 74 86 ', ' 51 71 75 79 ', ' 77 ', ' 81 ', ' 82 ', ' 66 78 83 85 ', ' 84 ', ' 87 ', ' 88 ', ' 89 ', ' 65 73 91 ', ' 52 64 9', ' 92 ', ' 57 93 ', ' 95 ', ' 96 ', ' 6', ' 97 ', ' 8', ' 94 98']

        i = 0
        while (i < len(schemaArray)):
            schemaArray[i] = schemaArray[i].strip()
            i += 1

        i = 0
        while (i < len(schemaArray)):
            actions = schemaArray[i].split(' ')
            l = []
            for a in actions:
                l.append(int(a))
            currentSchema[l[0]] = l
            i += 1

        # ###################################################################################################
        # #                                   load relational schema
        # ###################################################################################################
        #
        # # fileSchema = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/experimental result in paper/OptimalTime12.txt'
        # # fileRead = open(fileSchema, encoding='utf8')
        # # lines = fileRead.readlines()
        # # schamaString = lines[6]
        #
        # schamaString = self.newSchema
        # # schamaString ='1 0 2 0 3 0 4 0 5 0 54 0 56 0 58 0 59 0 53 62 0 63 0 55 61 67 70 0 68 76 0 69 0 72 0 74 86 0 51 71 75 79 0 77 0 81 0 82 0 66 78 83 85 0 84 0 87 0 88 0 89 0 65 73 91 0 52 64 90 92 0 57 93 0 95 0 96 0 60 97 0 80 94 98'
        #
        # schemaArray = re.split(r'\s[0]\s', schamaString)
        # # ['1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 54 ', ' 56 ', ' 58 ', ' 59 ', ' 53 62 ', ' 63 ', ' 55 61 67 7', ' ', ' 68 76 ', ' 69 ', ' 72 ', ' 74 86 ', ' 51 71 75 79 ', ' 77 ', ' 81 ', ' 82 ', ' 66 78 83 85 ', ' 84 ', ' 87 ', ' 88 ', ' 89 ', ' 65 73 91 ', ' 52 64 9', ' 92 ', ' 57 93 ', ' 95 ', ' 96 ', ' 6', ' 97 ', ' 8', ' 94 98']
        # # print(schemaArray)
        #
        # i = 0
        # while (i < len(schemaArray)):
        #     schemaArray[i] = schemaArray[i].strip()
        #     i += 1
        #
        # # ['1', '2', '3', '4', '5', '54', '56', '58', '59', '53 62', '63', '55 61 67 7', '', '68 76', '69', '72', '74 86', '51 71 75 79', '77', '81', '82', '66 78 83 85', '84', '87', '88', '89', '65 73 91', '52 64 9', '92', '57 93', '95', '96', '6', '97', '8', '94 98']
        # # print(schemaArray)
        #
        # # i = 0
        # # while (i < len(schemaArray)):
        # #     actions = schemaArray[i].split(' ')
        # #     if len(actions) > 1:
        # #         leftIndex = 0
        # #         rightIndex = 1
        # #         while (rightIndex < len(actions)):
        # #
        # #             if int(actions[leftIndex]) < 50 and int(actions[rightIndex]) < 50:
        # #                 left = currentTableContent[int(actions[leftIndex])]
        # #                 right = currentTableContent[int(actions[rightIndex])]
        # #                 currentTableContent[int(actions[leftIndex])] = pd.merge(left, right, on='objId', how='outer')
        # #                 # print(">>  currentTableContent", currentTableContent[randomTab])
        # #
        # #                 # update current relational schema
        # #                 currentSchema[int(actions[leftIndex])].extend(currentSchema[int(actions[rightIndex])])
        # #                 currentSchema[int(actions[leftIndex])].sort()
        # #                 del currentSchema[int(actions[rightIndex])]
        # #                 del currentTableContent[int(actions[rightIndex])]
        # #                 print(">> currentSchema: ", currentSchema)
        # #
        # #             if int(actions[leftIndex]) > 50 and int(actions[rightIndex]) > 50:
        # #                 left = currentTableContent[int(actions[leftIndex])]
        # #                 right = currentTableContent[int(actions[rightIndex])]
        # #                 currentTableContent[int(actions[leftIndex])] = pd.merge(left, right, on='key', how='outer')
        # #                 # print(">>  currentTableContent", currentTableContent[randomTab])
        # #
        # #                 # update current relational schema
        # #                 currentSchema[int(actions[leftIndex])].extend(currentSchema[int(actions[rightIndex])])
        # #                 currentSchema[int(actions[leftIndex])].sort()
        # #                 del currentSchema[int(actions[rightIndex])]
        # #                 del currentTableContent[int(actions[rightIndex])]
        # #                 print(">> currentSchema: ", currentSchema)
        # #
        # #             if (int(actions[leftIndex]) < 50 and int(actions[rightIndex]) > 50) or (
        # #                     int(actions[leftIndex]) > 50 and int(actions[rightIndex]) < 50):
        # #                 left = currentTableContent[int(actions[leftIndex])]
        # #                 right = currentTableContent[int(actions[rightIndex])]
        # #                 currentTableContent[int(actions[leftIndex])] = pd.merge(left, right, on='title', how='outer')
        # #                 # print(">>  currentTableContent", currentTableContent[randomTab])
        # #
        # #                 # update current relational schema
        # #                 currentSchema[int(actions[leftIndex])].extend(currentSchema[int(actions[rightIndex])])
        # #                 currentSchema[int(actions[leftIndex])].sort()
        # #                 del currentSchema[int(actions[rightIndex])]
        # #                 del currentTableContent[int(actions[rightIndex])]
        # #                 print(">> currentSchema: ", currentSchema)
        # #
        # #             rightIndex += 1
        # #     # print(a)
        # #     i += 1

        # creat connecting
        conn = MySQLdb.connect(
            host='localhost',  # your MySQL service address
            port=3306,  # port
            user='root',  # visiting database service's user name and password
            passwd='1',
            db='QLearning',  # database name
            charset='utf8mb4'  # for chinese
        )
        cur = conn.cursor()
        # cur.execute("drop database if exists QLearning")
        # cur.execute("Create database QLearning")
        # cur.execute("use QLearning")
        #
        # engine = create_engine(
        #     "mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', '1', 'localhost', 'QLearning', 'utf8mb4'))
        #
        # for key, value in currentTableContent.items():
        #     value.to_sql(name=noToAttributeDict[key], con=engine, if_exists='replace', index=False)

        # get execute time

        ##################################################################
        #######################################     query1    #######################################
        pageidNo_q1 = attributeToNoDict['pageid']
        # print(pageidNo_q1)
        wherePageid_q1 = 0
        for key, value in currentSchema.items():
            if pageidNo_q1 in value:
                wherePageid_q1 = key
                # print(wherePageid_q1)
                break

        # print(wherePageid_q1)

        pagidTable_q1 = noToAttributeDict[wherePageid_q1]

        # sql1 = "select pageid from arrayTable, %s where arrayTable.key = 'normalized' and arrayTable.index = 0 and arrayTable.valStr = 'Doris_Brougham' and %s.objId = arrayTable.objId" % (
        #     pagidTable_q1, pagidTable_q1)  # Doris_Brougham     Henry_Standing_Bear

        sql1 = self.query1[7:]

        middleTime = []
        recordEachQueryTime = []
        for t_i in range(3):
            time_start1 = time.time()
            cur.execute(sql1)
            time_end1 = time.time()
            query_time1 = time_end1 - time_start1
            middleTime.append(query_time1)

        middleTime.sort()
        totalQueryTime = - middleTime[1]
        recordEachQueryTime.append(middleTime[1])
        middleTime.clear()

        #######################################     query2    #######################################

        subjectNo_q2 = attributeToNoDict['subject']
        whereSubject_q2 = 0
        for key, value in currentSchema.items():
            if subjectNo_q2 in value:
                whereSubject_q2 = key
                break

        subjectTable_q2 = noToAttributeDict[whereSubject_q2]

        # sql2 = "select subject from %s where %s.key = 'Tor_Ahlsand'" % (subjectTable_q2, subjectTable_q2)
        sql2 = self.query2[7:]

        for t_i in range(3):
            time_start2 = time.time()
            cur.execute(sql2)
            time_end2 = time.time()
            query_time2 = time_end2 - time_start2
            middleTime.append(query_time2)

        middleTime.sort()
        totalQueryTime -= middleTime[1]
        recordEachQueryTime.append(middleTime[1])
        middleTime.clear()

        #######################################     query3    #######################################
        # we can not test in example

        birthDateNo_q3 = attributeToNoDict['birthDate']
        activeYearsStartYearNo_q3 = attributeToNoDict['activeYearsStartYear']
        activeYearsEndYearNo_q3 = attributeToNoDict['activeYearsEndYear']

        whereBirthDateNo_q3 = 0
        whereActiveYearsStartYearNo_q3 = 0
        whereActiveYearsEndYearNo_q3 = 0

        for key, value in currentSchema.items():
            if birthDateNo_q3 in value:
                whereBirthDateNo_q3 = key
                break

        for key, value in currentSchema.items():
            if activeYearsStartYearNo_q3 in value:
                whereActiveYearsStartYearNo_q3 = key
                break

        for key, value in currentSchema.items():
            if activeYearsEndYearNo_q3 in value:
                whereActiveYearsEndYearNo_q3 = key
                break

        birthDateTable_q3 = noToAttributeDict[whereBirthDateNo_q3]
        activeYearsStartYearTable_q3 = noToAttributeDict[whereActiveYearsStartYearNo_q3]
        activeYearsEndYearTable_q3 = noToAttributeDict[whereActiveYearsEndYearNo_q3]

        # queryKey = 'Heath_Ledger'
        if (whereBirthDateNo_q3 == whereActiveYearsStartYearNo_q3) or (
                whereBirthDateNo_q3 == whereActiveYearsEndYearNo_q3):  # a==b or a==c
            if whereActiveYearsStartYearNo_q3 == whereActiveYearsEndYearNo_q3:  # b==c e.g., (1,1,1)
                # sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s where %s.key = 'Heath_Ledger'" % (
                #     birthDateTable_q3, birthDateTable_q3)
                sql3 = self.query3[0]
            else:
                if (whereBirthDateNo_q3 == whereActiveYearsStartYearNo_q3) and (
                        whereActiveYearsStartYearNo_q3 != whereActiveYearsEndYearNo_q3):  # a == b and b!=c  (1,1,2)
                    # sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (
                    #     birthDateTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3, birthDateTable_q3,
                    #     activeYearsEndYearTable_q3)
                    sql3 = self.query3[1]
                else:  # a==c and b!=c (1,2,1)
                    # sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (
                    #     birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, birthDateTable_q3,
                    #     activeYearsStartYearTable_q3)
                    sql3 = self.query3[1]
        else:  # a!=b and a!=c
            if whereActiveYearsStartYearNo_q3 != whereActiveYearsEndYearNo_q3:  # a!=b, a!=c, b!=c (1,2,3)
                # sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key and %s.key = %s.key" % (
                #     birthDateTable_q3, activeYearsStartYearTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3,
                #     birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, activeYearsEndYearTable_q3)
                sql3 = self.query3[2]
            if whereActiveYearsStartYearNo_q3 == whereActiveYearsEndYearNo_q3:  ##a!=b and a!=c and b==c (2,1,1)
                # sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (
                #     birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, birthDateTable_q3,
                #     activeYearsStartYearTable_q3)
                sql3 = self.query3[2]

        for t_i in range(3):
            time_start3 = time.time()
            cur.execute(sql3)
            time_end3 = time.time()
            query_time3 = time_end3 - time_start3
            middleTime.append(query_time3)

        middleTime.sort()
        totalQueryTime -= middleTime[1]
        recordEachQueryTime.append(middleTime[1])
        middleTime.clear()
        #######################################     query4    #######################################

        original_q4 = attributeToNoDict['original']
        title_q4 = attributeToNoDict['title']
        pageid_q4 = attributeToNoDict['pageid']

        whereOriginal_q4 = 0
        whereTitle_q4 = 0
        wherePageid_q4 = 0

        for key, value in currentSchema.items():
            if original_q4 in value:
                whereOriginal_q4 = key
                break

        for key, value in currentSchema.items():
            if title_q4 in value:
                whereTitle_q4 = key
                break

        for key, value in currentSchema.items():
            if pageid_q4 in value:
                wherePageid_q4 = key
                break

        originalTable_q4 = noToAttributeDict[whereOriginal_q4]
        titleTable_q4 = noToAttributeDict[whereTitle_q4]
        pageidTable_q4 = noToAttributeDict[wherePageid_q4]
        queryKey_4 = 8484745
        # queryKey_4 = 43757531 #example

        if (whereOriginal_q4 == whereTitle_q4) or (whereOriginal_q4 == wherePageid_q4):  # a==b or a==c
            if whereTitle_q4 == wherePageid_q4:  # b==c e.g., (1,1,1)
                # sql4 = "select original, title from %s where %s.pageid = %s" % (
                #     originalTable_q4, originalTable_q4, queryKey_4)
                sql4 = self.query4[0]
            else:
                if (whereOriginal_q4 == whereTitle_q4) and (
                        whereTitle_q4 != wherePageid_q4):  # a == b and b!=c  (1,1,2)
                    # sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (
                    #     originalTable_q4, pageidTable_q4, pageidTable_q4, queryKey_4, originalTable_q4, pageidTable_q4)
                    sql4 = self.query4[1]
                else:  # a==c and b!=c (1,2,1)
                    # sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (
                    #     originalTable_q4, titleTable_q4, originalTable_q4, queryKey_4, originalTable_q4, titleTable_q4)
                    sql4 = self.query4[1]
        else:  # a!=b and a!=c
            if whereTitle_q4 != wherePageid_q4:  # a!=b, a!=c, b!=c (1,2,3)
                # sql4 = "select original, title from %s, %s, %s where %s.pageid = %s and %s.objId = %s.objId and %s.objId = %s.objId" % (
                #     originalTable_q4, titleTable_q4, pageidTable_q4, pageidTable_q4, queryKey_4, originalTable_q4,
                #     titleTable_q4, originalTable_q4, pageidTable_q4)
                sql4 = self.query4[2]
            if whereTitle_q4 == wherePageid_q4:  ##a!=b and a!=c and b==c (2,1,1)
                # sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (
                #     originalTable_q4, titleTable_q4, titleTable_q4, queryKey_4, originalTable_q4, titleTable_q4)
                sql4 = self.query4[2]

        for t_i in range(3):
            time_start4 = time.time()
            cur.execute(sql4)
            time_end4 = time.time()
            query_time4 = time_end4 - time_start4
            middleTime.append(query_time4)

        middleTime.sort()
        totalQueryTime -= middleTime[1]
        recordEachQueryTime.append(middleTime[1])
        middleTime.clear()

        #######################################     query5    #######################################
        birthYearNo_q5 = attributeToNoDict['birthYear']
        nsNo_q5 = attributeToNoDict['ns']

        whereBirthYear_q5 = 0
        whereNs_q5 = 0

        for key, value in currentSchema.items():
            if birthYearNo_q5 in value:
                whereBirthYear_q5 = key
                break

        for key, value in currentSchema.items():
            if nsNo_q5 in value:
                whereNs_q5 = key
                break

        BirthYearTable_q5 = noToAttributeDict[whereBirthYear_q5]
        nsTable_q5 = noToAttributeDict[whereNs_q5]

        # sql5 = "select %s.key, birthYear, ns from arrayTable, %s, %s where arrayTable.key = 'normalized' and arrayTable.index = 0 and arrayTable.valStr = 'Sadako_Sasaki' and %s.objId = arrayTable.objId and %s.key = arrayTable.valStr" % (
        #     BirthYearTable_q5, BirthYearTable_q5, nsTable_q5, nsTable_q5,
        #     BirthYearTable_q5)  # Sadako_Sasaki     Henry_Standing_Bear（example）
        sql5 = self.query5[7:]

        for t_i in range(3):
            time_start5 = time.time()
            cur.execute(sql5)
            time_end5 = time.time()
            query_time5 = time_end5 - time_start5
            middleTime.append(query_time5)

        middleTime.sort()
        totalQueryTime -= middleTime[1]
        recordEachQueryTime.append(middleTime[1])
        middleTime.clear()

        self.modifyui.plainTextEdit_TimeConsumption.setPlainText('{}'.format(str(-totalQueryTime)))

        ##################################################################
        # get space consumption
        #############################################################################
        sql_space = "select sum(DATA_LENGTH)+sum(INDEX_LENGTH) from information_schema.tables where table_schema='QLearning';"
        cur.execute(sql_space)
        results = str(cur.fetchone())  # get the return result
        self.modifyui.plainTextEdit_SpaceConsumption.setPlainText('{}'.format(results[1:-2]))

        # results = cur.fetchall()  # get the return result
        # displayResults = ""
        # for rel in results:
        #     displayResults = displayResults + str(rel) + '\n'
        # self.modifyui.plainTextEdit_SpaceConsumption.setPlainText('{}'.format(displayResults))

        # conn.close() close database connection
        conn.close()

    #
    # # Optimal Schema ----  Button
    # def openOptimalDialog(self):
    #     qfile_Dialog = QFile('optimalSchemaDiag.ui')
    #     qfile_Dialog.open(QFile.ReadOnly)
    #     qfile_Dialog.close()
    #     self.optimalui = QUiLoader().load(qfile_Dialog)
    #     self.optimalui.show()

    ####################################################################
    ################## Input Queries ----  Button
    ####################################################################
    def openQueriesDialog(self):
        qfile_Dialog = QFile('inputQueriesDiag.ui')
        qfile_Dialog.open(QFile.ReadOnly)
        qfile_Dialog.close()
        self.queryui = QUiLoader().load(qfile_Dialog)

        # # initial
        # self.queryui.plainTextEdit_query1.setPlainText('{}'.format(self.query1))
        # self.queryui.plainTextEdit_query2.setPlainText('{}'.format(self.query2))
        # self.queryui.plainTextEdit_query3.setPlainText('{}'.format(self.query3))
        # self.queryui.plainTextEdit_query4.setPlainText('{}'.format(self.query4))
        # self.queryui.plainTextEdit_query5.setPlainText('{}'.format(self.query5))
        # self.queryui.plainTextEdit_query6.setPlainText('{}'.format(self.query6))
        # self.queryui.plainTextEdit_query7.setPlainText('{}'.format(self.query7))

        file = open('/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/noToAttributeDict.txt', 'r')
        row = 0
        for line in file.readlines():
            line = line.strip()
            lineArray = line.split(' ')
            tempString = lineArray[0] + ': ' + lineArray[1]
            self.queryui.listWidget_notoAttributes.insertItem(row, tempString)
            row += 1
        file.close()
        self.queryui.show()
        self.queryui.accepted.connect(self.acceptInputQueries)

    def acceptInputQueries(self):
        self.query1 = self.queryui.plainTextEdit_query1.toPlainText()
        self.query2 = self.queryui.plainTextEdit_query2.toPlainText()
        query3_tmp = self.queryui.plainTextEdit_query3.toPlainText()
        query4_tmp = self.queryui.plainTextEdit_query4.toPlainText()
        self.query5 = self.queryui.plainTextEdit_query5.toPlainText()
        self.query6 = self.queryui.plainTextEdit_query6.toPlainText()
        self.query7 = self.queryui.plainTextEdit_query7.toPlainText()

        self.query3 = query3_tmp.split("\n")
        i = 0
        for q in self.query3:
            self.query3[i] = q[7:]
            print(self.query3[i])


        self.query4 = query4_tmp.split("\n")
        i = 0
        for q in self.query4:
            self.query4[i] = q[7:]
            print(self.query4[i])


    ########################################################
    ################# Constraint Pool ----  Button
    ########################################################
    def openConstraintDialog(self):
        qfile_Dialog = QFile('constraintPoolDiag.ui')
        qfile_Dialog.open(QFile.ReadOnly)
        qfile_Dialog.close()
        self.constraintui = QUiLoader().load(qfile_Dialog)

        # initial
        self.constraintui.plainTextEdit_constraints.setPlainText('{}'.format(self.constraintContes))

        # displayAttriuteMapping = ''
        file = open('/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/noToAttributeDict.txt', 'r')
        row = 0
        for line in file.readlines():
            line = line.strip()
            lineArray = line.split(' ')
            tempString = lineArray[0] + ': ' + lineArray[1]
            self.constraintui.listWidget_notoAttribute.insertItem(row, tempString)
            row += 1
        file.close()

        self.constraintui.show()
        self.constraintui.accepted.connect(self.acceptConstraints)

    def acceptConstraints(self):
        self.constraintContents = self.constraintui.plainTextEdit_constraints.toPlainText()

    ################################################
    ######### Parameter setting ----  Button
    ################################################
    def openParameterSettingDialog(self):
        qfile_Dialog = QFile('parameterSettingDiag.ui')
        qfile_Dialog.open(QFile.ReadOnly)
        qfile_Dialog.close()
        self.parameterui = QUiLoader().load(qfile_Dialog)

        # initial

        self.parameterui.lineEdit_LearningRate.setText('{}'.format(self.learning_rateSetting))
        self.parameterui.lineEdit_RewardDecay.setText('{}'.format(self.reward_decaySetting))
        self.parameterui.lineEdit_Greedy.setText('{}'.format(self.e_greedySetting))
        self.parameterui.lineEdit_Episode.setText('{}'.format(self.episodeSetting))
        self.parameterui.lineEdit_Competitor.setText('{}'.format(self.competitor))
        self.parameterui.lineEdit_ArangoDBTime.setText('{}'.format(self.arangoDBTime))
        self.parameterui.lineEdit_ArangoDBSpace.setText('{}'.format(self.arangoDBSpace))

        self.parameterui.show()

        self.parameterui.lineEdit_LearningRate.textChanged.connect(self.onChangedLearningRate)
        self.parameterui.lineEdit_RewardDecay.textChanged.connect(self.onChangedRewardDecay)
        self.parameterui.lineEdit_Greedy.textChanged.connect(self.onChangedGreedy)
        self.parameterui.lineEdit_Episode.textChanged.connect(self.onChangedEpisode)
        self.parameterui.lineEdit_Competitor.textChanged.connect(self.onChangedCompetitor)
        self.parameterui.lineEdit_ArangoDBTime.textChanged.connect(self.onChangedArangoDBTime)
        self.parameterui.lineEdit_ArangoDBSpace.textChanged.connect(self.onChangedArangoDBSpace)

        # self.parameterui.accepted.connect(self.acceptParameters)

    def onChangedArangoDBSpace(self, text):
        self.arangoDBSpace = text

    def onChangedArangoDBTime(self, text):
        self.arangoDBTime = text

    def onChangedCompetitor(self, text):
        self.competitor = text

    def onChangedLearningRate(self, text):
        self.learning_rateSetting = text

    def onChangedRewardDecay(self, text):
        self.reward_decaySetting = text

    def onChangedGreedy(self, text):
        self.e_greedySetting = text

    def onChangedEpisode(self, text):
        self.episodeSetting = text

    # accept in Parameters
    # def acceptParameters(self):
    #
    #     print(self.learning_rateSetting)
    #     print(self.reward_decaySetting)
    #     print(self.e_greedySetting)
    #     print(self.episodeSetting)

    ########################################
    ######### data Clean ----  Button
    ########################################
    def openDataCleanDialog(self):
        qfile_Dialog = QFile('dataCleanandGenerateInitialSchemaDiag.ui')
        qfile_Dialog.open(QFile.ReadOnly)
        qfile_Dialog.close()
        self.cleanui = QUiLoader().load(qfile_Dialog)

        # initial lineEdit (first time is empty. After users selecting file/directory, it is given a new value.)
        self.cleanui.lineEdit_JSON.setText('{}'.format(self.cleanJSONAddress))
        self.cleanui.lineEdit_RDF.setText('{}'.format(self.cleanRDFAddress))
        self.cleanui.lineEdit_Relation.setText('{}'.format(self.cleanRELATIONAddress))

        self.cleanui.lineEdit_cleanedJSON.setText('{}'.format(self.cleanedJSONAddress))
        self.cleanui.lineEdit_cleanedRDF.setText('{}'.format(self.cleanedRDFAddress))
        self.cleanui.lineEdit_cleanedRelation.setText('{}'.format(self.cleanedRELATIONAddress))

        self.cleanui.show()

        # button in load files dialog
        self.cleanui.toolButton_JSON.clicked.connect(self.openCleanJSONFilesDialog)
        self.cleanui.toolButton_RDF.clicked.connect(self.openCleanRDFFilesDialog)
        self.cleanui.toolButton_Relation.clicked.connect(self.openCleanRelationFilesDialog)

        self.cleanui.toolButton_cleanedJSON.clicked.connect(self.openCleanedJSONFilesDialog)
        self.cleanui.toolButton_cleanedRDF.clicked.connect(self.openCleanedRDFFilesDialog)
        self.cleanui.toolButton_cleanedRelation.clicked.connect(self.openCleanedRelationFilesDialog)

        # self.cleanJSONAddress = self.cleanui.lineEdit_JSON.text()
        # self.cleanRDFAddress = self.cleanui.lineEdit_RDF.text()
        # self.cleanRELATIONAddress = self.cleanui.lineEdit_Relation.text()

        self.cleanui.accepted.connect(self.acceptDataClean)

    # accept in Data Clean Dialog
    def acceptDataClean(self):
        # print(self.cleanJSONAddress)
        # print(self.cleanRDFAddress)

        ############################################################### transform JSON
        ###############################################################
        ###############################################################
        arrayTable = pd.DataFrame(columns=['objId', 'key', 'index', 'valStr'])

        attrs = ['pageid', 'ns', 'title', 'original']
        iniTablesDict = dict.fromkeys(attrs)
        for a in attrs:
            attrsInEachTable = ['objId']
            attrsInEachTable.append(a)
            tab = pd.DataFrame(columns=attrsInEachTable)
            iniTablesDict[a] = tab

        # print('The initial array table:', len(arrayTable))
        # print('The number of initial tables:', len(iniTablesDict))

        # print(arrayTable)
        # print(iniTablesDict)

        objIdtemp = 0

        with open(self.cleanJSONAddress,
                  'r+') as readfile:
            # with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/JSONcleanExample.json', 'r') as readfile:
            for obj in jsonlines.Reader(readfile):
                # print(obj['normalized'][0]['from'])

                # constructJSONobject = {}
                # tabTemp = tabTemp.append({'key': sv, pv: ov}, ignore_index=True)

                if obj.__contains__('normalized'):
                    # print(obj['normalized'][0])
                    # print(obj['normalized'][1])

                    try:
                        # obj['normalized'][0]
                        arrayTable = arrayTable.append({'objId': objIdtemp, 'key': "normalized", 'index': 0,
                                                        'valStr': obj['normalized'][0]}, ignore_index=True)
                    except IndexError:
                        pass

                    try:
                        # obj['normalized'][1]
                        arrayTable = arrayTable.append({'objId': objIdtemp, 'key': "normalized", 'index': 1,
                                                        'valStr': obj['normalized'][1]}, ignore_index=True)
                    except IndexError:
                        pass

                # print(arrayTable)

                if obj.__contains__('pageid'):
                    tabTemp = iniTablesDict['pageid']
                    tabTemp = tabTemp.append({'objId': objIdtemp, 'pageid': obj['pageid']}, ignore_index=True)
                    iniTablesDict['pageid'] = tabTemp

                if obj.__contains__('ns'):
                    tabTemp = iniTablesDict['ns']
                    tabTemp = tabTemp.append({'objId': objIdtemp, 'ns': obj['ns']}, ignore_index=True)
                    iniTablesDict['ns'] = tabTemp

                if obj.__contains__('title'):
                    tabTemp = iniTablesDict['title']
                    tabTemp = tabTemp.append({'objId': objIdtemp, 'title': obj['title']}, ignore_index=True)
                    iniTablesDict['title'] = tabTemp

                if obj.__contains__('original'):
                    tabTemp = iniTablesDict['original']
                    tabTemp = tabTemp.append({'objId': objIdtemp, 'original': obj['original']}, ignore_index=True)
                    iniTablesDict['original'] = tabTemp

                objIdtemp += 1

        #    print(iniTablesDict)

        for a in attrs:
            # iniTablesDict[a].to_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampleInitialTablesJSON/' + a + '.csv', index=False)
            iniTablesDict[a].to_csv(
                self.cleanedJSONAddress + '/' + a + '.csv',
                index=False)

        arrayTable.to_csv(
            self.cleanedJSONAddress + '/arrayTable.csv',
            index=False)

        ############################################################### transform RDF
        ###############################################################
        ###############################################################

        # data_csv_RDF = pd.read_csv(
        #     '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personGraph.csv')[1:]
        data_csv_RDF = pd.read_csv(self.cleanRDFAddress)[1:]

        attrs_RDF = data_csv_RDF['p'].array.unique()
        # print(attrs_RDF)
        # print('The size of attributes:', attrs_RDF.size)

        iniTablesDict_RDF = dict.fromkeys(attrs_RDF)
        # print('The number of initial tables:', len(iniTablesDict_RDF))
        # print(iniTablesDict_RDF)

        for a in attrs_RDF:
            # print(a)
            attrsInEachTable = ['key']
            attrsInEachTable.append(a)
            tab = pd.DataFrame(columns=attrsInEachTable)
            iniTablesDict_RDF[a] = tab
            # print(tab)

        # print(len(iniTablesDict_RDF))
        # print(iniTablesDict_RDF)

        for row in data_csv_RDF.itertuples():
            sv = getattr(row, 's')
            pv = getattr(row, 'p')
            ov = getattr(row, 'o')
            tabTemp = iniTablesDict_RDF[pv]
            # dictTem = {}
            # dictTem[sv] = ov
            tabTemp = tabTemp.append({'key': sv, pv: ov}, ignore_index=True)
            iniTablesDict_RDF[pv] = tabTemp
            # print(iniTablesDict_RDF)
            # print(sv, pv, ov)
            # break

        # print(iniTablesDict_RDF)
        # print(iniTablesDict_RDF['subject'])

        for a in attrs_RDF:
            # iniTablesDict_RDF[a].to_csv(
            #     '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/initialTablesRDF/' + a + '.csv',
            #     index=False)
            iniTablesDict_RDF[a].to_csv(
                self.cleanedRDFAddress + '/' + a + '.csv',
                index=False)

    def openCleanJSONFilesDialog(self):
        filename = QFileDialog.getOpenFileName()
        self.cleanui.lineEdit_JSON.setText('{}'.format(filename[0]))
        self.cleanJSONAddress = filename[0]
        # return filename[0]
        # print(filename[0])

    def openCleanRDFFilesDialog(self):
        filename = QFileDialog.getOpenFileName()
        self.cleanui.lineEdit_RDF.setText('{}'.format(filename[0]))
        self.cleanRDFAddress = filename[0]

    def openCleanRelationFilesDialog(self):
        filename = QFileDialog.getOpenFileName()
        self.cleanui.lineEdit_Relation.setText('{}'.format(filename[0]))
        self.cleanRELATIONAddress = filename[0]

    # save to cleaned directory
    def openCleanedJSONFilesDialog(self):
        filename = QFileDialog.getExistingDirectory()
        self.cleanui.lineEdit_cleanedJSON.setText('{}'.format(filename))
        self.cleanedJSONAddress = filename
        # return filename
        # print(filename)

    def openCleanedRDFFilesDialog(self):
        filename = QFileDialog.getExistingDirectory()
        self.cleanui.lineEdit_cleanedRDF.setText('{}'.format(filename))
        self.cleanedRDFAddress = filename

    def openCleanedRelationFilesDialog(self):
        filename = QFileDialog.getExistingDirectory()
        self.cleanui.lineEdit_cleanedRelation.setText('{}'.format(filename))
        self.cleanedRELATIONAddress = filename

    # def executeLearningButton(self):
    #     info = self.textEdit.toPlainText()  # get text
    #     print('execute')

    ########################
    #################################################   Load Load Multi-Model File ----  Button
    ########################

    def openLoadFilesDialog(self):
        qfile_loadFilesDialog = QFile('loadMultiModleFileDiag.ui')
        qfile_loadFilesDialog.open(QFile.ReadOnly)
        qfile_loadFilesDialog.close()
        self.uploadui = QUiLoader().load(qfile_loadFilesDialog)

        # initial lineEdit (first time is empty. After users selecting file/directory, it is given a new value.)
        self.uploadui.lineEdit_JSON.setText('{}'.format(self.loadJSONDirectory))
        self.uploadui.lineEdit_RDF.setText('{}'.format(self.loadRDFDirectory))
        self.uploadui.lineEdit_Relation.setText('{}'.format(self.loadRelationDirectory))

        self.uploadui.show()

        # button in load files dialog
        self.uploadui.toolButton_JSON.clicked.connect(self.openLoadJSONFilesDialog)
        self.uploadui.toolButton_RDF.clicked.connect(self.openLoadRDFFilesDialog)
        self.uploadui.toolButton_Relation.clicked.connect(self.openLoadRelationFilesDialog)

        self.uploadui.accepted.connect(self.acceptLoadData)

    # accept in Data Load Dialog
    def acceptLoadData(self):

        # print(self.loadJSONDirectory)
        # print(self.loadRDFDirectory)
        # print(self.loadRelationDirectory)

        ####################################################################################################
        #                                   load JSON files
        ###################################################################################################
        filenames_JSON = []
        directoryLocation_JSON = self.loadJSONDirectory
        os.chdir(directoryLocation_JSON)  # The specified directory

        for i in glob.glob("*.csv"):  # take all .csv files in the specified directory
            filenames_JSON.append(i[:-4])  # take file name, but does not include ".csv" suffix

        # attributeToNoDict = {}
        noToAttributeDict = {}

        ######## i starts from 1
        i = 1
        removeArrayTable = 0
        # iterate files
        for file_name_JSON in filenames_JSON:
            if file_name_JSON == 'arrayTable':
                removeArrayTable = i

            # attributeToNoDict[file_name_JSON] = i
            noToAttributeDict[i] = file_name_JSON
            i += 1

        # print("JSON read done")

        ####################################################################################################
        #                                   load RDF files
        ###################################################################################################
        filenames_RDF = []
        directoryLocation_RDF = self.loadRDFDirectory
        os.chdir(directoryLocation_RDF)  # The specified directory

        for i in glob.glob("*.csv"):  # take all .csv files in the specified directory
            filenames_RDF.append(i[:-4])  # take file name, but does not include ".csv" suffix

        # i starts from 51 for RDF files
        i = 51
        # iterate files
        for file_name_RDF in filenames_RDF:
            # if file_name_RDF == 'title':
            #     attributeToNoDict['title_RDF'] = i
            # else:
            #     attributeToNoDict[file_name_RDF] = i

            # if file_name_RDF == 'title':
            #     noToAttributeDict[i] = 'title_RDF'
            # else:
            #     noToAttributeDict[i] = file_name_RDF

            noToAttributeDict[i] = file_name_RDF

            i += 1

        # print('>> the size of attribute dictionary is: ', len(noToAttributeDict), ', whose content is')
        # print(noToAttributeDict)
        #
        # print('>> the ID of arratyTable is: ', removeArrayTable)

        file = open('/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/noToAttributeDict.txt', 'w')

        for k, v in noToAttributeDict.items():
            file.write(str(k) + ' ' + str(v) + '\n')
        file.close()

    def openLoadJSONFilesDialog(self):
        filename = QFileDialog.getExistingDirectory()
        self.uploadui.lineEdit_JSON.setText('{}'.format(filename))
        self.loadJSONDirectory = filename
        # return filename[0]
        # print(filename[0])

    def openLoadRDFFilesDialog(self):
        filename = QFileDialog.getExistingDirectory()
        self.uploadui.lineEdit_RDF.setText('{}'.format(filename))
        self.loadRDFDirectory = filename

    def openLoadRelationFilesDialog(self):
        filename = QFileDialog.getExistingDirectory()
        self.uploadui.lineEdit_Relation.setText('{}'.format(filename))
        self.loadRelationDirectory = filename

    #     self.ui.buttonExcute.clicked.connect(self.executeLearningButton)
    #
    #
    # def executeLearningButton(self):
    #     info = self.textEdit.toPlainText()  # get text
    #     print('execute')

    #
    # app = QApplication([])
    # mapGUI = Mortal()
    # mapGUI.mainWindow.show()
    # app.setWindowIcon(QIcon('a.png'))
    # app.exec_()

    ####################################################################################################
    #                                   queryTimeFunctoin
    ###################################################################################################
    # observation(schemaString) i.e., current state string 1 0 2 0 3 0 4 0 5 0 51 0 52 0 53 0 54 0 55 0 56 0 57
    # currentSchema i.e., current schema  #{1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}
    # currentTableContent i.e., {1: objId  ns(tuple)， 2: objId original(tuple), ...}
    def queryTimeFunctoin(self, schemaString, currentSchema, currentTableContent):

        # global schemaQueryTimeTotal
        # global eachQueryTimeandSchema
        # global rewardReport
        # global noToAttributeDict
        # global attributeToNoDict

        # creat connecting
        conn = MySQLdb.connect(
            host='localhost',  # your MySQL service address
            port=3306,  # port
            user='root',  # visiting database service's user name and password
            passwd='1',
            # db='QLearning',  # database name
            charset='utf8mb4'  # for chinese
        )
        cur = conn.cursor()
        cur.execute("drop database if exists QLearning")
        cur.execute("Create database QLearning")
        cur.execute("use QLearning")

        engine = create_engine(
            "mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', '1', 'localhost', 'QLearning', 'utf8mb4'))

        for key, value in currentTableContent.items():
            value.to_sql(name=self.noToAttributeDict[key], con=engine, if_exists='replace', index=False)

        #######################################     query1    #######################################
        pageidNo_q1 = self.attributeToNoDict['pageid']
        # print(pageidNo_q1)
        wherePageid_q1 = 0
        for key, value in currentSchema.items():
            if pageidNo_q1 in value:
                wherePageid_q1 = key
                # print(wherePageid_q1)
                break

        # print(wherePageid_q1)

        pagidTable_q1 = self.noToAttributeDict[wherePageid_q1]

        # print(">> query 1:")
        # print(pagidTable_q1)
        sql1 = "select pageid from arrayTable, %s where arrayTable.key = 'normalized' and arrayTable.index = 0 and arrayTable.valStr = 'Doris_Brougham' and %s.objId = arrayTable.objId" % (
        pagidTable_q1, pagidTable_q1)  # Doris_Brougham     Henry_Standing_Bear

        middleTime = []
        recordEachQueryTime = []
        for t_i in range(3):
            time_start1 = time.time()
            cur.execute(sql1)
            time_end1 = time.time()
            query_time1 = time_end1 - time_start1
            middleTime.append(query_time1)

        middleTime.sort()
        totalQueryTime = - middleTime[1]
        recordEachQueryTime.append(middleTime[1])
        # print('query time1', middleTime[1])
        # print('totalQueryTime: ', totalQueryTime)
        middleTime.clear()

        #######################################     query2    #######################################

        subjectNo_q2 = self.attributeToNoDict['subject']
        whereSubject_q2 = 0
        for key, value in currentSchema.items():
            if subjectNo_q2 in value:
                whereSubject_q2 = key
                break

        subjectTable_q2 = self.noToAttributeDict[whereSubject_q2]
        sql2 = "select subject from %s where %s.key = 'Tor_Ahlsand'" % (subjectTable_q2, subjectTable_q2)

        for t_i in range(3):
            time_start2 = time.time()
            cur.execute(sql2)
            time_end2 = time.time()
            query_time2 = time_end2 - time_start2
            middleTime.append(query_time2)

        middleTime.sort()
        totalQueryTime -= middleTime[1]
        recordEachQueryTime.append(middleTime[1])

        middleTime.clear()

        #######################################     query3    #######################################
        # we can not test in example

        birthDateNo_q3 = self.attributeToNoDict['birthDate']
        activeYearsStartYearNo_q3 = self.attributeToNoDict['activeYearsStartYear']
        activeYearsEndYearNo_q3 = self.attributeToNoDict['activeYearsEndYear']

        whereBirthDateNo_q3 = 0
        whereActiveYearsStartYearNo_q3 = 0
        whereActiveYearsEndYearNo_q3 = 0

        for key, value in currentSchema.items():
            if birthDateNo_q3 in value:
                whereBirthDateNo_q3 = key
                break

        for key, value in currentSchema.items():
            if activeYearsStartYearNo_q3 in value:
                whereActiveYearsStartYearNo_q3 = key
                break

        for key, value in currentSchema.items():
            if activeYearsEndYearNo_q3 in value:
                whereActiveYearsEndYearNo_q3 = key
                break

        birthDateTable_q3 = self.noToAttributeDict[whereBirthDateNo_q3]
        activeYearsStartYearTable_q3 = self.noToAttributeDict[whereActiveYearsStartYearNo_q3]
        activeYearsEndYearTable_q3 = self.noToAttributeDict[whereActiveYearsEndYearNo_q3]

        # queryKey = 'Heath_Ledger'
        if (whereBirthDateNo_q3 == whereActiveYearsStartYearNo_q3) or (
                whereBirthDateNo_q3 == whereActiveYearsEndYearNo_q3):  # a==b or a==c
            if whereActiveYearsStartYearNo_q3 == whereActiveYearsEndYearNo_q3:  # b==c e.g., (1,1,1)
                sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s where %s.key = 'Heath_Ledger'" % (
                birthDateTable_q3, birthDateTable_q3)
            else:
                if (whereBirthDateNo_q3 == whereActiveYearsStartYearNo_q3) and (
                        whereActiveYearsStartYearNo_q3 != whereActiveYearsEndYearNo_q3):  # a == b and b!=c  (1,1,2)
                    sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (
                    birthDateTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3, birthDateTable_q3,
                    activeYearsEndYearTable_q3)
                else:  # a==c and b!=c (1,2,1)
                    sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (
                    birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, birthDateTable_q3,
                    activeYearsStartYearTable_q3)
        else:  # a!=b and a!=c
            if whereActiveYearsStartYearNo_q3 != whereActiveYearsEndYearNo_q3:  # a!=b, a!=c, b!=c (1,2,3)
                sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key and %s.key = %s.key" % (
                birthDateTable_q3, activeYearsStartYearTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3,
                birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, activeYearsEndYearTable_q3)
            if whereActiveYearsStartYearNo_q3 == whereActiveYearsEndYearNo_q3:  ##a!=b and a!=c and b==c (2,1,1)
                sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (
                birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, birthDateTable_q3,
                activeYearsStartYearTable_q3)

        for t_i in range(3):
            time_start3 = time.time()
            cur.execute(sql3)
            time_end3 = time.time()
            query_time3 = time_end3 - time_start3
            middleTime.append(query_time3)

        middleTime.sort()
        totalQueryTime -= middleTime[1]
        recordEachQueryTime.append(middleTime[1])

        middleTime.clear()

        #######################################     query4    #######################################

        original_q4 = self.attributeToNoDict['original']
        title_q4 = self.attributeToNoDict['title']
        pageid_q4 = self.attributeToNoDict['pageid']

        whereOriginal_q4 = 0
        whereTitle_q4 = 0
        wherePageid_q4 = 0

        for key, value in currentSchema.items():
            if original_q4 in value:
                whereOriginal_q4 = key
                break

        for key, value in currentSchema.items():
            if title_q4 in value:
                whereTitle_q4 = key
                break

        for key, value in currentSchema.items():
            if pageid_q4 in value:
                wherePageid_q4 = key
                break

        originalTable_q4 = self.noToAttributeDict[whereOriginal_q4]
        titleTable_q4 = self.noToAttributeDict[whereTitle_q4]
        pageidTable_q4 = self.noToAttributeDict[wherePageid_q4]

        queryKey_4 = 8484745
        # queryKey_4 = 43757531 #example

        if (whereOriginal_q4 == whereTitle_q4) or (whereOriginal_q4 == wherePageid_q4):  # a==b or a==c
            if whereTitle_q4 == wherePageid_q4:  # b==c e.g., (1,1,1)
                sql4 = "select original, title from %s where %s.pageid = %s" % (
                originalTable_q4, originalTable_q4, queryKey_4)
            else:
                if (whereOriginal_q4 == whereTitle_q4) and (
                        whereTitle_q4 != wherePageid_q4):  # a == b and b!=c  (1,1,2)
                    sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (
                    originalTable_q4, pageidTable_q4, pageidTable_q4, queryKey_4, originalTable_q4, pageidTable_q4)
                else:  # a==c and b!=c (1,2,1)
                    sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (
                    originalTable_q4, titleTable_q4, originalTable_q4, queryKey_4, originalTable_q4, titleTable_q4)
        else:  # a!=b and a!=c
            if whereTitle_q4 != wherePageid_q4:  # a!=b, a!=c, b!=c (1,2,3)
                sql4 = "select original, title from %s, %s, %s where %s.pageid = %s and %s.objId = %s.objId and %s.objId = %s.objId" % (
                originalTable_q4, titleTable_q4, pageidTable_q4, pageidTable_q4, queryKey_4, originalTable_q4,
                titleTable_q4, originalTable_q4, pageidTable_q4)
            if whereTitle_q4 == wherePageid_q4:  ##a!=b and a!=c and b==c (2,1,1)
                sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (
                originalTable_q4, titleTable_q4, titleTable_q4, queryKey_4, originalTable_q4, titleTable_q4)

        for t_i in range(3):
            time_start4 = time.time()
            cur.execute(sql4)
            time_end4 = time.time()
            query_time4 = time_end4 - time_start4
            middleTime.append(query_time4)

        middleTime.sort()
        totalQueryTime -= middleTime[1]
        recordEachQueryTime.append(middleTime[1])
        middleTime.clear()

        #######################################     query5    #######################################
        birthYearNo_q5 = self.attributeToNoDict['birthYear']
        nsNo_q5 = self.attributeToNoDict['ns']

        whereBirthYear_q5 = 0
        whereNs_q5 = 0

        for key, value in currentSchema.items():
            if birthYearNo_q5 in value:
                whereBirthYear_q5 = key
                break

        for key, value in currentSchema.items():
            if nsNo_q5 in value:
                whereNs_q5 = key
                break

        BirthYearTable_q5 = self.noToAttributeDict[whereBirthYear_q5]
        nsTable_q5 = self.noToAttributeDict[whereNs_q5]

        sql5 = "select %s.key, birthYear, ns from arrayTable, %s, %s where arrayTable.key = 'normalized' and arrayTable.index = 0 and arrayTable.valStr = 'Sadako_Sasaki' and %s.objId = arrayTable.objId and %s.key = arrayTable.valStr" % (
        BirthYearTable_q5, BirthYearTable_q5, nsTable_q5, nsTable_q5,
        BirthYearTable_q5)  # Sadako_Sasaki     Henry_Standing_Bear（example）

        for t_i in range(3):
            time_start5 = time.time()
            cur.execute(sql5)
            time_end5 = time.time()
            query_time5 = time_end5 - time_start5
            middleTime.append(query_time5)

        middleTime.sort()
        totalQueryTime -= middleTime[1]
        recordEachQueryTime.append(middleTime[1])

        middleTime.clear()

        # for experimental statistics
        recordEachQueryTime.append(schemaString)
        recordEachQueryTime.insert(0, -totalQueryTime)

        # for display
        # newTableTuple = []
        # newTableTuple.append(schemaString)
        # newTableTuple.append(-totalQueryTime)

        ##################################################################
        # get space consumption
        #############################################################################
        sql_space = "select sum(DATA_LENGTH)+sum(INDEX_LENGTH) from information_schema.tables where table_schema='QLearning';"
        cur.execute(sql_space)
        results = str(cur.fetchone())  # get the return result

        recordEachQueryTime.append(results[1:-2])

        filetotalQueryTimeNamee = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/Results/totalQueryTimeArray' + str(
            self.outputExperimentStatisticsFileNo) + '.txt'
        filetotalQueryTime = open(filetotalQueryTimeNamee, 'a+')
        for i in recordEachQueryTime:
            filetotalQueryTime.write(str(i) + '\n')
        filetotalQueryTime.close()

        # Close the Cursor
        cur.close()

        # conn.close() close database connection
        conn.close()

        return totalQueryTime

    ####################################################################################################
    #                                   step
    ####################################################################################################
    # observation i.e., current state string 1 0 2 0 3 0 4 0 5 0 51 0 52 0 53 0 54 0 55 0 56 0 57
    # currentSchema i.e., current schema  #{1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}
    # currentTableContent i.e., {1: objId  ns(tuple)， 2: objId original(tuple), ...}

    def step(self, observation, action, currentSchema, currentTableContent, previousQueryTime):

        # we will check whether action space is empty, if it is empty, then this is terminal

        # global removeArrayTable
        # global noToAttributeDict
        # global attributeToNoDict
        # global secondRL
        # global randomTab
        # global done

        currentTableIDs = list(currentSchema.keys())

        if len(currentTableIDs) == 2:  # (randomTable == action, randomTab == removeArrayTable, unfinitely loop)
            s_ = observation
            reward = 0
            self.done = True
            return s_, reward, currentSchema, currentTableContent, 0

        self.randomTab = self.secondRL.secondTable_choose_action(action, currentTableIDs)
        while (
                self.randomTab == action or self.randomTab == self.removeArrayTable or self.randomTab not in currentTableIDs):  # avoid self-join
            self.randomTab = self.secondRL.secondTable_choose_action(action, currentTableIDs)

        ######################################  action < 50 and self.randomTab < 50 ######################################

        if action < 50 and self.randomTab < 50:  # both action(attribute) and table are from JSON
            if action == self.removeArrayTable:
                s_ = observation
                reward = 0
                return s_, reward, currentSchema, currentTableContent, 0
                # currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
                # return s_, reward, currentSchema, currentTableContent

            if action not in currentTableIDs:
                s_ = observation
                reward = 0
                # currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
                return s_, reward, currentSchema, currentTableContent, 0
            else:
                left = currentTableContent[action]
                right = currentTableContent[self.randomTab]
                currentTableContent[self.randomTab] = pd.merge(left, right, on='objId', how='outer')
                # print(">>  currentTableContent", currentTableContent[self.randomTab])

                # update current relational schema
                currentSchema[self.randomTab].extend(currentSchema[action])
                currentSchema[self.randomTab].sort()
                del currentSchema[action]
                del currentTableContent[action]
                # print(">> currentSchema: ", currentSchema)

                # update observation (state/schema string)
                s_list = []
                temAttriKeys = list(currentSchema.keys())  # [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
                temAttriKeys.sort()
                # print(temAttriKeys)
                for si in temAttriKeys:
                    s_list.extend(currentSchema[si])
                    s_list.append(0)
                s_list.pop()

                s_ = " ".join('%s' % i for i in s_list)

                # print(">> new state <50 <50 s_: ", s_)

                # currentQueryTime function
                currentQueryTime = self.queryTimeFunctoin(s_, currentSchema, currentTableContent)

                reward = currentQueryTime - previousQueryTime

                return s_, reward, currentSchema, currentTableContent, currentQueryTime

        ######################################  action > 50 and self.randomTab > 50 ######################################

        if action > 50 and self.randomTab > 50:  # both action(attribute) and random table are from RDF

            if action not in currentTableIDs:
                s_ = observation
                # currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
                reward = 0
                return s_, reward, currentSchema, currentTableContent, 0
            else:
                left = currentTableContent[action]
                right = currentTableContent[self.randomTab]
                currentTableContent[self.randomTab] = pd.merge(left, right, on='key', how='outer')
                # print(" >>")
                # print(">>  currentTableContent", currentTableContent[self.randomTab])

                # update current relational schema
                currentSchema[self.randomTab].extend(currentSchema[action])
                currentSchema[self.randomTab].sort()
                del currentSchema[action]
                del currentTableContent[action]
                # print(">> currentSchema: ", currentSchema)

                # update observation (state/schema string)
                s_list = []
                temAttriKeys = list(currentSchema.keys())  # [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
                temAttriKeys.sort()
                # print(temAttriKeys)
                for si in temAttriKeys:
                    s_list.extend(currentSchema[si])
                    s_list.append(0)
                s_list.pop()  # drop the last 0

                s_ = " ".join('%s' % i for i in s_list)

                # currentQueryTime function
                currentQueryTime = self.queryTimeFunctoin(s_, currentSchema, currentTableContent)

                reward = currentQueryTime - previousQueryTime

                return s_, reward, currentSchema, currentTableContent, currentQueryTime

        ######################################  (action < 50 and self.randomTab > 50) or (action > 50 and self.randomTab < 50) ######################################

        if (action < 50 and self.randomTab > 50) or (
                action > 50 and self.randomTab < 50):  # one is from action, another one is from RDF

            if action == self.removeArrayTable:
                s_ = observation
                # currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
                reward = 0
                return s_, reward, currentSchema, currentTableContent, 0

            if action not in currentTableIDs:
                s_ = observation
                # currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
                reward = 0
                return s_, reward, currentSchema, currentTableContent, 0
            else:

                actionTableName = self.noToAttributeDict[action]
                randomTabTableName = self.noToAttributeDict[self.randomTab]

                if (actionTableName == "title" and randomTabTableName == "title_RDF") or (
                        actionTableName == "title_RDF" and randomTabTableName == "title"):
                    left = currentTableContent[action]
                    right = currentTableContent[self.randomTab]
                    currentTableContent[self.randomTab] = pd.merge(left, right, on='title', how='outer')

                    # update current relational schema
                    currentSchema[self.randomTab].extend(currentSchema[action])
                    currentSchema[self.randomTab].sort()
                    del currentSchema[action]
                    del currentTableContent[action]
                    # print(">> currentSchema: ", currentSchema)

                    # update observation (state/schema string)
                    s_list = []
                    temAttriKeys = list(currentSchema.keys())  # [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
                    temAttriKeys.sort()
                    # print(temAttriKeys)
                    for si in temAttriKeys:
                        s_list.extend(currentSchema[si])
                        s_list.append(0)
                    s_list.pop()  # drop the last 0

                    s_ = " ".join('%s' % i for i in s_list)

                    # currentQueryTime function
                    currentQueryTime = self.queryTimeFunctoin(s_, currentSchema, currentTableContent)
                    reward = currentQueryTime - previousQueryTime

                    return s_, reward, currentSchema, currentTableContent, currentQueryTime
                else:  # do not update schema, just get the reward after this action
                    s_ = observation
                    # currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
                    reward = 0
                    return s_, reward, currentSchema, currentTableContent, 0


app = QApplication([])
mortal = Mortal()
# mortal.ui.setWindowIcon(QIcon('a.png'))
mortal.ui.show()

# app.setWindowIcon(QIcon('a.png'))
sys.exit(app.exec_())

##################################################################################
# # line chart time
# self.ui.widget_time.setContentsMargins(0, 0, 0, 0)
# lay_time = QtWidgets.QVBoxLayout(self.ui.widget_time)
# lay_time.setContentsMargins(0, 0, 0, 0)
#
# chartviewTime = QtCharts.QChartView()
# chartviewTime.setContentsMargins(0, 0, 0, 0)
# lay_time.addWidget(chartviewTime)
#
# series_time = QtCharts.QLineSeries()
#
# # for i in range(10):
# #     series_time << QtCore.QPointF(i, random.uniform(0, 10))
#
# series_time.append(0, 6)
# series_time.append(2, 4)
# series_time.append(3, 8)
# series_time.append(7, 4)
# series_time.append(10, 5)
#
# # Create Chart and set General Chart setting
# chart_time = QtCharts.QChart()
# chart_time.addSeries(series_time)
# chart_time.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
#
# chart_time.legend().hide()
#
# # X Axis Settings
# axisX = QtCharts.QValueAxis()
# chart_time.addAxis(axisX, QtCore.Qt.AlignBottom)
# series_time.attachAxis(axisX)
#
# # Y Axis Settings
# axisY = QtCharts.QValueAxis()
# chart_time.addAxis(axisY, QtCore.Qt.AlignLeft)
# series_time.attachAxis(axisY)
#
# chartviewTime.setChart(chart_time)
#
# ##################################################################################
# #line chart space
# self.ui.widget_space.setContentsMargins(0, 0, 0, 0)
# lay_space = QtWidgets.QVBoxLayout(self.ui.widget_space)
# lay_space.setContentsMargins(0, 0, 0, 0)
#
# chartviewSpace = QtCharts.QChartView()
# chartviewSpace.setContentsMargins(0, 0, 0, 0)
# lay_space.addWidget(chartviewSpace)
#
# series = QtCharts.QLineSeries()
#
# # for i in range(10):
# #     series_time << QtCore.QPointF(i, random.uniform(0, 10))
#
# series.append(0, 6)
# series.append(2, 4)
# series.append(3, 8)
# series.append(7, 4)
# series.append(10, 5)
#
#
# # Create Chart and set General Chart setting
# chart_space = QtCharts.QChart()
# chart_space.addSeries(series)
# chart_space.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
# chart_space.legend().hide()
# #chart_space.setTitle("Changes in Space")
#
# # X Axis Settings
# axisX = QtCharts.QValueAxis()
# chart_space.addAxis(axisX, QtCore.Qt.AlignBottom)
# series.attachAxis(axisX)
#
# # Y Axis Settings
# axisY = QtCharts.QValueAxis()
# chart_space.addAxis(axisY, QtCore.Qt.AlignLeft)
# series.attachAxis(axisY)
#
# chartviewSpace.setChart(chart_space)


# ##################################################################################
# #tablewidge
# data = [
#     [4, 9, 2],
#     [1, 0, 0],
#     [3, 5, 0],
#     [3, 3, 2],
#     [7, 8, 9],
# ]
#
#
# rowcnt = len(data)
# colcnt = len(data[0])
#
#
# # title = ["Schema", "fuga", "piyo"]
# # vheader = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Vertical)
# # #vheader.setResizeMode(QtWidgets.QHeaderView.ResizeToContents)
# # self.ui.tableWidget_output.setVerticalHeader(vheader)
# # hheader = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Horizontal)
# # #hheader.setResizeMode(QtWidgets.QHeaderView.ResizeToContents)
# # self.ui.tableWidget_output.setHorizontalHeader(hheader)
# # self.ui.tableWidget_output.setHorizontalHeaderLabels(title)
#
#
#
# self.ui.tableWidget_output.setRowCount(rowcnt)
# self.ui.tableWidget_output.setColumnCount(colcnt)
#
# for i in range(rowcnt):
#     for j in range(colcnt):
#         #item = QtGui.QTableWidgetItem(str(data[i][j]))
#         #self.ui.tableWidget_output.setItem(i, j, item)
#
#         item = QtWidgets.QTableWidgetItem(str(data[i][j]))
#         # model = QtGui.QTableWidgetItem(tokens[1])
#         # price = QtGui.QTableWidgetItem(tokens[2])
#         self.ui.tableWidget_output.setItem(i, j, item)
#         # self.table.setItem(i, 1, model)
#         # self.table.setItem(i, 2, price)
# #self.ui.tableWidget_output.resizeColumnsToContents()
#
# self.ui.tableWidget_output.cellDoubleClicked.connect(self.openModifyDialog)


# filenames_results = []
#         directoryLocation_results = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/Results'
#         os.chdir(directoryLocation_results)  # The specified directory
#
#         for i in glob.glob("*.txt"):  # take all .csv files in the specified directory
#             filenames_results.append(i[19:-4])  # take file name, but does not include ".csv" suffix
#         count = len(filenames_results)
#         print(count)
#
#
#         for filenames_r in filenames_results:
#             newTableTuple = []
#             directoryLocation_TXT = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/InformationStore/Results/totalQueryTimeArray' + str(filenames_r) + '.txt'
#             file = open(directoryLocation_TXT, encoding='utf8')
#             lines = file.readlines()
#             localOptimal = [None] * 8
#             if (len(lines) > 8):
#                 localOptimal[0] = lines[0]
#                 localOptimal[1] = lines[1]
#                 localOptimal[2] = lines[2]
#                 localOptimal[3] = lines[3]
#                 localOptimal[4] = lines[4]
#                 localOptimal[5] = lines[5]
#                 localOptimal[6] = lines[6]
#                 localOptimal[7] = lines[7]
#
#             count = 0
#             while (count < len(lines)):
#                 tempTotalTime = lines[count]
#                 # print(count)
#                 if float(tempTotalTime) < float(localOptimal[0]):
#                     j = 0
#                     while (j < 8):
#                         localOptimal[j] = lines[count + j]
#                         j += 1
#                     count += 8
#                 else:
#                     count += 8
#             file.close()
#
#             newTableTuple.append(localOptimal[6])   #schemaString
#             newTableTuple.append(localOptimal[0][0:7])   #time
#             newTableTuple.append(localOptimal[7])   #space
#
#
#             print("newTableTuple")
#             print(newTableTuple)
#
#             self.tableData.append(newTableTuple)
#
#             ##################################################################################
#             # tablewidge
#             rowcnt = len(self.tableData)
#             colcnt = len(self.tableData[0])
#
#
#             self.ui.tableWidget_output.setRowCount(rowcnt)
#             self.ui.tableWidget_output.setColumnCount(colcnt)
#
#             for i in range(rowcnt):
#                 for j in range(colcnt):
#                     item = QtWidgets.QTableWidgetItem(str(self.tableData[i][j]))
#                     self.ui.tableWidget_output.setItem(i, j, item)
#
#             self.series_time.append(self.outputExperimentStatisticsFileNo, float(newTableTuple[1]))
#             MysqlSpaceMB = float(newTableTuple[2][9:-3])/(math.pow(2, 20))
#             self.series_space.append(self.outputExperimentStatisticsFileNo, MysqlSpaceMB)
#
#             self.series_time2.append(self.outputExperimentStatisticsFileNo, self.arangoDBTime)
#             self.series_space2.append(self.outputExperimentStatisticsFileNo, self.arangoDBSpace)
#
#
#             self.outputExperimentStatisticsFileNo += 1
#
#
#
#             #################################################################################
#             # line chart time
#             # Create Chart and set General Chart setting
#
#
#
#
#
#
#         self.chart_time.addSeries(self.series_time)
#         self.chart_time.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
#         self.series_time.setName('SQL')
#         #self.chart_time.legend().hide()
#
#         # X Axis Settings
#         axisX = QtCharts.QValueAxis()
#         axisX.setTitleText('Episode')
#         self.chart_time.addAxis(axisX, QtCore.Qt.AlignBottom)
#         # axisX.setRange(0,20)
#         # axisX.setTickCount(10)  # how many of grid
#         # axisX.setMinorTickCount(2)      #setting min scalee of each grid
#         # axisX.setLabelFormat("%u")        # setting format of scale
#         self.series_time.attachAxis(axisX)
#
#         # Y Axis Settings
#         axisY = QtCharts.QValueAxis()
#         axisY.setTitleText('Time/s')
#         self.chart_time.addAxis(axisY, QtCore.Qt.AlignLeft)
#         #axisY.setRange(0,20)
#         self.series_time.attachAxis(axisY)
#         #self.chartviewTime.setChart(self.chart_time)
#
#
#
#         self.chart_time.addSeries(self.series_time2)
#         self.series_time2.setName(self.competitor)
#         self.series_time2.setColor(QColor(255, 0, 0))
#         self.series_time2.attachAxis(axisX)
#         self.series_time2.attachAxis(axisY)
#
#
#         self.chartviewTime.setChart(self.chart_time)
#
#         # PySide2.QtCharts.QChart.removeAxis(axis)
#
#
#
#         ##################################################################################
#         # line chart space
#         # Create Chart and set General Chart setting
#
#         self.chart_space.addSeries(self.series_space)
#         self.chart_space.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
#         self.series_space.setName('SQL')
#         #self.chart_space.legend().hide()
#         # chart_space.setTitle("Changes in Space")
#
#
#         # X Axis Settings
#         axisX_Space = QtCharts.QValueAxis()
#         axisX_Space.setTitleText('Episode')
#         self.chart_space.addAxis(axisX_Space, QtCore.Qt.AlignBottom)
#         self.series_space.attachAxis(axisX_Space)
#
#         # Y Axis Settings
#         axisY_Space = QtCharts.QValueAxis()
#         axisY_Space.setTitleText('Memory/B')
#         axisY_Space.setRange(390,480)
#         self.chart_space.addAxis(axisY_Space, QtCore.Qt.AlignLeft)
#         self.series_space.attachAxis(axisY_Space)
#
#         self.chart_space.addSeries(self.series_space2)
#         self.series_space2.setName(self.competitor)
#         self.series_space2.setColor(QColor(255, 0, 0))
#         self.series_space2.attachAxis(axisX_Space)
#         self.series_space2.attachAxis(axisY_Space)
#
#         self.chartviewSpace.setChart(self.chart_space)









