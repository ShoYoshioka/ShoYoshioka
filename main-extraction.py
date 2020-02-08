# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter as ttk
import extraction as ext


#各binに引数を入れる。
shiryou = {
    '1': '4335.8',
    '2': '5435.3',
    '3': '5369.8',
    '4': '1099.5',
    '5': '1034.0',
    '6': '65.5'}

r135 = {
    'weight': '1111.1',
    'ratio': '44.4',
    'bat': '777.7',
    'bat+wet': '1985.1',
    'bat+dry': '1984.1',
    'moisture': '1.00',
    'total': '0.94',}
    
r50 = {
    'weight': '2222.2',
    'ratio': '66.6',
    'bat': '888.8',
    'bat+wet': '2666.1',
    'bat+dry': '2555.1',
    'moisture': '0.89'}
    
shinnyu = {
    'first':'22',
    'second':'21',
    'third':'21'}

kaseki = {
    '19.0': '0',
    '13.2': '0',
    '4.75': '214.9',
    '2.36': '407.2',
    '0.60': '666.3',
    '0.30': '777.4',
    '0.15': '897.6',
    '0.075': '960.1',
    'total': '1031.2'}

zanryu = {
	'26.5': '0',
	'19.0': '0',
    '13.2': '0.0',
    '4.75': '20.8',
    '2.36': '39.4',
    '0.60': '64.4',
    '0.30': '75.2',
    '0.15': '86.8',
    '0.075': '92.9',
    'total': '99.7'}



#メインを実行する。
if __name__ == "__main__":

    root = tk.Tk()

    ext.title(root, tk)
    samples = ext.sample(root, ttk, tk, shiryou, r135)
    ext.clas(root, tk, ttk, r135, r50)
    average = ext.penetration(root, ttk, tk, shinnyu)
    tuuka = ext.accumulation(root, ttk, tk, kaseki, zanryu)
    kanri = ext.extraction(root, tk, ttk, tuuka)
    
    canvas = tk.Canvas(width = 700, height = 300, bg = "gray94")
    canvas.place(x=60, y=650)
    img = tk.PhotoImage(file="graingraph.gif")
    canvas.create_image(350, 150, image=img)
    canvas.create_line(81, 250, 144, 233, fill="black",width=2)
    canvas.create_line(144, 233, 205, 204, fill="black",width=2)
    canvas.create_line(205, 204, 268, 175, fill="black",width=2)
    canvas.create_line(268, 175, 393, 110, fill="black",width=2)
    canvas.create_line(393, 110, 456, 60, fill="black",width=2)
    canvas.create_line(456, 60, 551, 7, fill="black",width=2)
    
    root.mainloop()
