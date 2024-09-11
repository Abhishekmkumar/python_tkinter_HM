import customtkinter
from customtkinter import *
import random
from time import strftime
from datetime import datetime
import cx_Oracle
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = CTk()
root.title("Hotel Management")

root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
# ----------------------------------------------------------------------------------------------------------------------
HM = CTkLabel(root, text="Hotel Management", font=("Caliber", 45))
HM.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
# ----------------------------------------------------------------------------------------------------------------------
# logic
label_list_f2 = ['order_number_label_f2', 'cost_label_f2', 'service_cost_label_f2', 'tax_label_f2', 'sub_total_label_f2', 'total_label_f2']
entry_list_f1 = ['drink_entry_f1', 'burger_entry_f1', 'cherry_entry_f1', 'nacho_fries_entry_f1', 'pizza_entry_f1', 'biscuits_entry_f1', 'roll_entry_f1', 'tea_entry_f1']
def database():
    f2 = ["o_1_l", "o_2_l", "o_3_l", "o_4_l", "o_5_l", "o_6_l"]
    f1 = ["l_b_1", "l_b_2", "l_b_3", "l_b_4", "l_b_5", "l_b_6", "l_b_7", "l_b_8"]

    f1_ = {}
    for name, el_f1 in zip(f1, entry_list_f1):
        f1_[name] = entry_dict_f1[el_f1].get()

    c_l = time_string
    d_l = date_string
    t_5_f_e = text_f6.get("1.0", "end-1c")

    f2[0] = random_num
    f2[1] = cost_tot
    f2[2] = service_cost_tot
    f2[3] = tot_sub
    f2[4] = tot_tax
    f2[5] = tot

    con = cx_Oracle.connect("hr/hr@localhost:1521/orclpdb")
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO HOTEL_MAN(ORDER_NUMBER, DRINK, BURGER, CHERRY, NACHO_FRIES, PIZZA, BISCUIT, ROLL, TEA, "
            "COST_, SERVICE_COST, TAX, SUB_TOTAL, TOTAL, DATE_REC, TIME_REC, EXTRAS) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,"
            ":10,:11,:12,:13,:14,:15,:16,:17)", (
            f2[0], f1_[f1[0]], f1_[f1[1]], f1_[f1[2]], f1_[f1[3]], f1_[f1[4]], f1_[f1[5]], f1_[f1[6]], f1_[f1[7]], f2[1], f2[2], f2[4], f2[3], f2[5], d_l, c_l,
            t_5_f_e))

        con.commit()
        data_submit_message = messagebox.showinfo("Databse", "Data Inserted Successfully")

    except cx_Oracle.DatabaseError as e:
        print(e)

    finally:
        cur.close()
        con.close()

def close_price_win():
    global price_window

    if price_window is not None:
        price_window.destroy()
        price_window = None

price_window = None
def price():
    global price_window

    if price_window is None:
        price_window = CTkToplevel()
        price_window.title("Price")
        price_window.attributes('-topmost', True)
        price_window.configure(fg_color="Alice Blue")

        prize_label = ["Drink", "Burger", "Cherry", "Nacho Fries", "Pizza", "Biscuits", "Roll", "Tea"]
        amt = [180, 1000, 100, 500, 2000, 125, 75, 60]

        for i, text in enumerate(prize_label):
            label = CTkLabel(price_window, text=text, font=("Caliber", 20, "bold"), text_color="black")
            label.grid(row=i, column=0, padx=20, pady=10, sticky="w")

        for i, text in enumerate(amt):
            label = CTkLabel(price_window, text=text, font=("Caliber", 20, "bold"), text_color="black")
            label.grid(row=i, column=1, padx=20, pady=10)

        price_window.protocol("WM_DELETE_WINDOW", close_price_win)

def close_info_win():
    global info_window

    if info_window is not None:
        info_window.destroy()
        info_window = None

