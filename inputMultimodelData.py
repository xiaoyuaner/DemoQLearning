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

# engine = create_engine('mysql+pymysql://user:password@localhost/stonetest?charset=utf8mb4')
#schemaQueryTimeTotal = {}
#rewardReport = []
#eachQueryTimeandSchema = []

outputExperimentStatisticsFileNo = 0


#
# app = QApplication([])
#
# #main interface
# mainWindow = QMainWindow()
# mainWindow.resize(1000,900)
# mainWindow.move(300,300)
# mainWindow.setWindowTitle('Mapping Multi-Model to Relational Data with RL')
#
#
# #textbox
# textEdit = QPlainTextEdit(mainWindow)
# textEdit.setPlaceholderText("Please input JSON")
# textEdit.resize(100,100)
# textEdit.move(10,10)
#
#
# def executeLearningButton():
#     info = textEdit.toPlainText()   #get text
#     print('execute')
#
#
#
# #button
# buttonExcute = QPushButton('Execute', mainWindow)
# buttonExcute.move(600,700)
# buttonExcute.clicked.connect(executeLearningButton)
#
#
# mainWindow.show()
#
# app.exec_()
#
#
#


####################################################################################################
#                                   queryTimeFunctoin
###################################################################################################
#observation(schemaString) i.e., current state string 1 0 2 0 3 0 4 0 5 0 51 0 52 0 53 0 54 0 55 0 56 0 57
#currentSchema i.e., current schema  #{1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}
#currentTableContent i.e., {1: objId  ns(tuple)， 2: objId original(tuple), ...}
def queryTimeFunctoin(schemaString, currentSchema, currentTableContent):


    #global schemaQueryTimeTotal
    #global eachQueryTimeandSchema
    #global rewardReport
    global noToAttributeDict
    global attributeToNoDict
    global outputExperimentStatisticsFileNo


    # creat connecting
    conn = MySQLdb.connect(
        host='localhost',  # your MySQL service address
        port=3306,  # port
        user='root',  # visiting database service's user name and password
        passwd='1',
        #db='QLearning',  # database name
        charset='utf8mb4'  # for chinese
    )
    cur = conn.cursor()
    cur.execute("drop database if exists QLearning")
    cur.execute("Create database QLearning")
    cur.execute("use QLearning")



    engine = create_engine(
        "mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', '1', 'localhost', 'QLearning', 'utf8mb4'))

    for key,value in currentTableContent.items():
        value.to_sql(name=noToAttributeDict[key], con=engine, if_exists='replace', index=False)





    #######################################     query1    #######################################
    pageidNo_q1 = attributeToNoDict['pageid']
    #print(pageidNo_q1)
    wherePageid_q1 = 0
    for key, value in currentSchema.items():
        if pageidNo_q1 in value:
            wherePageid_q1 = key
            #print(wherePageid_q1)
            break

    #print(wherePageid_q1)

    pagidTable_q1 = noToAttributeDict[wherePageid_q1]

    # print(">> query 1:")
    # print(pagidTable_q1)
    sql1 = "select pageid from arrayTable, %s where arrayTable.key = 'normalized' and arrayTable.index = 0 and arrayTable.valStr = 'Doris_Brougham' and %s.objId = arrayTable.objId" %(pagidTable_q1, pagidTable_q1)             #Doris_Brougham     Henry_Standing_Bear

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


    # results = cur.fetchall()  # get the return result
    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/FinalResult/query1.txt", "a+") as f:
    #     for rel in results:
    #         f.write(str(rel)+"\n")



    #totalQueryTime = - query_time1
    #print(totalQueryTime)

    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampletimeResult/query1.txt", "a+") as f:
    #     f.write(str(query_time1)+"\n")


    #######################################     query2    #######################################

    subjectNo_q2 = attributeToNoDict['subject']
    whereSubject_q2 = 0
    for key, value in currentSchema.items():
        if subjectNo_q2 in value:
            whereSubject_q2 = key
            break


    subjectTable_q2 = noToAttributeDict[whereSubject_q2]

    # print(">> query 2:")
    # print(subjectTable_q2)
    # sql2 = "select %s.subject " \
    #        "from %s " \
    #        "where %s.key = 'Henry_Standing_Bear'" % (subjectTable_q2, subjectTable_q2, subjectTable_q2)
    #                                             # Tor_Ahlsand

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
    # print('query time2', middleTime[1])
    # print('totalQueryTime: ', totalQueryTime)
    middleTime.clear()



    #
    # results = cur.fetchall()  # get the return result
    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/FinalResult/query2.txt", "a+") as f:
    #     for rel in results:
    #         f.write(str(rel)+"\n")
    #     f.write("\n")


    #totalQueryTime += query_time2
    #totalQueryTime -= query_time2


    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampletimeResult/query2.txt",
    #           "a+") as f:
    #     f.write(str(query_time2) + "\n")







    #######################################     query3    #######################################
    #we can not test in example

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



    # print(">> query 3:")
    # print(birthDateTable_q3)
    # print(activeYearsStartYearTable_q3)
    # print(activeYearsEndYearTable_q3)

    #queryKey = 'Heath_Ledger'
    if (whereBirthDateNo_q3 == whereActiveYearsStartYearNo_q3) or (whereBirthDateNo_q3 == whereActiveYearsEndYearNo_q3):           #a==b or a==c
        if whereActiveYearsStartYearNo_q3 == whereActiveYearsEndYearNo_q3:      #b==c e.g., (1,1,1)
            sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s where %s.key = 'Heath_Ledger'" % (birthDateTable_q3, birthDateTable_q3)
        else:
            if (whereBirthDateNo_q3 == whereActiveYearsStartYearNo_q3) and (whereActiveYearsStartYearNo_q3 != whereActiveYearsEndYearNo_q3): #a == b and b!=c  (1,1,2)
                sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (birthDateTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsEndYearTable_q3)
            else:   #a==c and b!=c (1,2,1)
                sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsStartYearTable_q3)
    else:   #a!=b and a!=c
        if whereActiveYearsStartYearNo_q3 != whereActiveYearsEndYearNo_q3: #a!=b, a!=c, b!=c (1,2,3)
            sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key and %s.key = %s.key" % (birthDateTable_q3, activeYearsStartYearTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, activeYearsEndYearTable_q3)
        if whereActiveYearsStartYearNo_q3 == whereActiveYearsEndYearNo_q3:      ##a!=b and a!=c and b==c (2,1,1)
            sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsStartYearTable_q3)

    # if (birthDateTable_q3 == activeYearsStartYearTable_q3) or (birthDateTable_q3 == activeYearsEndYearTable_q3):           #a==b or a==c
    #     if activeYearsStartYearTable_q3 == activeYearsEndYearTable_q3:      #b==c e.g., (1,1,1)
    #         sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s where %s.key = 'Heath_Ledger'" % (birthDateTable_q3, birthDateTable_q3)
    #     else:
    #         if (birthDateTable_q3 == activeYearsStartYearTable_q3) and (activeYearsStartYearTable_q3 != activeYearsEndYearTable_q3): #a == b and b!=c  (1,1,2)
    #             sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (birthDateTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsEndYearTable_q3)
    #         else:   #a==c and b!=c (1,2,1)
    #             sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsStartYearTable_q3)
    # else:   #a!=b and a!=c
    #     if activeYearsStartYearTable_q3 != activeYearsEndYearTable_q3: #a!=b, a!=c, b!=c (1,2,3)
    #         sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key and %s.key = %s.key" % (birthDateTable_q3, activeYearsStartYearTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, activeYearsEndYearTable_q3)
    #     if activeYearsStartYearTable_q3 == activeYearsEndYearTable_q3:      ##a!=b and a!=c and b==c (2,1,1)
    #         sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = 'Heath_Ledger' and %s.key = %s.key" % (birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsStartYearTable_q3)



    for t_i in range(3):
        time_start3 = time.time()
        cur.execute(sql3)
        time_end3 = time.time()
        query_time3 = time_end3 - time_start3
        middleTime.append(query_time3)

    middleTime.sort()
    totalQueryTime -= middleTime[1]
    recordEachQueryTime.append(middleTime[1])
    # print('query time3', middleTime[1])
    # print('totalQueryTime: ', totalQueryTime)
    middleTime.clear()


    #
    # results = cur.fetchall()  # get the return result
    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/FinalResult/query3.txt", "a+") as f:
    #     for rel in results:
    #         f.write(str(rel)+"\n")
    #     f.write("\n")





    #
    # ###totalQueryTime += query_time3
    # #totalQueryTime -= query_time3
    #
    #
    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampletimeResult/query3.txt",
    #           "a+") as f:
    #     f.write(str(query_time3) + "\n")








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

    # print(">> query 4:")
    # print(originalTable_q4)
    # print(titleTable_q4)
    # print(pageidTable_q4)

    #print(originalTable_q4, titleTable_q4, pageidTable_q4)

    # if originalTable_q4 == titleTable_q4:
    #     sql4 = "select original, title from %s where %s.pageid = 8484745" % (subjectTable_q2, subjectTable_q2)

    queryKey_4 = 8484745
    #queryKey_4 = 43757531 #example

    if (whereOriginal_q4 == whereTitle_q4) or (whereOriginal_q4 == wherePageid_q4):           #a==b or a==c
        if whereTitle_q4 == wherePageid_q4:      #b==c e.g., (1,1,1)
            sql4 = "select original, title from %s where %s.pageid = %s" % (originalTable_q4, originalTable_q4, queryKey_4)
        else:
            if (whereOriginal_q4 == whereTitle_q4) and (whereTitle_q4 != wherePageid_q4): #a == b and b!=c  (1,1,2)
                sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (originalTable_q4, pageidTable_q4, pageidTable_q4, queryKey_4, originalTable_q4, pageidTable_q4)
            else:   #a==c and b!=c (1,2,1)
                sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (originalTable_q4, titleTable_q4, originalTable_q4, queryKey_4, originalTable_q4, titleTable_q4)
    else:   #a!=b and a!=c
        if whereTitle_q4 != wherePageid_q4: #a!=b, a!=c, b!=c (1,2,3)
            sql4 = "select original, title from %s, %s, %s where %s.pageid = %s and %s.objId = %s.objId and %s.objId = %s.objId" % (originalTable_q4, titleTable_q4, pageidTable_q4, pageidTable_q4, queryKey_4, originalTable_q4, titleTable_q4, originalTable_q4, pageidTable_q4)
        if whereTitle_q4 == wherePageid_q4:      ##a!=b and a!=c and b==c (2,1,1)
            sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (originalTable_q4, titleTable_q4, titleTable_q4, queryKey_4, originalTable_q4, titleTable_q4)



    # if (originalTable_q4 == titleTable_q4) or (originalTable_q4 == pageidTable_q4):           #a==b or a==c
    #     if titleTable_q4 == pageidTable_q4:      #b==c e.g., (1,1,1)
    #         sql4 = "select original, title from %s where %s.pageid = %s" % (originalTable_q4, originalTable_q4, queryKey_4)
    #     else:
    #         if (originalTable_q4 == titleTable_q4) and (titleTable_q4 != pageidTable_q4): #a == b and b!=c  (1,1,2)
    #             sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (originalTable_q4, pageidTable_q4, pageidTable_q4, queryKey_4, originalTable_q4, pageidTable_q4)
    #         else:   #a==c and b!=c (1,2,1)
    #             sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (originalTable_q4, titleTable_q4, originalTable_q4, queryKey_4, originalTable_q4, titleTable_q4)
    # else:   #a!=b and a!=c
    #     if titleTable_q4 != pageidTable_q4: #a!=b, a!=c, b!=c (1,2,3)
    #         sql4 = "select original, title from %s, %s, %s where %s.pageid = %s and %s.objId = %s.objId and %s.objId = %s.objId" % (originalTable_q4, titleTable_q4, pageidTable_q4, pageidTable_q4, queryKey_4, originalTable_q4, titleTable_q4, originalTable_q4, pageidTable_q4)
    #     if titleTable_q4 == pageidTable_q4:      ##a!=b and a!=c and b==c (2,1,1)
    #         sql4 = "select original, title from %s, %s where %s.pageid = %s and %s.objId = %s.objId" % (originalTable_q4, titleTable_q4, titleTable_q4, queryKey_4, originalTable_q4, titleTable_q4)

    for t_i in range(3):
        time_start4 = time.time()
        cur.execute(sql4)
        time_end4 = time.time()
        query_time4 = time_end4 - time_start4
        middleTime.append(query_time4)

    middleTime.sort()
    totalQueryTime -= middleTime[1]
    recordEachQueryTime.append(middleTime[1])
    # print('query time4', middleTime[1])
    # print('totalQueryTime: ', totalQueryTime)
    middleTime.clear()




    # results = cur.fetchall()  # get the return result
    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/FinalResult/query4.txt", "a+") as f:
    #     for rel in results:
    #         f.write(str(rel)+"\n")
    #     f.write("\n")



    #totalQueryTime += query_time4
    #totalQueryTime -= query_time4
    #print(totalQueryTime)
    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampletimeResult/query4.txt",
    #           "a+") as f:
    #     f.write(str(query_time4) + "\n")



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



    # print(">> query 5:")
    # print(BirthYearTable_q5)
    # print(nsTable_q5)


    sql5 = "select %s.key, birthYear, ns from arrayTable, %s, %s where arrayTable.key = 'normalized' and arrayTable.index = 0 and arrayTable.valStr = 'Sadako_Sasaki' and %s.objId = arrayTable.objId and %s.key = arrayTable.valStr" % (BirthYearTable_q5, BirthYearTable_q5, nsTable_q5, nsTable_q5, BirthYearTable_q5)  # Sadako_Sasaki     Henry_Standing_Bear（example）

    for t_i in range(3):
        time_start5 = time.time()
        cur.execute(sql5)
        time_end5 = time.time()
        query_time5 = time_end5 - time_start5
        middleTime.append(query_time5)

    middleTime.sort()
    totalQueryTime -= middleTime[1]
    recordEachQueryTime.append(middleTime[1])
    # print('query time5', middleTime[1])
    # print('totalQueryTime: ', totalQueryTime)
    middleTime.clear()





    # results = cur.fetchall()  # get the return result
    # with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/FinalResult/query5.txt", "a+") as f:
    #     for rel in results:
    #         f.write(str(rel)+"\n")
    #     f.write("\n")






    #totalQueryTime -= query_time5
    #totalQueryTime += query_time5
    #print(totalQueryTime)
    # with open(
    #         "/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampletimeResult/query5.txt",
    #         "a+") as f:
    #     f.write(str(query_time5) + "\n")




    #append total time
    # recordEachQueryTime.append(-totalQueryTime)
    # schemaQueryTimeTotal[schemaString] = recordEachQueryTime

    #for experimental statistics
    recordEachQueryTime.append(schemaString)
    recordEachQueryTime.insert(0, -totalQueryTime)



    filetotalQueryTimeNamee = '/Users/yuan/PycharmProjects/DemoQLearningMultimodle/Person_dataset/processed_dataset/FinalResult/totalQueryTimeArray' + str(outputExperimentStatisticsFileNo) + '.txt'
    filetotalQueryTime = open(filetotalQueryTimeNamee, 'a+')
    for i in recordEachQueryTime:
        filetotalQueryTime.write(str(i) + '\n')
    filetotalQueryTime.close()



    # results = cur.fetchall()  # get the return result
    #
    # for rel in results:
    #     print(rel)

    # Close the Cursor
    cur.close()

    # conn.close() close database connection
    conn.close()

    return totalQueryTime




