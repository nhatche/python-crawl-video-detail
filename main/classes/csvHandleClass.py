from pytube import YouTube
import pandas as pd
'''
1 - get data from main 
2 - turn into dataframe by pandas
3 - turn dataframe into csv file and save that csv file
'''

class csvHandle:
  
  dataDictionary = {}
  maxKeyDict = 0
  listData = []

  @classmethod
  def HandleInfomation(cls, listInfo):
    for i in range(len(listInfo)):
      csvHandle.dataDictionary[i] = listInfo[i]
    youtubeData = pd.DataFrame(data = csvHandle.dataDictionary)
    youtubeData.to_csv('news.csv')

  def HandleOneInfomation(self, info):
    # maxKey = max([*csvHandle.dataDictionary]) if len(csvHandle.dataDictionary) >0 else 0
    # maxKey = csvHandle.maxKeyDict
    # print('info',info)
    # print('maxkey',maxKey)
    # print('dataDictionary',csvHandle.dataDictionary)
    # csvHandle.dataDictionary[maxKey] = info
    # csvHandle.maxKeyDict = maxKey + 1
    self.listData.append(info)
    if(len(self.listData) == 20):
      csvHandle.createCsv()
    print(self.listData)

  def createCsv():
    csvHandle.HandleInfomation(csvHandle.listData)
    print('done createCsv')

  def showInfo(self):
    print('show info function', self.dataDictionary)



