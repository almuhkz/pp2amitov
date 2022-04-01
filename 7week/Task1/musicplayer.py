import tkinter as tk 
import fnmatch
import os
import pygame as pg

canvas = tk.Tk()
canvas.title("Almuh's music player")
canvas.geometry("600x600")
canvas.config(bg = 'black')


rootpath = "C:\\Users\\amito\\OneDrive\\Documents\\PP2\\7week\\Task1"
pattern="*.mp3"

pg.init()
space_pressed = pg.key.get_pressed() [pg.K_SPACE]
prev_img= tk.PhotoImage(file = "prev.png") 
stop_img= tk.PhotoImage(file= "stop.png")
play_img= tk.PhotoImage(file = "play.png")
pause_img= tk.PhotoImage(file = "pause.png")
next_img =tk.PhotoImage(file="next.png")
logo_img=tk.PhotoImage(file="logo.png")

def select():
    label.config(text= listBox.get("anchor"))
    pg.mixer.music.load(rootpath + "\\"+ listBox.get("anchor"))
    pg.mixer.music.play()


def stop():
    pg.mixer.music.stop() 
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection ()
    next_song = next_song [0] + 1
    next_song_name= listBox.get(next_song)
    label.config(text = next_song_name)
    pg.mixer.music.load(rootpath + "\\" + next_song_name)
    pg.mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(next_song) 
    listBox.select_set(next_song)

def play_prev():
    p_song = listBox.curselection ()
    p_song = p_song [0] - 1
    p_song_name= listBox.get(p_song)
    label.config(text = p_song_name)
    pg.mixer.music.load(rootpath + "\\" + p_song_name)
    pg.mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(p_song) 
    listBox.select_set(p_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        pg.mixer.music.pause() 
        pauseButton ["text"] = "Play"
    else:
        pg.mixer.music.unpause()
        pauseButton["text"] = "Pause"
def keypress(event):
    print(event)
    if event.char == 'p':
        select()
    elif event.char == 'n':
        play_next()
    elif event.char == 'b':
        play_prev()
    elif event.char == 's':
        pause_song()
    elif event.char == 'x':
        stop()
    else:
        pass
canvas.bind('p',keypress)
canvas.bind('n',keypress)
canvas.bind('b',keypress)
canvas.bind('s',keypress)
canvas.bind('x',keypress)

listBox =  tk. Listbox (canvas, fg = "red", bg= "black", width= 100)
listBox.pack(padx= 15, pady = 15)
label =  tk.Label (canvas,text='', fg = "red", bg= "black", width= 100)
label.pack( pady = 15)

top = tk.Frame (canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

tutorial_txt =  tk.Label (canvas,text='P key to PLAY SONG\nN key to play NEXT SONG\nB key to play PREVIOUS SONG\nS key to PAUSE SONG\nX key to STOP SONG\n', fg = "red", bg= "black", width= 100)
tutorial_txt.pack( pady = 5)

logo = tk.Label(canvas,image=logo_img)
logo.pack(pady=30)

prevButton = tk.Button(canvas, text = "Prev", image= prev_img, bg = 'black', borderwidth = 0, command=play_prev)
prevButton.pack(pady = 15, in_= top, side = 'left')

StopButton= tk.Button(canvas, text = "Stop", image= stop_img, bg = 'black', borderwidth = 0,command=stop) 
StopButton.pack(pady = 15, in_= top, side = 'left')

playButton = tk.Button(canvas, text = "Play", image= play_img, bg = 'black', borderwidth = 0,command=select) 
playButton.pack(pady = 15, in_= top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause", image= pause_img, bg = 'black', borderwidth = 0, command=pause_song) 
pauseButton.pack(pady = 15, in_= top, side = 'left')

nextButton = tk.Button(canvas, text = "Next", image= next_img, bg = 'black', borderwidth = 0,command=play_next) 
nextButton.pack(pady = 15, in_= top, side = 'left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter (files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()