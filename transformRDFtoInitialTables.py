import pandas as pd
import numpy as np


#generate example
# data = pd.read_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personGraph.csv')
# print(data.head(30))
# data.head(30).to_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/retordfexample.csv', index=False)



# print(data.loc[0:2])




# data_csv_RDF = pd.read_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/retordfexample.csv')[1:]

data_csv_RDF = pd.read_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personGraph.csv')[1:]

print('The top 3 tuples in data:', data_csv_RDF.head(3))
print('The number of triples:', data_csv_RDF.shape[0])

#tupleKey = data_csv_RDF['s'].array.unique()
#print(tupleKey)

attrs_RDF = data_csv_RDF['p'].array.unique()
#print(attrs_RDF)
print('The size of attributes:', attrs_RDF.size)



iniTablesDict_RDF = dict.fromkeys(attrs_RDF)
print('The number of initial tables:', len(iniTablesDict_RDF))
#print(iniTablesDict_RDF)

for a in attrs_RDF:
    #print(a)
    attrsInEachTable = ['key']
    attrsInEachTable.append(a)
    tab = pd.DataFrame(columns=attrsInEachTable)
    iniTablesDict_RDF[a] = tab
    #print(tab)



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
    #print(iniTablesDict_RDF)
    #print(sv, pv, ov)
    #break

#print(iniTablesDict_RDF)
#print(iniTablesDict_RDF['subject'])


for a in attrs_RDF:
    #iniTablesDict_RDF[a].to_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/exampleInitialTablesRDF/' + a + '.csv', index=False)
    iniTablesDict_RDF[a].to_csv(
        '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/initialTablesRDF/' + a + '.csv',
        index=False)









# listTables.append('Google')
# listTables.append('Runoob')
#
# initialTable = pd.DataFrame(columns=attr, index=tupleKey)
# print(initialTable)




















# data = pd.read_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personGraph.csv')
#
# data.to_csv('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personGraphInitialTable.csv')





















# create list of DataFrame
# listTables = []
#
# for a in attrs_RDF:
#     #print(a)
#     attrsInEachTable = ['key']
#     attrsInEachTable.append(a)
#     tab = pd.DataFrame(columns=attrsInEachTable)
#     listTables.append(tab)
#     #print(tab)
#     #print(listTables)
#
#
# print(len(listTables))
