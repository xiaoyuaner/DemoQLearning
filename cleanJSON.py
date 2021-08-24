

# Opening JSON file
# returns JSON object as
# a dictionary
# with open("/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/person.json", 'r') as f:
#     data = json.load(f)
#     print(data)


import jsonlines
import json



# class Person:
#     def __init__(self, normalized, pageid, ns, title, original):
#         self.normalized = normalized
#         self.pageid = pageid
#         self.ns = ns
#         self.title = title
#         self.original = original
#
# def personDecoder(obj):
#         return Person(obj['query']['normalized'], list(obj['query']['pages'].values())[0]['pageid'], list(obj['query']['pages'].values())[0]['ns'], list(obj['query']['pages'].values())[0]['title'], list(obj['query']['pages'].values())[0]['thumbnail']['original'])


# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/try.json', 'r+') as f:
#     for item in jsonlines.Reader(f):
#         content = personDecoder(item)
#         print(content)





######################################################################################################################

# results = []
#
#
# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/try.json', 'r+') as f:
#     for obj in jsonlines.Reader(f):
#         constructJSONobject = {}
#         constructJSONobject['normalized'] = obj['query']['normalized']
#         constructJSONobject['pageid'] = list(obj['query']['pages'].values())[0]['pageid']
#         constructJSONobject['ns'] = list(obj['query']['pages'].values())[0]['ns']
#         constructJSONobject['title'] = list(obj['query']['pages'].values())[0]['title']
#         constructJSONobject['original'] = list(obj['query']['pages'].values())[0]['thumbnail']['original']
#
#
#         print(obj)
#
#         if obj['query'].__contains__('normalized'):
#             print("a")
#         print(obj['query']['normalized'])
#         print(list(obj['query']['pages'].values())[0]['pageid'])
#         print(list(obj['query']['pages'].values())[0]['ns'])
#         print(list(obj['query']['pages'].values())[0]['title'])
#         print(list(obj['query']['pages'].values())[0]['thumbnail']['original'])
#
#         results.append(constructJSONobject)
#
#
#
# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/data.json', 'w') as outfile:
#     json.dump(results, outfile)
#######################################################################################################################









#
# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/try.json', 'r+') as readfile:
#     for obj in jsonlines.Reader(readfile):
#         constructJSONobject = {}
#         constructJSONobject['normalized'] = obj['query']['normalized']
#         constructJSONobject['pageid'] = list(obj['query']['pages'].values())[0]['pageid']
#         constructJSONobject['ns'] = list(obj['query']['pages'].values())[0]['ns']
#         constructJSONobject['title'] = list(obj['query']['pages'].values())[0]['title']
#         constructJSONobject['original'] = list(obj['query']['pages'].values())[0]['thumbnail']['original']
#
#
#
#         with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/data.json', 'a+') as outfile:
#             json.dump(constructJSONobject, outfile)
#             outfile.write('\n')

########################################################################################################################






# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/person.json', 'r+') as readfile:
#     for obj in jsonlines.Reader(readfile):
#         constructJSONobject = {}
#
#         if obj['query'].__contains__('normalized'):
#             constructJSONobject['normalized'] = obj['query']['normalized']
#
#         if list(obj['query']['pages'].values())[0].__contains__('pageid'):
#             constructJSONobject['pageid'] = list(obj['query']['pages'].values())[0]['pageid']
#
#         if list(obj['query']['pages'].values())[0].__contains__('ns'):
#             constructJSONobject['ns'] = list(obj['query']['pages'].values())[0]['ns']
#
#         if list(obj['query']['pages'].values())[0].__contains__('title'):
#             constructJSONobject['title'] = list(obj['query']['pages'].values())[0]['title']
#
#         if list(obj['query']['pages'].values())[0].__contains__('thumbnail'):
#             constructJSONobject['original'] = list(obj['query']['pages'].values())[0]['thumbnail']['original']
#
#
#
#         with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personCleaned.json', 'a+') as outfile:
#             json.dump(constructJSONobject, outfile)
#             outfile.write('\n')


# result:
# {"normalized": [{"from": "Henry_Standing_Bear", "to": "Henry Standing Bear"}], "pageid": 43757531, "ns": 0, "title": "Henry Standing Bear", "original": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Henry_Standing_Bear3.png"}
# {"normalized": [{"from": "Ern\u0151_Rubik", "to": "Ern\u0151 Rubik"}], "pageid": 335331, "ns": 0, "title": "Ern\u0151 Rubik", "original": "https://upload.wikimedia.org/wikipedia/commons/6/66/Erno_Rubik_Genius_Gala_2014.jpg"}




with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/raw/person.json', 'r+') as readfile:
#with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/try.json', 'r+') as readfile:
    for obj in jsonlines.Reader(readfile):
        constructJSONobject = {}

        if obj['query'].__contains__('normalized'):
            arrayLt = []
            if obj['query']['normalized'][0].__contains__('from'):
                arrayLt.append(obj['query']['normalized'][0]['from'])

            if obj['query']['normalized'][0].__contains__('to'):
                arrayLt.append(obj['query']['normalized'][0]['to'])

            constructJSONobject['normalized'] = arrayLt

        if list(obj['query']['pages'].values())[0].__contains__('pageid'):
            constructJSONobject['pageid'] = list(obj['query']['pages'].values())[0]['pageid']

        if list(obj['query']['pages'].values())[0].__contains__('ns'):
            constructJSONobject['ns'] = list(obj['query']['pages'].values())[0]['ns']

        if list(obj['query']['pages'].values())[0].__contains__('title'):
            constructJSONobject['title'] = list(obj['query']['pages'].values())[0]['title']

        if list(obj['query']['pages'].values())[0].__contains__('thumbnail'):
            constructJSONobject['original'] = list(obj['query']['pages'].values())[0]['thumbnail']['original']



        with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personCleaned.json', 'a+') as outfile:
        # with open(
        #         '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/various code examples/JSONcleanExample.json',
        #         'a+') as outfile:
            json.dump(constructJSONobject, outfile)
            outfile.write('\n')




