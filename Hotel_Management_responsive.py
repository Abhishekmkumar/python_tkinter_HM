import datetime
from tkinter import *
import time
from time import strftime
import random
from datetime import datetime
import cx_Oracle
from tkinter import messagebox

root = Tk()
root.title("Hotel Management")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Initialize variables
random_num = None
cost = None
random_s_c = None
round_tax = None
sub_tot = None
tot = None

# database
def database():
    global random_num, cost, random_s_c, round_tax, sub_tot, tot, date_string

    o_1_l = random_num

    l_b_1 = first_label_but.get()
    l_b_2 = second_label_but.get()
    l_b_3 = third_label_but.get()
    l_b_4 = fourth_label_but.get()
    l_b_5 = fifth_label_but.get()
    l_b_6 = sixth_label_but.get()
    l_b_7 = seventh_label_but.get()
    l_b_8 = eighth_label_but.get()

    o_2_l = cost
    o_3_l = random_s_c
    o_4_l = round_tax
    o_5_l = sub_tot
    o_6_l = tot

    c_l = clock_label.cget("text")
    d_l = date_string

    t_5_f_e = text_fifth_frame_entry.get("1.0", "end-1c")

    # create database
    # CREATE TABLE HOTEL_MAN( order_number NUMBER(7) PRIMARY KEY, drink NUMBER, burger
    # NUMBER, cherry NUMBER, nacho_fries NUMBER, pizza NUMBER, biscuit NUMBER, roll NUMBER, tea NUMBER, cost_ NUMBER,
    # service_cost NUMBER, tax NUMBER, sub_total NUMBER, total NUMBER, date_rec VARCHAR2(20), time_rec VARCHAR2(20), extras VARCHAR2(132));

    con = cx_Oracle.connect("hr/hr@localhost:1521/orclpdb")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO HOTEL_MAN(ORDER_NUMBER, DRINK, BURGER, CHERRY, NACHO_FRIES, PIZZA, BISCUIT, ROLL, TEA, "
                    "COST_, SERVICE_COST, TAX, SUB_TOTAL, TOTAL, DATE_REC, TIME_REC, EXTRAS) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,"
                    ":10,:11,:12,:13,:14,:15,:16,:17)", (o_1_l, l_b_1, l_b_2, l_b_3, l_b_4, l_b_5, l_b_6, l_b_7, l_b_8, o_2_l, o_3_l, o_4_l, o_5_l, o_6_l, d_l, c_l, t_5_f_e))

        con.commit()
        data_submit_message = messagebox.showinfo("Databse", "Data Inserted Successfully")

    except cx_Oracle.DatabaseError as e:
        print(e)

    finally:
        cur.close()
        con.close()

# prize windpw destroy
def close_prize_window():
    global prize_window
    if prize_window is not None:
        prize_window.destroy()
        prize_window = None

