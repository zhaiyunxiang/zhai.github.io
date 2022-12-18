import tkinter as tk
from tkinter import messagebox
from tkinter import *

def fifo():
    s=[]
    a=en1.get()
    b=en2.get()
    a1=a.split(",")
    if len(a1)<=int(b):
        s=[]
        cnt=0
        que=0
        for i in range(len(a1)):
            if a1[i] in s:
                txt.insert(END,"(%d)"%(i+1))
                txt.insert(END,s)
                txt.insert(END,",")
                continue
            s.append(a1[i])
            que+=1
            txt.insert(END,"(%d)"%(i+1))
            txt.insert(END,s)
            txt.insert(END,",")
        txt.insert(END,"中断次数为：%d,"%que)
        txt.insert(END,"置换次数为：%d"%cnt)
    elif len(a1)>int(b):
        s1=[]
        cnt1=0
        que1=0
        for j in range(len(a1)):
            if a1[j] not in s1 and len(s1)<int(b):
                s1.append(a1[j])
                que1+=1
                txt.insert(END,"(%d)"%(j+1))
                txt.insert(END,s1)
                txt.insert(END,",")
            elif a1[j] in s1:
                txt.insert(END,"(%d)"%(j+1))
                txt.insert(END,s1)
                txt.insert(END,",")
                continue
            elif a1[j] not in s1 and len(s1)==int(b):
                z=[]
                for k in range((j-1),-1,-1):
                    if a1[k] not in z:
                        z.append(a1[k])
                    if len(z)==int(b):
                        break
                s1=[a1[j]if i==a1[k] else i for i in s1]
                que1+=1
                cnt1+=1
                txt.insert(END,"(%d)"%(j+1))
                txt.insert(END,s1)
                txt.insert(END,",")
        txt.insert(END,"中断次数为：%d,"%que1)
        txt.insert(END,"置换次数为：%d\n"%cnt1)
                
        

def cleck():
    a =en1.get()
    b=en2.get()
    if a=='' or b=='':
        messagebox.showerror(title="很抱歉",message="请输入正确的相应内容")
        return
    fifo()

root = tk.Tk()
root.title("先进先出FIFO算法")
root.geometry('500x500')
lb = tk.Label(root, text="先进先出FIFO算法", fg="black", font=("宋体", 20))
lb.pack()

la1 = tk.Label(root, text="输入执行页面",fg="black")
la1.place(x=1,y=30,width=100,height=30)

en1=tk.Entry(root,bd=2)
en1.place(x=105,y=30,width=300,height=30)

la2=tk.Label(root,text="分配物理块数",fg="black")
la2.place(x=1,y=70,width=100,height=30)

en2=tk.Entry(root,bd=2)
en2.place(x=105,y=70,width=300,height=30)

bt=tk.Button(root,text="确定",command=cleck)
bt.place(x=420,y=30,width=80,height=30)


lb3=tk.Label(root,text="Answer:")
lb3.place(x=1,y=90,width=100,height=30)
txt=tk.Text(root)
txt.place(x=0,y=120,width=500,height=300)

root.mainloop()