info_window = None
def info():
    global info_window

    if info_window is None:
        info_window = CTkToplevel()
        info_window.title("Info")
        info_window.attributes('-topmost', True)
        info_window.configure(fg_color="Alice Blue")

        info_texts = [
            "This is a dedicated hotel management application.",
            "Enter the required number of items in the input field next to the label in the first frame.",
            "To view the price of each item, press the 'Price' button.",
            "To calculate the subtotal and total amounts, press the 'Total' button.",
            "The 'Reset' button clears all entries and output fields, including designated labels.",
            "The 'Exit' button closes the main window, as well as any other open windows.",
            "C button in calculator works as a backspace if clicked.",
            "To clear entire entry in calculator press and hold C button.",
            "Submit button submits entire value including date and time to database."
        ]

        title = CTkLabel(info_window, text="HOTEL MANAGEMENT", font=("Caliber", 30, "bold"), text_color="black")
        title.grid(row=0, column=0, padx=10, pady=10)

        for i, text in enumerate(info_texts):
            lable = CTkLabel(info_window, text=f"{i+1}) {text}", font=("Caliber", 20, "bold"), text_color="black")
            lable.grid(row=i+1, column=0, padx=20, pady=10, sticky="w")

        info_window.protocol("WM_DELETE_WINDOW", close_info_win)

def order_number():
    global label_list_f2, random_num

    if cost_tot is None or cost_tot == 0:
        random_num = 0
    else:
        order_number_rec = []
        label_dict_f2[label_list_f2[0]].grid_forget()
        # random
        random_num = random.getrandbits(20)
        while random_num in order_number_rec:
            random_num = random.getrandbits(20)
        order_number_rec.append(random_num)
    label_dict_f2[label_list_f2[0]].configure(text=f"{random_num}")
    label_dict_f2[label_list_f2[0]].grid(row=0, column=1, padx=10, pady=10, sticky="e")

def cost():
    global label_list_f2, cost_tot, entry_list_f1

    cost_name = ["b1_f1", "b2_f1", "b3_f1", "b4_f1", "b5_f1", "b6_f1", "b7_f1", "b8_f1"]

    cost_dict = {}
    for entry_key, cost_key in zip(entry_list_f1, cost_name):
         cost_dict[cost_key] = entry_dict_f1[entry_key].get()

    ans_values = []
    num = [180, 1000, 100, 500, 2000, 125, 75, 60]
    for cost_key, value in zip(cost_name, num):
        ans = int(cost_dict[cost_key]) if cost_dict[cost_key] else 0
        ans_values.append(ans * value)
    cost_tot = sum(ans_values)
    label_dict_f2[label_list_f2[1]].configure(text=f"{cost_tot}")
    label_dict_f2[label_list_f2[1]].grid(row=1, column=1, padx=10, pady=10, sticky="e")

    if cost_tot is None or cost_tot == 0:
        root_submit.configure(state="disabled")
    else:
        root_submit.configure(state="normal")

def service_cost():
    global label_list_f2, service_cost_tot

    if cost_tot is None or cost_tot == 0:
        service_cost_tot = 0
    else:
        service_cost_tot = random.getrandbits(6)
    label_dict_f2[label_list_f2[2]].configure(text=f"{service_cost_tot}")
    label_dict_f2[label_list_f2[2]].grid(row=2, column=1, padx=10, pady=10, sticky="e")

def tax():
    global tot_tax

    tot_tax = round((tot_sub*18)/100)
    label_dict_f2[label_list_f2[3]].configure(text=f"{tot_tax}")
    label_dict_f2[label_list_f2[3]].grid(row=3, column=1, padx=10, pady=10, sticky="e")

def sub_tot():
    global tot_sub

    tot_sub = cost_tot+service_cost_tot
    label_dict_f2[label_list_f2[4]].configure(text=f"{tot_sub}")
    label_dict_f2[label_list_f2[4]].grid(row=4, column=1, padx=10, pady=10, sticky="e")

def total():
    global tot

    tot = tot_sub+tot_tax
    label_dict_f2[label_list_f2[5]].configure(text=f"{tot}")
    label_dict_f2[label_list_f2[5]].grid(row=5, column=1, padx=10, pady=10, sticky="e")

