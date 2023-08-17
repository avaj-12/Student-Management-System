from tkinter import *
from tkinter.messagebox import *
from location import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt

def functioncall(num):
	if num==1:
		add_win.deiconify()
		Window_main.withdraw()
	elif num==2:
		view_win.deiconify()
		Window_main.withdraw()
		text_area.delete(1.0,END)
		info=''
		con=None
		try:
			con=connect('kit.db')
			cursor=con.cursor()
			sql="select * from student "
			cursor.execute(sql)
			cursor.execute("SELECT * FROM student ORDER BY rno")
			data=cursor.fetchall()
			for d in data:
					info=info+"Roll NO:"+str(d[0])+"\t\t"+"Name: "+str(d[1])+"\t\t"+"Marks: "+str(d[2])+"\n \n"
			text_area.insert(INSERT, info)
		except ValueError:
			showerror("Error","Enter Integer only")
			con.rollback()		
		except Exception as e:
			showerror('Failure', e)
			con.rollback()
		finally:
			if con is not None:
				con.close()
	elif num==3:
		update_win.deiconify()
		Window_main.withdraw()
	elif num==4:
		delete_win.deiconify() 
		Window_main.withdraw()
	elif num==5:
		marks=[ ]
		name=[ ]
		info=''
		con=None
		try:
			con=connect('kit.db')
			cursor=con.cursor()
			sql="select * from student "
			cursor.execute(sql)
			cursor.execute("SELECT * FROM student ORDER BY rno")
			data=cursor.fetchall()
			for d in data:
				marks.append(int(d[2]))
				name.append(d[1])
		except Exception as e:
			print('Failure', e)
		
		finally:
			if con is not None:
				con.close()
		plt.bar(name,marks,width=0.25)
		plt.title("Class performance")
		plt.xlabel("Name")
		plt.ylabel("Marks")
		plt.show()
	elif num==6:
		add_win.withdraw()
		Window_main.deiconify()  
	elif num==7:
		view_win.withdraw()
		Window_main.deiconify()  
	elif num==8:
		update_win.withdraw()
		Window_main.deiconify()    
	elif num==9:
		delete_win.withdraw()
		Window_main.deiconify()    