# new window prize
prize_window = None
def prize():
    global prize_window
    if prize_window is None:
        prize_window = Toplevel()
        prize_window.title("Prize")

        bg_col = "Alice Blue"
        prize_window.config(bg=bg_col)

        # 1st label
        label_1 = Label(prize_window, text="Drink", font=("Caliber",15,"bold"), bg=bg_col)
        label_1.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        label_2 = Label(prize_window, text="Burger", font=("Caliber",15,"bold"), bg=bg_col)
        label_2.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        label_3 = Label(prize_window, text="Cherry", font=("Caliber",15,"bold"), bg=bg_col)
        label_3.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        label_4 = Label(prize_window, text="Nacho Fries", font=("Caliber",15,"bold"), bg=bg_col)
        label_4.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        label_5 = Label(prize_window, text="Pizza", font=("Caliber",15,"bold"), bg=bg_col)
        label_5.grid(row=4, column=0, sticky="w", padx=10, pady=10)
        label_6 = Label(prize_window, text="Biscuit", font=("Caliber",15,"bold"), bg=bg_col)
        label_6.grid(row=5, column=0, sticky="w", padx=10, pady=10)
        label_7 = Label(prize_window, text="Roll", font=("Caliber",15,"bold"), bg=bg_col)
        label_7.grid(row=6, column=0, sticky="w", padx=10, pady=10)
        label_8 = Label(prize_window, text="Tea", font=("Caliber",15,"bold"), bg=bg_col)
        label_8.grid(row=7, column=0, sticky="w", padx=10, pady=10)

        # 2nd label
        label_1 = Label(prize_window, text="180", font=("Caliber", 15, "bold"), bg=bg_col)
        label_1.grid(row=0, column=1, padx=10, pady=10)
        label_2 = Label(prize_window, text="1000", font=("Caliber", 15, "bold"), bg=bg_col)
        label_2.grid(row=1, column=1, padx=10, pady=10)
        label_3 = Label(prize_window, text="100", font=("Caliber", 15, "bold"), bg=bg_col)
        label_3.grid(row=2, column=1, padx=10, pady=10)
        label_4 = Label(prize_window, text="500", font=("Caliber", 15, "bold"), bg=bg_col)
        label_4.grid(row=3, column=1, padx=10, pady=10)
        label_5 = Label(prize_window, text="2000", font=("Caliber", 15, "bold"), bg=bg_col)
        label_5.grid(row=4, column=1, padx=10, pady=10)
        label_6 = Label(prize_window, text="125", font=("Caliber", 15, "bold"), bg=bg_col)
        label_6.grid(row=5, column=1, padx=10, pady=10)
        label_7 = Label(prize_window, text="75", font=("Caliber", 15, "bold"), bg=bg_col)
        label_7.grid(row=6, column=1, padx=10, pady=10)
        label_8 = Label(prize_window, text="60", font=("Caliber", 15, "bold"), bg=bg_col)
        label_8.grid(row=7, column=1, padx=10, pady=10)
        label_b = Button(prize_window, text="Close", command=close_prize_window, font=("Caliber", 10), borderwidth=2, height=2, width=10)
        label_b.grid(row=8, column=1, padx=20, pady=20)
        sys_close = prize_window.protocol("WM_DELETE_WINDOW", close_prize_window)

# new window info
def close_info_window():
    global info_window
    if info_window is not None:
        info_window.destroy()
        info_window=None

info_window = None
def info():
    global info_window
    if info_window is None:
        info_window = Toplevel()
        info_window.title("Info")

        font_info = ("Caliber", 15, "bold")
        bg_col = "Alice Blue"
        info_window.config(bg=bg_col)

        info_l0 = Label(info_window, text="HOTEL MANAGEMENT", font=("Caliber", 19, "bold"), bg=bg_col, fg="Midnight blue")
        info_l0.grid(row=0, column=0, pady=20, padx=10)
        info_l1 = Label(info_window, text="1)  This is a dedicated hotel management application.", font=font_info, bg=bg_col)
        info_l1.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        info_l2 = Label(info_window, text="2)  Enter the required number of items in the input field next to the label in the first frame.", font=font_info, bg=bg_col)
        info_l2.grid(row=2, column=0, pady=10, padx=10, sticky='w')
        info_l3 = Label(info_window, text="3)  To view the price of each item, press the 'Price' button.", font=font_info, bg=bg_col)
        info_l3.grid(row=3, column=0, pady=10, padx=10, sticky='w')
        info_l4 = Label(info_window, text="4)  To calculate the subtotal and total amounts, press the 'Total' button.", font=font_info, bg=bg_col)
        info_l4.grid(row=4, column=0, pady=10, padx=10, sticky='w')
        info_l5 = Label(info_window, text="5)  The 'Reset' button clears all entries and output fields, including designated labels.", font=font_info, bg=bg_col)
        info_l5.grid(row=5, column=0, pady=10, padx=10, sticky='w')
        info_l6 = Label(info_window, text="6)  The 'Exit' button closes the main window, as well as any other open windows.", font=font_info, bg=bg_col)
        info_l6.grid(row=6, column=0, pady=10, padx=10, sticky='w')
        info_l7 = Label(info_window, text="7)  C button in calculator works as a backspace if clicked.", font=font_info, bg=bg_col)
        info_l7.grid(row=7, column=0, pady=10, padx=10, sticky='w')
        info_l8 = Label(info_window, text="8)  To clear entire entry in calculator press and hold C button.", font=font_info, bg=bg_col)
        info_l8.grid(row=8, column=0, pady=10, padx=10, sticky='w')
        info_l9 = Label(info_window, text="9)  Submit button submits entire value including date and time to database.", font=font_info, bg=bg_col)
        info_l9.grid(row=9, column=0, pady=10, padx=10, sticky='w')
        info_window.protocol("WM_DELETE_WINDOW", close_info_window)