####################################################################################################
#                                   step
####################################################################################################
#observation i.e., current state string 1 0 2 0 3 0 4 0 5 0 51 0 52 0 53 0 54 0 55 0 56 0 57
#currentSchema i.e., current schema  #{1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}
#currentTableContent i.e., {1: objId  ns(tuple)， 2: objId original(tuple), ...}

def step(observation, action, currentSchema, currentTableContent, previousQueryTime):

    #we will check whether action space is empty, if it is empty, then this is terminal

    global removeArrayTable
    global noToAttributeDict
    global attributeToNoDict
    global secondRL
    global randomTab
    global done


    currentTableIDs = list(currentSchema.keys())


    if len(currentTableIDs) == 2:               #(randomTable == action, randomTab == removeArrayTable, unfinitely loop)
        s_ = observation
        reward = 0
        done = True
        return s_, reward, currentSchema, currentTableContent, 0


    randomTab = secondRL.secondTable_choose_action(action, currentTableIDs)
    while(randomTab == action or randomTab == removeArrayTable or randomTab not in currentTableIDs):                 #avoid self-join
        randomTab = secondRL.secondTable_choose_action(action, currentTableIDs)



    # randomTab = np.random.choice(currentTableIDs)
    # while(randomTab == action or randomTab == removeArrayTable):                 #avoid self-join
    #     #randomTab = np.random.choice(currentTableIDs)





    # print('act: ', action)
    # print('randomTab: ', randomTab)

    #s_ = None
    #reward = 0
    #test code
    # action = 2
    # randomTab = 1


    # action = 51
    # randomTab = 52

    #
    # action = 5
    # randomTab = 57

    #
    # action = 57
    # randomTab = 5


    #
    # action = 3
    # randomTab = 55

    #
    # action = 72
    # randomTab = 51

    #print(currentSchema)


    ######################################  action < 50 and randomTab < 50 ######################################

    if action < 50 and randomTab < 50:     #both action(attribute) and table are from JSON
        if action == removeArrayTable:
            s_ = observation
            reward = 0
            return s_, reward, currentSchema, currentTableContent, 0
            # currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
            # return s_, reward, currentSchema, currentTableContent


        if action not in currentTableIDs:
            s_ = observation
            reward = 0
            #currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
            return s_, reward, currentSchema, currentTableContent, 0
        else:
            left = currentTableContent[action]
            right = currentTableContent[randomTab]
            currentTableContent[randomTab] = pd.merge(left, right, on='objId', how='outer')
            # print(">>  currentTableContent", currentTableContent[randomTab])

            #update current relational schema
            currentSchema[randomTab].extend(currentSchema[action])
            currentSchema[randomTab].sort()
            del currentSchema[action]
            del currentTableContent[action]
            print(">> currentSchema: ", currentSchema)


            #update observation (state/schema string)
            s_list = []
            temAttriKeys = list(currentSchema.keys())  # [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
            temAttriKeys.sort()
            #print(temAttriKeys)
            for si in temAttriKeys:
                s_list.extend(currentSchema[si])
                s_list.append(0)
            s_list.pop()

            s_ = " ".join('%s' % i for i in s_list)


            #print(">> new state <50 <50 s_: ", s_)

            # currentQueryTime function
            currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)

            reward = currentQueryTime - previousQueryTime

            return s_, reward, currentSchema, currentTableContent, currentQueryTime



    ######################################  action > 50 and randomTab > 50 ######################################


    if action > 50 and randomTab > 50:     #both action(attribute) and random table are from RDF

        if action not in currentTableIDs:
            s_ = observation
            #currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
            reward = 0
            return s_, reward, currentSchema, currentTableContent, 0
        else:
            left = currentTableContent[action]
            right = currentTableContent[randomTab]
            currentTableContent[randomTab] = pd.merge(left, right, on='key', how='outer')
            #print(" >>")
            #print(">>  currentTableContent", currentTableContent[randomTab])

            #update current relational schema
            currentSchema[randomTab].extend(currentSchema[action])
            currentSchema[randomTab].sort()
            del currentSchema[action]
            del currentTableContent[action]
            print(">> currentSchema: ", currentSchema)


            #update observation (state/schema string)
            s_list = []
            temAttriKeys = list(currentSchema.keys())  # [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
            temAttriKeys.sort()
            #print(temAttriKeys)
            for si in temAttriKeys:
                s_list.extend(currentSchema[si])
                s_list.append(0)
            s_list.pop()            #drop the last 0

            s_ = " ".join('%s' % i for i in s_list)


            #print(">> new state >50 >50 s_: ", s_)

            # currentQueryTime function
            currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)

            reward = currentQueryTime - previousQueryTime

            return s_, reward, currentSchema, currentTableContent, currentQueryTime

    ######################################  (action < 50 and randomTab > 50) or (action > 50 and randomTab < 50) ######################################

    if (action < 50 and randomTab > 50) or (action > 50 and randomTab < 50):  # one is from action, another one is from RDF

        if action == removeArrayTable:
            s_ = observation
            #currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
            reward = 0
            return s_, reward, currentSchema, currentTableContent, 0

        if action not in currentTableIDs:
            s_ = observation
            #currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
            reward = 0
            return s_, reward, currentSchema, currentTableContent, 0
        else:

            actionTableName = noToAttributeDict[action]
            randomTabTableName = noToAttributeDict[randomTab]

            if (actionTableName == "title" and randomTabTableName == "title_RDF") or (actionTableName == "title_RDF" and randomTabTableName == "title"):
                left = currentTableContent[action]
                right = currentTableContent[randomTab]
                currentTableContent[randomTab] = pd.merge(left, right, on='title', how='outer')

                # print(" >>")
                # print(">>  currentTableContent", currentTableContent[randomTab])

                # update current relational schema
                currentSchema[randomTab].extend(currentSchema[action])
                currentSchema[randomTab].sort()
                del currentSchema[action]
                del currentTableContent[action]
                print(">> currentSchema: ", currentSchema)

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

                #print(">> new state s_: ", s_)

                # currentQueryTime function
                currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
                reward = currentQueryTime - previousQueryTime

                return s_, reward, currentSchema, currentTableContent, currentQueryTime
            else:   #do not update schema, just get the reward after this action
                s_ = observation
                #currentQueryTime = queryTimeFunctoin(s_, currentSchema, currentTableContent)
                reward = 0
                return s_, reward, currentSchema, currentTableContent, 0






    # s = self.canvas.coords(self.rect)
    # base_action = np.array([0, 0])
    # if action == 0:  # up
    #     if s[1] > UNIT:
    #         base_action[1] -= UNIT
    # elif action == 1:  # down
    #     if s[1] < (MAZE_H - 1) * UNIT:
    #         base_action[1] += UNIT
    # elif action == 2:  # right
    #     if s[0] < (MAZE_W - 1) * UNIT:
    #         base_action[0] += UNIT
    # elif action == 3:  # left
    #     if s[0] > UNIT:
    #         base_action[0] -= UNIT
    #
    # self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent
    #
    # s_ = self.canvas.coords(self.rect)  # next state
    #
    # # reward function
    # if s_ == self.canvas.coords(self.oval):
    #     reward = 1
    #     done = True
    #     s_ = 'terminal'
    # elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2)]:
    #     reward = -1
    #     done = True
    #     s_ = 'terminal'
    # else:
    #     reward = 0
    #     done = False

    #return s_, reward, done, currentSchema, currentTableContent













