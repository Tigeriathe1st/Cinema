#A0BFFF
#4f5d73
#c75c5c
#b04535
from tkinter import *
import tkinter.messagebox
import pymysql
from pymysql.cursors import DictCursor


# Головний клас, який створює вікно і на ньому розміщаються емблема та назва програми
class MainWindow:
    def __init__(self, root):
        self.root = root
        #визначаємо ширину екрану і розміщаємо програму по центру
        self.w = self.root.winfo_screenwidth() // 2
        self.h = self.root.winfo_screenheight() // 2
        self.w = self.w - 550
        self.h = self.h - 380
        self.root.geometry(f'1100x700+{self.w}+{self.h}')
        self.root.config(bg='#A0BFFF')
        self.root.overrideredirect(1)
        #виводимо на екран емблему і назву
        self.close_btn = Button(self.root, text='Quit',font=('Courier',13), bd=0,bg='#c75c5c',fg='#000',activebackground='#b04535',activeforeground='#fff', command =self.close)
        self.close_btn.place(x=1050,y=0)
        #self.ico = PhotoImage(file='mainico.gif')
        #self.name = PhotoImage(file='D:\Boys\Ibrahim\cinema\namelbl.gif')
        #self.icolbl = Label(self.root,image='mainico.gif',bg='#A0BFFF')
        #self.icolbl.place(x=40,y=35)
        #self.namelbl = Label(self.root,image='namelbl.gif',bg='#A0BFFF')
        #self.namelbl.place(x=190,y=0)
        
    def close(self):
        self.root.destroy()


#Підклас головного вікна, на ньому елементи входу.
class LoginWindow(MainWindow):
    def __init__(self,root,conn,cursor):
        self.root = root
        self.conn = conn
        self.cursor = cursor
    def drawWind(self):
        self.login_main_lbl = Label(self.root,text='Login',font=('Courier',28,'bold'),bg='#A0BFFF',fg='#4f5d73')
        self.login_main_lbl.place(x=540,y=230)
        self.war_entry_lbl = Label(self.root,text='Fill in this form!',font=('Courier',20),bg='#A0BFFF',fg='#A0BFFF')
        self.war_entry_lbl.place(x=450,y=270)
        self.war_login_lbl = Label(self.root,text='''Doesn't exist!''',font=('Courier',20),bg='#A0BFFF',fg='#A0BFFF')
        self.war_login_lbl.place(x=430,y=350)
        self.war_pass_lbl = Label(self.root,text='Inncorrect password!',font=('Courier',20),bg='#A0BFFF',fg='#A0BFFF')
        self.war_pass_lbl.place(x=430,y=420)
        self.login_lbl = Label(self.root,text='Login:',font=('Courier',20),bg='#A0BFFF',fg='#4f5d73')
        self.login_lbl.place(x=320,y=320)
        self.login_entry = Entry(self.root,font=('Courier',20),bd=0,justify='center')
        self.login_entry.place(x=430,y=320)
        
        self.pass_lbl = Label(self.root,text='Password:',font=('Courier',20),bg='#A0BFFF',fg='#4f5d73')
        self.pass_lbl.place(x=285,y=390)
        self.pass_entry = Entry(self.root,font=('Courier',20),bd=0,justify='center',show='•')
        self.pass_entry.place(x=430,y=390)
        
        self.log_btn = Button(self.root,text='Login',font=('Courier',22), bd=0,bg='#c75c5c',fg='#fff',activebackground='#b04535',activeforeground='#000',command=self.login_in)
        self.log_btn.place(x=540,y=470)
        
        self.reg_btn = Button(self.root,text='Make a new account!',font=('Courier',22), bd=0,bg='#c75c5c',fg='#fff',activebackground='#b04535',activeforeground='#000',command = lambda: reg_in(self,reg))
        self.reg_btn.place(x=400,y=550)
    def deleteWind(self):
        self.login_main_lbl.destroy()
        self.login_lbl.destroy()
        self.login_entry.destroy()
        self.pass_lbl.destroy()
        self.pass_entry.destroy()
        self.log_btn.destroy()
        self.reg_btn.destroy()
        self.war_entry_lbl.destroy()
    def entry(self):
        if self.login_entry.get().strip() == '' or self.pass_entry.get().strip() == '':
            return True
        else:
            False
    def login_in(self):
        if self.entry():
            self.war_entry_lbl.config(fg='#c75c5c')
        else:
            self.war_entry_lbl.config(fg='#A0BFFF')
            self.cursor.execute('''
            SELECT login FROM users WHERE login=%s
            ''',self.login_entry.get())
            if self.cursor.fetchall() == ():
                self.war_login_lbl.config(fg='#c75c5c')
            else:
                self.war_login_lbl.config(fg='#A0BFFF')
                self.data = (self.login_entry.get(),self.pass_entry.get())
                self.cursor.execute('''
                SELECT * FROM users WHERE login=%s and password=%s
                ''',self.data)
                if self.cursor.fetchall() == ():
                    self.war_pass_lbl.config(fg='#c75c5c')
                else:
                    self.war_pass_lbl.config(fg='#A0BFFF')
                    self.deleteWind()
                    tkinter.messagebox.showinfo(message = 'Login successful!')
    

