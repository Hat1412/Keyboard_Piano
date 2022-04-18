from random import choice
from tkinter import *
from pygame import mixer

root = Tk()
root.title("Piano")
root.config(bg = "pink")
mixer.init()
note = 1

def play(filename):
    mixer.music.load(f"music/{filename}")
    mixer.music.play()

def num_play(passcode):
    global note
    d = {
    "9":"B0.mp3",
    "7":"A0.mp3",
    "0":f"A{note}.mp3",
    "1":f"B{note}.mp3",
    "2":f"C{note}.mp3",
    "3":f"D{note}.mp3",
    "4":f"E{note}.mp3",
    "5":f"F{note}.mp3",
    "6":f"G{note}.mp3"
    }
    play(d[passcode])
    btn = d[passcode].replace(".mp3","")
    l = [G6,F6,E6,D6,C6,B6,G5,F5,E5,D5,C5,B5,G4,F4,E4,D4,C4,B4,G3,F3,E3,D3,C3,B3,G2,F2,E2,D2,C2,B2,G1,F1,E1,D1,C1,B1,A0,B0]
    for i in l:
        if i.cget('text') == btn:
            i.config(bg = "red")

G6 = Button(root,font = ("Times New Roman",18),text = "G6",command = lambda: play("G6.mp3"),bg = "red")
F6 = Button(root,font = ("Times New Roman",18),text = "F6",command = lambda: play("F6.mp3"),bg = "red")
E6 = Button(root,font = ("Times New Roman",18),text = "E6",command = lambda: play("E6.mp3"),bg = "red")
D6 = Button(root,font = ("Times New Roman",18),text = "D6",command = lambda: play("D6.mp3"),bg = "red")
C6 = Button(root,font = ("Times New Roman",18),text = "C6",command = lambda: play("C6.mp3"),bg = "red")
B6 = Button(root,font = ("Times New Roman",18),text = "B6",command = lambda: play("B6.mp3"),bg = "red")
G5 = Button(root,font = ("Times New Roman",18),text = "G5",command = lambda: play("G5.mp3"),bg = "red")
F5 = Button(root,font = ("Times New Roman",18),text = "F5",command = lambda: play("F5.mp3"),bg = "red")
E5 = Button(root,font = ("Times New Roman",18),text = "E5",command = lambda: play("E5.mp3"),bg = "red")
D5 = Button(root,font = ("Times New Roman",18),text = "D5",command = lambda: play("D5.mp3"),bg = "red")
C5 = Button(root,font = ("Times New Roman",18),text = "C5",command = lambda: play("C5.mp3"),bg = "red")
B5 = Button(root,font = ("Times New Roman",18),text = "B5",command = lambda: play("B5.mp3"),bg = "red")
G4 = Button(root,font = ("Times New Roman",18),text = "G4",command = lambda: play("G4.mp3"),bg = "red")
F4 = Button(root,font = ("Times New Roman",18),text = "F4",command = lambda: play("F4.mp3"),bg = "red")
E4 = Button(root,font = ("Times New Roman",18),text = "E4",command = lambda: play("E4.mp3"),bg = "red")
D4 = Button(root,font = ("Times New Roman",18),text = "D4",command = lambda: play("D4.mp3"),bg = "red")
C4 = Button(root,font = ("Times New Roman",18),text = "C4",command = lambda: play("C4.mp3"),bg = "red")
B4 = Button(root,font = ("Times New Roman",18),text = "B4",command = lambda: play("B4.mp3"),bg = "red")
G3 = Button(root,font = ("Times New Roman",18),text = "G3",command = lambda: play("G3.mp3"),bg = "red")
F3 = Button(root,font = ("Times New Roman",18),text = "F3",command = lambda: play("F3.mp3"),bg = "red")
E3 = Button(root,font = ("Times New Roman",18),text = "E3",command = lambda: play("E3.mp3"),bg = "red")
D3 = Button(root,font = ("Times New Roman",18),text = "D3",command = lambda: play("D3.mp3"),bg = "red")
C3 = Button(root,font = ("Times New Roman",18),text = "C3",command = lambda: play("C3.mp3"),bg = "red")
B3 = Button(root,font = ("Times New Roman",18),text = "B3",command = lambda: play("B3.mp3"),bg = "red")
G2 = Button(root,font = ("Times New Roman",18),text = "G2",command = lambda: play("G2.mp3"),bg = "red")
F2 = Button(root,font = ("Times New Roman",18),text = "F2",command = lambda: play("F2.mp3"),bg = "red")
E2 = Button(root,font = ("Times New Roman",18),text = "E2",command = lambda: play("E2.mp3"),bg = "red")
D2 = Button(root,font = ("Times New Roman",18),text = "D2",command = lambda: play("D2.mp3"),bg = "red")
C2 = Button(root,font = ("Times New Roman",18),text = "C2",command = lambda: play("C2.mp3"),bg = "red")
B2 = Button(root,font = ("Times New Roman",18),text = "B2",command = lambda: play("B2.mp3"),bg = "red")
G1 = Button(root,font = ("Times New Roman",18),text = "G1",command = lambda: play("G1.mp3"),bg = "red")
F1 = Button(root,font = ("Times New Roman",18),text = "F1",command = lambda: play("F1.mp3"),bg = "red")
E1 = Button(root,font = ("Times New Roman",18),text = "E1",command = lambda: play("E1.mp3"),bg = "red")
D1 = Button(root,font = ("Times New Roman",18),text = "D1",command = lambda: play("D1.mp3"),bg = "red")
C1 = Button(root,font = ("Times New Roman",18),text = "C1",command = lambda: play("C1.mp3"),bg = "red")
B1 = Button(root,font = ("Times New Roman",18),text = "B1",command = lambda: play("B1.mp3"),bg = "red")
A0 = Button(root,font = ("Times New Roman",18),text = "A0",command = lambda: play("A0.mp3"),bg = "red")
B0 = Button(root,font = ("Times New Roman",18),text = "B0",command = lambda: play("B0.mp3"),bg = "red")

