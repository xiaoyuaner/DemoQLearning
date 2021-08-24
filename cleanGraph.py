import re
import csv

#
# count = 1
#
# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/person.graph','r') as readf:
#     for line in readf:
#         if count < 10:
#             newLine = re.split(r'[\s]+', line.strip())
#             str = " ".join(newLine)
#             print(str)
#             count+=1
#             outf = open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/graphsampleList.txt', 'a+')
#
#             outf.write(str)
#             outf.write('\n')
#             outf.close()


# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/graphsampleList.csv', 'a+') as csvfile:
#     writer = csv.writer(csvfile)
#     # 先写入columns_name
#     writer.writerow(["s", "p", "o"])
#
#
#
# total=0
# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/person.graph',
#           'r') as readf:
#     for line in readf:
#         if total < 10:
#             newLine = re.split(r'[\s]+', line.strip())
#             print(newLine)
#             with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/graphsampleList.csv',
#                   'a+') as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow(newLine)
#             total += 1
#
# print(total)




# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personCleaned.csv', 'a+') as csvfile:
#     writer = csv.writer(csvfile)
#     # 先写入columns_name
#     writer.writerow(["s", "p", "o"])
#
#
#
# total=0
# with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/person.graph',
#           'r') as readf:
#     for line in readf:
#         newLine = re.split(r'[\s]+', line.strip())
#
#         with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personCleaned.csv',
#                   'a+') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(newLine)
#
#         total+=1
#
#
# print(total)


with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personCleaned.tsv', 'a+', newline='') as tsvfile:
    tsv_output = csv.writer(tsvfile, delimiter='\t')
    tsv_output.writerow(["s", "p", "o"])





total=0
with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/person.graph',
          'r') as readf:
    for line in readf:
        newLine = re.split(r'[\s]+', line.strip())

        with open('/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/personCleaned.tsv',
                  'a+', newline='') as tsvfile:
            tsv_output = csv.writer(tsvfile, delimiter='\t')
            tsv_output.writerow(newLine)

        total+=1
        # if total == 10:
        #     break


print(total)