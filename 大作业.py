import sqlite3
import tkinter
import tkinter.ttk
import tkinter.messagebox
import webbrowser

def dosql(sql):
    #连接数据库，并执行操作，主要用于查询
    conn=sqlite3.connect("d:\\2021大学计算机报告\\mydatabase.sqlite")
    cur=conn.cursor()
    x=cur.execute(sql)
    x=list(x)
    conn.commit()
    conn.close()
    return x
def dosql2(sql):
    #连接数据库，执行操作，主要用于其他
    conn=sqlite3.connect("d:\\2021大学计算机报告\\mydatabase.sqlite")
    cur=conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
#创建主界面
root=tkinter.Tk()
root.geometry('500x500')
root.title("各国人均GDP比较")
root.resizable(False,False)
#插入文本框组件
paiming=tkinter.Label(root,text="排名:")
paiming.place(x=5,y=5,width=40,height=20)
srpm=tkinter.Entry(root)
srpm.place(x=50,y=5,width=150,height=20)

guojia=tkinter.Label(root,text="国家:")
guojia.place(x=200,y=5,width=40,height=20)
srgj=tkinter.Entry(root)
srgj.place(x=250,y=5,width=150,height=20)

szz=tkinter.Label(root,text="所在洲:")
szz.place(x=5,y=50,width=50,height=20)
xzszz=tkinter.ttk.Combobox(root,values=("亚洲","欧洲","非洲","大洋洲","美洲"))
xzszz.place(x=50,y=50,width=150,height=20)

gdp=tkinter.Label(root,text="GDP")
gdp.place(x=200,y=50,width=40,height=20)
srgdp=tkinter.Entry(root)
srgdp.place(x=250,y=50,width=150,height=20)
 
#插入表格
frame=tkinter.Frame(root)
frame.place(x=0,y=180,width=480,height=280)
#确定表格内部填充格式与内容
scrollbar=tkinter.Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

tal=tkinter.ttk.Treeview(frame,columns=("c1","c2","c3","c4"),show="headings",yscrollcommand=scrollbar.set)
tal.column("c1",width=70,anchor="center")
tal.column("c2",width=120,anchor="center")
tal.column("c3",width=70,anchor="center")
tal.column("c4",width=120,anchor="center")
tal.heading("c1",text="排名")
tal.heading("c2",text="国家地区")
tal.heading("c3",text="所在洲")
tal.heading("c4",text="人均GDP")
tal.pack(side=tkinter.RIGHT,fill=tkinter.Y)
scrollbar.config(command=tal.yview)
#更新数据的函数并显示在表中
def binddata():
    for row in tal.get_children():
        tal.delete(row)
    conn=sqlite3.connect("d:\\2021大学计算机报告\\mydatabase.sqlite")
    cur=conn.cursor()
    cur.execute("select * from new")
    temp=cur.fetchall()
    conn.close()
    for i,j in enumerate(temp):
        if i == 0:
            continue
        tal.insert("",i,values=j)
binddata()

nametd=tkinter.StringVar("")
def tclick(event):
    if not tal.selection():
        return
    j=tal.selection()[0]
    nametd.set(tal.item(j,"values")[0])
tal.bind("<Button-1>",tclick)
#添加按钮函数
def bac():
    #检查排名
    paiming1=srpm.get().strip()
    if paiming1=="":
        tkinter.messagebox.showerror(title="很抱歉",message="必须输入排名")
        return 
    if not paiming1.isdigit():
        tkinter.messagebox.showerror(title="很抱歉",message="排名必须为数字")
        return
    #检查所在洲
    suozaizhou1=xzszz.get().strip()
    if suozaizhou1=="":
        tkinter.messagebox.showerror(title="很抱歉",message="必须输入所在洲")
        return
    guojia1=srgj.get().strip()
    if guojia1=="":
        tkinter.messagebox.showerror(title="很抱歉",message="必须输入国家")
        return
    GDP1=srgdp.get().strip()
    if GDP1=="":
        tkinter.messagebox.showerror(title="很抱歉",message="必须输入GDP")
        return
    
    if not GDP1.isdigit():
        tkinter.messagebox.showerror(title="很抱歉",message="GDP必须为数字")
        return
    
    sql="insert into new(排名,国家地区,所在洲,人均GDP美元计)values('%s','%s','%s','%s')"%(paiming1,guojia1,suozaizhou1,GDP1)
    dosql2(sql)
    binddata()
buttonadd=tkinter.Button(root,text="添加",command=bac)
buttonadd.place(x=120,y=140,width=80,height=20)
#删除按钮函数
def buttondelet():
    paiming1=nametd.get()
    print(paiming1)
    if paiming1=="":
        tkinter.messagebox.showerror(title="很抱歉",message="请选择一条记录")
        return
    sql="delete from new where 排名=%s"%paiming1
    dosql(sql)
    tkinter.messagebox.showinfo("恭喜","删除成功")
    nametd.set("")
    binddata()
buttond=tkinter.Button(root,text="删除",command=buttondelet)
buttond.place(x=240,y=140,width=80,height=20)

#按排名查询
def chaxun():
    a=srpm.get().strip()
    if a=="":
        tkinter.messagebox.showerror(title="很抱歉",message="必须输入排名")
    if int(a)>203:
        tkinter.messagebox.showerror(title="很抱歉",message="排名必须在1到203之间")
        return
    sql="select * from new where 排名=%s"%a
    b=dosql(sql)
    c=str(b)
    tkinter.messagebox.showinfo("查询结果",c)
    binddata()
buttonc=tkinter.Button(root,text="查询排名",command=chaxun)
buttonc.place(x=120,y=120,width=80,height=20)

#按国家查询
def chaxun1():
    d=srgj.get().strip()
    if d=="":
        tkinter.messagebox.showerror(title="很抱歉",message="请输入国家")
        return
    sql="select * from new where 国家地区='%s'"%d
    e=dosql(sql)
    f=str(e)
    if e==[]:
        tkinter.messagebox.showerror(title="很抱歉",message="所查询国家不存在")
        return
    tkinter.messagebox.showinfo("查询结果",f)
    binddata()
buttonf=tkinter.Button(root,text="查询国家",command=chaxun1)
buttonf.place(x=240,y=120,width=80,height=20)
#按所在洲查询
def chaxun2():
    g=xzszz.get().strip()
    if g=="":
        tkinter.messagebox.showerror(title="很抱歉",message="请选择要查询的洲")
        return
    sql="select * from new where 所在洲='%s'"%g
    h=dosql(sql)
    o=str(h)
    tkinter.messagebox.showinfo("查询结果",o)
    binddata()
buttono=tkinter.Button(root,text="查询所在洲",command=chaxun2)
buttono.place(x=120,y=100,width=80,height=20)

def zhchaxun():
    a1=srpm.get().strip()
    a2=xzszz.get().strip()
    a3=srgj.get().strip()
    sql="select * from new where 1=1 "

    if a1!=None:
        sql=sql+"and 排名='%s'"%a1
    if a2!=None:
        sql=sql+"and 所在洲='%s'"%a2
    if a3!=None:
        sql=sql+"and 国家地区='%s'"%a3
    
    b1=dosql(sql)
    b2=str(b1)
    if b2=="[]":
        tkinter.messagebox.showerror(title="很抱歉",message="请正确输入前三条信息")
    else:
        tkinter.messagebox.showinfo("综合查询结果",b2)
    binddata()
buttonzh=tkinter.Button(root,text="综合查询",command=zhchaxun)
buttonzh.place(x=240,y=100,width=80,height=20)

root.mainloop()


