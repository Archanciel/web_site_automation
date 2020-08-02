# pip install pytube3
from pytube import YouTube
import re, os

YOUTUBE_STREAM_AUDIO = '140'

if os.name == 'posix':
	CONVERT = False
	DOWNLOAD_DIR = '/storage/emulated/0/Download'
else:
	CONVERT = False # can be set to True
	DOWNLOAD_DIR = 'D:\\Users\\Jean-Pierre\\Downloads'

# download a file with only audio, to save space
# if the final goal is to convert to mp3
#youtubeLink = 'https://youtu.be/nII-KRCER4E' "Occe Nach"
youtubeLink = 'https://youtu.be/5SLERnIOr7g' "Marie de Solemne"
youTubeVideo = YouTube(youtubeLink)
audioStream = youTubeVideo.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
audioStream.download(output_path=DOWNLOAD_DIR)

for file in [n for n in os.listdir(DOWNLOAD_DIR) if re.search('mp4', n)]:
	fullPath = os.path.join(DOWNLOAD_DIR, file)
	outputPath = os.path.join(DOWNLOAD_DIR, os.path.splitext(file)[0] + '.mp3')

	if CONVERT:
		import moviepy.editor as mp  # not working on Android
	#	clip = mp.AudioFileClip(full_path).subclip(10, )  # disable if do not want any clipping
		clip = mp.AudioFileClip(fullPath)
		clip.write_audiofile(outputPath)
	else:
		os.rename(fullPath, outputPath)
