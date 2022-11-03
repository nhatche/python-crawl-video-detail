from pytube import YouTube
import pandas as pd
'''
1 - get data from main 
2 - turn into dataframe by pandas
3 - turn dataframe into csv file and save that csv file
'''

class csvHandle:
  
  dataDictionary = {}

  @classmethod
  def HandleInfomation(cls, listInfo):
    for i in range(len(listInfo)):
      csvHandle.dataDictionary[i] = listInfo[i]
    youtubeData = pd.DataFrame(data = csvHandle.dataDictionary)
    youtubeData.to_csv('news.csv')

  def showInfo(self):
    print(self.dataDictionary)



