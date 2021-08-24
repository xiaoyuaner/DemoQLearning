import glob
import os
import time

time_start = time.time()
filenames_TXT = []
directoryLocation_TXT = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/FinalResult'
os.chdir(directoryLocation_TXT)  # The specified directory

for i in glob.glob("*.txt"):  # take all .csv files in the specified directory
    filenames_TXT.append(i[19:-4])  # take file name, but does not include ".csv" suffix
count = len(filenames_TXT)
print('>> local result files：', count)
for i in range(0, count):
    print(filenames_TXT[i])





resultDict = {}

resultTimeArray = [None] * 100

# iterate files
for file_name_txt in filenames_TXT:
    file = open(directoryLocation_TXT + '/totalQueryTimeArray' + file_name_txt + '.txt', encoding='utf8')
    print(">>", file_name_txt)
    lines = file.readlines()
    localOptimal = [None] * 7
    if (len(lines) > 7):
        localOptimal[0] = lines[0]
        localOptimal[1] = lines[1]
        localOptimal[2] = lines[2]
        localOptimal[3] = lines[3]
        localOptimal[4] = lines[4]
        localOptimal[5] = lines[5]
        localOptimal[6] = lines[6]

    count = 0
    while(count < len(lines)):
        tempTotalTime = lines[count]
        #print(count)
        if float(tempTotalTime) < float(localOptimal[0]):
            j = 0
            while(j < 7):
                localOptimal[j] = lines[count+j]
                j += 1
            count += 7
        else:
            count += 7
    file.close()


    #
    # fileOutputTime = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/experimental result in paper/drawFigureTime.txt'
    # fileOutDrawFigureTime = open(fileOutputTime, 'a+')
    # fileOutDrawFigureTime.write(file_name_txt + ' ' + localOptimal[0])
    # fileOutDrawFigureTime.close()

    resultTimeArray[int(file_name_txt)] = localOptimal[0]

    resultDict[file_name_txt] = localOptimal.copy()

    localOptimal.clear()
    lines.clear()



fileOutputTime = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/experimental result in paper/drawFigureTime.txt'
fileOutDrawFigureTime = open(fileOutputTime, 'a+')
j = 0
while (j < len(resultTimeArray)):
    fileOutDrawFigureTime.write(str(j) + ' ' + resultTimeArray[j])
    j += 1
fileOutDrawFigureTime.close()




###########find optimal schema
fileKey = ''
optimalOne = [100]
for key, value in resultDict.items():
    if(float(value[0]) < float(optimalOne[0])):
        optimalOne = value.copy()
        fileKey = key



fileOutputOptimal = '/Users/yuan/PycharmProjects/QLearningMultimodle/Person_dataset/processed_dataset/experimental result in paper/OptimalTime' + fileKey + '.txt'
fileOptimalTime = open(fileOutputOptimal, 'a+')
for i in optimalOne:
    fileOptimalTime.write(str(i))
fileOptimalTime.close()


time_end = time.time()
print(">> time:", time_end - time_start)







