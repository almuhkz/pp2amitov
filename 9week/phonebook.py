from  tkinter import *
import psycopg2
root = Tk()
root.title('ALMUKHAMEDS PHONEBOOK')
root.iconbitmap('C:\\Users\\amito\\OneDrive\\Documents\\PP2\\9week\\phonebook.png')
root.geometry("700x750")
def query():
    config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='almuh'
    )
    c = config.cursor()
#create phonebook table
    c.execute('''CREATE TABLE IF NOT EXISTS customers
    (c_id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    phone_number INTEGER)
    ''')
    config.commit()
    config.close()
def submit():
    config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='almuh'
    )
    c = config.cursor()
    #insert data
    c.execute('''INSERT INTO customers (c_id , first_name, last_name, phone_number)
    VALUES(%s, %s, %s, %s)''', (i_name.get(),f_name.get(),l_name.get(),p_name.get()
    ))
    config.commit()
    config.close()

def update():
    config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='almuh'
    )
    c = config.cursor()
    c.execute("SELECT * FROM customers")
    records = c.fetchall()
    output = ''
    #loop cherez data
    for record in records:
        output_label.config(text=f'{output}\n{record[0]} {record[1]} {record[2]} {record[3]}')
        output = output_label['text']
    config.close()
def edit():
    config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='almuh'
    )
    c = config.cursor()
    #insert data
    sql ='''UPDATE customers set first_name = %s, phone_number=%s where c_id = %s'''
    c.execute(sql,(f_name.get(),p_name.get(),i_name.get()))
    config.commit()
    update()
    config.close()
def delete():
    config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='almuh'
    )
    c = config.cursor()
    #insert data
    sql ='''DELETE from customers where first_name=%s;'''
    c.execute(sql,(f_name.get(),))
    config.commit()
    update()
    config.close()
# Create The GUI For The App
my_frame = LabelFrame(root, text="Postgres PHONEBOOK BY ALMUH")
my_frame.pack(pady=20)

f_label= Label(my_frame, text="First Name:")
f_label.grid (row=0, column=0, pady=10, padx=10)
f_name = Entry(my_frame, font=("Impact, 18")) 
f_name.grid (row=0, column=1, pady=10, padx=10)

l_label= Label (my_frame, text="Last Name:")
l_label.grid (row=1, column=0, pady=10, padx=10)
l_name = Entry(my_frame, font=("Impact, 18")) 
l_name.grid (row=1, column=1, pady=10, padx=10)

p_label= Label (my_frame, text="Phone Number:")
p_label.grid (row=2, column=0, pady=10, padx=10)
p_name = Entry(my_frame, font=("Impact, 18")) 
p_name.grid (row=2, column=1, pady=10, padx=10)

i_label= Label (my_frame, text="ID: ")
i_label.grid (row=3, column=0, pady=10, padx=10)
i_name = Entry(my_frame, font=("Impact, 18")) 
i_name.grid (row=3, column=1, pady=10, padx=10)

submit_button = Button (my_frame, text="Submit", command=submit)
submit_button.grid(row=4, column=0, pady=10, padx=10)

update_button = Button (my_frame, text="Update", command=update)
update_button.grid (row=4, column=1, pady=10, padx=10)

edit_button = Button (my_frame, text="EDIT DATA", command=edit)
edit_button.grid (row=4, column=2, pady=10, padx=10)

edit_button = Button (my_frame, text="DELETE CUSTOMER", command=delete)
edit_button.grid (row=4, column=2, pady=10, padx=10)


#dropall_button = Button (my_frame, text="DROP ALL DATA", command=drop)
#dropall_button.grid (row=3, column=2, pady=10, padx=10)

output_label= Label (root, text="")
output_label.pack(pady=50)

query()
root.mainloop()