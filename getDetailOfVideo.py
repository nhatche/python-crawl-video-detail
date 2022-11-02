from pytube import YouTube

'''
Lấy tên của kênh tên của video youtube, thời gian chạy của video, số comment, số lượt like cuaủa video
'''

video = YouTube('https://www.youtube.com/watch?v=HCjNJDNzw8Y')

print('video channel',video.author)
print('video title',video.title)
print('video length',video.length)
print('video comments number',video.length)
print('video likes number',video.likes)