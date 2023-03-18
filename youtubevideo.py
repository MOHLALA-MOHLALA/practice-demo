from pytube import YouTube

# Ask user to input the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object with the video URL
youtube = YouTube(video_url)

# Get the video stream with the highest resolution
video_stream = youtube.streams.get_highest_resolution()

# Download the video to the current working directory
video_stream.download()
.