def execute_all():
    cost()
    order_number()
    service_cost()
    sub_tot()
    tax()
    total()

def root_total():
    execute_all()

def reset():
    global entry_list_f1, label_list_f2

    for elist_f1 in entry_list_f1:
        entry_dict_f1[elist_f1].delete(0, END)

    for llist_f2 in (label_list_f2):
        label_dict_f2[llist_f2].grid_forget()

    entry_f5.delete(0, END)
    text_f6.delete(1.0,END)

    root_submit.configure(state="disabled")

def exit():
    root.destroy()

def button_click(value):
    if entry_f5.get() == "ERROR":
        entry_f5.delete(0, END)
        entry_f5.insert(END, value)
    else:
        entry_f5.insert(END, value)

def equals():
    e_f5 = entry_f5.get()
    try:
        ans = eval(e_f5)
        entry_f5.delete(0, END)
        entry_f5.insert(END, ans)
    except:
        entry_f5.delete(0, END)
        entry_f5.insert(END, "ERROR")

def clear():
    entry_f5.delete(0, END)
# ----------------------------------------------------------------------------------------------------------------------
# first frame
first_frame = CTkFrame(root, border_width=1, border_color="white", height=370, width=320)
first_frame.grid(row=1,column=0, padx=10, pady=10)

first_frame.grid_columnconfigure(0, weight=1)
first_frame.grid_columnconfigure(1, weight=1)
first_frame.grid_rowconfigure([i for i in range(8)], weight=1)
first_frame.grid_propagate(False)

# first frame labels
labels_f1 = ["Drink", "Burger", "Cherry", "Nacho Fries", "Pizza", "Biscuits", "Roll", "Tea"]

for i, text in enumerate(labels_f1):
    label_f1 = CTkLabel(first_frame, text=text, font=("Caliber", 20))
    label_f1.grid(row=i, column=0, sticky="w", padx=10, pady=10)

# first frame entries
entry_dict_f1 = {}
for i, text in enumerate(labels_f1):
    entry_name_f1 = f"{text.lower().replace(" ", "_")}_entry_f1"
    entry_dict_f1[entry_name_f1] = CTkEntry(first_frame)
    entry_dict_f1[entry_name_f1].grid(row=i, column=1, sticky="e", padx=10)
# ----------------------------------------------------------------------------------------------------------------------
# second frame
second_frame = CTkFrame(root, border_width=1, border_color="white", height=300, width=300)
second_frame.grid(row=1, column=1, padx=10, pady=10)

second_frame.grid_columnconfigure(0, weight=1)
second_frame.grid_columnconfigure(1, weight=1)
second_frame.grid_rowconfigure([i for i in range(6)], weight=1)
second_frame.grid_propagate(False)

# second frame labels
labels_f2 = ["Order Number", "Cost", "Service Cost", "Tax", "Sub Total", "Total"]

for i, text in enumerate(labels_f2):
    label_f2 = CTkLabel(second_frame, text=text, font=("Caliber", 20))
    label_f2.grid(row=i, column=0, padx=10, pady=10, sticky="w")

label_dict_f2 = {}
for i, text in enumerate(labels_f2):
    label_name_f2 = f"{text.lower().replace(" ", "_")}_label_f2"
    label_dict_f2[label_name_f2] = CTkLabel(second_frame, text="", font=("Caliber", 20))
    # label_dict_f2[label_name_f2].grid(row=i, column=1, padx=10, sticky="e", pady=10)
# ----------------------------------------------------------------------------------------------------------------------
# third frame
third_frame = CTkFrame(root, border_color="white")
third_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

third_frame.grid_columnconfigure([i for i in range(4)], weight=1)
third_frame.grid_rowconfigure(0, weight=1)

# third frame buttons
buttons_f3 = ["Price", "Total", "Reset", "Exit"]
buttons_command_list_f3 = [price, root_total, reset, exit]

for i, (text, bcl_f3) in enumerate(zip(buttons_f3, buttons_command_list_f3)):
    button_f3 = CTkButton(third_frame, text=text, font=("Caliber", 15), height=40, command=bcl_f3)
    button_f3.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
