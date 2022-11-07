from pytube import YouTube
import pandas as pd
'''
1 - get data from main 
2 - turn into dataframe by pandas
3 - turn dataframe into csv file and save that csv file
'''

class CsvHandle:
  
  data_ditionary = {}
  list_data = []

  @classmethod
  def HandleInfomation(cls, listInfo):
    for i in range(len(listInfo)):
      CsvHandle.data_ditionary[i] = listInfo[i]
    youtubeData = pd.DataFrame(data = CsvHandle.data_ditionary)
    youtubeData.to_csv('news.csv')

  def handle_one_informatio(self, info):
    self.list_data.append(info)
    if(len(self.list_data) == 20):
      CsvHandle.createCsv()
    # print(self.list_data)

  def createCsv():
    CsvHandle.HandleInfomation(CsvHandle.list_data)
    print('done createCsv')

  def showInfo(self):
    print('show info function', self.data_ditionary)



