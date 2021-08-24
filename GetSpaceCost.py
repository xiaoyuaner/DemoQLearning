import copy
import glob
import os







###################################################################################################
#                                   load JSON files
###################################################################################################
import re

import MySQLdb
import pandas as pd
from sqlalchemy import create_engine

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



#currentSchema_Initial
currentSchema = copy.deepcopy(currentSchema_Initial)


# print('>>  currentSchema copy:')
# print(currentSchema)

#currentTableContent_Initia
currentTableContent = copy.deepcopy(currentTableContent_Initial)




###################################################################################################
#                                   load relational schema
###################################################################################################

fileSchema = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/experimental result in paper/OptimalTime12.txt'
fileRead = open(fileSchema, encoding='utf8')
lines = fileRead.readlines()


schamaString = lines[6]
#schamaString ='1 0 2 0 3 0 4 0 5 0 54 0 56 0 58 0 59 0 53 62 0 63 0 55 61 67 70 0 68 76 0 69 0 72 0 74 86 0 51 71 75 79 0 77 0 81 0 82 0 66 78 83 85 0 84 0 87 0 88 0 89 0 65 73 91 0 52 64 90 92 0 57 93 0 95 0 96 0 60 97 0 80 94 98'



schemaArray = re.split(r'\s[0]\s', schamaString)
#['1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 54 ', ' 56 ', ' 58 ', ' 59 ', ' 53 62 ', ' 63 ', ' 55 61 67 7', ' ', ' 68 76 ', ' 69 ', ' 72 ', ' 74 86 ', ' 51 71 75 79 ', ' 77 ', ' 81 ', ' 82 ', ' 66 78 83 85 ', ' 84 ', ' 87 ', ' 88 ', ' 89 ', ' 65 73 91 ', ' 52 64 9', ' 92 ', ' 57 93 ', ' 95 ', ' 96 ', ' 6', ' 97 ', ' 8', ' 94 98']
# print(schemaArray)

i = 0
while(i < len(schemaArray)):
    schemaArray[i] = schemaArray[i].strip()
    i += 1

#['1', '2', '3', '4', '5', '54', '56', '58', '59', '53 62', '63', '55 61 67 7', '', '68 76', '69', '72', '74 86', '51 71 75 79', '77', '81', '82', '66 78 83 85', '84', '87', '88', '89', '65 73 91', '52 64 9', '92', '57 93', '95', '96', '6', '97', '8', '94 98']
#print(schemaArray)


i = 0
while(i < len(schemaArray)):
    actions = schemaArray[i].split(' ')
    if len(actions) > 1:
        leftIndex = 0
        rightIndex = 1
        while(rightIndex < len(actions)):

            if int(actions[leftIndex]) < 50 and int(actions[rightIndex]) < 50:
                left = currentTableContent[int(actions[leftIndex])]
                right = currentTableContent[int(actions[rightIndex])]
                currentTableContent[int(actions[leftIndex])] = pd.merge(left, right, on='objId', how='outer')
                # print(">>  currentTableContent", currentTableContent[randomTab])

                # update current relational schema
                currentSchema[int(actions[leftIndex])].extend(currentSchema[int(actions[rightIndex])])
                currentSchema[int(actions[leftIndex])].sort()
                del currentSchema[int(actions[rightIndex])]
                del currentTableContent[int(actions[rightIndex])]
                print(">> currentSchema: ", currentSchema)

            if int(actions[leftIndex]) > 50 and int(actions[rightIndex]) > 50:
                left = currentTableContent[int(actions[leftIndex])]
                right = currentTableContent[int(actions[rightIndex])]
                currentTableContent[int(actions[leftIndex])] = pd.merge(left, right, on='key', how='outer')
                # print(">>  currentTableContent", currentTableContent[randomTab])

                # update current relational schema
                currentSchema[int(actions[leftIndex])].extend(currentSchema[int(actions[rightIndex])])
                currentSchema[int(actions[leftIndex])].sort()
                del currentSchema[int(actions[rightIndex])]
                del currentTableContent[int(actions[rightIndex])]
                print(">> currentSchema: ", currentSchema)

            if (int(actions[leftIndex]) < 50 and int(actions[rightIndex]) > 50) or (int(actions[leftIndex]) > 50 and int(actions[rightIndex]) < 50):
                left = currentTableContent[int(actions[leftIndex])]
                right = currentTableContent[int(actions[rightIndex])]
                currentTableContent[int(actions[leftIndex])] = pd.merge(left, right, on='title', how='outer')
                # print(">>  currentTableContent", currentTableContent[randomTab])

                # update current relational schema
                currentSchema[int(actions[leftIndex])].extend(currentSchema[int(actions[rightIndex])])
                currentSchema[int(actions[leftIndex])].sort()
                del currentSchema[int(actions[rightIndex])]
                del currentTableContent[int(actions[rightIndex])]
                print(">> currentSchema: ", currentSchema)

            rightIndex += 1
    #print(a)
    i += 1








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




