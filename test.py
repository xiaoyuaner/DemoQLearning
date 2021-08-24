# # creat connecting
# import MySQLdb
#
# conn = MySQLdb.connect(
#         host='localhost',  # your MySQL service address
#         port=3306,  # port
#         user='root',  # visiting database service's user name and password
#         passwd='1',
#         db='QLearning',  # database name
#         charset='utf8mb4'  # for chinese
#     )
# cur = conn.cursor()
#
# subjectTable_q2 = 'subject'
#
# sql2 = "select %s.subject from %s where %s.key = 'Tor_Ahlsand';" % (subjectTable_q2, subjectTable_q2, subjectTable_q2)
#
#
#
# cur.execute(sql2)
#
#
# results = cur.fetchall()  # get the return result
#
# for rel in results:
#     print(rel)
#
# # Close the Cursor
# cur.close()
#
#
# # conn.close() close database connection
# conn.close()




#
# f = open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/FinalResult/totalQueryTimeArray0.txt")
# lines = f.readlines()
# print(lines[0])
# for line in lines:
#     print (line)
#     print(type(line))
#     break
# f.close()

#
# # creat connecting
# import MySQLdb
#
# conn = MySQLdb.connect(
#     host='localhost',  # your MySQL service address
#     port=3306,  # port
#     user='root',  # visiting database service's user name and password
#     passwd='1',
#     # db='QLearning',  # database name
#     charset='utf8mb4'  # for chinese
# )
# cur = conn.cursor()
#
# sql_space = "select sum(DATA_LENGTH)+sum(INDEX_LENGTH) from information_schema.tables where table_schema='QLearning';"
# cur.execute(sql_space)
# results = str(cur.fetchone())  # get the return result
#
# # results = cur.fetchall()  # get the return result
# # displayResults = ""
# # for rel in results:
# #     displayResults = displayResults + str(rel) + '\n'
#
#
# print(results[1:-2])
#         #self.modifyui.plainTextEdit_SpaceConsumption.setPlainText('{}'.format(displayResults))
# cur.close()

#query3_tmp[i]

query3_tmp = ['sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s where %s.key = \'Heath_Ledger\'" % (birthDateTable_q3, birthDateTable_q3)', 'sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s where %s.key = \'Heath_Ledger\' and %s.key = %s.key" % (birthDateTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsEndYearTable_q3)', 'sql3 = "select birthDate, activeYearsStartYear, activeYearsEndYear from %s, %s, %s where %s.key = \'Heath_Ledger\' and %s.key = %s.key and %s.key = %s.key" % (birthDateTable_q3, activeYearsStartYearTable_q3, activeYearsEndYearTable_q3, birthDateTable_q3, birthDateTable_q3, activeYearsStartYearTable_q3, birthDateTable_q3, activeYearsEndYearTable_q3)']
i = 0
for q in query3_tmp:
     aTemp= q[7:]
     print(aTemp)

