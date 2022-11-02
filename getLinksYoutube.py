from pytube import Playlist

playlists_url = 'https://youtube.com/playlist?list=PLEOpjQfxLxYqThXVDdbldCPGnyTYuZpwU'

playlist = Playlist(playlists_url)

for video in playlist.video_urls:
  print(video)

'''
20 url

https://www.youtube.com/watch?v=JGwWNGJdvx8
https://www.youtube.com/watch?v=HCjNJDNzw8Y
https://www.youtube.com/watch?v=k2qgadSvNyU
https://www.youtube.com/watch?v=lp-EO5I60KA
https://www.youtube.com/watch?v=OPf0YbXqDm0
https://www.youtube.com/watch?v=RgKAFK5djSk
https://www.youtube.com/watch?v=3tmd-ClpJxA
https://www.youtube.com/watch?v=09R8_2nJtjg
https://www.youtube.com/watch?v=60ItHLz5WEA
https://www.youtube.com/watch?v=rtOvBOTyX00
https://www.youtube.com/watch?v=NGLxoKOvzu4
https://www.youtube.com/watch?v=papuvlVeZg8
https://www.youtube.com/watch?v=3AtDnEC4zak
https://www.youtube.com/watch?v=Io0fBr1XBUA
https://www.youtube.com/watch?v=pRpeEdMmmQ0
https://www.youtube.com/watch?v=hT_nvWreIhg
https://www.youtube.com/watch?v=ALZHF5UqnU4
https://www.youtube.com/watch?v=wIft-t-MQuE
https://www.youtube.com/watch?v=LjhCEhWiKXk
https://www.youtube.com/watch?v=fLexgOxsZu0
'''