class RegisterWindow(MainWindow):
    def __init__(self,root , conn,cursor):
        self.root = root
        self.conn = conn
        self.cursor = cursor
    def drawWind(self):
        self.war_entry_lbl = Label(self.root,text='Fill this form!',font=('Courier',20),bg='#A0BFFF',fg='#A0BFFF')
        self.war_entry_lbl.place(x=400,y=220)
        self.war_login_lbl = Label(self.root,text='Login is already taken!',font=('Courier',18),bg='#A0BFFF',fg='#A0BFFF')
        self.war_login_lbl.place(x=150,y=265)
        self.reg_main_lbl = Label(self.root,text='Registration',font=('Courier',28,'bold'),bg='#A0BFFF',fg='#4f5d73')
        self.reg_main_lbl.place(x=430,y=180)
        self.login_lbl = Label(self.root,text='Login:',font=('Courier',20),bg='#A0BFFF',fg='#4f5d73')
        self.login_lbl.place(x=45,y=300)
        self.login_entry = Entry(self.root,font=('Courier',20),bd=0,justify='center')
        self.login_entry.place(x=150,y=302)
        
        self.pass_lbl = Label(self.root,text='Password:',font=('Courier',20),bg='#A0BFFF',fg='#4f5d73')
        self.pass_lbl.place(x=0,y=360)
        self.pass_entry = Entry(self.root,font=('Courier',20),bd=0,justify='center',show='•')
        self.pass_entry.place(x=150,y=362)


        self.name_lbl = Label(self.root,text="Name:",font=('Courier',20),bg='#A0BFFF',fg='#4f5d73')
        self.name_lbl.place(x=650,y=300)
        self.name_entry = Entry(self.root,font=('Courier',20),bd=0,justify='center')
        self.name_entry.place(x=740,y=302)

        self.firstname_lbl = Label(self.root,text="Surname:",font=('Courier',20),bg='#A0BFFF',fg='#4f5d73')
        self.firstname_lbl.place(x=600,y=360)
        self.firstname_entry = Entry(self.root,font=('Courier',20),bd=0,justify='center')
        self.firstname_entry.place(x=740,y=362)
        

        self.age_lbl = Label(self.root,text="Your age:",font=('Courier',20),bg='#A0BFFF',fg='#4f5d73')
        self.age_lbl.place(x=380,y=450)
        self.age_entry = Entry(self.root,font=('Courier',20),bd=0,justify='center',width=3)
        self.age_entry.place(x=540,y=452)

        
        
        self.back_btn = Button(self.root,text='Назад',font=('Courier',22), bd=0,bg='#c75c5c',fg='#fff',activebackground='#b04535',activeforeground='#000',command = lambda: log_in(login, self))
        self.back_btn.place(x=500,y=610)
        
        self.reg_btn = Button(self.root,text='Зареєструватися',font=('Courier',22), bd=0,bg='#c75c5c',fg='#fff',activebackground='#b04535',activeforeground='#000',command = self.registration)
        self.reg_btn.place(x=410,y=540)
        
    def deleteWind(self):
        self.reg_main_lbl.destroy()
        self.login_lbl.destroy()
        self.login_entry.destroy()
        self.pass_lbl.destroy()
        self.pass_entry.destroy()
        self.name_lbl.destroy()
        self.name_entry.destroy()
        self.firstname_lbl.destroy()
        self.firstname_entry.destroy()
        self.age_lbl.destroy()
        self.age_entry.destroy()
        self.back_btn.destroy()
        self.reg_btn.destroy()
        self.war_entry_lbl.destroy()
        self.war_login_lbl.destroy()
    
    def entry(self):
        if self.login_entry.get().strip() == '' or self.pass_entry.get().strip() == '' or self.name_entry.get().strip() == '' or self.firstname_entry.get().strip() == '' or self.age_entry.get().strip() == '':
            return True
        else:
            return False
    
    def isloginfree(self):
        self.cursor.execute('''
        SELECT * FROM users WHERE login=%s
        ''',self.login_entry.get())
        if self.cursor.fetchall() == ():
            return False
        else:
            return True 
    
    def registration(self):
        self.login = self.login_entry.get()
        self.password = self.pass_entry.get()
        self.name = self.name_entry.get()
        self.firstname = self.firstname_entry.get()
        self.age = self.age_entry.get()
        self.data = (self.login, self.password, self.name, self.firstname, self.age)
        if self.entry():
            self.war_entry_lbl.config(fg='#c75c5c')
        else:
            self.war_entry_lbl.config(fg='#A0BFFF')
            if self.isloginfree():
                self.war_login_lbl.config(fg='#c75c5c')
            else:
                self.war_login_lbl.config(fg='#A0BFFF')
                sql = '''
                INSERT INTO users(login, password, name, first_name, age) VALUES(%s,%s,%s,%s,%s)
                '''
                self.cursor.execute(sql,self.data)
                self.conn.commit()
                log_in(login,self)
                tkinter.messagebox.showinfo(message = 'Account was created successful!')
        
