from pytube import YouTube

class youtubeDetail:
  channel = ''
  title = ''
  length = 0

  @classmethod
  def getVideoDetail(cls, url):
    # video = YouTube(youtubeDetail.url)
    video = YouTube(url)
    youtubeDetail.channel = video.author
    youtubeDetail.title = video.title
    youtubeDetail.length = video.length
    # # channel name
    # print('channel:',video.author)
    # # title
    # print('title:',video.title)
    # # length
    # print('length:',video.length)
    return [ video.author, video.title, video.length ]