####################################################################################################
#                                   load JSON files
###################################################################################################
filenames_JSON = []
directoryLocation_JSON = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/initialTablesJSON'
#directoryLocation_JSON = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampleInitialTablesJSON'
os.chdir(directoryLocation_JSON)  # The specified directory

for i in glob.glob("*.csv"):  # take all .csv files in the specified directory
    filenames_JSON.append(i[:-4])  # take file name, but does not include ".csv" suffix
count = len(filenames_JSON)
print('>> local JSON files (initial tables)：', count)
for i in range(0, count):
    print(filenames_JSON[i])

# attribute dict
# 0 is saved to be an interval bit between different tables, so we get the dictionary of attribute,
# and map each attribute to an integer from 1 to n
#{1: 'ns', 2: 'original', 3: 'pageid', 4: 'arrayTable', 5: 'title', 51: 'subject', 52: 'occupation', 53: 'personFunction', 54: 'birthYear', 55: 'birthPlace', 56: 'birthDate', 57: 'title'}
noToAttributeDict = {}

attributeToNoDict = {}
# for i in range(0, count):
#     noToAttributeDict[filenames_JSON[i]] = i + 1


#currentSchema_Initial i.e., current schema  #{1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}
currentSchema_Initial = {}

#{1: objId  ns(tuple)， 2: objId original(tuple), ...}
currentTableContent_Initial = {}

