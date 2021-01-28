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
    print("Video akan di save di : {}".format(file_path()))
    #Input 
    yt_url = input("Copy dan paste Youtube URL Mu: ")
    print(yt_url)
    print ("Mengakses URL Video di YouTube ...")

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
    
    # Ambil List Kualitas Video nya. 
    try:
        print("Pilih Kualitas Video")
        quality = int(input("Input nomornya aja : ")) - 1
    except:
        quality = 0

    # Ambil Video Untuk Didownload
    video_type = video.streams.filter(progressive = True, res=list_quality[quality]).first()
    print(video_type, list_quality[quality])

    # Ambil Judul Video
    title = video.title

    # Menyiapkan Video untuk didownload
    print ("Fetching: {}...".format(title))
    global file_size
    file_size = video_type.filesize
    
    # Mulai Download Process
    video_type.download(file_path())
 
    print ("Siap Untuk Mendownload Video Berikutnya!.\n\n")
    again = main()

file_size = 0

if __name__ == "__main__":
    main()