# prize_range&calc
def prize_range_and_calc():
    global cost

    but_1l = first_label_but.get()
    but_2l = second_label_but.get()
    but_3l = third_label_but.get()
    but_4l = fourth_label_but.get()
    but_5l = fifth_label_but.get()
    but_6l = sixth_label_but.get()
    but_7l = seventh_label_but.get()
    but_8l = eighth_label_but.get()

    if but_1l:
        ans1 = int(but_1l) * 180
    else:
        ans1 = 0
    if but_2l:
        ans2 = int(but_2l) * 1000
    else:
        ans2 = 0
    if but_3l:
        ans3 = int(but_3l) * 100
    else:
        ans3 = 0
    if but_4l:
        ans4 = int(but_4l) * 500
    else:
        ans4 = 0
    if but_5l:
        ans5 = int(but_5l) * 2000
    else:
        ans5 = 0
    if but_6l:
        ans6 = int(but_6l) * 125
    else:
        ans6 = 0
    if but_7l:
        ans7 = int(but_7l) * 75
    else:
        ans7 = 0
    if but_8l:
        ans8 = int(but_8l) * 60
    else:
        ans8 = 0

    cost = ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7 + ans8
    output_second_label_f2.config(text=f"{cost}")
    output_second_label_f2.grid(row=1, column=1, pady=10, padx=60, sticky='e')

#  order number
def order_number():
    global random_num

    if cost is None or cost == 0:
        output_first_label_f2.config(text=f"{0}")
    else:
        order_num_rec = []
        output_first_label_f2.grid_forget()
        # random
        random_num = random.getrandbits(20) # 0-1048575
        while random_num in order_num_rec:
            random_num = random.getrandbits(20)
        order_num_rec.append(random_num)
        output_first_label_f2.config(text=f"{random_num}")

    output_first_label_f2.grid(row=0, column=1, pady=10, padx=60, sticky='e')

# service cost
def service_cost():
    global random_s_c

    output_third_label_f2.grid_forget()
    # random
    if cost:
        random_s_c = random.getrandbits(6) # 0-63
    else:
        random_s_c = 0
    output_third_label_f2.config(text=f"{random_s_c}")

    output_third_label_f2.grid(row=2, column=1, pady=10, padx=60, sticky='e')

# Tax
def tax():
    global round_tax

    tax_cal = (sub_tot*18)/100
    round_tax = round(tax_cal)
    output_fourth_label_f2.config(text=f"{round_tax}")
    output_fourth_label_f2.grid(row=3, column=1, pady=10, padx=60, sticky='e')

# sub total
def sub_total():
    global sub_tot

    sub_tot = cost + random_s_c
    output_fifth_label_f2.config(text=f"{sub_tot}")
    output_fifth_label_f2.grid(row=4, column=1, pady=10, padx=60, sticky='e')

# second frame total
def sec_frame_tot():
    global tot

    tot = (sub_tot+round_tax)
    output_sixth_label_f2.config(text=f"{tot}")
    output_sixth_label_f2.grid(row=5, column=1, pady=10, padx=60, sticky='e')