# for i in range(0, count):
#     noToAttributeDict[i + 1] = filenames_JSON[i]            #{1: 'ns', 2: 'original', 3: 'pageid', 4: 'arrayTable', 5: 'title', 51: 'subject', 52: 'occupation', 53: 'personFunction', 54: 'birthYear', 55: 'birthPlace', 56: 'birthDate', 57: 'title'}
#     attributeToNoDict[filenames_JSON[i]] = i + 1
#     currentSchema_Initial[i + 1] = [i + 1]                        #{1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}



######## i starts from 1
i = 1
removeArrayTable = 0
# iterate files
for file_name_JSON in filenames_JSON:
    file = open(directoryLocation_JSON + '/' + file_name_JSON + '.csv', encoding='utf8')
    data_csv = pd.read_csv(file, encoding='utf8mb4')  # use pandas to read csv file
    # print(data_csv.head())

    if file_name_JSON == 'arrayTable':
        removeArrayTable = i

    noToAttributeDict[i] = file_name_JSON            #{1: 'ns', 2: 'original', 3: 'pageid', 4: 'arrayTable', 5: 'title', 51: 'subject', 52: 'occupation', 53: 'personFunction', 54: 'birthYear', 55: 'birthPlace', 56: 'birthDate', 57: 'title'}
    attributeToNoDict[file_name_JSON] = i
    currentSchema_Initial[i] = [i]                        #{1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 51: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57]}
    currentTableContent_Initial[i] = data_csv
    i+=1


    #currentTableContent_Initial[file_name_JSON] = data_csv
    #data_csv.to_sql(name=file_name_JSON, con=engine, if_exists='replace', index=False)


