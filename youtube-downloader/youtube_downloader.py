from pytube import YouTube

def YouTubeVideoDownloader(link):
    try:
        youtubeObject = YouTube(link)
        video_stream = youtubeObject.streams.get_highest_resolution()
        video_stream.download()
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")
        print("There has been an error in downloading your YouTube video")

if __name__ == "__main__":
    video_link = input("Enter the YouTube link here: ")
    YouTubeVideoDownloader(video_link)
