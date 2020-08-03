import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140'
DOWNLOAD_DIR = 'D:\\Users\\Jean-Pierre\\Downloads'

playlist = Playlist('https://www.youtube.com/playlist?list=PLzwWSJNcZTMSW-v1x6MhHFKkwrGaEgQ-L')
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
	print(url)

for video in playlist.videos:
	audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
	audioStream.download(output_path=DOWNLOAD_DIR)