print("JSON read done")







####################################################################################################
#                                   load RDF files
###################################################################################################
filenames_RDF = []
directoryLocation_RDF = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/initialTablesRDF'
#directoryLocation_RDF = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampleInitialTablesRDF'
os.chdir(directoryLocation_RDF)  # The specified directory

for i in glob.glob("*.csv"):  # take all .csv files in the specified directory
    filenames_RDF.append(i[:-4])  # take file name, but does not include ".csv" suffix
count = len(filenames_RDF)
print('>> local RDF files (initial tables)：', count)
for i in range(0, count):
    print(filenames_RDF[i])

# attribute dict
# 0 is saved to be an interval bit between different tables, so we get the dictionary of attribute,
# and map each attribute to an integer from 51 to n (this is used to make a distinction between JSON attributes and RDF attributes)
# for i in range(0, count):
#     if filenames_RDF[i] == 'title':
#         attributeToNoDict['title_RDF'] = i + 51
#     else:
#         attributeToNoDict[filenames_RDF[i]] = i + 51

#
# for i in range(0, count):
#     if filenames_RDF[i] == 'title':
#         noToAttributeDict[i + 51] = 'title_RDF'
#         attributeToNoDict['title_RDF'] = i + 51
#         currentSchema_Initial[i + 51] = [i + 51]
#     else:
#         noToAttributeDict[i + 51] = filenames_RDF[i]
#         attributeToNoDict[filenames_RDF[i]] = i + 51
#         currentSchema_Initial[i + 51] = [i + 51]

