import csv
import tkinter as tk

root=tk.Tk()
root.title("Contact Info")
root.geometry("150x150")

def read_csv():
    read=tk.Tk()
    read.title("See Contacts")
    read.geometry("500x500")
    contact_info=tk.Label(read,text="")
    contact_info.pack(pady=3)
    info=[]
    with open("contact.csv","r",newline="") as file:
        reader=csv.reader(file)
        for row in reader:
            info.append(row)
    contact_info.config(text="\n".join([", ".join(r) for r in info]))
    dele=tk.Button(read,text="Delete Contact",command=del_contact)
    dele.pack(pady=5)
    read.mainloop()
def del_contact():
    delet= tk.Tk()
    delet.title("Delete Contact")
    delet.geometry("400x200")

    def delete():
        contact_delete = name_entry.get()
        info = []
        cont_find=False
        with open("contact.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != contact_delete:
                    info.append(row)
                else:
                    cont_find=True

        with open("contact.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(info)

        if cont_find:
            res.config(text=f"Contact '{contact_delete}' deleted.")
        else:
            res.config(text=f"Contact '{contact_delete}' was not found. Try Again.")
        name_entry.delet(0, tk.END)

    label_name = tk.Label(delet, text="Name of Contact to Delete:")
    label_name.pack(pady=5)
    name_entry = tk.Entry(delet)
    name_entry.pack(pady=5)
    submit = tk.Button(delet, text="Delete", command=delete)
    submit.pack(pady=5)
    res = tk.Label(delet, text="")
    res.pack(pady=5)
    delet.mainloop()
def add_contact():
    add=tk.Tk()
    add.title("Add Contact")
    add.geometry("400x350")
    def add_contact1():
        name=name_entry.get()
        phone=int(number_entry.get())
        email=mail_entry.get()
        result=""
        try:
            contact=[name,phone,email]
            with open("contact.csv","a",newline="") as file:
                wr=csv.writer(file)
                wr.writerow(contact)
            result="Contact Added"
            res.config(text=result)
        except Exception as e:
            result="Something Went Wrong"
            res.config(text=result)
    label_name=tk.Label(add,text="Name:")
    label_name.pack(pady=5)
    name_entry=tk.Entry(add)
    name_entry.pack(pady=5)
    label_phone=tk.Label(add,text="Phone:")
    label_phone.pack(pady=5)
    number_entry=tk.Entry(add)
    number_entry.pack(pady=5)
    label_email=tk.Label(add,text="Email:")
    label_email.pack(pady=5)
    mail_entry=tk.Entry(add)
    mail_entry.pack(pady=5)
    submit=tk.Button(add,text="Add",command=add_contact1)
    submit.pack(pady=5)
    res=tk.Label(add,text="")
    res.pack(pady=5)
    add.mainloop()

seeContact=tk.Button(root,text="See Contacts",command=read_csv)
seeContact.pack(pady=10)
contactAdd=tk.Button(root,text="Add Contact",command=add_contact)
contactAdd.pack(pady=10)

root.mainloop()