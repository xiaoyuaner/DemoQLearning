
import jsonlines
import json

import numpy as np
import pandas as pd

arrayTable = pd.DataFrame(columns=['objId', 'key', 'index', 'valStr'])

attrs = ['pageid', 'ns', 'title', 'original']
iniTablesDict = dict.fromkeys(attrs)
for a in attrs:
    attrsInEachTable = ['objId']
    attrsInEachTable.append(a)
    tab = pd.DataFrame(columns=attrsInEachTable)
    iniTablesDict[a] = tab



print('The initial array table:', len(arrayTable))
print('The number of initial tables:', len(iniTablesDict))

# print(arrayTable)
# print(iniTablesDict)




objIdtemp = 0

with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personCleaned.json', 'r+') as readfile:
#with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/JSONcleanExample.json', 'r') as readfile:
    for obj in jsonlines.Reader(readfile):
        #print(obj['normalized'][0]['from'])


        #constructJSONobject = {}
        #tabTemp = tabTemp.append({'key': sv, pv: ov}, ignore_index=True)



        if obj.__contains__('normalized'):
            # print(obj['normalized'][0])
            # print(obj['normalized'][1])

            try:
                #obj['normalized'][0]
                arrayTable = arrayTable.append({'objId': objIdtemp, 'key': "normalized", 'index': 0,
                                                'valStr': obj['normalized'][0]}, ignore_index=True)
            except IndexError:
                pass


            try:
                #obj['normalized'][1]
                arrayTable = arrayTable.append({'objId': objIdtemp, 'key': "normalized", 'index': 1,
                                                'valStr': obj['normalized'][1]}, ignore_index=True)
            except IndexError:
                pass

    #print(arrayTable)

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



        objIdtemp+=1

#    print(iniTablesDict)





for a in attrs:
    #iniTablesDict[a].to_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampleInitialTablesJSON/' + a + '.csv', index=False)
     iniTablesDict[a].to_csv(
        '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/initialTablesJSON/' + a + '.csv',
        index=False)



arrayTable.to_csv(
    '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/initialTablesJSON/arrayTable.csv',
    index=False)



#
# arrayTable.to_csv(
#     '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampleInitialTablesJSON/arrayTable.csv',
#     index=False)




























        # if obj.__contains__('normalized'):
        #     print(obj['normalized'][0]['from'])
        #     print(obj['normalized'][0]['to'])
        #
        #     if obj['normalized'][0].__contains__('from'):
        #         arrayTable = arrayTable.append({'objId': objIdtemp, 'key': "normalized[0].from", 'index': None,
        #                                         'valStr': obj['normalized'][0]['from']}, ignore_index=True)
        #     if obj['normalized'][0].__contains__('to'):
        #         arrayTable = arrayTable.append({'objId': objIdtemp, 'key': "normalized[0].to", 'index': None,
        #                                         'valStr': obj['normalized'][0]['to']}, ignore_index=True)
        # print(arrayTable)



# # parse the nested JSON, one layer at a time
# def json_to_columns(df,col_name):
#     for i in df[col_name][0].keys():         # 对dict的第一层key进行循环
#         list2=[j[i] for j in df[col_name]]   # 存储对应上述key的value至列表推导式
#         df[i]=list2                          # 存储到新的列中
#     df.drop(col_name,axis=1,inplace=True)    # 删除原始列
#     return df
#
# ### terate through the dataframe, processing all columns whose value type is dict
# def json_parse(df):
#     for i in df.keys():
#         if type(df[i][0])==dict and df[i][0]!={}:
#             df=json_to_columns(df,i)   #recall the previous function
#     return df
#
# ### Processes columns of value type List and converts them to dict
# def list_parse(df):
#     for i in df.keys():
#         if type(df[i][0])==list and df[i][0]!=[]:
#             list1=[j[0] if j!=[] else np.nan for j in df[i]]
#             df[i]=list1
#     return df

