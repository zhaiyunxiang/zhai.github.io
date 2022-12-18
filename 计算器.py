import tkinter as tk
import tkinter.messagebox as messagebox
root=tk.Tk()
root.geometry("290x273+200+200")
root.title("计算器")
varentry=tk.StringVar()

entry=tk.Entry(root,bg="black",fg="white",textvariable=varentry,font="宋体")
entry.grid(row=0,column=0,sticky=tk.EW,ipady=5)



def shuzi(a):
    txt=str(a.widget.configure().get("text")[-1])
    if("=" in varentry.get()):
        varentry.set("")
    elif (txt=="清空"):
        varentry.set("")
    elif txt=="退格":
        varentry.set(varentry.get()[0:len(varentry.get())-1])

    elif txt=="!":
        try:
            a1=str(varentry.get())
            a2=1
            for j in range(1,int(a1)+1):
                a2=a2*j
            varentry.set(varentry.get()+"!"+"="+str(a2))
        except:
            varentry.set(varentry.get()+txt)
            messagebox.showerror("很抱歉","请输入正确的式子")
        

        
    elif txt=="=":
        try:
            result=eval(varentry.get())
            varentry.set(varentry.get()+"="+str(result))
        except:
            messagebox.showerror("很抱歉","请输入正确的计算公式")
            pass
    else:
        varentry.set(varentry.get()+txt)
   
    pass



def pdss(a):
    txt1=varentry.get()
    if txt1=="":
        messagebox.showerror("很抱歉","请输入要判断的数字")
    elif txt1!="":
        try:
            f=0
            txt1=int(varentry.get())
            for k in range(2,txt1):
                if txt1%k==0:
                    f=0
                    break
                elif txt1%k!=0:
                    f=1
            if f==0:
                messagebox.showinfo("判断素数","这不是一个素数。")
            else:
                messagebox.showinfo("判断素数","这是一个素数。")
        except:
            messagebox.showerror("很抱歉","必须输入正确形式")

def jjcfb(a):
    
   messagebox.showinfo("九九乘法表","1*1=1\n 2*1=2 2*2=4\n 3*1=3 3*2=6 3*3=9\n 4*1=4 4*2=8 4*3=12 4*4=16\n 5*1=5 5*2=10 5*3=15 5*4=20 5*5=25\n 6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36\n 7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49\n 8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64\n 9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81\n")
   

frame=tk.Frame(root)
frame.grid(row=1,column=0)
fh=[7,8,9,"+",4,5,6,"-",1,2,3,"*",0,".","=","/","**","开方","!","积分","(",")","%"]
ri=2
ci=0
for i in fh:
    if (ci!=0 and ci%4==0):
        ri=ri+1
        ci=0
    btn1=tk.Button(frame,text=i,width=9)
    btn1.bind("<Button-1>",shuzi)
    btn1.grid(row=ri,column=ci)
    ci=ci+1

btn2=tk.Button(root,text="判断素数")
btn2.place(x=0,y=243,width=145,height=30)
btn2.bind("<Button-1>",pdss)


btn3=tk.Button(root,text="九九乘法表")
btn3.place(x=145,y=243,width=145,height=30)
btn3.bind("<Button-1>",jjcfb)

btn4=tk.Button(root,text="小游戏")
btn4.place(x=219,y=183,width=72,height=30)
btn4.bind("<Button-1>",shuzi)


btn3=tk.Button(root,text="退格")
btn3.place(x=0,y=212,width=145,height=30)
btn3.bind("<Button-1>",shuzi)

btn2=tk.Button(root,text="清空")
btn2.place(x=145,y=212,width=145,height=30)
btn2.bind("<Button-1>",shuzi)

root.mainloop()