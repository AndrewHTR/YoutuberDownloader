from tkinter import *
from tkinter import ttk
import pytube
import youtube_dl
from moviepy.editor import *

def main():
    icone = "icon.ico"
    root = Tk()
    root.geometry('300x100')
    root.title('Youtuber Downloader')
    root.iconbitmap("icon.ico")
    """frame1 = ttk.Frame(root)
    frame1.grid()"""

    textosimples = ttk.Label(text='Coloque aqui o link do video que deseja baixar:')
    textosimples.place(x=25,y=10)

    caixinhadownload = ttk.Entry()
    caixinhadownload.place(x=85,y=33)

    botaodownload = ttk.Button(text='Download MP4')
    botaodownload['command'] = (lambda: downloadyt(caixinhadownload))
    botaodownload.place(x=50,y=62)
    
    
    
    botaodownloadmp3 = ttk.Button(text='Download MP3')
    botaodownloadmp3['command'] = (lambda: downloadytmp3(caixinhadownload))
    botaodownloadmp3.place(x=160,y=62)
    

    root.mainloop()

def downloadytmp3(entry_box):
    video_url = entry_box.get()
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
def downloadyt(entry_box):

    url = entry_box.get()

    yt = pytube.YouTube(url)

    print(f'O video: {yt.title}')

    video = yt.streams.get_by_itag(22)

    video.download()
    video.on_complete(print('O download foi concluido!'))
   
    
