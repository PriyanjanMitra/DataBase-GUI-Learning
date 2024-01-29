import mysql.connector
import tkinter
from tkinter import ttk
import csv


def login():
    global user_label
    global user_entry
    global pass_label
    global pass_entry
    global login_button_new
    login_button.place_forget()
    user_label = tkinter.Label(root, text="Username:", font=("Times New Roman", 15, "bold"))
    pass_label = tkinter.Label(root, text="Password:", font=("Times New Roman", 15, "bold"))
    user_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    pass_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"), show="*")
    login_button_new = tkinter.Button(root, text="Login", font=("Times New Roman", 15, "bold"),
                                      command=login_check)
    user_entry.place(x=200, y=200)
    pass_entry.place(x=200, y=250)
    user_label.place(x=100, y=200)
    pass_label.place(x=100, y=250)
    login_button_new.place(x=270, y=300)


def login_check():
    global success
    global menu_button
    global failed
    login = open('login.csv', 'r')
    reader = list(csv.reader(login))
    username = user_entry.get()
    password = pass_entry.get()
    if [username, password] in reader:
        user_entry.place_forget()
        user_label.place_forget()
        pass_entry.place_forget()
        pass_label.place_forget()
        login_button_new.place_forget()
        success = tkinter.Label(root, text="Login Successful", font=("Times New Roman", 15, "bold"))
        menu_button = tkinter.Button(root, text="Continue", font=("Times New Roman", 15, "bold"), command=menu)
        success.place(x=250, y=300)
        menu_button.place(x=270, y=350)
        failed.place_forget()
    else:
        failed = tkinter.Label(root, text="Login Failed.Try Again", font=("Times New Roman", 15, "bold"))
        failed.place(x=200, y=400)


def menu():
    global showall_button
    global add_button
    global delete_button
    global update_button
    global logout_button
    showall_button = tkinter.Button(root, text="Display all Aircraft", font=("Times New Roman", 15, "bold"),
                                    command=display)
    add_button = tkinter.Button(root, text="Add Aircraft", font=("Times New Roman", 15, "bold"), command=add)
    delete_button = tkinter.Button(root, text="Delete Aircraft", font=("Times New Roman", 15, "bold"), command=delete)
    update_button = tkinter.Button(root, text="Update Aircraft", font=("Times New Roman", 15, "bold"), command=update)
    logout_button = tkinter.Button(root, text="Logout", font=("Times New Roman", 15, "bold"), command=logout)
    success.place_forget()
    menu_button.place_forget()
    heading.place(x=50, y=0)
    showall_button.place(x=200, y=100)
    add_button.place(x=200, y=200)
    delete_button.place(x=200, y=300)
    update_button.place(x=200, y=400)
    logout_button.place(x=200, y=500)


def display():
    global arrival_display
    global departure_display
    arrival_display = tkinter.Button(root, text="Arrival", font=("Times New Roman", 15, "bold"),
                                     command=display_arrival)
    departure_display = tkinter.Button(root, text="Departure", font=("Times New Roman", 15, "bold"),
                                       command=display_departure)
    arrival_display.place(x=250, y=300)
    departure_display.place(x=250, y=400)
    showall_button.place_forget()
    add_button.place_forget()
    delete_button.place_forget()
    update_button.place_forget()
    logout_button.place_forget()


def display_arrival():
    global arr_dis_tree
    global goback
    heading.place_forget()
    arrival_display.place_forget()
    departure_display.place_forget()
    arr_dis_tree = ttk.Treeview(root)
    # Define Columns
    arr_dis_tree['columns'] = ('Callsign', "Departed From", "ETA")
    # Format Columns
    arr_dis_tree.column("#0", width=0, stretch=tkinter.NO)
    arr_dis_tree.column("Callsign", anchor=tkinter.CENTER, width=100)
    arr_dis_tree.column("Departed From", anchor=tkinter.CENTER, width=100)
    arr_dis_tree.column("ETA", anchor=tkinter.CENTER, width=100)
    # Create Headings
    arr_dis_tree.heading("#0", text="", anchor=tkinter.CENTER)
    arr_dis_tree.heading("Callsign", text="Callsign", anchor=tkinter.CENTER)
    arr_dis_tree.heading("Departed From", text="Departed From", anchor=tkinter.CENTER)
    arr_dis_tree.heading("ETA", text="ETA", anchor=tkinter.CENTER)
    airportcursor.execute("select * from arrival")
    count = 0
    for i in airportcursor:
        arr_dis_tree.insert(parent='', index='end', iid=count, text='', values=(i[0], i[1], i[2]))
        count += 1
    arr_dis_tree.pack()
    goback = tkinter.Button(root, text="Go Back", font=("Times New Roman", 15, "bold"), command=goback_display_arrival)
    goback.place(x=250, y=500)