# total
def total_all():
    prize_range_and_calc()
    order_number()
    service_cost()
    sub_total()
    tax()
    sec_frame_tot()

    if tot != 0 and not None:
        submit["state"] = "normal"
    else:
        submit["state"] = "disabled"

# reset
def reset():
    global random_num, cost, random_s_c, round_tax, sub_tot, tot

    first_label_but.delete(0, END)
    second_label_but.delete(0, END)
    third_label_but.delete(0, END)
    fourth_label_but.delete(0, END)
    fifth_label_but.delete(0, END)
    sixth_label_but.delete(0, END)
    seventh_label_but.delete(0, END)
    eighth_label_but.delete(0, END)

    output_first_label_f2.grid_forget()
    output_second_label_f2.grid_forget()
    output_third_label_f2.grid_forget()
    output_fourth_label_f2.grid_forget()
    output_fifth_label_f2.grid_forget()
    output_sixth_label_f2.grid_forget()

    clock_label.cget("text")
    # date_label.cget("text")

    calc_entry.delete(0,END)

    text_fifth_frame_entry.delete(1.0, END)

    random_num = None
    cost = None
    random_s_c = None
    round_tax = None
    sub_tot = None
    tot = None

    submit["state"] = "disabled"

# exit
def exit():
    root.quit()

# fifth frame button clear function
def fifth_frame_btn_clr_fun():
    text_fifth_frame_entry.delete(1.0, END)
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Hotel management
HM = Label(root, text="Hotel Management", font="Caliber 30", fg="Midnight Blue")
HM.grid(row=0,column=0, pady=20, columnspan=2)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# first_frame
first_frame = Frame(root, width=386, height=430, relief="raised", borderwidth=5, bg='Medium Turquoise')
first_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

first_frame.grid_columnconfigure(0, weight=1)
first_frame.grid_columnconfigure(1, weight=1)

first_frame.grid_rowconfigure([i for i in range(8)], weight=1)

first_frame.grid_propagate(False)
# ----------------------------------------------------------------------------------------------------------------------

# label
first_label = Label(first_frame, text="Drink", bg='Medium Turquoise', font="caliber 14")
first_label.grid(row=0, column=0, sticky='w')

# button
first_label_but = Entry(first_frame, font="caliber 14", borderwidth=3)
first_label_but.grid(row=0, column=1, sticky='ew', pady=10, padx=10)
# ----------------------------------------------------------------------------------------------------------------------

# label
second_label = Label(first_frame, text="Burger", bg='Medium Turquoise', font="caliber 14")
second_label.grid(row=1, column=0, sticky='w')

# button
second_label_but = Entry(first_frame, font="caliber 14", borderwidth=3)
second_label_but.grid(row=1, column=1, sticky='ew', pady=10, padx=10)
# ----------------------------------------------------------------------------------------------------------------------

# label
third_label = Label(first_frame, text="Cherry", bg='Medium Turquoise', font="caliber 14")
third_label.grid(row=2, column=0, sticky='w')

# button
third_label_but = Entry(first_frame, font="caliber 14", borderwidth=3)
third_label_but.grid(row=2, column=1, sticky='ew', pady=10, padx=10)
# ----------------------------------------------------------------------------------------------------------------------

# label
fourth_label = Label(first_frame, text="Nacho Fries", bg='Medium Turquoise', font="caliber 14")
fourth_label.grid(row=3, column=0, sticky='w')

# button
fourth_label_but = Entry(first_frame, font="caliber 14", borderwidth=3)
fourth_label_but.grid(row=3, column=1, sticky='ew', pady=10, padx=10)
# ----------------------------------------------------------------------------------------------------------------------

# label
fifth_label = Label(first_frame, text="Pizza", bg='Medium Turquoise', font="caliber 14")
fifth_label.grid(row=4, column=0, sticky='w')

