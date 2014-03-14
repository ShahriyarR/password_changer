
# Written Quick script for Oracle User Password Changing
# Email: rzayev.sehriyar@gmail.com

#SQL> create user xxx identified by xyz123;
#
#User created.
#
#SQL> grant create session to xxx;
#
#Grant succeeded.


#SQL> create user passwd identified by Bxyz123$Pasha;
#
#User created.
#
#SQL> grant create session to passwd;
#
#Grant succeeded.
#
#SQL> grant alter user to passwd;
#
#Grant succeeded.

from Tkinter import Label,Entry,Button,Tk,END,Toplevel,Message
import cx_Oracle


master = Tk()


Label(master, text="Username:").grid(row=1)
Label(master, text="Old Password:").grid(row=2)
Label(master, text="New Password:").grid(row=3)


e2 = Entry(master)
e3 = Entry(master,show="*")
e4 = Entry(master, show="*")


e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

def OnButtonClick():
    

    e2.focus_set()
    e2.selection_range(0, END)

    e3.focus_set()
    e3.selection_range(0, END)

    e4.focus_set()
    e4.selection_range(0, END)
    
    win = Toplevel()
    win.title("Program Answer")
    if len(oracle_old_connection(e2.get(), e3.get())) > 0:
        cur = oracle_connection()
        alter_string = 'alter user %s identified by %s' % (e2.get(), e4.get())
        cur.execute(alter_string)
        message = "Password Successfully Updated"
        
        msg = Message(win, text=message)
        msg.pack()
        button = Button(win, text='OK', command=win.destroy)
        button.pack()
    else:
        message = "Error!!!!"
        
        msg = Message(win, text=message)
        msg.pack()
        button = Button(win, text='OK', command=win.destroy)
        button.pack()
        

def ClearFields():
    
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

button = Button(master, text=u"Change Password !", command=OnButtonClick)
button.grid(column=0, row=5, sticky='EW')


clear_fields = Button(master, text=u"Clear Fields!", command=ClearFields)
clear_fields.grid(column=0, row=4)

master.grid_columnconfigure(0, weight=3)
master.resizable(True, False)

def oracle_connection():
    pass_string = 'passwd/Bxyz123$Pasha@IP_ADDRESS_HERE/ORACLE_SID_HERE'
    
    con = cx_Oracle.connect(pass_string)
    cur = con.cursor()
    return cur



def oracle_old_connection(username, old_password):
    pass_actual_string = '%s/%s@IP_ADDRESS_HERE/ORACLE_SID_HERE' % (username, old_password)
    con = cx_Oracle.connect(pass_actual_string)
    return con.version


master.title("Password Changer")
master.geometry('300x200')
master.mainloop()