def goback_display_arrival():
    goback.place_forget()
    arr_dis_tree.pack_forget()
    menu()


def display_departure():
    global dep_dis_tree
    global goback
    heading.place_forget()
    arrival_display.place_forget()
    departure_display.place_forget()
    dep_dis_tree = ttk.Treeview(root)
    # Define Columns
    dep_dis_tree['columns'] = ('Callsign', "Destination", "ETD")
    # Format Columns
    dep_dis_tree.column("#0", width=0, stretch=tkinter.NO)
    dep_dis_tree.column("Callsign", anchor=tkinter.CENTER, width=100)
    dep_dis_tree.column("Destination", anchor=tkinter.CENTER, width=100)
    dep_dis_tree.column("ETD", anchor=tkinter.CENTER, width=100)
    # Create Headings
    dep_dis_tree.heading("#0", text="", anchor=tkinter.CENTER)
    dep_dis_tree.heading("Callsign", text="Callsign", anchor=tkinter.CENTER)
    dep_dis_tree.heading("Destination", text="Destination", anchor=tkinter.CENTER)
    dep_dis_tree.heading("ETD", text="ETD", anchor=tkinter.CENTER)
    airportcursor.execute("select * from departure")
    count = 0
    for i in airportcursor:
        dep_dis_tree.insert(parent='', index='end', iid=count, text='', values=(i[0], i[1], i[2]))
        count += 1
    dep_dis_tree.pack()
    goback = tkinter.Button(root, text="Go Back", font=("Times New Roman", 15, "bold"),
                            command=goback_display_departure)
    goback.place(x=250, y=500)


def goback_display_departure():
    goback.place_forget()
    dep_dis_tree.pack_forget()
    menu()


def add():
    global arrival_add
    global departure_add
    arrival_add = tkinter.Button(root, text="Arrival", font=("Times New Roman", 15, "bold"),
                                 command=add_arrival)
    departure_add = tkinter.Button(root, text="Departure", font=("Times New Roman", 15, "bold"),
                                   command=add_departure)
    arrival_add.place(x=250, y=300)
    departure_add.place(x=250, y=400)
    showall_button.place_forget()
    add_button.place_forget()
    delete_button.place_forget()
    update_button.place_forget()
    logout_button.place_forget()


def add_arrival():
    global arrival_callsign_label
    global arrival_callsign_entry
    global arrival_departed_label
    global arrival_departed_entry
    global arrival_eta_label
    global arrival_eta_entry
    global arrival_add_button
    arrival_add.place_forget()
    departure_add.place_forget()
    arrival_callsign_label = tkinter.Label(root, text="Callsign:", font=("Times New Roman", 15, "bold"))
    arrival_departed_label = tkinter.Label(root, text="Departed From:", font=("Times New Roman", 15, "bold"))
    arrival_eta_label = tkinter.Label(root, text="ETA:", font=("Times New Roman", 15, "bold"))
    arrival_callsign_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    arrival_departed_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    arrival_eta_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    arrival_add_button = tkinter.Button(root, text="Add", font=("Times New Roman", 15, "bold"),
                                        command=add_arrival_continuation)
    arrival_callsign_entry.place(x=300, y=200)
    arrival_departed_entry.place(x=300, y=250)
    arrival_eta_entry.place(x=300, y=300)
    arrival_callsign_label.place(x=100, y=200)
    arrival_departed_label.place(x=100, y=250)
    arrival_eta_label.place(x=100, y=300)
    arrival_add_button.place(x=270, y=500)


def add_arrival_continuation():
    global details_added
    global goback
    arrival_add_button.place_forget()
    arrival_callsign_label.place_forget()
    arrival_callsign_entry.place_forget()
    arrival_departed_label.place_forget()
    arrival_departed_entry.place_forget()
    arrival_eta_label.place_forget()
    arrival_eta_entry.place_forget()
    airportcursor.execute("insert into arrival values(%s,%s,%s)",
                          (arrival_callsign_entry.get(), arrival_departed_entry.get(), arrival_eta_entry.get(),))
    airportdb.commit()
    details_added = tkinter.Label(root, text="Aircraft details added", font=("Times New Roman", 15, "bold"))
    goback = tkinter.Button(root, text="Go Back", font=("Times New Roman", 15, "bold"), command=goback_add_arrival)
    details_added.place(x=250, y=300)
    goback.place(x=250, y=400)