G6.grid(row = 0,column = 0,padx = 10,pady = 10)
F6.grid(row = 1,column = 0,padx = 10,pady = 10)
E6.grid(row = 2,column = 0,padx = 10,pady = 10)
D6.grid(row = 3,column = 0,padx = 10,pady = 10)
C6.grid(row = 4,column = 0,padx = 10,pady = 10)
B6.grid(row = 5,column = 0,padx = 10,pady = 10)
G5.grid(row = 0,column = 1,padx = 10,pady = 10)
F5.grid(row = 1,column = 1,padx = 10,pady = 10)
E5.grid(row = 2,column = 1,padx = 10,pady = 10)
D5.grid(row = 3,column = 1,padx = 10,pady = 10)
C5.grid(row = 4,column = 1,padx = 10,pady = 10)
B5.grid(row = 5,column = 1,padx = 10,pady = 10)
G4.grid(row = 0,column = 2,padx = 10,pady = 10)
F4.grid(row = 1,column = 2,padx = 10,pady = 10)
E4.grid(row = 2,column = 2,padx = 10,pady = 10)
D4.grid(row = 3,column = 2,padx = 10,pady = 10)
C4.grid(row = 4,column = 2,padx = 10,pady = 10)
B4.grid(row = 5,column = 2,padx = 10,pady = 10)
G3.grid(row = 0,column = 3,padx = 10,pady = 10)
F3.grid(row = 1,column = 3,padx = 10,pady = 10)
E3.grid(row = 2,column = 3,padx = 10,pady = 10)
D3.grid(row = 3,column = 3,padx = 10,pady = 10)
C3.grid(row = 4,column = 3,padx = 10,pady = 10)
B3.grid(row = 5,column = 3,padx = 10,pady = 10)
G2.grid(row = 0,column = 4,padx = 10,pady = 10)
F2.grid(row = 1,column = 4,padx = 10,pady = 10)
E2.grid(row = 2,column = 4,padx = 10,pady = 10)
D2.grid(row = 3,column = 4,padx = 10,pady = 10)
C2.grid(row = 4,column = 4,padx = 10,pady = 10)
B2.grid(row = 5,column = 4,padx = 10,pady = 10)
G1.grid(row = 0,column = 5,padx = 10,pady = 10)
F1.grid(row = 1,column = 5,padx = 10,pady = 10)
E1.grid(row = 2,column = 5,padx = 10,pady = 10)
D1.grid(row = 3,column = 5,padx = 10,pady = 10)
C1.grid(row = 4,column = 5,padx = 10,pady = 10)
B1.grid(row = 5,column = 5,padx = 10,pady = 10)
A0.grid(row = 6,column = 2,padx = 10,pady = 10)
B0.grid(row = 6,column = 3,padx = 10,pady = 10)

def add_note(_):
    global note
    note += 1
    if note > 6:
        note = 1

def sub_note(_):
    global note
    note -= 1
    if note == 0:
        note = 6

root.bind("0",lambda x: num_play("0"))
root.bind("1",lambda x: num_play("1"))
root.bind("2",lambda x: num_play("2"))
root.bind("3",lambda x: num_play("3"))
root.bind("4",lambda x: num_play("4"))
root.bind("5",lambda x: num_play("5"))
root.bind("6",lambda x: num_play("6"))
root.bind("7",lambda x: num_play("7"))
root.bind("9",lambda x: num_play("9"))
root.bind("p",add_note)
root.bind("q",sub_note)

def color_change():
    C = "green"
    l = [G6,F6,E6,D6,C6,B6,G5,F5,E5,D5,C5,B5,G4,F4,E4,D4,C4,B4,G3,F3,E3,D3,C3,B3,G2,F2,E2,D2,C2,B2,G1,F1,E1,D1,C1,B1,A0,B0]
    for i in l:
        i.config(bg = C)

    root.after(2000,color_change)

color_change()
mainloop()