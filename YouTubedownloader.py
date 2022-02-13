from pytube import YouTube

link = input("Enter your link here: ")
yt_link = YouTube(link)

print("The title of the video is:")
print(yt_link.title + "\n")

print("The number of views of the video is:")
print(yt_link.views)

print("The length of the video is:")
print(yt_link.length)

print("The description of the video is:")
print(yt_link.description + "\n")

print("The rating of the video is:")
print(yt_link.rating)

print("List of available streams for the video are:")
print(yt_link.streams)

print("List of available streams with res = 480p for the video are:")
print(yt_link.streams.filter(res="480p"))

print("The maximum resolution for the video is :")
print(yt_link.streams.get_highest_resolution())
yt_res = yt_link.streams.get_highest_resolution()

location = input("Enter the location where you want to download the video: ")
print("starting to download...")

yt_res.download(location)

print("Download complete")