# button
fifth_label_but = Entry(first_frame, font="caliber 14", borderwidth=3)
fifth_label_but.grid(row=4, column=1, sticky='ew', pady=10, padx=10)
# ----------------------------------------------------------------------------------------------------------------------

# label
sixth_label = Label(first_frame, text="Biscuits", bg='Medium Turquoise', font="caliber 14")
sixth_label.grid(row=5, column=0, sticky='w')

# button
sixth_label_but = Entry(first_frame, font="caliber 14", borderwidth=3)
sixth_label_but.grid(row=5, column=1, sticky='ew', pady=10, padx=10)
# ----------------------------------------------------------------------------------------------------------------------

# label
seventh_label = Label(first_frame, text="Roll", bg='Medium Turquoise', font="caliber 14")
seventh_label.grid(row=6, column=0, sticky='w')

# button
seventh_label_but = Entry(first_frame, font="caliber 14", borderwidth=3)
seventh_label_but.grid(row=6, column=1, sticky='ew', pady=10, padx=10)
# ----------------------------------------------------------------------------------------------------------------------

# label
eighth_label = Label(first_frame, text="Tea", bg='Medium Turquoise', font="caliber 14")
eighth_label.grid(row=7, column=0, sticky='w')

# button
eighth_label_but = Entry(first_frame, font="caliber 14", borderwidth=3)
eighth_label_but.grid(row=7, column=1, sticky='ew', pady=10, padx=10)
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# second_frame
second_frame = Frame(root, width=386, height=430, relief="raised", borderwidth=5, bg="Light Salmon")
second_frame.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')

second_frame.grid_columnconfigure(0, weight=1)
second_frame.grid_columnconfigure(1, weight=1)

second_frame.grid_rowconfigure([i for i in range(6)], weight=1)

second_frame.grid_propagate(False)
# ----------------------------------------------------------------------------------------------------------------------

# 1st label
first_label_f2 = Label(second_frame, text="Order Number", font="caliber 14", bg="Light Salmon")
first_label_f2.grid(row=0, column=0, pady=10, padx=10, sticky='w')

second_label_f2 = Label(second_frame, text="Cost", font="caliber 14", bg="Light Salmon")
second_label_f2.grid(row=1, column=0, pady=10, padx=10, sticky='w')

third_label_f2 = Label(second_frame, text="Service Cost", font="caliber 14", bg="Light Salmon")
third_label_f2.grid(row=2, column=0, pady=10, padx=10, sticky='w')

fourth_label_f2 = Label(second_frame, text="Tax", font="caliber 14", bg="Light Salmon")
fourth_label_f2.grid(row=3, column=0, pady=10, padx=10, sticky='w')

fifth_label_f2 = Label(second_frame, text="Sub Total", font="caliber 14", bg="Light Salmon")
fifth_label_f2.grid(row=4, column=0, pady=10, padx=10, sticky='w')

sixth_label_f2 = Label(second_frame, text="Total", font="caliber 14", bg="Light Salmon")
sixth_label_f2.grid(row=5, column=0, pady=10, padx=10, sticky='w')
# ----------------------------------------------------------------------------------------------------------------------

# 2nd label
output_first_label_f2 = Label(second_frame, text="", font="caliber 14", bg="Light Salmon")
# output_first_label_f2.grid(row=0, column=1, pady=10, padx=60, sticky='e')

output_second_label_f2 = Label(second_frame, text="", font="caliber 14", bg="Light Salmon")
# output_second_label_f2.grid(row=1, column=1, pady=10, padx=60, sticky='e')

output_third_label_f2 = Label(second_frame, text="", font="caliber 14", bg="Light Salmon")
# output_third_label_f2.grid(row=2, column=1, pady=10, padx=60, sticky='e')

output_fourth_label_f2 = Label(second_frame, text="", font="caliber 14", bg="Light Salmon")
# output_fourth_label_f2.grid(row=3, column=1, pady=10, padx=60, sticky='e')

