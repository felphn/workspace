import tkinter as tk
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from os import name, getlogin, remove, sep
from os.path import abspath
# pytube3 is usually getting download issues, so we can go for pytubeX instead.
# 'pip uninstall pytube3' --> 'pip install pytubeX'


class YtToPC(tk.Frame):
    #Master init & general properties:
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.envProp()


    def envProp(self):
        #program status properties:
        self.status = tk.Label(self, textvariable=currStatus, font=('helvetica', 10))
        self.status.pack(pady=3)
        #input box properties:
        self.setLink = tk.Entry(self, textvariable=ytLink, width=35)
        self.setLink.pack(pady=3)
        #"DownMP4" button properties:
        self.downVid = tk.Button(self, text='Download .MP4 format', fg='blue', font=('helvetica', 11, 'bold'), command=self.downToMp4)
        self.downVid.pack(pady=3)
        #"DownMP3" button properties:
        self.downAud = tk.Button(self, text='Download .MP3 format', fg='blue', font=('helvetica', 11, 'bold'), command=self.downToMp3)
        self.downAud.pack(pady=3)
        #"Exit" button properties:
        self.exit = tk.Button(self, text='     Exit     ', fg='red', font=('helvetica', 10, 'bold'), command=self.master.destroy)
        self.exit.pack(pady=5)
        #program info properties:
        self.info = tk.Label(self, text='made by felpshn', fg='grey', font=('helvetica', 9, 'italic'))
        self.info.pack(pady=3)


    def downToMp4(self):
        try:
            currStatus.set('[1/2] Downloading...') #sets a new status for the app.
            root.update() #updates the app.
            ytVid = YouTube(ytLink.get()) #gets from the user the yt video link.
            if name == 'nt':
                downPath = f'{abspath(sep)}Users\\{getlogin()}\\Downloads' #sets the download dir path.
                tempVidFilePath = f'{downPath}\\tempVidFile.mp4'
                tempAudFilePath = f'{downPath}\\tempAudFile.mp4'
                clipFilePath = f'{downPath}\\{ytVid.title}.mp4'
            else:
                downPath = f'/home/{getlogin()}/Downloads'
                tempVidFilePath = f'{downPath}/tempVidFile.mp4'
                tempAudFilePath = f'{downPath}/tempAudFile.mp4'
                clipFilePath = f'{downPath}/{ytVid.title}.mp4'
            ytVid.streams.filter(adaptive=True, type='video').first().download(downPath, filename='tempVidFile') #"adaptative" gets the best video or audio quality possible.
            ytVid.streams.filter(adaptive=True, type='audio').first().download(downPath, filename='tempAudFile') #"first" gets the first video listed inside the array defined by adaptative param.
            tempVidFile = VideoFileClip(tempVidFilePath) #assigns the file as a video file.       #"filename" defines a new name to the downloaded file.
            tempAudFile = AudioFileClip(tempAudFilePath) #assigns the file as a audio file.
            currStatus.set('[2/2] Converting & mounting...')
            ytLink.set('This step may take some minutes.')
            root.update()
            clipMount = tempVidFile.set_audio(tempAudFile) #assign an audio clip as the soundtrack of a video clip.
            clipMount.write_videofile(clipFilePath, fps=30) #builds the clip.
            tempVidFile.close() #closes the internal reader.
            tempAudFile.close()
            clipMount.close()
            remove(tempVidFilePath) #deletes the temp vid and aud file.
            remove(tempAudFilePath)
            currStatus.set('Done!')
            ytLink.set('Check your "Downloads" folder.')
            root.update()
        except Exception as e:
            print(e)
            currStatus.set('Error! something went wrong.')
            ytLink.set('Invalid Link!')
            root.update()


    def downToMp3(self):
        try:
            currStatus.set('[1/2] Downloading...')
            root.update()
            ytVid = YouTube(ytLink.get())
            if name == 'nt':
                downPath = f'{abspath(sep)}Users\\{getlogin()}\\Downloads'
                tempAudFilePath = f'{downPath}\\tempAudFile.mp4'
                audFilePath = f'{downPath}\\{ytVid.title}.mp3'
            else:
                downPath = f'/home/{getlogin()}/Downloads'
                tempAudFilePath = f'{downPath}/tempAudFile.mp4'
                audFilePath = f'{downPath}/{ytVid.title}.mp3'
            ytVid.streams.first().download(downPath, filename='tempAudFile')
            tempAudFile = VideoFileClip(tempAudFilePath)
            currStatus.set('[2/2] Converting & mounting...')
            ytLink.set('It will be ready in a sec.')
            root.update()
            audMount = tempAudFile.audio
            audMount.write_audiofile(audFilePath)
            tempAudFile.close()
            audMount.close()
            remove(tempAudFilePath)
            currStatus.set('Done!')
            ytLink.set('Check your "Downloads" folder.')
            root.update()
        except Exception as e:
            print(e)
            currStatus.set('Error! something went wrong.')
            ytLink.set('Invalid link!')
            root.update()


#Tk call & general GUI properties:
root = tk.Tk()
root.title('YouTube 2 PC')
root.geometry('280x190')
root.resizable(0, 0)
#String vars:
currStatus = tk.StringVar()
currStatus.set('Enter the YouTube link below.')
ytLink = tk.StringVar()

app = YtToPC(master=root)
app.mainloop()