class MainInWindow(MainWindow):
    def __init__(self,root):
        self.root = root
    def drawWind(self):
        self.acc_btn = Button(self.root,text='Account',font=('Courier',22), bd=0,bg='#c75c5c',fg='#fff',activebackground='#b04535',activeforeground='#000',command=lambda:change(self,changeWind))
        self.acc_btn.place(x=940,y=60)
        self.hot_lbl = Label(self.root,text='New movies',font=('Courier',20,'bold'),bg='#A0BFFF',fg='#c75c5c')
        self.hot_lbl.place(x=45,y=180)
        self.schedule_lbl = Label(self.root,text='Timetable of sessions',font=('Courier',20,'bold'),bg='#A0BFFF',fg='#4f5d73')
        self.schedule_lbl.place(x=500,y=180)
        self.tick_lbl = Label(self.root,text='My tickets',font=('Courier',20,'bold'),bg='#A0BFFF',fg='#4f5d73')
        self.tick_lbl.place(x=900,y=180)
        self.hot_lbl.bind('<Button-1>', self.hot_click)
        self.schedule_lbl.bind('<Button-1>', self.schedule_click)
        self.tick_lbl.bind('<Button-1>', self.tick_click)
        
        self.hot_lbl.bind('<Enter>', self.hot_in)
        self.hot_lbl.bind('<Leave>', self.hot_out)
        self.schedule_lbl.bind('<Enter>', self.schedule_in)
        self.schedule_lbl.bind('<Leave>', self.schedule_out)
        self.tick_lbl.bind('<Enter>', self.tick_in)
        self.tick_lbl.bind('<Leave>', self.tick_out)
    def deleteWind(self):
        self.acc_btn.destroy()
        self.hot_lbl.destroy()
        self.schedule_lbl.destroy()
        self.tick_lbl.destroy()
    def hot_click(self,event):
        self.hot_lbl.config(fg='#c75c5c')
        self.schedule_lbl.config(fg='#4f5d73')
        self.tick_lbl.config(fg='#4f5d73')
    def schedule_click(self,event):
        self.hot_lbl.config(fg='#4f5d73')
        self.schedule_lbl.config(fg='#c75c5c')
        self.tick_lbl.config(fg='#4f5d73')
    def tick_click(self,event):
        self.hot_lbl.config(fg='#4f5d73')
        self.schedule_lbl.config(fg='#4f5d73')
        self.tick_lbl.config(fg='#c75c5c')
    def hot_in(self,event):
        self.hot_lbl.config(borderwidth=1, relief="solid")
    def hot_out(self,event):
        self.hot_lbl.config(borderwidth=0)
    def schedule_in(self,event):
        self.schedule_lbl.config(borderwidth=1, relief="solid")
    def schedule_out(self,event):
        self.schedule_lbl.config(borderwidth=0)
    def tick_in(self,event):
        self.tick_lbl.config(borderwidth=1, relief="solid")
    def tick_out(self,event):
        self.tick_lbl.config(borderwidth=0)
class ChangeWind(MainWindow):
    def __init__(self,root,conn,cursor):
        self.root = root
        self.conn = conn
        self.cursor = cursor
    def drawWind(self):
        self.exit_btn = Button(self.root,text='Logout',font=('Courier',22), bd=0,bg='#c75c5c',fg='#fff',activebackground='#b04535',activeforeground='#000',command=lambda:log_in(login,self))
        self.exit_btn.place(x=940,y=60)
    def deleteWind(self):
        self.exit_btn.destroy()

def reg_in(loginwindow, regwindow):
    loginwindow.deleteWind()
    regwindow.drawWind()
def log_in(loginwindow, regwindow):
    regwindow.deleteWind()
    loginwindow.drawWind()
        
#функції, для руху програми з будь-якого місця
def on_mouse_down(event):
    global dif_x, dif_y
    win_position = [int(coord) for coord in root.wm_geometry().split('+')[1:]]
    dif_x, dif_y = win_position[0] - event.x_root, win_position[1] - event.y_root
def update_position(event):
    root.wm_geometry("+%d+%d" % (event.x_root + dif_x, event.y_root + dif_y))

conn = pymysql.connect(
    host='91.239.233.38',
    user='fmewmhwr_dasdoom',
    password='danya123@',
    db='fmewmhwr_theatre',
    cursorclass=DictCursor
)
cursor = conn.cursor()

root = Tk() 
#root.iconphoto(False,PhotoImage(file='icon.ico')) 
root.bind('<ButtonPress-1>', on_mouse_down)
root.bind('<B1-Motion>', update_position)
main = MainWindow(root)
login = LoginWindow(root,conn,cursor)
login.drawWind()
reg = RegisterWindow(root,conn,cursor)
inwind = MainInWindow(root)
changeWind = ChangeWind(root,conn,cursor)
changeWind.drawWind()
root.mainloop()
conn.close()
