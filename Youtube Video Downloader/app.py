from pytube import YouTube

url = input("Enter the youtube link URL: ")
yt = YouTube(url) #Fetch the video

print(f"Title: {yt.title}")
videos = yt.streams

#Enumerate the fetched video and print it out.
for i,video in enumerate(videos):
    print(f"{str(i)} {str(video)}")

num = int(input("Enter your choice: ")) #For video formats/sizes
video = videos[num] #Get the required video format/size

print("Downloading the video. Please wait...")
video.download() #Finally, download the video
