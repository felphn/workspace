import tkinter as tk
from os import name, system, remove, startfile
from os.path import isfile, dirname, realpath
from psutil import process_iter
from time import sleep


def taskKill():
    for p in process_iter():
        if p.cmdline() == ['a.exe']:
            p.kill()
            break


class GppCompiler(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.envProps()


    def envProps(self):
        self.run = tk.Button(self, text='     Run     ', fg='green', font=('helvetica', 11, 'bold'), command=self.startGpp)
        self.run.pack(pady=2)
        self.quit = tk.Button(self, text='     Quit     ', fg='red', font=('helvetica', 10, 'bold'), command=self.master.destroy)
        self.quit.pack(pady=2)
        self.info = tk.Label(self, text='made by felpshn\nMinGW environment', fg='grey')
        self.info.pack(pady=2)


    def startGpp(self):
        compFileExists = isfile(f'{dirname(realpath(__file__))}\\a.exe')
        if compFileExists:
            try:
                taskKill()
            except:
                pass
        system(f'g++ "{cFile}"')
        if compFileExists:
            startfile(f'{dirname(realpath(__file__))}\\a.exe')


if name == 'nt':
    system('cls')
    getFile = str(input('File name?\n> '))
    fileExists = isfile(f'{dirname(realpath(__file__))}\\{getFile}')
    if fileExists:
        print('-'*22, '\nDone! Process started.')
        sleep(.5)
        system('cls')
        cFile = f'{dirname(realpath(__file__))}\\{getFile}'
        root = tk.Tk()
        root.title('C/C++ Compiler')
        root.geometry('260x105')
        root.resizable(0, 0)
        app = GppCompiler(master=root)
        app.mainloop()
    else:
        print('-'*44, "\n!>> Error: Couldn't find the specified file!\n")
        print('Check if the c/cpp file is in the same directory as the compiler.\n')
        system('pause')
else:
    print('\n!>> Not a Windows OS!')
    input('Press any key to continue ...')
