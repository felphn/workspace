import tkinter as tk

from pytube import YouTube

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

from os import name, getlogin, remove, sep
from os.path import abspath

# pytube3 is outdated, so we'll use pytubeX instead:

# pip uninstall pytube pytube3 pytubeX
# pip install git+https://github.com/nficano/pytube


class YtToPC(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.envProp()


    def envProp(self):
        self.status = tk.Label(self, textvariable=currStatus, font=('helvetica', 10))
        self.status.pack(pady=3)

        self.setLink = tk.Entry(self, textvariable=ytLink, width=35)
        self.setLink.pack(pady=3)

        self.downVid = tk.Button(self, text='Download .MP4 format', fg='blue', font=('helvetica', 11, 'bold'), command=self.downToMp4)
        self.downVid.pack(pady=3)

        self.downAud = tk.Button(self, text='Download .MP3 format', fg='blue', font=('helvetica', 11, 'bold'), command=self.downToMp3)
        self.downAud.pack(pady=3)

        self.exit = tk.Button(self, text='     Exit     ', fg='red', font=('helvetica', 10, 'bold'), command=self.master.destroy)
        self.exit.pack(pady=5)

        self.info = tk.Label(self, text='made by felpshn', fg='grey', font=('helvetica', 9, 'italic'))
        self.info.pack(pady=3)


    def downToMp4(self):
        try:
            currStatus.set('[1/2] Downloading...')
            root.update()
            ytVid = YouTube(ytLink.get())
            if name == 'nt':
                downPath = f'{abspath(sep)}Users\\{getlogin()}\\Downloads'
                tempVidFilePath = f'{downPath}\\tempVidFile.mp4'
                tempAudFilePath = f'{downPath}\\tempAudFile.mp4'
                clipFilePath = f'{downPath}\\{ytVid.title}.mp4'
            else:
                downPath = f'/home/{getlogin()}/Downloads'
                tempVidFilePath = f'{downPath}/tempVidFile.mp4'
                tempAudFilePath = f'{downPath}/tempAudFile.mp4'
                clipFilePath = f'{downPath}/{ytVid.title}.mp4'
            ytVid.streams.filter(adaptive=True, type='video').first().download(downPath, filename='tempVidFile')
            ytVid.streams.filter(adaptive=True, type='audio').first().download(downPath, filename='tempAudFile')
            tempVidFile = VideoFileClip(tempVidFilePath)
            tempAudFile = AudioFileClip(tempAudFilePath)
            currStatus.set('[2/2] Converting & mounting...')
            ytLink.set('This step may take some minutes.')
            root.update()
            clipMount = tempVidFile.set_audio(tempAudFile)
            clipMount.write_videofile(clipFilePath, fps=30)
            tempVidFile.close()
            tempAudFile.close()
            clipMount.close()
            remove(tempVidFilePath)
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


root = tk.Tk()
root.title('YouTube 2 PC')
root.geometry('280x190')
root.resizable(0, 0)

currStatus = tk.StringVar()
currStatus.set('Enter the YouTube link below.')
ytLink = tk.StringVar()

app = YtToPC(master=root)
app.mainloop()