def oprationcall(num):
	if num==1:
		con=None
		try:
			con=connect('kit.db')
			cursor=con.cursor()
			sql="insert into student values('%d', '%s', '%d')"
			rollno=int(ent_roll.get())
			name=ent_name.get()
			mark=int(ent_mark.get())
			if (rollno>0) and (len(name)>=2 and name.isalpha()) and (mark<=100 and mark>=0):
				cursor.execute(sql % (rollno, name, mark))
				con.commit()
				showinfo("Success", "Record Added")
				ent_name.delete(0,END)
				ent_mark.delete(0,END)
				ent_roll.delete(0,END)
			else:
				if (not type(rollno) is int) or (rollno<=0):
					ent_roll.delete(0,END)
					raise TypeError(showerror("Invalid Input", "Roll Number Should Positive and Non-Zero"))
				if len(name)<2 or(name==" ")or not (name.isalpha()):
					ent_name.delete(0,END)
					raise Exception(showerror("Invalid Input", "Invalid Name"))
				if (not type(mark) is int) or (mark>100 or mark<0):
					ent_mark.delete(0,END)
					raise TypeError(showerror("Invalid Input", "Marks Should Less Than 100 and Positive"))
		except ValueError:
			showerror("Error","Enter Integer only")
			con.rollback()
			ent_mark.delete(0,END)
			ent_roll.delete(0,END)

		finally:
			if con is not None:
				con.close()			
	elif num==2:
		con=None
		try:
			con=connect('kit.db')
			cursor=con.cursor()
			rno=int(ent_uroll.get())
			name=ent_uname.get()
			marks=int(ent_umark.get())
			sql="update student set name='%s',marks='%d' where rno='%d'"
			if (rno>0) and (len(name)>=2 and name.isalpha()) and (marks<=100 and marks>=0):
				cursor.execute(sql%(name,marks , rno))
				if cursor.rowcount>0:
					showinfo("Success","Record Updated")
					ent_uname.delete(0,END)
					ent_umark.delete(0,END)
					ent_uroll.delete(0,END)
					con.commit()
				else:
					ent_uname.delete(0,END)
					ent_umark.delete(0,END)
					ent_uroll.delete(0,END)
					showerror("Error","Record does not exist")
			else:
				if (not type(rno) is int) or (rno<=0):
					ent_uroll.delete(0,END)
					raise TypeError(showerror("Invalid Input", "Roll Number Should Positive and Non-Zero"))
				elif len(name)<2 or(name==" ") or not (name.isalpha()):
					ent_uname.delete(0,END)
					raise Exception(showerror("Invalid Input", "Invalid Name"))
				elif (not type(marks) is int) or (marks>100 or marks<0):
					ent_umark.delete(0,END)
					raise TypeError(showerror("Invalid Input", "Marks Should Less Than 100 and Positive"))
		except ValueError:
			showerror("Error","Enter Integer only")
			con.rollback()
			ent_mark.delete(0,END)
			ent_roll.delete(0,END)
		except Exception as e:
				showerror("issue ",e)
				con.rollback()
		finally:
			if con is not None:
				con.close()
	elif num==3:
		con=None
		try:
			con=connect("kit.db")
			cursor=con.cursor()
			sql="delete from student where rno='%d'"
			rno=int(ent_droll.get())
			if (rno>0):
				cursor.execute(sql%(rno))
				if cursor.rowcount>0:
					showinfo("Success","Record Deleted")
					ent_droll.delete(0,END)
					ent_droll.focus()
					con.commit()
				else:
					ent_droll.delete(0,END)
					showerror("Error","Record does not exist")
			else:
				if (not type(rno) is int) or (rno<=0):
					ent_droll.delete(0,END)
					raise TypeError(showerror("Invalid Input", "Roll Number Should Positive and Non-Zero"))	
		except ValueError:
			showerror("Error","Enter Integer only")
			ent_droll.delete(0,END)
			con.rollback()
		except Exception as e:
			ent_droll.delete(0,END)
			showerror("Error","issue ")
			con.rollback()
		finally:
			if con is not None:
				con.close()

l=('arial',20,'bold')

Window_main=Tk()


Window_main.title("Student Management System")
Window_main.geometry("1000x700+100+20")
Window_main.configure(bg="light blue")


btn_add=Button(Window_main,text='Add',width=6,font=l,command=lambda:functioncall(1))

btn_view=Button(Window_main,text='View',width=6,font=l,command=lambda:functioncall(2))

btn_update=Button(Window_main,text='Update',width=6,font=l,command=lambda:functioncall(3))

btn_delete=Button(Window_main,text='Delete',width=6,font=l,command=lambda:functioncall(4))

btn_charts=Button(Window_main,text='Charts',width=6,font=l,command=lambda:functioncall(5))

btn_add.configure(bg="#4C516D")
btn_view.configure(bg="#4C516D")
btn_update.configure(bg="#4C516D")
btn_delete.configure(bg="#4C516D")
btn_charts.configure(bg="#4C516D")



loc="Location:"+location+'\t\t'+"Temperature: "+str(temp)
loc_label=Label(Window_main,text=loc,font=l,justify='left',anchor='w')

quot_label=Label(Window_main,text='Quote:\n'+msg,font=l,justify='left',wrap=800,anchor='w')

quot_label.configure(bg="light blue")

loc_label.configure(bg="light blue")

btn_add.pack(pady=10)
btn_view.pack(pady=10)
btn_update.pack(pady=10)
btn_delete.pack(pady=10)
btn_charts.pack(pady=10)

quot_label.pack(side='bottom',fill='both')

loc_label.pack(side='bottom',fill='both')


add_win=Toplevel(Window_main)

add_win.title("Add  New Student")
add_win.geometry("1000x700+100+20")

lbl_entr=Label(add_win,text="Enter Roll",font=l,anchor='n')
ent_roll=Entry(add_win,bd=5,font=l)