def goback_add_arrival():
    details_added.place_forget()
    goback.place_forget()
    menu()


def add_departure():
    global departure_callsign_label
    global departure_callsign_entry
    global departure_destination_label
    global departure_destination_entry
    global departure_etd_label
    global departure_etd_entry
    global departure_add_button
    arrival_add.place_forget()
    departure_add.place_forget()
    departure_callsign_label = tkinter.Label(root, text="Callsign:", font=("Times New Roman", 15, "bold"))
    departure_destination_label = tkinter.Label(root, text="Destination:", font=("Times New Roman", 15, "bold"))
    departure_etd_label = tkinter.Label(root, text="ETD:", font=("Times New Roman", 15, "bold"))
    departure_callsign_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    departure_destination_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    departure_etd_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    departure_add_button = tkinter.Button(root, text="Add", font=("Times New Roman", 15, "bold"),
                                          command=add_departure_continuation)
    departure_callsign_entry.place(x=300, y=200)
    departure_destination_entry.place(x=300, y=250)
    departure_etd_entry.place(x=300, y=300)
    departure_callsign_label.place(x=100, y=200)
    departure_destination_label.place(x=100, y=250)
    departure_etd_label.place(x=100, y=300)
    departure_add_button.place(x=270, y=500)


def add_departure_continuation():
    global details_added
    global goback
    departure_add_button.place_forget()
    departure_callsign_label.place_forget()
    departure_callsign_entry.place_forget()
    departure_destination_label.place_forget()
    departure_destination_entry.place_forget()
    departure_etd_label.place_forget()
    departure_etd_entry.place_forget()
    airportcursor.execute("insert into departure values(%s,%s,%s)",
                          (
                              departure_callsign_entry.get(), departure_destination_entry.get(),
                              departure_etd_entry.get(),))
    airportdb.commit()
    details_added = tkinter.Label(root, text="Aircraft details added", font=("Times New Roman", 15, "bold"))
    goback = tkinter.Button(root, text="Go Back", font=("Times New Roman", 15, "bold"), command=goback_add_departure)
    details_added.place(x=250, y=300)
    goback.place(x=250, y=400)


def goback_add_departure():
    details_added.place_forget()
    goback.place_forget()
    menu()


def delete():
    global arrival_delete
    global departure_delete
    arrival_delete = tkinter.Button(root, text="Arrival", font=("Times New Roman", 15, "bold"),
                                    command=delete_arrival)
    departure_delete = tkinter.Button(root, text="Departure", font=("Times New Roman", 15, "bold"),
                                      command=delete_departure)
    arrival_delete.place(x=250, y=300)
    departure_delete.place(x=250, y=400)
    showall_button.place_forget()
    add_button.place_forget()
    delete_button.place_forget()
    update_button.place_forget()
    logout_button.place_forget()


def delete_arrival():
    global arrival_callsign_label
    global arrival_callsign_entry
    global arrival_delete_button
    arrival_delete.place_forget()
    departure_delete.place_forget()
    arrival_callsign_label = tkinter.Label(root, text="Callsign:", font=("Times New Roman", 15, "bold"))
    arrival_callsign_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    arrival_delete_button = tkinter.Button(root, text="Delete", font=("Times New Roman", 15, "bold"),
                                           command=delete_arrival_continuation)
    arrival_callsign_entry.place(x=300, y=200)
    arrival_callsign_label.place(x=100, y=200)
    arrival_delete_button.place(x=270, y=500)


def delete_arrival_continuation():
    global details_deleted
    global goback
    arrival_delete_button.place_forget()
    arrival_callsign_label.place_forget()
    arrival_callsign_entry.place_forget()
    airportcursor.execute("delete from arrival where callsign=%s", (arrival_callsign_entry.get(),))
    airportdb.commit()
    details_deleted = tkinter.Label(root, text="Aircraft details deleted", font=("Times New Roman", 15, "bold"))
    goback = tkinter.Button(root, text="Go Back", font=("Times New Roman", 15, "bold"), command=goback_delete_arrival)
    details_deleted.place(x=250, y=300)
    goback.place(x=250, y=400)


def goback_delete_arrival():
    details_deleted.place_forget()
    goback.place_forget()
    menu()


