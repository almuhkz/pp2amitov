from tkinter import *#almuh ispolzuet snova tkinter
import tkinter as tk #uprostit
from tkinter import ttk #vidzhet
from tkinter import messagebox, filedialog  #dlya gui
import psycopg2 #sql
import csv
import os

mydata= [] #dlya csv



def update(rows):
    global mydata
    mydata = rows
    trv.delete(*trv.get_children())#tkinter treeview dlya tablic
    for i in rows: 
        trv.insert('', 'end', values=i)
             
def search():
    q2 = q.get()
    query= "SELECT id, first_name, last_name, phone_number FROM customers WHERE first_name LIKE '%"+q2+"%' OR last_name LIKE '%"+q2+"%' OR phone_number LIKE '%"+q2+"%'" 
    cursor.execute(query) 
    rows= cursor.fetchall()
    update(rows)

def clear():
    query= "SELECT id, first_name, last_name, phone_number FROM customers"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def getrow(event):#otobrazhenie texta v secii customer
    rowid = trv.identify_row(event.y)
    item=trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1]) 
    t3.set(item['values'][2])
    t4.set(item['values'][3])

def update_customer():
    fname = t2.get() 
    lname= t3.get()
    phone_number = t4.get()
    custid = t1.get()
    if messagebox.askyesno ("Confirm Please", "Are You Sure you want to update this customer?"): 
        query= "UPDATE customers SET first_name = %s, last_name = %s, phone_number=%s WHERE id=%s" 
        cursor.execute(query, (fname, lname, phone_number, custid))
        mydb.commit()
        clear()
    else:
        return True

def add_new():
    id = t1.get()
    fname = t2.get()
    lname = t3.get() 
    phone_number = t4.get()
    query= "INSERT INTO customers(id, first_name, last_name, phone_number) VALUES (NULL, %s, %s, %s)" 
    cursor.execute(query, (fname, lname, phone_number))
    mydb.commit()
    clear()

def delete_customer():
    customer_id = t1.get()
    if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this customer?"): 
        query= "DELETE FROM customers WHERE id= "+customer_id 
        cursor.execute(query)
        mydb.commit()
        clear()
    else:
        return True

def export():
    if len(mydata) < 1:
        messagebox.showerror("No Data", "No data available to export") 
        return False
    fln= filedialog.asksaveasfilename(initialdir = os.getcwd(), title="Save CSV", filetypes=(("CSV File", ".csv"), ("All Files", "*.*"))) 
    with open(fln, mode='w') as myfile: 
        exp_writer = csv.writer(myfile, delimiter=',')
        for i in mydata:
            exp_writer.writerow(1)
    messagebox.showinfo("Data Exported", "Your data has been exported to "+os.path.basename(fln)+" successfully.")

def importcsv():
    mydata.clear()
    fln= filedialog.askopenfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File", ".csv"), ("ALL Files", "*.*")))
    with open(fln) as myfile:
        csvread = csv.reader(myfile, delimiter=",") 
        for i in csvread:
            mydata.append(i)

def savedb():
    if messagebox.askyesno("Confirmation", "Are you sure you want to save data to Database"):
        for i in mydata: 
            id = i[0]
            fname = i[0]
            lname = i[1]
            phone_number=i[2]
            query= "INSERT INTO customers( first_name, last_name, phone_number) VALUES ( %s, %s, %s)" 
            cursor.execute(query, (fname, lname, phone_number)) 
            mydb.commit()
            clear()
            messagebox.showinfo("Data Saved", "Data has been saved to database")
    else:
        return False 

mydb= psycopg2.connect(host='localhost', database='postgres',port = '5432',user='postgres', password='almuh') 
cursor= mydb.cursor()

root = Tk()

q = StringVar() 
t1 =  StringVar() 
t2 = StringVar()
t3= StringVar()
t4= StringVar()

wrapper1= LabelFrame (root, text="Customer List")
wrapper2 = LabelFrame (root, text="Search") 
wrapper3 = LabelFrame (root, text="Customer Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10) 
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="6") 
trv.pack()

trv.heading(1, text="Customer ID")
trv.heading(2, text="First Name") 
trv.heading(3, text="Last Name")
trv.heading(4, text="Phone Number")

trv.bind('<Double 1>', getrow)
expbtn= Button(wrapper1, text="Export CSV", command=export) 
expbtn.pack(side=tk.LEFT, padx=10, pady=10)

impbtn = Button (wrapper1, text="Import CSV", command=importcsv) 
impbtn.pack(side=tk.LEFT, padx=10, pady=10)

savebtn = Button (wrapper1, text="Save Data", command=savedb) 
savebtn.pack(side=tk.LEFT, padx=10, pady=10)

extbtn = Button (wrapper1, text="Exit", command=lambda: exit()) 
extbtn.pack(side=tk.LEFT, padx=10, pady=10)

query= "SELECT id, first_name, last_name, phone_number from customers"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)


#Search Section
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk. LEFT, padx=10)

ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk. LEFT, padx=6)

btn= Button(wrapper2, text="Search", command=search)
btn.pack(side= tk. LEFT, padx=6)

#User Data Section
lbl1 = Label(wrapper3, text="Customer ID") 
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3) 

lbl2= Label(wrapper3, text="First Name") 
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2= Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label (wrapper3, text="Last Name") 
lbl3.grid(row=2, column=0, padx=5, pady=3) 
ent3 = Entry(wrapper3, textvariable=t3) 
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label (wrapper3, text="Phone Number") 
lbl4.grid(row=3, column=0, padx=5, pady=3) 
ent4 = Entry(wrapper3, textvariable=t4) 
ent4.grid(row=3, column=1, padx=5, pady=3)


up_btn = Button (wrapper3, text="Update", command=update_customer) 
add_btn= Button (wrapper3, text="Add New", command=add_new) 
delete_btn= Button (wrapper3, text="Delete", command=delete_customer)

add_btn.grid(row=4, column=0, padx=5, pady=3) 
up_btn.grid (row=4, column=1, padx=5, pady=3) 
delete_btn.grid (row=4, column=2, padx=5, pady=3)


root.title("ALMUKHAMEDS PHONEBOOK") 
root.geometry("800x700") 
root.iconbitmap(r'phonebook.ico')
root.mainloop()