lbl_entr.pack(pady=10,fill='both')
ent_roll.pack(pady=10)
lbl_entr.configure(bg="light blue")

lbl_entn=Label(add_win,text="Enter Name",font=l,anchor='n')
ent_name=Entry(add_win,bd=5,font=l)

lbl_entn.pack(pady=10,fill='both')
ent_name.pack(pady=10)
lbl_entn.configure(bg="light blue")

lbl_entm=Label(add_win,text="Enter Marks",font=l,anchor='n')

ent_mark=Entry(add_win,bd=5,font=l)
lbl_entm.pack(pady=10,fill='both')
ent_mark.pack(pady=10)
lbl_entm.configure(bg="light blue")

btn_save=Button(add_win,text='Save',width=6,font=l,command=lambda:oprationcall(1))	

btn_back=Button(add_win,text='Back',width=6,font=l,command=lambda:functioncall(6))	

btn_save.pack(pady=10)
btn_back.pack(pady=10)

btn_save.configure(bg="#4C516D")
btn_back.configure(bg="#4C516D")

add_win.configure(bg="light blue")
add_win.withdraw()
view_win=Toplevel(Window_main)
view_win.configure(bg="light blue")
view_win.title("View Student")
view_win.geometry("1000x700+100+20")

text_area=ScrolledText(view_win,width=60,height=15,font=l)
text_area.pack()
text_area.configure(bg="#95C8D8")
btn_viewback=Button(view_win,text='Back',width=6,font=l,command=lambda:functioncall(7))
btn_viewback.pack(pady=10)
btn_viewback.configure(bg="#4C516D")


view_win.withdraw()

update_win=Toplevel(Window_main)

update_win.title("Update Student")
update_win.geometry("1000x700+100+20")

lbl_uentr=Label(update_win,text="Enter Roll",font=l,anchor='n')
ent_uroll=Entry(update_win,bd=5,font=l)

lbl_uentr.pack(pady=10,fill='both')
ent_uroll.pack(pady=10)
lbl_uentr.configure(bg="light blue")

lbl_uentn=Label(update_win,text="Enter Name",font=l,anchor='n')
ent_uname=Entry(update_win,bd=5,font=l)

lbl_uentn.pack(pady=10,fill='both')
ent_uname.pack(pady=10)
lbl_uentn.configure(bg="light blue")

lbl_uentm=Label(update_win,text="Enter Marks",font=l,anchor='n')

ent_umark=Entry(update_win,bd=5,font=l)
lbl_uentm.pack(pady=10,fill='both')
ent_umark.pack(pady=10)
lbl_uentm.configure(bg="light blue")

btn_usave=Button(update_win,text='Save',width=6,font=l,command=lambda:oprationcall(2))	
btn_uback=Button(update_win,text='Back',width=6,font=l,command=lambda:functioncall(8))	
btn_usave.pack(pady=10)
btn_uback.pack(pady=10)

btn_usave.configure(bg="#4C516D")
btn_uback.configure(bg="#4C516D")

update_win.configure(bg="light blue")
update_win.withdraw()

delete_win=Toplevel(Window_main)
delete_win.configure(bg="light blue")
delete_win.title("Delete Student")
delete_win.geometry("1000x700+100+20")

lbl_dentr=Label(delete_win,text="Enter Roll",font=l,anchor='n')
lbl_dentr.pack(pady=10,fill='both')
lbl_dentr.configure(bg="light blue")

ent_droll=Entry(delete_win,bd=5,font=l)
ent_droll.pack(pady=10)


btn_delete=Button(delete_win,text='Delete',width=6,font=l,command=lambda:oprationcall(3))	
btn_dback=Button(delete_win,text='Back',width=6,font=l,command=lambda:functioncall(9))	
btn_delete.pack(pady=10)
btn_dback.pack(pady=10)
btn_delete.configure(bg="#4C516D")
btn_dback.configure(bg="#4C516D")
delete_win.withdraw()

Window_main.mainloop()
