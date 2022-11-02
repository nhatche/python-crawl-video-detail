from pytube import YouTube

'''
1 - get data from main 
2 - turn into dataframe by pandas
3 - turn dataframe into csv file and save that csv file
'''

class csvHandle:
  
  dataDictionary = None 

  @classmethod
  def HandleInfomation(cls, listInfo):
    for i in range(len(listInfo)):
      csvHandle.dataDictionary[i] = listInfo[i]
      print('dataDictionary', csvHandle.dataDictionary)


