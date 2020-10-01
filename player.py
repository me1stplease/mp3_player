import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


player = tkr.Tk()
player.title("MP3 Player")
player.geometry('400x300')

directory = askdirectory()
os.chdir(directory)


Slist = os.listdir()
Playlist = tkr.Listbox(player, font ="Courier 12" , bg="white", selectmode = tkr.SINGLE) 

for s in Slist:
    pos = 0
    Playlist.insert(pos, s)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(Playlist.get(tkr.ACTIVE))
    var.set(Playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def Exitplayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Playbutton = tkr.Button(player, font ="Times 12 bold" , text="Play",command=play,bg="green",fg="white")
Exitbutton = tkr.Button(player, font ="Times 12 bold" , text="Stop",command=Exitplayer,bg="red",fg="white")
Pausebutton = tkr.Button(player, font ="Times 12 bold" , text="Pause",command=pause,bg="blue",fg="white")
Unpausebutton = tkr.Button(player, font ="Times 12 bold" , text="Unpause",command=unpause,bg="purple",fg="white")

var = tkr.StringVar()
songtitle = tkr.Label(player,font="Times 12",textvariable=var)

songtitle.pack()

Playlist.pack(fill="both",expand="yes")
Playbutton.pack(fill="x")
Exitbutton.pack(fill="x")
Pausebutton.pack(fill="x")
Unpausebutton.pack(fill="x")


player.mainloop()