output_fifth_label_f2 = Label(second_frame, text="", font="caliber 14", bg="Light Salmon")
# output_fifth_label_f2.grid(row=4, column=1, pady=10, padx=60, sticky='e')

output_sixth_label_f2 = Label(second_frame, text="", font="caliber 14", bg="Light Salmon")
# output_sixth_label_f2.grid(row=5, column=1, pady=10, padx=60, sticky='e')
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# calculator functions
def calc_equals():
    cal_e = calc_entry.get()
    try:
        ans = eval(cal_e)
        calc_entry.delete(0, END)
        calc_entry.insert(END, ans)
    except:
        calc_entry.delete(0, END)
        calc_entry.insert(END, "ERROR")
def button_click(value):
    if calc_entry.get() == "ERROR":
        calc_entry.delete(0,END)
        calc_entry.insert(END, value)
    else:
        calc_entry.insert(END, value)

def on_single_click():
    calc_e = calc_entry.get()
    if calc_e:
        back = calc_e[:-1]
        calc_entry.delete(0, END)
        calc_entry.insert(END, back)

def on_press_and_hold(event):
    global hold_timer, click_timer
    click_timer = None  # Cancel any pending single-click action
    hold_timer = root.after(200, perform_hold_action)  # Start hold action timer

def perform_hold_action():
    global is_holding
    is_holding = True
    calc_entry.delete(0, END)

def on_release(event):
    global hold_timer, click_timer, is_holding
    if hold_timer:
        root.after_cancel(hold_timer)  # Cancel hold action if button is released quickly
        hold_timer = None

    if not is_holding:
        click_timer = root.after(100, on_single_click)  # Trigger single-click action after a short delay
    else:
        is_holding = False  # Reset the hold flag

# third_frame
third_frame = Frame(root, relief="sunken", borderwidth=5)
third_frame.grid(row=1, column=2, padx=20, pady=20, sticky='nsew')

third_frame.grid_columnconfigure([i for i in range(4)], weight=1)
third_frame.grid_rowconfigure([i for i in range(5)], weight=1)

calc_entry = Entry(third_frame, font="Caliber 19", borderwidth=4)
calc_entry.grid(row=0, column=0, pady=5, padx=5, columnspan=4, sticky='nsew')

b1 = Button(third_frame, text='1', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('1'))
b1.grid(row=1,column=0, sticky='nsew')

b2 = Button(third_frame, text='2', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('2'))
b2.grid(row=1,column=1, sticky='nsew')

b3 = Button(third_frame, text='3', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('3'))
b3.grid(row=1,column=2, sticky='nsew')

b4 = Button(third_frame, text='+', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('+'))
b4.grid(row=1,column=3, sticky='nsew')

b5 = Button(third_frame, text='4', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('4'))
b5.grid(row=2,column=0, sticky='nsew')

b6 = Button(third_frame, text='5', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('5'))
b6.grid(row=2,column=1, sticky='nsew')

b7 = Button(third_frame, text='6', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('6'))
b7.grid(row=2,column=2, sticky='nsew')

b8 = Button(third_frame, text='-', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('-'))
b8.grid(row=2,column=3, sticky='nsew')

b9 = Button(third_frame, text='7', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('7'))
b9.grid(row=3,column=0, sticky='nsew')

b10 = Button(third_frame, text='8', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('8'))
b10.grid(row=3,column=1, sticky='nsew')

b11 = Button(third_frame, text='9', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('9'))
b11.grid(row=3,column=2, sticky='nsew')

b12 = Button(third_frame, text='*', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('*'))
b12.grid(row=3,column=3, sticky='nsew')

b13 = Button(third_frame, text='C', width=4, height=1, font="Caliber 21", relief="flat")
b13.grid(row=4,column=0, sticky='nsew')
b13.bind("<ButtonPress-1>", on_press_and_hold)
b13.bind("<ButtonRelease-1>", on_release)
hold_timer = None
click_timer = None
is_holding = False

