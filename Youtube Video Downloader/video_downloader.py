from pytube import YouTube

link = input("Enter a YouTube video URL: ")
yt = YouTube(link)
mp4_file = yt.streams.filter(file_extension="mp4")
video_resolution = mp4_file.get_highest_resolution()

try:
  video_resolution.download(r"C:\Users\based\Videos\YouTube Videos")
  print("The video has been successfully downloaded!")
except:
  print("An error has been occurred.")