def delete_departure():
    global departure_callsign_label
    global departure_callsign_entry
    global departure_delete_button
    arrival_delete.place_forget()
    departure_delete.place_forget()
    departure_callsign_label = tkinter.Label(root, text="Callsign:", font=("Times New Roman", 15, "bold"))
    departure_callsign_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    departure_delete_button = tkinter.Button(root, text="Delete", font=("Times New Roman", 15, "bold"),
                                             command=delete_departure_continuation)
    departure_callsign_entry.place(x=300, y=200)
    departure_callsign_label.place(x=100, y=200)
    departure_delete_button.place(x=270, y=500)


def delete_departure_continuation():
    global details_deleted
    global goback
    departure_delete_button.place_forget()
    departure_callsign_label.place_forget()
    departure_callsign_entry.place_forget()
    airportcursor.execute("delete from departure where callsign=%s", (departure_callsign_entry.get(),))
    airportdb.commit()
    details_deleted = tkinter.Label(root, text="Aircraft details deleted", font=("Times New Roman", 15, "bold"))
    goback = tkinter.Button(root, text="Go Back", font=("Times New Roman", 15, "bold"), command=goback_delete_departure)
    details_deleted.place(x=250, y=300)
    goback.place(x=250, y=400)


def goback_delete_departure():
    details_deleted.place_forget()
    goback.place_forget()
    menu()


def update():
    global arrival_update
    global departure_update
    arrival_update = tkinter.Button(root, text="Arrival", font=("Times New Roman", 15, "bold"),
                                    command=update_arrival)
    departure_update = tkinter.Button(root, text="Departure", font=("Times New Roman", 15, "bold"),
                                      command=update_departure)
    arrival_update.place(x=250, y=300)
    departure_update.place(x=250, y=400)
    showall_button.place_forget()
    add_button.place_forget()
    delete_button.place_forget()
    update_button.place_forget()
    logout_button.place_forget()


def update_arrival():
    global arrival_callsign_old_label
    global arrival_callsign_old_entry
    global arrival_update_button
    global arrival_callsign_new_entry
    global arrival_callsign_new_label
    global arrival_departed_new_entry
    global arrival_departed_new_label
    global arrival_eta_new_entry
    global arrival_eta_new_label
    arrival_update.place_forget()
    departure_update.place_forget()
    arrival_callsign_old_label = tkinter.Label(root, text="Old Callsign:", font=("Times New Roman", 15, "bold"))
    arrival_callsign_old_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    arrival_update_button = tkinter.Button(root, text="Update", font=("Times New Roman", 15, "bold"),
                                           command=update_arrival_continuation)
    arrival_callsign_old_entry.place(x=300, y=200)
    arrival_callsign_old_label.place(x=100, y=200)
    arrival_update_button.place(x=270, y=500)
    arrival_callsign_new_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    arrival_callsign_new_label = tkinter.Label(root, text="New Callsign:", font=("Times New Roman", 15, "bold"))
    arrival_departed_new_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    arrival_departed_new_label = tkinter.Label(root, text="New Departed From:", font=("Times New Roman", 15, "bold"))
    arrival_eta_new_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    arrival_eta_new_label = tkinter.Label(root, text="New ETA:", font=("Times New Roman", 15, "bold"))
    arrival_callsign_old_label.place(x=100, y=200)
    arrival_callsign_old_entry.place(x=300, y=200)
    arrival_callsign_new_label.place(x=100, y=250)
    arrival_callsign_new_entry.place(x=300, y=250)
    arrival_departed_new_label.place(x=100, y=300)
    arrival_departed_new_entry.place(x=300, y=300)
    arrival_eta_new_label.place(x=100, y=350)
    arrival_eta_new_entry.place(x=300, y=350)
    arrival_update_button.place(x=270, y=500)


def update_arrival_continuation():
    global details_updated
    global goback
    arrival_update_button.place_forget()
    arrival_callsign_old_label.place_forget()
    arrival_callsign_old_entry.place_forget()
    arrival_callsign_new_label.place_forget()
    arrival_callsign_new_entry.place_forget()
    arrival_departed_new_label.place_forget()
    arrival_departed_new_entry.place_forget()
    arrival_eta_new_label.place_forget()
    arrival_eta_new_entry.place_forget()
    airportcursor.execute("update arrival set callsign=%s, departedfrom=%s, eta=%s where callsign=%s",
                          (arrival_callsign_new_entry.get(), arrival_departed_new_entry.get(),
                           arrival_eta_new_entry.get(), arrival_callsign_old_entry.get(),))
    airportdb.commit()
    details_updated = tkinter.Label(root, text="Aircraft details updated", font=("Times New Roman", 15, "bold"))
    goback = tkinter.Button(root, text="Go Back", font=("Times New Roman", 15, "bold"), command=goback_update_arrival)
    details_updated.place(x=250, y=300)
    goback.place(x=250, y=400)


