import tkinter as tk
import dijkstraimpl as dj

def show(): #调用dijstrat算法，并放到label_result的text中
    start_city = e_start.get()
    end_city = e_end.get()
    string = dj.dijkstra(start_city, end_city)
    label_result["text"] = string


win = tk.Tk()   #初始化一个窗口
win.title("Dijkstra最短路径")   #窗口名称
win.geometry("600x400+500+50")  #窗口大小

label_start = tk.Label(win, text='起点', font=('宋体',16))  #起点标签
label_start.grid(row=0, column=0,padx=20,pady=20)   #起点标签的位置
e_start=tk.Entry(win)   #起点输入框
e_start.grid(row=0,column=1)    #起点输入框的位置
e_start.focus()     #打开程序，鼠标焦点自动放到起点输入框

label_end = tk.Label(win, text='终点', font=('宋体',16))    #终点标签
label_end.grid(row=0, column=2,padx=20,pady=20)     #终点标签位置
e_end=tk.Entry(win)     #终点输入框
e_end.grid(row=0,column=3)      #终点输入框的位置

button=tk.Button(win, text="查找路径", width=10, command=show)      #Button
button.grid(row=0, column=4, sticky=tk.E, padx=10, pady=10)     #Button位置

label_result = tk.Label(win, text="", font=('宋体', 16), justify="left")      #放置查询结果的标签
label_result.grid(row=3, columnspan=4)          #标签位置

win.mainloop()      #程序跑起来
