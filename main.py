from pytube import YouTube, Playlist
import os

def progress_function(stream, chunk, remaining):
    percent = (100 * (file_size - remaining))/file_size
    print("{:00.0f}% downloaded".format(percent))

#Grabs the file path for Download
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path

def get_resolution(the_video):
    the_video = the_video.streams.filter(progressive = True)
    list_quality = [stream.resolution for stream in the_video]
    return list_quality

def main():
    print("Your video will be saved to: {}".format(file_path()))
    #Input 
    yt_url = input("Copy and paste your YouTube URL here: ")
    print(yt_url)
    print ("Accessing YouTube URL...")

    # Searches for the video and sets up the callback to run the progress indicator. 
    try:
        video = YouTube(yt_url, on_progress_callback=progress_function)
    except:
        print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
        redo = start()
    
    # Get the quality
    list_quality = get_resolution(video)
    for idx, ps in enumerate(list_quality):
        print((idx + 1),".", ps)
    
    # get the input of quality
    try:
        print("Select Quality of Video")
        quality = int(input("Input the number : ")) - 1
    except:
        quality = 0

    # Get the video download
    video_type = video.streams.filter(progressive = True, res=list_quality[quality]).first()
    print(video_type, list_quality[quality])

    # Gets the title of the video
    title = video.title

    # Prepares the file for download
    print ("Fetching: {}...".format(title))
    global file_size
    file_size = video_type.filesize
    
    # Starts the download process
    video_type.download(file_path())
 
    print ("Ready to download another video.\n\n")
    again = main()

file_size = 0

if __name__ == "__main__":
    main()