# ----------------------------------------------------------------------------------------------------------------------
# fourth frame
fourth_frame = CTkFrame(root, border_width=1, border_color="white")
fourth_frame.grid(row=0, column=2, padx=10, pady=10)

fourth_frame.grid_rowconfigure([i for i in range(2)], weight=1)
fourth_frame.grid_columnconfigure(0, weight=1)

def update_time():
    global time_string, date_string

    time_string = strftime('%I:%M:%S %p')
    clock_label.configure(text=f"{time_string}")
    clock_label.after(1000, update_time)

    today = datetime.today().date()
    date_string = strftime('%d-%m-%y')
    date_label.configure(text=f"{date_string}")

clock_label = CTkLabel(fourth_frame, text="", font=("Caliber", 30, "bold"))
clock_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

date_label = CTkLabel(fourth_frame, text="", font=("Caliber", 20, "bold"))
date_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

update_time()
# ----------------------------------------------------------------------------------------------------------------------
# fifth frame
fifth_frame = CTkFrame(root, border_width=0, border_color="white")
fifth_frame.grid(row=1, column=2, padx=10, pady=10)

fifth_frame.grid_columnconfigure([i for i in range(4)], weight=1)
fifth_frame.grid_rowconfigure([i for i in range(5)], weight=1)

entry_f5 = CTkEntry(fifth_frame, height=30, width=100, font=("Caliber", 15))
entry_f5.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons_name_list_f5 = ["b1_f5", "b2_f5", "b3_f5", "b4_f5", "b5_f5", "b6_f5", "b7_f5", "b8_f5", "b9_f5", "b10_f5", "b11_f5", "b12_f5", "b13_f5", "b14_f5", "b15_f5", "b16_f5"]
button_1_f5 = ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", "C", "0", "=", "/"]
buttons_command_list_f5 = [lambda:button_click("1"), lambda:button_click("2"), lambda:button_click("3"), lambda:button_click("+"), lambda:button_click("4"),
                           lambda:button_click("5"), lambda:button_click("6"), lambda:button_click("-"), lambda:button_click("7"), lambda:button_click("8"),
                           lambda:button_click("9"), lambda:button_click("*"), clear, lambda:button_click("0"), equals, lambda:button_click("/")]

button_dict_f5 = {}
for i, (button_f5, button_1_f5, bcl_f5) in enumerate(zip(buttons_name_list_f5, button_1_f5, buttons_command_list_f5)):
    row = i//4
    column = i%4
    button_dict_f5[button_f5] = CTkButton(fifth_frame, text=button_1_f5, width=80, height=60, command=bcl_f5)
    button_dict_f5[button_f5].grid(row=row+1, column=column, padx=2, pady=2, sticky="nsew")
# ----------------------------------------------------------------------------------------------------------------------
# sixth frame
global text_f6

sixth_frame = CTkFrame(root, border_width=0, border_color="white")
sixth_frame.grid(row=2, column=2, padx=10, pady=30)

sixth_frame.grid_rowconfigure([i for i in range(2)], weight=1)
sixth_frame.grid_columnconfigure(0, weight=1)
def clear_f6():
    text_f6.delete(1.0, END)

text_f6 = CTkTextbox(sixth_frame, height=90, width=330, font=("Caliber", 15))
text_f6.grid(row=0, column=0, sticky="nsew")

button_f6 = CTkButton(sixth_frame, text="Clear", font=("Caliber",15), command=clear_f6)
button_f6.grid(row=1,column=0, sticky="nsew")
# ----------------------------------------------------------------------------------------------------------------------
# info button
info = CTkButton(root, text="i", width=50, height=50, corner_radius=100, font=("Caliber", 25, "bold"), command=info)
info.grid(row=0, column=3, padx=10, pady=10)

# submit button
root_submit = CTkButton(root, text="Submit", height=40, width=120, state="disabled", command=database)
root_submit.grid(row=2, column=3, padx=20, sticky="ew")

root.mainloop()