# for i in range(0, count):
#     noToAttributeDict[i + 51] = filenames_RDF[i]
#     currentSchema_Initial[i + 51] = [i + 51]




# i starts from 51 for RDF files
i = 51
# iterate files
for file_name_RDF in filenames_RDF:
    file = open(directoryLocation_RDF + '/' + file_name_RDF + '.csv', encoding='utf8')
    data_csv = pd.read_csv(file, encoding='utf8mb4')  # use pandas to read csv file
    # print(data_csv.head())


    if file_name_RDF == 'title':
        noToAttributeDict[i] = 'title_RDF'
        attributeToNoDict['title_RDF'] = i
    else:
        noToAttributeDict[i] = file_name_RDF
        attributeToNoDict[file_name_RDF] = i

    currentSchema_Initial[i] = [i]
    currentTableContent_Initial[i] = data_csv
    i+=1

    # if file_name_RDF == 'title':
    #     currentTableContent_Initial['title_RDF'] = data_csv
    #     #data_csv.to_sql(name='title_RDF', con=engine, if_exists='replace', index=False)
    #     continue
    # currentTableContent_Initial[file_name_RDF] = data_csv
    # #data_csv.to_sql(name=file_name_RDF, con=engine, if_exists='replace', index=False)

print('>> the size of attribute dictionary is: ', len(noToAttributeDict), ', whose content is')
print(noToAttributeDict)