def goback_update_arrival():
    details_updated.place_forget()
    goback.place_forget()
    menu()


def update_departure():
    global departure_callsign_old_label
    global departure_callsign_old_entry
    global departure_update_button
    global departure_callsign_new_entry
    global departure_callsign_new_label
    global departure_destination_new_entry
    global departure_destination_new_label
    global departure_etd_new_entry
    global departure_etd_new_label
    departure_update.place_forget()
    arrival_update.place_forget()
    departure_callsign_old_label = tkinter.Label(root, text="Old Callsign:", font=("Times New Roman", 15, "bold"))
    departure_callsign_old_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    departure_update_button = tkinter.Button(root, text="Update", font=("Times New Roman", 15, "bold"),
                                             command=update_departure_continuation)
    departure_etd_new_label = tkinter.Label(root, text="New ETD:", font=("Times New Roman", 15, "bold"))
    departure_etd_new_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    departure_destination_new_label = tkinter.Label(root, text="New Destination:", font=("Times New Roman", 15, "bold"))
    departure_destination_new_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    departure_callsign_new_entry = tkinter.Entry(root, font=("Times New Roman", 15, "bold"))
    departure_callsign_new_label = tkinter.Label(root, text="New Callsign:", font=("Times New Roman", 15, "bold"))
    departure_callsign_old_label.place(x=100, y=200)
    departure_callsign_old_entry.place(x=300, y=200)
    departure_callsign_new_label.place(x=100, y=250)
    departure_callsign_new_entry.place(x=300, y=250)
    departure_destination_new_label.place(x=100, y=300)
    departure_destination_new_entry.place(x=300, y=300)
    departure_etd_new_label.place(x=100, y=350)
    departure_etd_new_entry.place(x=300, y=350)
    departure_update_button.place(x=270, y=500)


def update_departure_continuation():
    global details_updated
    global goback
    departure_update_button.place_forget()
    departure_callsign_old_label.place_forget()
    departure_callsign_old_entry.place_forget()
    departure_callsign_new_label.place_forget()
    departure_callsign_new_entry.place_forget()
    departure_destination_new_label.place_forget()
    departure_destination_new_entry.place_forget()
    departure_etd_new_label.place_forget()
    departure_etd_new_entry.place_forget()
    airportcursor.execute("update departure set callsign=%s, destination=%s, etd=%s where callsign=%s",
                          (departure_callsign_new_entry.get(), departure_destination_new_entry.get(),
                           departure_etd_new_entry.get(), departure_callsign_old_entry.get(),))
    airportdb.commit()
    details_updated = tkinter.Label(root, text="Aircraft details updated", font=("Times New Roman", 15, "bold"))
    goback = tkinter.Button(root, text="Go Back", font=("Times New Roman", 15, "bold"), command=goback_update_departure)
    details_updated.place(x=250, y=300)
    goback.place(x=250, y=400)


def goback_update_departure():
    details_updated.place_forget()
    goback.place_forget()
    menu()


def logout():
    showall_button.place_forget()
    add_button.place_forget()
    delete_button.place_forget()
    update_button.place_forget()
    logout_button.place_forget()
    thank_you = tkinter.Label(root, text="Thank You", font=("Times New Roman", 35, "bold"))
    thank_you.place(x=200, y=300)
    destroy()


def destroy():
    root.after(5000, lambda:root.destroy())


airportdb = mysql.connector.connect(host="localhost", user=YOUR_USERNAME,
                                    password=YOUR_PASSWORD, database=YOUR_DATABASE)
airportcursor = airportdb.cursor(buffered=True)
root = tkinter.Tk()
root.geometry('600x600')
root.title("Airport Management System")
heading = tkinter.Label(root, text="Delhi Airport Management System", font=("Times New Roman", 25, "bold"))
heading.place(x=50, y=0)
login_button = tkinter.Button(root, text="Login", font=("Times New Roman", 15, "bold"), command=login)
login_button.place(x=270, y=300)
root.mainloop()
