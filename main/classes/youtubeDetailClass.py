from pytube import YouTube

class YoutubeDetail:
  channel = ''
  title = ''
  length = 0

  @classmethod
  def getVideoDetail(cls, url):
    video = YouTube(url)
    YoutubeDetail.channel = video.author
    YoutubeDetail.title = video.title
    YoutubeDetail.length = video.length
  
    return [ video.author, video.title, video.length ]