print('>> the size of attributeToNoDict is: ', len(attributeToNoDict), ', whose content is')
print(attributeToNoDict)

print('>> the size of currentSchema_Initial is: ', len(currentSchema_Initial), ', whose content is')
print(currentSchema_Initial)


print('>> the ID of arratyTable is: ', removeArrayTable)


#print(removeArrayTable)


#print('>> the number of tables is: ', len(currentTableContent_Initial), ', whose content is')
# print(currentTableContent_Initial)

# initial state e.g., [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 51, 0, 52, 0, 53, 0, 54, 0, 55, 0, 56, 0, 57]
initialState = []
allAttr = list(noToAttributeDict.keys())  # [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
# print(allAttr)
for i in range(0, len(allAttr)):
    initialState.append(allAttr[i])
    initialState.append(0)

initialState.pop()  # remove the last 0

observation_ini = " ".join('%s' %i for i in initialState)

#print(">> initialState", initialState)



####################################################################################################
#
###################################################################################################

RL = QLearningTable(actions=allAttr)
secondRL = QLearningTable(actions=allAttr)

randomTab = 0

for episode in range(100):

    break






    # fresh

    # initial observation(state) string 1 0 2 0 3 0 4 0 5 0 51 0 52 0 53 0 54 0 55 0 56 0 57
    observation = str(observation_ini)
    #print(">> initial observation: ", observation)

    # action space [1, 2, 3, 4, 5, 51, 52, 53, 54, 55, 56, 57]
    action_space = copy.deepcopy(allAttr)



    #currentSchema_Initial
    currentSchema = copy.deepcopy(currentSchema_Initial)


    # print('>>  currentSchema copy:')
    # print(currentSchema)

    #currentTableContent_Initia
    currentTableContent = copy.deepcopy(currentTableContent_Initial)

    # print('>>  currentTableContent copy:')
    # print(currentTableContent.keys())


    #we do not consider JSON array to join
    action_space.remove(removeArrayTable)


    #record the previous query timee
    previousQueryTime = 0

    while True:

        # RL choose action based on observation
        # In our situation, action space is Real-time changing
        # After choosing one action (one attribute), this action will be removed from action space.
        action, action_space, done = RL.choose_action(observation, action_space)

        # # RL take action and current state (observation) to get next observation and reward
        observation_, reward, currentSchema, currentTableContent, currentQueryTime = step(observation, action, currentSchema, currentTableContent, previousQueryTime)



        # # RL learn from this transition
        # maxExpectedValue = RL.learn(observation, action, reward, observation_, done)
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
        secondRL.secondTableLearn(action, randomTab, reward, maxExpectedValue)

        #
        # # swap observation
        observation = observation_

        if reward != 0:
            previousQueryTime = currentQueryTime
        #currentTableContent = currentTableContent_

        # break while loop when end of this episode
        if done:
            break

    # end of game
    print('>> finish one episode')
    outputExperimentStatisticsFileNo +=1