b14 = Button(third_frame, text='0', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('0'))
b14.grid(row=4,column=1, sticky='nsew')

b15 = Button(third_frame, text='=', width=4, height=1, font="Caliber 21", relief="flat", command=calc_equals)
b15.grid(row=4,column=2, sticky='nsew')

b16 = Button(third_frame, text='/', width=4, height=1, font="Caliber 21", relief="flat", command=lambda: button_click('/'))
b16.grid(row=4,column=3, sticky='nsew')
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# time
def update_time():
    global date_string
    time_string = strftime('%I:%M:%S %p')
    clock_label.config(text=time_string)
    clock_label.after(1000, update_time)

    today = datetime.today().date()
    date_string = strftime('%d-%m-%y')
    # date_label.config(text=f"{date_string}")


clock_label = Label(root, font=('calibri', 40, 'bold'), foreground='black')
clock_label.grid(row=0, column=2, padx=20, pady=20)

# date_label = Label(root, font=('calibri', 20, 'bold'), foreground='black')
# date_label.grid(row=0,column=2)
# date_label.place(relx=0.79, rely=0.14, anchor='e')


# Start the time update loop
update_time()
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# fourth_frame
fourth_frame = Frame(root, relief="raised", borderwidth=5, width=810, height=100, bg="Teal")
fourth_frame.grid(row=2, column=0, padx=20, pady=20, columnspan=2, sticky='nsew')

fourth_frame.grid_columnconfigure(0, weight=1)
fourth_frame.grid_columnconfigure(1, weight=1)
fourth_frame.grid_columnconfigure(2, weight=1)
fourth_frame.grid_columnconfigure(3, weight=1)

fourth_frame.grid_rowconfigure(0, weight=1)

fourth_frame.grid_propagate(False)
# ----------------------------------------------------------------------------------------------------------------------

# buttons
fourth_frame_but_1 = Button(fourth_frame, text="Price", font=("Caliber", 12, "bold"), width=10, height=2, borderwidth=4, command=prize)
fourth_frame_but_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

fourth_frame_but_2 = Button(fourth_frame, text="Total", font=("Caliber", 12, "bold"), width=10, height=2, borderwidth=4,command=total_all)
fourth_frame_but_2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

fourth_frame_but_3 = Button(fourth_frame, text="Reset", font=("Caliber", 12, "bold"), width=10, height=2, borderwidth=4, command=reset)
fourth_frame_but_3.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

fourth_frame_but_4 = Button(fourth_frame, text="Exit", font=("Caliber", 12, "bold"), width=10, height=2, borderwidth=4, command=exit)
fourth_frame_but_4.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# fifth_frame
fifth_frame = Frame(root, width=386, height=100, relief="sunken", borderwidth=5)
fifth_frame.grid(row=2, column=2)

fifth_frame.grid_columnconfigure(0, weight=1)
fifth_frame.grid_columnconfigure(1, weight=1)

fifth_frame.grid_rowconfigure(0, weight=1)

fifth_frame.grid_propagate(False)
# ----------------------------------------------------------------------------------------------------------------------

# Entry
text_fifth_frame_entry = Text(fifth_frame, width=386, height=100, font="Caliber 15")
text_fifth_frame_entry.grid(row=0, column=0)
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# fifth frame button clear
# fifth_frame_btn_clear = Button(root, text="CLEAR", height=2, width=10, font=("Caliber", 10, "bold"), command=fifth_frame_btn_clr_fun)
# fifth_frame_btn_clear.grid()
# fifth_frame_btn_clear.place(x=852, y=554)

# info
info_but = Button(root, text="i", height=1, width=3, font=("caliber",20,"bold"), command=info, fg="red")
info_but.grid(row=0, column=3)

# submit
submit = Button(root, text="SUBMIT", height=2, width=10, font=("Caliber", 10, "bold"), command=database, state="disabled")
submit.grid(row=2, column=3, padx=20, sticky='e')

root.mainloop()

