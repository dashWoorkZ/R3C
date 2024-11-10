#!/usr/bin/env python
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
         
                
#Main Window
window = tk.Tk()

# Center The Main Program Window When Launched
width = 500
height = 250
x = (window.winfo_screenwidth()//2)-(width//2)
y = (window.winfo_screenheight()//2)-(height//2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.title("R3C Calc v1")
window.configure(background="burlywood")
style=ttk.Style()   # ttk Style Library
menu = tk.Menu(window, background="antiquewhite")
style.theme_use("clam")

#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


#    Copyright 2024 Lord: Dash: La Londe.
#    R3C Calc - Resistor Colour Code Calculator
#    Three Band, Four Band, Five Band and Six Band Resistors
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


# ================================================================================================================================================================
# ================================================= Start of Main Styling =============================================================================
# ================================================================================================================================================================

style.configure("lawfulLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("privacyLight.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#70c5c2", foreground="#347898", highlightbackground='##ffebcd', highlightcolor='#48d1cc', anchor="center")
style.configure("lawfulLight.TFrame",  relief=tk.FLAT,takefocus=False, background="#ffe4c4")

# <<< R3C Calc v1 Styles >>>
style.configure("mainFrame.TFrame", font=("Times New Roman", 10, "bold"), relief=tk.FLAT, takefocus=False,  highlightthickness=5, bd=5, background="#5de67f", foreground="#1e90ff", highlightbackground='##ffebcd', highlightcolor='#48d1cc', anchor="center", justify="center", )
style.configure("bandValue.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("bandColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#00ffff",  activeforeground="#347898", font=("Times New Roman", 11, "bold"),  background="#fb8604", foreground="#ffff00",  highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("bandTitle.TLabel",relief=tk.RAISED, direction="below", bd=5, activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="#5de67f", foreground="#00ffff", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=5, takefocus=True, justify="center", anchor="center")
style.configure("resLabel.TLabel",relief=tk.RAISED, direction="below", bd=5, activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 12, "bold"),  background="#38b3d8", foreground="purple", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=5, takefocus=True, justify="center", anchor="center")
style.configure("band_btn.TButton", relief=tk.FLAT, font=("Times New Roman", 11, "bold"), background="#4f788a", foreground="#00ffff", ipady=2, ipadx=5, highlightbackground='##ffebcd', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("r3cCalcTitleLight.TLabel", font=("Times New Roman", 14, "bold"), relief=tk.RAISED, takefocus=False, highlightthickness=5, background="#5de67f", foreground="#800080", highlightbackground='##ffebcd', highlightcolor='#48d1cc', justify="center", anchor="center")
style.configure("copyright.TLabel", font=("Times New Roman", 10, "bold"), relief=tk.RAISED, takefocus=False, highlightthickness=5, background="#5de67f", foreground="#800080", highlightbackground='##ffebcd', highlightcolor='#48d1cc', justify="center", anchor="center")
style.configure("B4Bands.TFrame",relief=tk.RAISED, direction="below", bd=10, activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 14, "bold"),  background="dodgerblue", foreground="#5de67f", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=5, takefocus=True, anchor="center", justify="center", )
style.configure("valueLabel.TLabel",relief=tk.RAISED, direction="below", bd=5, activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 14, "bold"),  background="#d4a075", foreground="#0000ff", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=5, takefocus=True, justify="center", anchor="center")
style.configure("blackColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="black", foreground="white", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("brownColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="brown", foreground="white", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("redColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="red", foreground="white", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("orangeColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="orange", foreground="white", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("yellowColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="yellow", foreground="dodgerblue", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("greenColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="green", foreground="white", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("blueColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="blue", foreground="white", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("purpleColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="purple", foreground="white", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("grayColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="gray", foreground="blue", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("whiteColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="white", foreground="dodgerblue", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("goldColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="gold", foreground="dodgerblue", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("silverColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="silver", foreground="dodgerblue", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("pinkColour.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="pink", foreground="dodgerblue", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")

# ================================================================================================================================================================
# ============================================================== Styles Used In This Program =====================================================================
# ==== Note: Some styles may have attributes with values, that have not been properly assigned, for the most part it is the highlight colors, bg and anchor, i   =
# ====       find them intrusive with what i had styled, and while i tried to edit them the best i could, i found working with tkinter styling quite annoying in =
# ====       the vanilla form, so i often left them unfinished while i paid attention to issues, i thought to be of more importance, feel free to edit them as   =
# ====       you please, i will be looking to update in some form the way in which styles are being applied, as well as some other edits that i hope will make   =
# ====       the program more stable.    =========================================================================================================================                                                                                                                         ====
# ================================================================================================================================================================

# ================================================================================================================================================================
# ========================================================== End Of Conversion Styling ===========================================================================
# ================================================================================================================================================================


# Apps Menu to Open and Close TempCalc and to Exit the Program
apps_menu = tk.Menu(menu, tearoff = False, activeforeground="#d17c1a", activebackground="#5c3608", background="antiquewhite", foreground="#d17c1a")
# apps_menu.add_command(label = "Three", command=lambda: showThree())
# apps_menu.add_command(label = "Four", command=lambda: showFour())
# apps_menu.add_command(label = "Five", command=lambda: showFive())
# apps_menu.add_command(label = "Six", command=lambda: showSix())
apps_menu.add_command(label = "Home", command=lambda: getMain())
apps_menu.add_command(label = "Exit", command = lambda: quit_main())

menu.add_cascade(label ="Bands", menu = apps_menu, foreground="#854c0c", background="burlywood", activebackground="antiquewhite", activeforeground="burlywood")
# info Menu to display the info page
info_menu = tk.Menu(menu, tearoff = False, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
info_menu.add_command(label = "Lawful Notice", command=lambda: open_privacy_window())
info_menu.add_command(label = "Contact", command=lambda: open_contact_window())
info_menu.add_command(label = "Support", command=lambda: open_support_window())
info_menu.add_command(label = "Credits", command=lambda: open_credits_window())
menu.add_cascade(label ="Info", menu = info_menu, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")


B3_b1_label_value = IntVar()
B3_b2_label_value = IntVar()
B3_M_label_value = StringVar()

B4_b1_label_value = IntVar()
B4_b2_label_value = IntVar()
B4_M_label_value = StringVar()
B4_T_label_value = StringVar()

B5_b1_label_value = IntVar()
B5_b2_label_value = IntVar()
B5_b3_label_value = IntVar()
B5_M_label_value = StringVar()
B5_T_label_value = StringVar()

B6_b1_label_value = IntVar()
B6_b2_label_value = IntVar()
B6_b3_label_value = IntVar()
B6_M_label_value = StringVar()
B6_T_label_value = StringVar()
B6_TCR_label_value = StringVar()

# List of Function Calls
def B6_res_value_label() -> str:
        tValue = B6_T_label_value.get()
        tcrValue = B6_TCR_label_value.get()
        b1 = B6_b1_label_value.get()
        b2 = B6_b2_label_value.get()
        b3 = B6_b3_label_value.get()
        M = B6_M_label_value.get()
        if M == " ":
                resistor_value =  ((b1*100) + (b2*10) + (b3*1))
                resistor_6B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT NINE}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 9)) / pow(10, 9)), 2)
                resistor_6B_value_label.configure(text=f"{resistor_value}G \u2126 {tValue} {tcrValue} ppm")
        elif M == "10\N{SUPERSCRIPT EIGHT}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 8)) / pow(10, 9)), 2)
                resistor_6B_value_label.configure(text=f"{resistor_value}G \u2126 {tValue} {tcrValue} ppm")
        elif M == "10\N{SUPERSCRIPT SEVEN}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 7)) / pow(10, 9)), 2)
                resistor_6B_value_label.configure(text=f"{resistor_value}G \u2126 {tValue} {tcrValue} ppm")
        elif M == "10\N{SUPERSCRIPT SIX}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 6)) / pow(10, 6)), 2)
                resistor_6B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue} {tcrValue} ppm")
        elif M == "10\N{SUPERSCRIPT FIVE}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 5)) / pow(10, 6)), 2)
                resistor_6B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue} {tcrValue} ppm")
        elif M == "10\N{SUPERSCRIPT FOUR}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 4)) / pow(10, 6)), 2)
                resistor_6B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue} {tcrValue}  ppm")
        elif M == "10\N{SUPERSCRIPT THREE}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 3)) / pow(10, 3)), 1)
                resistor_6B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue} {tcrValue}ppm")
        elif M == "10\N{SUPERSCRIPT TWO}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 2)) / pow(10, 3)), 2)
                resistor_6B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue} {tcrValue} ppm")
        elif M == "10\N{SUPERSCRIPT ONE}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 1)) / pow(10, 3)), 2)
                resistor_6B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue} {tcrValue} ppm")
        elif M == "10\N{SUPERSCRIPT ZERO}":
                resistor_value =  round((((b1*100) + (b2*10) + (b3*1)) * pow(10, 0)), 0)
                resistor_6B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue} {tcrValue} ppm")
        elif M == 0.001:
                resistor_value =  round((((b1*100) + (b2*10) + (b3*1)) * M), 0)
                resistor_6B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue} {tcrValue} ppm")
        elif M == 0.01:
                resistor_value =  round((((b1*100) + (b2*10) + (b3*1)) * M), 0)
                resistor_6B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue} {tcrValue} ppm")
        elif M == 0.1:
                resistor_value =  round((((b1*100) + (b2*10) + (b3*1)) * M), 0)
                resistor_6B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue} {tcrValue} ppm")
        else:
                resistor_value =  ((b1*100) + (b2*10) + (b3*1))
                resistor_6B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")


def B5_res_value_label() -> str:
        tValue = B5_T_label_value.get()
        b1 = B5_b1_label_value.get()
        b2 = B5_b2_label_value.get()
        b3 = B5_b3_label_value.get()
        M = B5_M_label_value.get()
        if M == "":
                resistor_value =  ((b1*100) + (b2*10) + (b3*1))
                resistor_5B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT NINE}":
                resistor_value =  round(((b1*100) + (b2*10) + (b3*1)), 0)
                resistor_5B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT EIGHT}":
                resistor_value =  round(((b1*100) + (b2*10) + (b3*1)), 0)
                resistor_5B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT SEVEN}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 7)) / pow(10, 9)), 2)
                resistor_5B_value_label.configure(text=f"{resistor_value}G \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT SIX}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 6)) / pow(10, 6)), 2)
                resistor_5B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT FIVE}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 5)) / pow(10, 6)), 2)
                resistor_5B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT FOUR}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 4)) / pow(10, 6)), 2)
                resistor_5B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT THREE}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 3)) / pow(10, 3)), 2)
                resistor_5B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT TWO}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 2)) / pow(10, 3)), 1)
                resistor_5B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT ONE}":
                resistor_value =  round(((((b1*100) + (b2*10) + (b3*1)) * pow(10, 1)) / pow(10, 3)), 1)
                resistor_5B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT ZERO}":
                resistor_value =  round((((b1*100) + (b2*10) + (b3*1)) * pow(10, 0)), 1)
                resistor_5B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        else:
                resistor_value =  round(((b1*100) + (b2*10) + (b3*1)), 1)
                resistor_5B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}") 


def B4_res_value_label() -> str:
        tValue = B4_T_label_value.get()
        b1 = B4_b1_label_value.get()
        b2 = B4_b2_label_value.get()
        M = B4_M_label_value.get()
        if M == "10\N{SUPERSCRIPT NINE}":
                resistor_value =  round((((b1*10) + (b2*1))), 0)
                resistor_4B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT EIGHT}":
                resistor_value =  round((((b1*10) + (b2*1))), 0)
                resistor_4B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT SEVEN}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 7)) / pow(10, 6)), 2)
                resistor_4B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT SIX}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 6)) / pow(10, 6)), 2)
                resistor_4B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT FIVE}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 5)) / pow(10, 6)), 2)
                resistor_4B_value_label.configure(text=f"{resistor_value}M \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT FOUR}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 4)) / pow(10, 3)), 1)
                resistor_4B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT THREE}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 3)) / pow(10, 3)), 2)
                resistor_4B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT TWO}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 2)) / pow(10, 3)), 1)
                resistor_4B_value_label.configure(text=f"{resistor_value}K \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT ONE}":
                resistor_value =  round((((b1*10) + (b2*1)) * pow(10, 1)), 1)
                resistor_4B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        elif M == "10\N{SUPERSCRIPT ZERO}":
                resistor_value =  round((((b1*10) + (b2*1)) * pow(10, 0)), 1)
                resistor_4B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")
        else:
                resistor_value =  round(((b1*10) + (b2*1)), 1)
                resistor_4B_value_label.configure(text=f"{resistor_value}R \u2126 {tValue}")



def B3_res_value_label() -> str:
        b1 = B3_b1_label_value.get()
        b2 = B3_b2_label_value.get()
        M = B3_M_label_value.get()
        if M == "10\N{SUPERSCRIPT NINE}":
                resistor_value =  round(((((int(b1)*10) + (b2*1)) * pow(10, 9)) / pow(10, 9)), 2)
                resistor_3B_value_label.configure(text=f"{resistor_value}G \u2126")
        elif M == "10\N{SUPERSCRIPT EIGHT}":
                resistor_value =  round(((((int(b1)*10) + (b2*1)) * pow(10, 8)) / pow(10, 9)), 2)
                resistor_3B_value_label.configure(text=f"{resistor_value}M \u2126")
        elif M == "10\N{SUPERSCRIPT SEVEN}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 7)) / pow(10, 6)), 2)
                resistor_3B_value_label.configure(text=f"{resistor_value}M \u2126")
        elif M == "10\N{SUPERSCRIPT SIX}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 6)) / pow(10, 6)), 2)
                resistor_3B_value_label.configure(text=f"{resistor_value}M \u2126")
        elif M == "10\N{SUPERSCRIPT FIVE}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 5)) / pow(10, 6)), 2)
                resistor_3B_value_label.configure(text=f"{resistor_value}M \u2126")
        elif M == "10\N{SUPERSCRIPT FOUR}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 4)) / pow(10, 3)), 2)
                resistor_3B_value_label.configure(text=f"{resistor_value}K \u2126")
        elif M == "10\N{SUPERSCRIPT THREE}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 3)) / pow(10, 3)), 2)
                resistor_3B_value_label.configure(text=f"{resistor_value}K \u2126")
        elif M == "10\N{SUPERSCRIPT TWO}":
                resistor_value =  round(((((b1*10) + (b2*1)) * pow(10, 2)) / pow(10, 3)), 2)
                resistor_3B_value_label.configure(text=f"{resistor_value}K \u2126")
        elif M == "10\N{SUPERSCRIPT ONE}":
                resistor_value =  round((((b1*10) + (b2*1)) * pow(10, 1)), 0)
                resistor_3B_value_label.configure(text=f"{resistor_value}R \u2126")
        elif M == "10\N{SUPERSCRIPT ZERO}":
                resistor_value =  round((((b1*10) + (b2*1)) * pow(10, 0)), 1)
                resistor_3B_value_label.configure(text=f"{resistor_value}R \u2126")
        else:
                resistor_value =  round(((b1*10) + (b2*1)), 1)
                resistor_3B_value_label.configure(text=f"{resistor_value}R \u2126")


# <<< Start Four Band Selection >>>

# <<< Three Band Selection >
def B3_b1_selected(choice) -> str:
        choice = B3_b1_bandColour.get()
        B3_b1_bandColour.set(choice)
        if choice == "Black":
                B3_b1_bandColours.configure(style="blackColour.TLabel")
                B3_b1_label_value.set(0)
        elif choice == "Brown":
                B3_b1_bandColours.configure(style="brownColour.TLabel")
                B3_b1_label_value.set(1)
        elif choice == "Red":
                B3_b1_bandColours.configure(style="redColour.TLabel")
                B3_b1_label_value.set(2)
        elif choice == "Orange":
                B3_b1_bandColours.configure(style="orangeColour.TLabel")
                B3_b1_label_value.set(3)
        elif choice == "Yellow":
                B3_b1_bandColours.configure(style="yellowColour.TLabel")
                B3_b1_label_value.set(4)
        elif choice == "Green":
                B3_b1_bandColours.configure(style="greenColour.TLabel")
                B3_b1_label_value.set(5)
        elif choice == "Blue":
                B3_b1_bandColours.configure(style="blueColour.TLabel")
                B3_b1_label_value.set(6)
        elif choice == "Purple":
                B3_b1_bandColours.configure(style="purpleColour.TLabel")
                B3_b1_label_value.set(7)
        elif choice == "Gray":
                B3_b1_bandColours.configure(style="grayColour.TLabel")
                B3_b1_label_value.set(8)
        elif choice == "White":
                B3_b1_bandColours.configure(style="whiteColour.TLabel")
                B3_b1_label_value.set(9)
        else:
                B3_b1_bandColours.configure(style="bandColour.TLabel")
                B3_b1_label_value.set(str(" "))
                resistor_3B_b1_label_value.configure(text=B3_b1_label_value)
                breakpoint


def B3_b2_selected(choice) -> str:
        choice = B3_b2_bandColour.get()
        B3_b2_bandColour.set(choice)
        if choice == "Black":
                B3_b2_bandColours.configure(style="blackColour.TLabel")
                B3_b2_label_value.set(0)
        elif choice == "Brown":
                B3_b2_bandColours.configure(style="brownColour.TLabel")
                B3_b2_label_value.set(1)
        elif choice == "Red":
                B3_b2_bandColours.configure(style="redColour.TLabel")
                B3_b2_label_value.set(2)
        elif choice == "Orange":
                B3_b2_bandColours.configure(style="orangeColour.TLabel")
                B3_b2_label_value.set(3)
        elif choice == "Yellow":
                B3_b2_bandColours.configure(style="yellowColour.TLabel")
                B3_b2_label_value.set(4)
        elif choice == "Green":
                B3_b2_bandColours.configure(style="greenColour.TLabel")
                B3_b2_label_value.set(5)
        elif choice == "Blue":
                B3_b2_bandColours.configure(style="blueColour.TLabel")
                B3_b2_label_value.set(6)
        elif choice == "Purple":
                B3_b2_bandColours.configure(style="purpleColour.TLabel")
                B3_b2_label_value.set(7)
        elif choice == "Gray":
                B3_b2_bandColours.configure(style="grayColour.TLabel")
                B3_b2_label_value.set(8)
        elif choice == "White":
                B3_b2_bandColours.configure(style="whiteColour.TLabel")
                B3_b2_label_value.set(9)
        else:
                B3_b2_bandColours.configure(style="bandColour.TLabel")
                B3_b2_label_value.set(str(" "))
                resistor_3B_b2_label_value.configure(text=B3_b2_label_value)
                breakpoint


def B3_M_selected(choice) -> str:
        choice = B3_M_bandColour.get()
        B3_M_bandColour.set(choice)
        if choice == "Black":
                B3_M_bandColours.configure(style="blackColour.TLabel")
                B3_M_label_value.set("10\N{SUPERSCRIPT ZERO}")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "Brown":
                B3_M_bandColours.configure(style="brownColour.TLabel")
                B3_M_label_value.set("10\N{SUPERSCRIPT ONE}")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "Red":
                B3_M_bandColours.configure(style="redColour.TLabel")
                B3_M_label_value.set("10\N{SUPERSCRIPT TWO}")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "Orange":
                B3_M_bandColours.configure(style="orangeColour.TLabel")
                B3_M_label_value.set("10\N{SUPERSCRIPT THREE}")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "Yellow":
                B3_M_bandColours.configure(style="yellowColour.TLabel")
                B3_M_label_value.set("10\N{SUPERSCRIPT FOUR}")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "Green":
                B3_M_bandColours.configure(style="greenColour.TLabel")
                B3_M_label_value.set("10\N{SUPERSCRIPT FIVE}")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "Blue":
                B3_M_bandColours.configure(style="blueColour.TLabel")
                B3_M_label_value.set("10\N{SUPERSCRIPT SIX}")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "Purple":
                B3_M_bandColours.configure(style="purpleColour.TLabel")
                B3_M_label_value.set("10\N{SUPERSCRIPT SEVEN}")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "Gray":
                B3_M_bandColours.configure(style="grayColour.TLabel")
                B3_M_label_value.set(" ")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        elif choice == "White":
                B3_M_bandColours.configure(style="whiteColour.TLabel")
                B3_M_label_value.set(" ")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
        else:
                B3_M_bandColours.configure(style="bandColour.TLabel")
                B3_M_label_value.set(" ")
                resistor_3B_M_label_value.configure(text=B3_M_label_value)
                B3_res_value_label()
                breakpoint


# <<< Four Band Selection >
def B4_b1_selected(choice) -> str:
        choice = B4_b1_bandColour.get()
        B4_b1_bandColour.set(choice)
        if choice == "Black":
                B4_b1_bandColours.configure(style="blackColour.TLabel")
                B4_b1_label_value.set(0)
        elif choice == "Brown":
                B4_b1_bandColours.configure(style="brownColour.TLabel")
                B4_b1_label_value.set(1)
        elif choice == "Red":
                B4_b1_bandColours.configure(style="redColour.TLabel")
                B4_b1_label_value.set(2)
        elif choice == "Orange":
                B4_b1_bandColours.configure(style="orangeColour.TLabel")
                B4_b1_label_value.set(3)
        elif choice == "Yellow":
                B4_b1_bandColours.configure(style="yellowColour.TLabel")
                B4_b1_label_value.set(4)
        elif choice == "Green":
                B4_b1_bandColours.configure(style="greenColour.TLabel")
                B4_b1_label_value.set(5)
        elif choice == "Blue":
                B4_b1_bandColours.configure(style="blueColour.TLabel")
                B4_b1_label_value.set(6)
        elif choice == "Purple":
                B4_b1_bandColours.configure(style="purpleColour.TLabel")
                B4_b1_label_value.set(7)
        elif choice == "Gray":
                B4_b1_bandColours.configure(style="grayColour.TLabel")
                B4_b1_label_value.set(8)
        elif choice == "White":
                B4_b1_bandColours.configure(style="whiteColour.TLabel")
                B4_b1_label_value.set(9)
        else:
                B4_b1_bandColours.configure(style="bandColour.TLabel")
                B4_b1_label_value.set(" ")
                resistor_4B_b1_label_value.configure(text=B4_b1_label_value)
                breakpoint


def B4_b2_selected(choice) -> str:
        choice = B4_b2_bandColour.get()
        B4_b2_bandColour.set(choice)
        if choice == "Black":
                B4_b2_bandColours.configure(style="blackColour.TLabel")
                B4_b2_label_value.set(0)
        elif choice == "Brown":
                B4_b2_bandColours.configure(style="brownColour.TLabel")
                B4_b2_label_value.set(1)
        elif choice == "Red":
                B4_b2_bandColours.configure(style="redColour.TLabel")
                B4_b2_label_value.set(2)
        elif choice == "Orange":
                B4_b2_bandColours.configure(style="orangeColour.TLabel")
                B4_b2_label_value.set(3)
        elif choice == "Yellow":
                B4_b2_bandColours.configure(style="yellowColour.TLabel")
                B4_b2_label_value.set(4)
        elif choice == "Green":
                B4_b2_bandColours.configure(style="greenColour.TLabel")
                B4_b2_label_value.set(5)
        elif choice == "Blue":
                B4_b2_bandColours.configure(style="blueColour.TLabel")
                B4_b2_label_value.set(6)
        elif choice == "Purple":
                B4_b2_bandColours.configure(style="purpleColour.TLabel")
                B4_b2_label_value.set(7)
        elif choice == "Gray":
                B4_b2_bandColours.configure(style="grayColour.TLabel")
                B4_b2_label_value.set(8)
        elif choice == "White":
                B4_b2_bandColours.configure(style="whiteColour.TLabel")
                B4_b2_label_value.set(9)
        else:
                B4_b2_bandColours.configure(style="bandColour.TLabel")
                B4_b2_label_value.set(" ")
                resistor_4B_b2_label_value.configure(text=B4_b2_label_value)
                breakpoint


def B4_M_selected(choice) -> str:
        choice = B4_M_bandColour.get()
        B4_M_bandColour.set(choice)
        if choice == "Black":
                B4_M_bandColours.configure(style="blackColour.TLabel")
                B4_M_label_value.set("10\N{SUPERSCRIPT ZERO}")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "Brown":
                B4_M_bandColours.configure(style="brownColour.TLabel")
                B4_M_label_value.set("10\N{SUPERSCRIPT ONE}")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "Red":
                B4_M_bandColours.configure(style="redColour.TLabel")
                B4_M_label_value.set("10\N{SUPERSCRIPT TWO}")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "Orange":
                B4_M_bandColours.configure(style="orangeColour.TLabel")
                B4_M_label_value.set("10\N{SUPERSCRIPT THREE}")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "Yellow":
                B4_M_bandColours.configure(style="yellowColour.TLabel")
                B4_M_label_value.set("10\N{SUPERSCRIPT FOUR}")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "Green":
                B4_M_bandColours.configure(style="greenColour.TLabel")
                B4_M_label_value.set("10\N{SUPERSCRIPT FIVE}")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "Blue":
                B4_M_bandColours.configure(style="blueColour.TLabel")
                B4_M_label_value.set("10\N{SUPERSCRIPT SIX}")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "Purple":
                B4_M_bandColours.configure(style="purpleColour.TLabel")
                B4_M_label_value.set("10\N{SUPERSCRIPT SEVEN}")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "Gray":
                B4_M_bandColours.configure(style="grayColour.TLabel")
                B4_M_label_value.set(" ")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        elif choice == "White":
                B4_M_bandColours.configure(style="whiteColour.TLabel")
                B4_M_label_value.set(" ")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
        else:
                B4_M_bandColours.configure(style="bandColour.TLabel")
                B4_M_label_value.set(" ")
                resistor_4B_M_label_value.configure(text=B4_M_label_value)
                breakpoint


def B4_T_selected(choice) -> str:
        choice = B4_T_bandColour.get()
        B4_T_bandColour.set(choice)
        if choice == "Black":
                B4_T_bandColours.configure(style="blackColour.TLabel")
                B4_T_label_value.set(" ")
                B4_res_value_label()
        elif choice == "Brown":
                B4_T_bandColours.configure(style="brownColour.TLabel")
                B4_T_label_value.set("\u00B1" + "1\u0025")
                B4_res_value_label()
        elif choice == "Red":
                B4_T_bandColours.configure(style="redColour.TLabel")
                B4_T_label_value.set("\u00B1" + "2\u0025")
                B4_res_value_label()
        elif choice == "Orange":
                B4_T_bandColours.configure(style="orangeColour.TLabel")
                B4_T_label_value.set(" ")
                B4_res_value_label()
        elif choice == "Yellow":
                B4_T_bandColours.configure(style="yellowColour.TLabel")
                B4_T_label_value.set(" ")
                B4_res_value_label()
        elif choice == "Green":
                B4_T_bandColours.configure(style="greenColour.TLabel")
                B4_T_label_value.set("\u00B1" + "0.5\u0025")
                B4_res_value_label()
        elif choice == "Blue":
                B4_T_bandColours.configure(style="blueColour.TLabel")
                B4_T_label_value.set("\u00B1" + "0.25\u0025")
                B4_res_value_label()
        elif choice == "Purple":
                B4_T_bandColours.configure(style="purpleColour.TLabel")
                B4_T_label_value.set("\u00B1" + "0.1\u0025")
                B4_res_value_label()
        elif choice == "Gray":
                B4_T_bandColours.configure(style="grayColour.TLabel")
                B4_T_label_value.set("\u00B1" + "0.05\u0025")
                B4_res_value_label()
        elif choice == "White":
                B4_T_bandColours.configure(style="whiteColour.TLabel")
                B4_T_label_value.set(" ")
                B4_res_value_label()
        else:
                B4_T_bandColours.configure(style="bandColour.TLabel")
                B4_T_label_value.set(" ")
                B4_res_value_label()
                breakpoint
# <<< End Four Band Selection >>>



# <<< Start Five Band Selection >>>
def B5_b1_selected(choice) -> str:
        choice = B5_b1_bandColour.get()
        B5_b1_bandColour.set(choice)
        if choice == "Black":
                B5_b1_bandColours.configure(style="blackColour.TLabel")
                B5_b1_label_value.set(0)
        elif choice == "Brown":
                B5_b1_bandColours.configure(style="brownColour.TLabel")
                B5_b1_label_value.set(1)
        elif choice == "Red":
                B5_b1_bandColours.configure(style="redColour.TLabel")
                B5_b1_label_value.set(2)
        elif choice == "Orange":
                B5_b1_bandColours.configure(style="orangeColour.TLabel")
                B5_b1_label_value.set(3)
        elif choice == "Yellow":
                B5_b1_bandColours.configure(style="yellowColour.TLabel")
                B5_b1_label_value.set(4)
        elif choice == "Green":
                B5_b1_bandColours.configure(style="greenColour.TLabel")
                B5_b1_label_value.set(5)
        elif choice == "Blue":
                B5_b1_bandColours.configure(style="blueColour.TLabel")
                B5_b1_label_value.set(6)
        elif choice == "Purple":
                B5_b1_bandColours.configure(style="purpleColour.TLabel")
                B5_b1_label_value.set(7)
        elif choice == "Gray":
                B5_b1_bandColours.configure(style="grayColour.TLabel")
                B5_b1_label_value.set(8)
        elif choice == "White":
                B5_b1_bandColours.configure(style="whiteColour.TLabel")
                B5_b1_label_value.set(9)
        else:
                B5_b1_bandColours.configure(style="bandColour.TLabel")
                B5_b1_label_value.set(" ")
                resistor_5B_b1_label_value.configure(text=B5_b1_label_value)
                breakpoint


def B5_b2_selected(choice) -> str:
        choice = B5_b2_bandColour.get()
        B5_b2_bandColour.set(choice)
        if choice == "Black":
                B5_b2_bandColours.configure(style="blackColour.TLabel")
                B5_b2_label_value.set(0)
        elif choice == "Brown":
                B5_b2_bandColours.configure(style="brownColour.TLabel")
                B5_b2_label_value.set(1)
        elif choice == "Red":
                B5_b2_bandColours.configure(style="redColour.TLabel")
                B5_b2_label_value.set(2)
        elif choice == "Orange":
                B5_b2_bandColours.configure(style="orangeColour.TLabel")
                B5_b2_label_value.set(3)
        elif choice == "Yellow":
                B5_b2_bandColours.configure(style="yellowColour.TLabel")
                B5_b2_label_value.set(4)
        elif choice == "Green":
                B5_b2_bandColours.configure(style="greenColour.TLabel")
                B5_b2_label_value.set(5)
        elif choice == "Blue":
                B5_b2_bandColours.configure(style="blueColour.TLabel")
                B5_b2_label_value.set(6)
        elif choice == "Purple":
                B5_b2_bandColours.configure(style="purpleColour.TLabel")
                B5_b2_label_value.set(7)
        elif choice == "Gray":
                B5_b2_bandColours.configure(style="grayColour.TLabel")
                B5_b2_label_value.set(8)
        elif choice == "White":
                B5_b2_bandColours.configure(style="whiteColour.TLabel")
                B5_b2_label_value.set(9)
        else:
                B5_b2_bandColours.configure(style="bandColour.TLabel")
                B5_b2_label_value.set(" ")
                resistor_5B_b2_label_value.configure(text=B5_b2_label_value)
                breakpoint


def B5_b3_selected(choice) -> str:
        choice = B5_b3_bandColour.get()
        B5_b3_bandColour.set(choice)
        if choice == "Black":
                B5_b3_bandColours.configure(style="blackColour.TLabel")
                B5_b3_label_value.set(0)
        elif choice == "Brown":
                B5_b3_bandColours.configure(style="brownColour.TLabel")
                B5_b3_label_value.set(1)
        elif choice == "Red":
                B5_b3_bandColours.configure(style="redColour.TLabel")
                B5_b3_label_value.set(2)
        elif choice == "Orange":
                B5_b3_bandColours.configure(style="orangeColour.TLabel")
                B5_b3_label_value.set(3)
        elif choice == "Yellow":
                B5_b3_bandColours.configure(style="yellowColour.TLabel")
                B5_b3_label_value.set(4)
        elif choice == "Green":
                B5_b3_bandColours.configure(style="greenColour.TLabel")
                B5_b3_label_value.set(5)
        elif choice == "Blue":
                B5_b3_bandColours.configure(style="blueColour.TLabel")
                B5_b3_label_value.set(6)
        elif choice == "Purple":
                B5_b3_bandColours.configure(style="purpleColour.TLabel")
                B5_b3_label_value.set(7)
        elif choice == "Gray":
                B5_b3_bandColours.configure(style="grayColour.TLabel")
                B5_b3_label_value.set(8)
        elif choice == "White":
                B5_b3_bandColours.configure(style="whiteColour.TLabel")
                B5_b3_label_value.set(9)
        else:
                B5_b3_bandColours.configure(style="bandColour.TLabel")
                B5_b3_label_value.set(" ")
                resistor_5B_b3_label_value.configure(text=B5_b3_label_value)
                breakpoint


def B5_M_selected(choice) -> str:
        choice = B5_M_bandColour.get()
        B5_M_bandColour.set(choice)
        if choice == "Black":
                B5_M_bandColours.configure(style="blackColour.TLabel")
                B5_M_label_value.set("10\N{SUPERSCRIPT ZERO}")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "Brown":
                B5_M_bandColours.configure(style="brownColour.TLabel")
                B5_M_label_value.set("10\N{SUPERSCRIPT ONE}")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "Red":
                B5_M_bandColours.configure(style="redColour.TLabel")
                B5_M_label_value.set("10\N{SUPERSCRIPT TWO}")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "Orange":
                B5_M_bandColours.configure(style="orangeColour.TLabel")
                B5_M_label_value.set("10\N{SUPERSCRIPT THREE}")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "Yellow":
                B5_M_bandColours.configure(style="yellowColour.TLabel")
                B5_M_label_value.set("10\N{SUPERSCRIPT FOUR}")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "Green":
                B5_M_bandColours.configure(style="greenColour.TLabel")
                B5_M_label_value.set("10\N{SUPERSCRIPT FIVE}")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "Blue":
                B5_M_bandColours.configure(style="blueColour.TLabel")
                B5_M_label_value.set("10\N{SUPERSCRIPT SIX}")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "Purple":
                B5_M_bandColours.configure(style="purpleColour.TLabel")
                B5_M_label_value.set("10\N{SUPERSCRIPT SEVEN}")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "Gray":
                B5_M_bandColours.configure(style="grayColour.TLabel")
                B5_M_label_value.set(" ")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
        elif choice == "White":
                B5_M_bandColours.configure(style="whiteColour.TLabel")
                B5_M_label_value.set(" ")
                resistor_4B_M_label_value.configure(text=B5_M_label_value)
        else:
                B5_M_bandColours.configure(style="bandColour.TLabel")
                B5_M_label_value.set(" ")
                resistor_5B_M_label_value.configure(text=B5_M_label_value)
                breakpoint


def B5_T_selected(choice) -> str:
        choice = B5_T_bandColour.get()
        B5_T_bandColour.set(choice)
        if choice == "Black":
                B5_T_bandColours.configure(style="blackColour.TLabel")
                B5_T_label_value.set("")
                B5_res_value_label()
        elif choice == "Brown":
                B5_T_bandColours.configure(style="brownColour.TLabel")
                B5_T_label_value.set("\u00B1" + "1\u0025")
                B5_res_value_label()
        elif choice == "Red":
                B5_T_bandColours.configure(style="redColour.TLabel")
                B5_T_label_value.set("\u00B1" + "2\u0025")
                B5_res_value_label()
        elif choice == "Orange":
                B5_T_bandColours.configure(style="orangeColour.TLabel")
                B5_T_label_value.set(" ")
                B5_res_value_label()
        elif choice == "Yellow":
                B5_T_bandColours.configure(style="yellowColour.TLabel")
                B5_T_label_value.set(" ")
                B5_res_value_label()
        elif choice == "Green":
                B5_T_bandColours.configure(style="greenColour.TLabel")
                B5_T_label_value.set("\u00B1" + "0.5\u0025")
                B5_res_value_label()
        elif choice == "Blue":
                B5_T_bandColours.configure(style="blueColour.TLabel")
                B5_T_label_value.set("\u00B1" + "0.25\u0025")
                B5_res_value_label()
        elif choice == "Purple":
                B5_T_bandColours.configure(style="purpleColour.TLabel")
                B5_T_label_value.set("\u00B1" + "0.1\u0025")
                B5_res_value_label()
        elif choice == "Gray":
                B5_T_bandColours.configure(style="grayColour.TLabel")
                B5_T_label_value.set("\u00B1" + "0.05\u0025")
                B5_res_value_label()
        elif choice == "White":
                B5_T_bandColours.configure(style="whiteColour.TLabel")
                B5_T_label_value.set(" ")
                B5_res_value_label()
        else:
                B5_T_bandColours.configure(style="bandColour.TLabel")
                B5_T_label_value.set(" ")
                resistor_5B_T_label_value.configure(text=B5_T_label_value)
                B5_res_value_label()
                breakpoint

# <<< End Five Band Selection >>>


# <<< Start Six Band Selection >>>
def B6_b1_selected(choice) -> int:
        choice = B6_b1_bandColour.get()
        B6_b1_bandColour.set(choice)
        if choice == "Black":
                B6_b1_bandColours.configure(style="blackColour.TLabel")
                B6_b1_label_value.set(0)
        elif choice == "Brown":
                B6_b1_bandColours.configure(style="brownColour.TLabel")
                B6_b1_label_value.set(1)
        elif choice == "Red":
                B6_b1_bandColours.configure(style="redColour.TLabel")
                B6_b1_label_value.set(2)
        elif choice == "Orange":
                B6_b1_bandColours.configure(style="orangeColour.TLabel")
                B6_b1_label_value.set(3)
        elif choice == "Yellow":
                B6_b1_bandColours.configure(style="yellowColour.TLabel")
                B6_b1_label_value.set(4)
        elif choice == "Green":
                B6_b1_bandColours.configure(style="greenColour.TLabel")
                B6_b1_label_value.set(5)
        elif choice == "Blue":
                B6_b1_bandColours.configure(style="blueColour.TLabel")
                B6_b1_label_value.set(6)
        elif choice == "Purple":
                B6_b1_bandColours.configure(style="purpleColour.TLabel")
                B6_b1_label_value.set(7)
        elif choice == "Gray":
                B6_b1_bandColours.configure(style="grayColour.TLabel")
                B6_b1_label_value.set(8)
        elif choice == "White":
                B6_b1_bandColours.configure(style="whiteColour.TLabel")
                B6_b1_label_value.set(9)
        elif choice == "Gold":
                B6_b1_bandColours.configure(style="goldColour.TLabel")
                B6_b1_label_value.set("")
        elif choice == "Silver":
                B6_b1_bandColours.configure(style="silverColour.TLabel")
                B6_b1_label_value.set("")
        elif choice == "Pink":
                B6_b1_bandColours.configure(style="pinkColour.TLabel")
                B6_b1_label_value.set("")
        else:
                B6_b1_bandColours.configure(style="bandColour.TLabel")
                B6_b1_label_value.set(" ")
                resistor_5B_b1_label_value.configure(text=B6_b1_label_value)
                breakpoint


def B6_b2_selected(choice) -> int:
        choice = B6_b2_bandColour.get()
        B6_b2_bandColour.set(choice)
        if choice == "Black":
                B6_b2_bandColours.configure(style="blackColour.TLabel")
                B6_b2_label_value.set(0)
        elif choice == "Brown":
                B6_b2_bandColours.configure(style="brownColour.TLabel")
                B6_b2_label_value.set(1)
        elif choice == "Red":
                B6_b2_bandColours.configure(style="redColour.TLabel")
                B6_b2_label_value.set(2)
        elif choice == "Orange":
                B6_b2_bandColours.configure(style="orangeColour.TLabel")
                B6_b2_label_value.set(3)
        elif choice == "Yellow":
                B6_b2_bandColours.configure(style="yellowColour.TLabel")
                B6_b2_label_value.set(4)
        elif choice == "Green":
                B6_b2_bandColours.configure(style="greenColour.TLabel")
                B6_b2_label_value.set(5)
        elif choice == "Blue":
                B6_b2_bandColours.configure(style="blueColour.TLabel")
                B6_b2_label_value.set(6)
        elif choice == "Purple":
                B6_b2_bandColours.configure(style="purpleColour.TLabel")
                B6_b2_label_value.set(7)
        elif choice == "Gray":
                B6_b2_bandColours.configure(style="grayColour.TLabel")
                B6_b2_label_value.set(8)
        elif choice == "White":
                B6_b2_bandColours.configure(style="whiteColour.TLabel")
                B6_b2_label_value.set(9)
        elif choice == "Gold":
                B6_b2_bandColours.configure(style="goldColour.TLabel")
                B6_b2_label_value.set(str(" "))
        elif choice == "Silver":
                B6_b2_bandColours.configure(style="silverColour.TLabel")
                B6_b2_label_value.set(str(" "))
        elif choice == "Pink":
                B6_b2_bandColours.configure(style="pinkColour.TLabel")
                B6_b2_label_value.set(str(" "))
        else:
                B6_b2_bandColours.configure(style="bandColour.TLabel")
                B6_b2_label_value.set(str(" "))
                resistor_5B_b2_label_value.configure(text=B6_b2_label_value)
                breakpoint


def B6_b3_selected(choice) -> int:
        choice = B6_b3_bandColour.get()
        B6_b3_bandColour.set(choice)
        if choice == "Black":
                B6_b3_bandColours.configure(style="blackColour.TLabel")
                B6_b3_label_value.set(0)
        elif choice == "Brown":
                B6_b3_bandColours.configure(style="brownColour.TLabel")
                B6_b3_label_value.set(1)
        elif choice == "Red":
                B6_b3_bandColours.configure(style="redColour.TLabel")
                B6_b3_label_value.set(2)
        elif choice == "Orange":
                B6_b3_bandColours.configure(style="orangeColour.TLabel")
                B6_b3_label_value.set(3)
        elif choice == "Yellow":
                B6_b3_bandColours.configure(style="yellowColour.TLabel")
                B6_b3_label_value.set(4)
        elif choice == "Green":
                B6_b3_bandColours.configure(style="greenColour.TLabel")
                B6_b3_label_value.set(5)
        elif choice == "Blue":
                B6_b3_bandColours.configure(style="blueColour.TLabel")
                B6_b3_label_value.set(6)
        elif choice == "Purple":
                B6_b3_bandColours.configure(style="purpleColour.TLabel")
                B6_b3_label_value.set(7)
        elif choice == "Gray":
                B6_b3_bandColours.configure(style="grayColour.TLabel")
                B6_b3_label_value.set(8)
        elif choice == "White":
                B6_b3_bandColours.configure(style="whiteColour.TLabel")
                B6_b3_label_value.set(9)
        elif choice == "Gold":
                B6_b3_bandColours.configure(style="goldColour.TLabel")
                B6_b3_label_value.set("")
        elif choice == "Silver":
                B6_b3_bandColours.configure(style="silverColour.TLabel")
                B6_b3_label_value.set("")
        elif choice == "Pink":
                B6_b3_bandColours.configure(style="pinkColour.TLabel")
                B6_b3_label_value.set("")
        else:
                B6_b3_bandColours.configure(style="bandColour.TLabel")
                B6_b3_label_value.set(" ")
                resistor_5B_b3_label_value.configure(text=B6_b3_label_value)
                breakpoint


def B6_M_selected(choice) -> int:
        choice = B6_M_bandColour.get()
        B6_M_bandColour.set(choice)
        if choice == "Black":
                B6_M_bandColours.configure(style="blackColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT ZERO}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Brown":
                B6_M_bandColours.configure(style="brownColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT ONE}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Red":
                B6_M_bandColours.configure(style="redColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT TWO}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Orange":
                B6_M_bandColours.configure(style="orangeColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT THREE}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Yellow":
                B6_M_bandColours.configure(style="yellowColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT FOUR}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Green":
                B6_M_bandColours.configure(style="greenColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT FIVE}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Blue":
                B6_M_bandColours.configure(style="blueColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT SIX}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Purple":
                B6_M_bandColours.configure(style="purpleColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT SEVEN}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Gray":
                B6_M_bandColours.configure(style="grayColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT EIGHT}")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "White":
                B6_M_bandColours.configure(style="whiteColour.TLabel")
                B6_M_label_value.set("10\N{SUPERSCRIPT NINE}")
                resistor_4B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Gold":
                B6_M_bandColours.configure(style="goldColour.TLabel")
                B6_M_label_value.set(0.1)
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Silver":
                B6_M_bandColours.configure(style="silverColour.TLabel")
                B6_M_label_value.set(0.01)
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        elif choice == "Pink":
                B6_M_bandColours.configure(style="pinkColour.TLabel")
                B6_M_label_value.set(0.001)
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
        else:
                B6_M_bandColours.configure(style="bandColour.TLabel")
                B6_M_label_value.set(" ")
                resistor_5B_M_label_value.configure(text=B6_M_label_value)
                breakpoint


def B6_T_selected(choice) -> str:
        choice = B6_T_bandColour.get()
        B6_T_bandColour.set(choice)
        if choice == "Black":
                B6_T_bandColours.configure(style="blackColour.TLabel")
                B6_T_label_value.set("")
        elif choice == "Brown":
                B6_T_bandColours.configure(style="brownColour.TLabel")
                B6_T_label_value.set("\u00B1" + "1\u0025")
        elif choice == "Red":
                B6_T_bandColours.configure(style="redColour.TLabel")
                B6_T_label_value.set("\u00B1" + "2\u0025")
        elif choice == "Orange":
                B6_T_bandColours.configure(style="orangeColour.TLabel")
                B6_T_label_value.set(" ")
        elif choice == "Yellow":
                B6_T_bandColours.configure(style="yellowColour.TLabel")
                B6_T_label_value.set(" ")
        elif choice == "Green":
                B6_T_bandColours.configure(style="greenColour.TLabel")
                B6_T_label_value.set("\u00B1" + "0.5\u0025")
        elif choice == "Blue":
                B6_T_bandColours.configure(style="blueColour.TLabel")
                B6_T_label_value.set("\u00B1" + "0.25\u0025")
        elif choice == "Purple":
                B6_T_bandColours.configure(style="purpleColour.TLabel")
                B6_T_label_value.set("\u00B1" + "0.1\u0025")
        elif choice == "Gray":
                B6_T_bandColours.configure(style="grayColour.TLabel")
                B6_T_label_value.set("\u00B1" + "0.05\u0025")
        elif choice == "White":
                B6_T_bandColours.configure(style="whiteColour.TLabel")
                B6_T_label_value.set(" ")
        elif choice == "Gold":
                B6_T_bandColours.configure(style="goldColour.TLabel")
                B6_T_label_value.set("\u00B1" + "5\u0025")
        elif choice == "Silver":
                B6_T_bandColours.configure(style="silverColour.TLabel")
                B6_T_label_value.set("\u00B1" + "10\u0025")
        elif choice == "Pink":
                B6_T_bandColours.configure(style="pinkColour.TLabel")
                B6_T_label_value.set(" ")
        else:
                B6_T_bandColours.configure(style="bandColour.TLabel")
                B6_T_label_value.set(" ")
                resistor_5B_T_label_value.configure(text=B6_T_label_value)
                breakpoint


def B6_TCR_selected(choice) -> str:
        choice = B6_TCR_bandColour.get()
        B6_TCR_bandColour.set(choice)
        if choice == "Black":
                B6_TCR_bandColours.configure(style="blackColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "250")
                B6_res_value_label()
        elif choice == "Brown":
                B6_TCR_bandColours.configure(style="brownColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "100")
                B6_res_value_label()
        elif choice == "Red":
                B6_TCR_bandColours.configure(style="redColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "50")
                B6_res_value_label()
        elif choice == "Orange":
                B6_TCR_bandColours.configure(style="orangeColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "15")
                B6_res_value_label()
        elif choice == "Yellow":
                B6_TCR_bandColours.configure(style="yellowColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "25")
                B6_res_value_label()
        elif choice == "Green":
                B6_TCR_bandColours.configure(style="greenColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "20")
                B6_res_value_label()
        elif choice == "Blue":
                B6_TCR_bandColours.configure(style="blueColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "10")
                B6_res_value_label()
        elif choice == "Purple":
                B6_TCR_bandColours.configure(style="purpleColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "5")
                B6_res_value_label()
        elif choice == "Gray":
                B6_TCR_bandColours.configure(style="grayColour.TLabel")
                B6_TCR_label_value.set("\u00B1" + "1")
                B6_res_value_label()
        elif choice == "White":
                B6_TCR_bandColours.configure(style="whiteColour.TLabel")
                B6_TCR_label_value.set(" ")
                B6_res_value_label()
        elif choice == "Gold":
                B6_TCR_bandColours.configure(style="goldColour.TLabel")
                B6_TCR_label_value.set(" ")
                B6_res_value_label()
        elif choice == "Silver":
                B6_TCR_bandColours.configure(style="silverColour.TLabel")
                B6_TCR_label_value.set(" ")
                B6_res_value_label()
        elif choice == "Pink":
                B6_TCR_bandColours.configure(style="pinkColour.TLabel")
                B6_TCR_label_value.set(" ")
                B6_res_value_label()
        else:
                B6_TCR_bandColours.configure(style="bandColour.TLabel")
                B6_TCR_label_value.set(" ")
                B6_res_value_label()
                breakpoint

# <<< End Six Band Selection >>>


def getMain():
        # Center The Main Program Window When Launched
        width = 335
        height = 167
        x = (window.winfo_screenwidth()//2)-(width//2)
        y = (window.winfo_screenheight()//2)-(height//2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        r3cCalc_label_title.grid()
        landing_frame.grid(row=1, column=0, rowspan=4, columnspan=6, padx=5, pady=5)
        r3cCalc_main_frame.grid_forget()
        r3cCalc_band_frame.grid_forget()
        resistor_3B_Frame.pack_forget()
        resistor_4B_Frame.pack_forget()
        resistor_6B_Frame.pack_forget()
        resistor_5B_Frame.pack_forget()
        copyright_label.grid()
        breakpoint


def showThree():
        # Center The Main Program Window When Launched
        width = 325
        height = 332
        x = (window.winfo_screenwidth()//2)-(width//2)
        y = (window.winfo_screenheight()//2)-(height//2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        r3cCalc_label_title.grid()
        landing_frame.grid()
        r3cCalc_main_frame.grid()      
        r3cCalc_band_frame.grid()
        resistor_3B_Frame.pack()
        resistor_4B_Frame.pack_forget()
        resistor_6B_Frame.pack_forget()
        resistor_5B_Frame.pack_forget()
        copyright_label.grid()
        clearThreeBandTable()
        breakpoint



def showFour():
        # Center The Main Program Window When Launched
        width = 335
        height = 332
        x = (window.winfo_screenwidth()//2)-(width//2)
        y = (window.winfo_screenheight()//2)-(height//2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        r3cCalc_label_title.grid()
        landing_frame.grid()
        r3cCalc_main_frame.grid()
        r3cCalc_band_frame.grid()
        resistor_4B_Frame.pack()
        resistor_3B_Frame.pack_forget()
        resistor_6B_Frame.pack_forget()
        resistor_5B_Frame.pack_forget()
        copyright_label.grid()
        clearFourBandTable()
        breakpoint


def showFive():
        # Center The Main Program Window When Launched
        width = 420
        height = 332
        x = (window.winfo_screenwidth()//2)-(width//2)
        y = (window.winfo_screenheight()//2)-(height//2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        r3cCalc_label_title.grid()
        landing_frame.grid()
        r3cCalc_main_frame.grid()
        r3cCalc_band_frame.grid()
        resistor_5B_Frame .pack()
        resistor_3B_Frame.pack_forget()
        resistor_4B_Frame .pack_forget()
        resistor_6B_Frame .pack_forget()
        copyright_label.grid()
        clearFiveBandTable()
        breakpoint


def showSix():
        # Center The Main Program Window When Launched
        width = 512
        height = 332
        x = (window.winfo_screenwidth()//2)-(width//2)
        y = (window.winfo_screenheight()//2)-(height//2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        r3cCalc_label_title.grid()
        clearSixBandTable()
        landing_frame.grid()
        r3cCalc_main_frame.grid()
        r3cCalc_band_frame.grid()
        resistor_6B_Frame .pack()
        resistor_3B_Frame.pack_forget()
        resistor_4B_Frame .pack_forget()
        resistor_5B_Frame .pack_forget()
        copyright_label.grid()
        breakpoint


# Apps Menu Item to Exit the Program
def quit_main():
        window.quit()
        breakpoint


# ======================================================================================================================================
# ================================================================ Start Main Frame Layout =============================================
# ======================================================================================================================================
r3c_frame = tk.Frame(master = window)
r3cCalc_label_title = ttk.Label(master = r3c_frame)
r3cCalc_label_title.configure(text="Resistor Colour Code Calculator", style="r3cCalcTitleLight.TLabel") 
r3cCalc_label_title.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

# ///=== Landing Page ===\\\ #
landing_frame = ttk.Frame(master = r3c_frame)
landing_frame.configure(style="mainFrame.TFrame")

# ============= Logo to be put in a Canvas ======================#
# ---------------------------------------------------------------#
r3c_logo_label = ttk.Label(master = landing_frame)
r3c_logo_label.configure(style="r3cCalcTitleLight.TLabel", justify="center", anchor="center")
r3cLogo = tk.Canvas(landing_frame, width=110, height=70, bg='#5de67f')
logo_image = tk.PhotoImage(file='imgs/r3c_logo.png')
r3cLogo.create_image((55, 35), image=logo_image)
r3cLogo.grid(row=0, column=0, columnspan=2, padx=5)
r3c_logo_label.grid(row=0, column=0, columnspan=2, ipadx=5, ipady=10)
# ---------------------------------------------------------------#
# ============= Logo to be put in a Canvas ======================#

brand_btn_frame = ttk.Frame(master = landing_frame)
brand_btn_frame.configure(style="mainFrame.TFrame")

band3_button = ttk.Button(master = brand_btn_frame)
band3_button.configure(style="band_btn.TButton", takefocus=True, command=showThree, text="Three Band")
band3_button.grid(row=0, column=0, columnspan=2, padx=5)

band4_button = ttk.Button(master = brand_btn_frame)
band4_button.configure(style="band_btn.TButton", takefocus=True, command=showFour, text="Four Band")
band4_button.grid(row=0, column=3, columnspan=2, padx=5)

band5_button = ttk.Button(master = brand_btn_frame)
band5_button.configure(style="band_btn.TButton", takefocus=True, command=showFive, text="Five Band")
band5_button.grid(row=1, column=0, columnspan=2, pady=5)

band6_button = ttk.Button(master = brand_btn_frame)
band6_button.configure(style="band_btn.TButton", takefocus=True, command=showSix, text="Six Band")
band6_button.grid(row=1, column=3, columnspan=2)

brand_btn_frame.grid(row=0, column=3, columnspan=4, padx=5, pady=5)
landing_frame.grid(row=1, column=0, rowspan=4, columnspan=6, pady=5, ipadx=7)


# ///=== Main Frame ===\\\ #
r3cCalc_main_frame = ttk.Frame(master = r3c_frame)
r3cCalc_main_frame.configure(style="mainFrame.TFrame")

r3cCalc_band_frame = ttk.Frame(master= r3cCalc_main_frame)
resistor_3B_Frame = ttk.Frame(master = r3cCalc_band_frame)
resistor_3B_Frame.configure(style="B4Bands.TFrame")
resistor_3B_label = ttk.Label(master=resistor_3B_Frame)
resistor_3B_label.configure(style="resLabel.TLabel", text="Three Band Resister")
resistor_3B_label.pack(side="top", expand=True, fill="x")

# <<< Start Four Band Resistor Frame >>>
B3_bands_frame = ttk.Frame(master=resistor_3B_Frame)
resistor_3B_b1_labelFrame = ttk.LabelFrame(master = B3_bands_frame)
resistor_3B_b1_labelFrame.configure(style="bandTitle.TLabel", text=" 1st Band ")

# creating Option Menu widget ==================================
B3_b1_bandColourSet = ['B1','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B3_b1_bandColour = StringVar()
B3_b1_bandColour.set(B3_b1_bandColourSet[0])
B3_b1_bandColours = ttk.OptionMenu(
resistor_3B_b1_labelFrame,
B3_b1_bandColour,
*B3_b1_bandColourSet,
command=B3_b1_selected)
B3_b1_bandColours.configure(style="bandColour.TLabel", width=7)
B3_b1_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_3B_b1_label_value = ttk.Label(master = resistor_3B_b1_labelFrame, textvariable=B3_b1_label_value)
resistor_3B_b1_label_value.configure(style="bandValue.TLabel")
resistor_3B_b1_label_value.pack(side="bottom", expand=True, fill="x", padx=5, pady=5)
resistor_3B_b1_labelFrame.pack(side="left", expand=True, fill="y", pady=10, ipadx=10)


resistor_3B_b2_labelFrame = ttk.LabelFrame(master = B3_bands_frame)
resistor_3B_b2_labelFrame.configure(style="bandTitle.TLabel", text=" 2nd Band ")

# creating Option Menu widget ==================================
B3_b2_bandColourSet = ['B2','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B3_b2_bandColour = StringVar()
B3_b2_bandColour.set(B3_b2_bandColourSet[0])
B3_b2_bandColours = ttk.OptionMenu(
resistor_3B_b2_labelFrame,
B3_b2_bandColour,
*B3_b2_bandColourSet,
command=B3_b2_selected)
B3_b2_bandColours.configure(style="bandColour.TLabel", width=7)
B3_b2_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_3B_b2_label_value = ttk.Label(master = resistor_3B_b2_labelFrame, textvariable=B3_b2_label_value)
resistor_3B_b2_label_value.configure(style="bandValue.TLabel")
resistor_3B_b2_label_value.pack(side="bottom", expand=True, fill="x")
resistor_3B_b2_labelFrame.pack(side="left", expand=True, fill="y", pady=10, ipadx=10)

resistor_3B_M_labelFrame = ttk.LabelFrame(master = B3_bands_frame)
resistor_3B_M_labelFrame.configure(style="bandTitle.TLabel", text=" M Band ")

# creating Option Menu widget ==================================
B3_M_bandColourSet = ['M','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B3_M_bandColour = StringVar()
B3_M_bandColour.set(B3_M_bandColourSet[0])
B3_M_bandColours = ttk.OptionMenu(
resistor_3B_M_labelFrame,
B3_M_bandColour,
*B3_M_bandColourSet,
command=B3_M_selected)
B3_M_bandColours.configure(style="bandColour.TLabel", width=7)
B3_M_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_3B_M_label_value = ttk.Label(master = resistor_3B_M_labelFrame, textvariable=B3_M_label_value)
resistor_3B_M_label_value.configure(style="bandValue.TLabel")
resistor_3B_M_label_value.pack(side="bottom", expand=True, fill="x")
resistor_3B_M_labelFrame.pack(side="left", expand=True, fill="y", pady=10, ipadx=10)

b3_resistor_value = IntVar()
b3_resistor_value.set("")
B3_bands_frame.pack(side="top", expand=True, fill="both", padx=5, pady=5, anchor="center")
resistor_3B_value_label = ttk.Label(master=resistor_3B_Frame)
resistor_3B_value_label.configure(style="valueLabel.TLabel", text="")
resistor_3B_value_label.pack(side="top", expand=True, fill="both")
resistor_3B_Frame.pack(side="top", expand=True, fill="both", padx=5, pady=5, anchor="center")
# <<< End three Band >>>
# <<<<<<<<<<<<<>>>>>>>>>>> #

resistor_4B_Frame = ttk.Frame(master = r3cCalc_band_frame)
resistor_4B_Frame.configure(style="B4Bands.TFrame")
resistor_4B_label = ttk.Label(master=resistor_4B_Frame)
resistor_4B_label.configure(style="resLabel.TLabel", text="Four Band Resister")
resistor_4B_label.pack(side="top", expand=True, fill="x")

# <<< Start Four Band Resistor Frame >>>
B4_bands_frame = ttk.Frame(master=resistor_4B_Frame)
resistor_4B_b1_labelFrame = ttk.LabelFrame(master = B4_bands_frame)
resistor_4B_b1_labelFrame.configure(style="bandTitle.TLabel", text=" 1st Band ")

# creating Option Menu widget ==================================
B4_b1_bandColourSet = ['B1','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B4_b1_bandColour = StringVar()
B4_b1_bandColour.set(B4_b1_bandColourSet[0])
B4_b1_bandColours = ttk.OptionMenu(
resistor_4B_b1_labelFrame,
B4_b1_bandColour,
*B4_b1_bandColourSet,
command=B4_b1_selected)
B4_b1_bandColours.configure(style="bandColour.TLabel", width=7)
B4_b1_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_4B_b1_label_value = ttk.Label(master = resistor_4B_b1_labelFrame, textvariable=B4_b1_label_value)
resistor_4B_b1_label_value.configure(style="bandValue.TLabel")
resistor_4B_b1_label_value.pack(side="bottom", expand=True, fill="x")
resistor_4B_b1_labelFrame.pack(side="left", expand=True, fill="y", pady=10)
resistor_4B_b2_labelFrame = ttk.LabelFrame(master = B4_bands_frame)
resistor_4B_b2_labelFrame.configure(style="bandTitle.TLabel", text=" 2nd Band ")

# creating Option Menu widget ==================================
B4_b2_bandColourSet = ['B2','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B4_b2_bandColour = StringVar()
B4_b2_bandColour.set(B4_b2_bandColourSet[0])
B4_b2_bandColours = ttk.OptionMenu(
resistor_4B_b2_labelFrame,
B4_b2_bandColour,
*B4_b2_bandColourSet,
command=B4_b2_selected)
B4_b2_bandColours.configure(style="bandColour.TLabel", width=7)
B4_b2_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_4B_b2_label_value = ttk.Label(master = resistor_4B_b2_labelFrame, textvariable=B4_b2_label_value)
resistor_4B_b2_label_value.configure(style="bandValue.TLabel")
resistor_4B_b2_label_value.pack(side="bottom", expand=True, fill="x")
resistor_4B_b2_labelFrame.pack(side="left", expand=True, fill="y", pady=10)
resistor_4B_M_labelFrame = ttk.LabelFrame(master = B4_bands_frame)
resistor_4B_M_labelFrame.configure(style="bandTitle.TLabel", text=" M Band ")

# creating Option Menu widget ==================================
B4_M_bandColourSet = ['M','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B4_M_bandColour = StringVar()
B4_M_bandColour.set(B4_M_bandColourSet[0])
B4_M_bandColours = ttk.OptionMenu(
resistor_4B_M_labelFrame,
B4_M_bandColour,
*B4_M_bandColourSet,
command=B4_M_selected)
B4_M_bandColours.configure(style="bandColour.TLabel", width=7)
B4_M_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_4B_M_label_value = ttk.Label(master = resistor_4B_M_labelFrame, textvariable=B4_M_label_value)
resistor_4B_M_label_value.configure(style="bandValue.TLabel")
resistor_4B_M_label_value.pack(side="bottom", expand=True, fill="x")
resistor_4B_M_labelFrame.pack(side="left", expand=True, fill="y", pady=10)

b4_resistor_value = IntVar()
b4_resistor_value.set("")

resistor_4B_T_labelFrame = ttk.LabelFrame(master = B4_bands_frame)
resistor_4B_T_labelFrame.configure(style="bandTitle.TLabel", text=" T Band ")

# creating Option Menu widget ==================================
B4_T_bandColourSet = ['T','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B4_T_bandColour = StringVar()
B4_T_bandColour.set(B4_T_bandColourSet[0])
B4_T_bandColours = ttk.OptionMenu(
resistor_4B_T_labelFrame,
B4_T_bandColour,
*B4_T_bandColourSet,
command=B4_T_selected)
B4_T_bandColours.configure(style="bandColour.TLabel", width=7)
B4_T_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_4B_T_label_value = ttk.Label(master = resistor_4B_T_labelFrame, textvariable=B4_T_label_value)
resistor_4B_T_label_value.configure(style="bandValue.TLabel")
resistor_4B_T_label_value.pack(side="bottom", expand=True, fill="x")
resistor_4B_T_labelFrame.pack(side="left", expand=True, fill="y", pady=10)
B4_bands_frame.pack(side="top", expand=True, fill="both", padx=5, pady=5,  anchor="center")
resistor_4B_value_label = ttk.Label(master=resistor_4B_Frame)
resistor_4B_value_label.configure(style="valueLabel.TLabel", text="")
resistor_4B_value_label.pack(side="top", expand=True, fill="both", padx=5, pady=5)
resistor_4B_Frame.pack(side="top", expand=True, fill="both", padx=5, pady=5)
# << End Four Band Frame >>>



# <<< Start Five Band Frame >>>
resistor_5B_Frame = ttk.Frame(master = r3cCalc_band_frame)
resistor_5B_Frame.configure(style="B4Bands.TFrame")
resistor_5B_label = ttk.Label(master=resistor_5B_Frame)
resistor_5B_label.configure(style="resLabel.TLabel", text="Five Band Resister")
resistor_5B_label.pack(side="top", expand=True, fill="x")

# <<< Start Five Band Resistor Frame >>>
B5_bands_frame = ttk.Frame(master=resistor_5B_Frame)
resistor_5B_b1_labelFrame = ttk.LabelFrame(master = B5_bands_frame)
resistor_5B_b1_labelFrame.configure(style="bandTitle.TLabel", text=" 1st Band ")

# creating Option Menu widget ==================================
B5_b1_bandColourSet = ['B1','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B5_b1_bandColour = StringVar()
B5_b1_bandColour.set(B5_b1_bandColourSet[0])
B5_b1_bandColours = ttk.OptionMenu(
resistor_5B_b1_labelFrame,
B5_b1_bandColour,
*B5_b1_bandColourSet,
command=B5_b1_selected)
B5_b1_bandColours.configure(style="bandColour.TLabel", width=7)
B5_b1_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_5B_b1_label_value = ttk.Label(master = resistor_5B_b1_labelFrame, textvariable=B5_b1_label_value)
resistor_5B_b1_label_value.configure(style="bandValue.TLabel")
resistor_5B_b1_label_value.pack(side="bottom", expand=True, fill="x")
resistor_5B_b1_labelFrame.pack(side="left", expand=True, fill="y", pady=10)


resistor_5B_b2_labelFrame = ttk.LabelFrame(master = B5_bands_frame)
resistor_5B_b2_labelFrame.configure(style="bandTitle.TLabel", text=" 2nd Band ")

# creating Option Menu widget ==================================
B5_b2_bandColourSet = ['B2','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B5_b2_bandColour = StringVar()
B5_b2_bandColour.set(B5_b2_bandColourSet[0])
B5_b2_bandColours = ttk.OptionMenu(
resistor_5B_b2_labelFrame,
B5_b2_bandColour,
*B5_b2_bandColourSet,
command=B5_b2_selected)
B5_b2_bandColours.configure(style="bandColour.TLabel", width=7)
B5_b2_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_5B_b2_label_value = ttk.Label(master = resistor_5B_b2_labelFrame, textvariable=B5_b2_label_value)
resistor_5B_b2_label_value.configure(style="bandValue.TLabel")
resistor_5B_b2_label_value.pack(side="bottom", expand=True, fill="x")
resistor_5B_b2_labelFrame.pack(side="left", expand=True, fill="y", pady=10)

resistor_5B_b3_labelFrame = ttk.LabelFrame(master = B5_bands_frame)
resistor_5B_b3_labelFrame.configure(style="bandTitle.TLabel", text=" 3rd Band ")

# creating Option Menu widget ==================================
B5_b3_bandColourSet = ['b3','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B5_b3_bandColour = StringVar()
B5_b3_bandColour.set(B5_b3_bandColourSet[0])
B5_b3_bandColours = ttk.OptionMenu(
resistor_5B_b3_labelFrame,
B5_b3_bandColour,
*B5_b3_bandColourSet,
command=B5_b3_selected)
B5_b3_bandColours.configure(style="bandColour.TLabel", width=7)
B5_b3_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_5B_b3_label_value = ttk.Label(master = resistor_5B_b3_labelFrame, textvariable=B5_b3_label_value)
resistor_5B_b3_label_value.configure(style="bandValue.TLabel")
resistor_5B_b3_label_value.pack(side="bottom", expand=True, fill="x")
resistor_5B_b3_labelFrame.pack(side="left", expand=True, fill="y", pady=10)

resistor_5B_M_labelFrame = ttk.LabelFrame(master = B5_bands_frame)
resistor_5B_M_labelFrame.configure(style="bandTitle.TLabel", text=" M Band ")

# creating Option Menu widget ==================================
B5_M_bandColourSet = ['M','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B5_M_bandColour = StringVar()
B5_M_bandColour.set(B5_M_bandColourSet[0])
B5_M_bandColours = ttk.OptionMenu(
resistor_5B_M_labelFrame,
B5_M_bandColour,
*B5_M_bandColourSet,
command=B5_M_selected)
B5_M_bandColours.configure(style="bandColour.TLabel", width=7)
B5_M_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_5B_M_label_value = ttk.Label(master = resistor_5B_M_labelFrame, textvariable=B5_M_label_value)
resistor_5B_M_label_value.configure(style="bandValue.TLabel")
resistor_5B_M_label_value.pack(side="bottom", expand=True, fill="x")
resistor_5B_M_labelFrame.pack(side="left", expand=True, fill="y", pady=10)

B5_resistor_value = IntVar()
B5_resistor_value.set("")

resistor_5B_T_labelFrame = ttk.LabelFrame(master = B5_bands_frame)
resistor_5B_T_labelFrame.configure(style="bandTitle.TLabel", text=" T Band ")

# creating Option Menu widget ==================================
B5_T_bandColourSet = ['T','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White']

# setting variable for Integers and Strings ========================
B5_T_bandColour = StringVar()
B5_T_bandColour.set(B5_T_bandColourSet[0])
B5_T_bandColours = ttk.OptionMenu(
resistor_5B_T_labelFrame,
B5_T_bandColour,
*B5_T_bandColourSet,
command=B5_T_selected)
B5_T_bandColours.configure(style="bandColour.TLabel", width=7)
B5_T_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_5B_T_label_value = ttk.Label(master = resistor_5B_T_labelFrame, textvariable=B5_T_label_value)
resistor_5B_T_label_value.configure(style="bandValue.TLabel")
resistor_5B_T_label_value.pack(side="bottom", expand=True, fill="x")
resistor_5B_T_labelFrame.pack(side="left", expand=True, fill="y", pady=10)
B5_bands_frame.pack(side="top", expand=True, fill="both", padx=5, pady=5)
resistor_5B_value_label = ttk.Label(master=resistor_5B_Frame)
resistor_5B_value_label.configure(style="valueLabel.TLabel", text="")
resistor_5B_value_label.pack(side="top", expand=True, fill="both", padx=5, pady=5)
resistor_5B_Frame.pack(side="top", expand=True, fill="both", padx=5, pady=5)
# <<< End Five Band Resistor Frame >>>
# <<< End Five Band Frame >>>


# <<< Start Six Band Frame >>>
resistor_6B_Frame = ttk.Frame(master = r3cCalc_band_frame)
resistor_6B_Frame.configure(style="B4Bands.TFrame")
resistor_6B_label = ttk.Label(master=resistor_6B_Frame)
resistor_6B_label.configure(style="resLabel.TLabel", text="Six Band Resister")
resistor_6B_label.pack(side="top", expand=True, fill="x")

# <<< Start Five Band Resistor Frame >>>
B6_bands_frame = ttk.Frame(master=resistor_6B_Frame)
resistor_6B_b1_labelFrame = ttk.LabelFrame(master = B6_bands_frame)
resistor_6B_b1_labelFrame.configure(style="bandTitle.TLabel", text=" 1st Band ")

# creating Option Menu widget ==================================
B6_b1_bandColourSet = ['B1','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White', 'Gold', 'Silver', 'Pink']

# setting variable for Integers and Strings ========================
B6_b1_bandColour = StringVar()
B6_b1_bandColour.set(B6_b1_bandColourSet[0])
B6_b1_bandColours = ttk.OptionMenu(
resistor_6B_b1_labelFrame,
B6_b1_bandColour,
*B6_b1_bandColourSet,
command=B6_b1_selected)
B6_b1_bandColours.configure(style="bandColour.TLabel", width=7)
B6_b1_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_6B_b1_label_value = ttk.Label(master = resistor_6B_b1_labelFrame, textvariable=B6_b1_label_value)
resistor_6B_b1_label_value.configure(style="bandValue.TLabel")
resistor_6B_b1_label_value.pack(side="bottom", expand=True, fill="x")
resistor_6B_b1_labelFrame.pack(side="left", expand=True, fill="y", pady=10)


resistor_6B_b2_labelFrame = ttk.LabelFrame(master = B6_bands_frame)
resistor_6B_b2_labelFrame.configure(style="bandTitle.TLabel", text=" 2nd Band ")

# creating Option Menu widget ==================================
B6_b2_bandColourSet = ['B2','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White', 'Gold', 'Silver', 'Pink']

# setting variable for Integers and Strings ========================
B6_b2_bandColour = StringVar()
B6_b2_bandColour.set(B6_b2_bandColourSet[0])
B6_b2_bandColours = ttk.OptionMenu(
resistor_6B_b2_labelFrame,
B6_b2_bandColour,
*B6_b2_bandColourSet,
command=B6_b2_selected)
B6_b2_bandColours.configure(style="bandColour.TLabel", width=7)
B6_b2_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_6B_b2_label_value = ttk.Label(master = resistor_6B_b2_labelFrame, textvariable=B6_b2_label_value)
resistor_6B_b2_label_value.configure(style="bandValue.TLabel")
resistor_6B_b2_label_value.pack(side="bottom", expand=True, fill="x")
resistor_6B_b2_labelFrame.pack(side="left", expand=True, fill="y", pady=10)

resistor_6B_b3_labelFrame = ttk.LabelFrame(master = B6_bands_frame)
resistor_6B_b3_labelFrame.configure(style="bandTitle.TLabel", text=" 3rd Band ")

# creating Option Menu widget ==================================
B6_b3_bandColourSet = ['B3','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White', 'Gold', 'Silver', 'Pink']

# setting variable for Integers and Strings ========================
B6_b3_bandColour = StringVar()
B6_b3_bandColour.set(B6_b3_bandColourSet[0])
B6_b3_bandColours = ttk.OptionMenu(
resistor_6B_b3_labelFrame,
B6_b3_bandColour,
*B6_b3_bandColourSet,
command=B6_b3_selected)
B6_b3_bandColours.configure(style="bandColour.TLabel", width=7)
B6_b3_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_6B_b3_label_value = ttk.Label(master = resistor_6B_b3_labelFrame, textvariable=B6_b3_label_value)
resistor_6B_b3_label_value.configure(style="bandValue.TLabel")
resistor_6B_b3_label_value.pack(side="bottom", expand=True, fill="x")
resistor_6B_b3_labelFrame.pack(side="left", expand=True, fill="y", pady=10)

resistor_6B_M_labelFrame = ttk.LabelFrame(master = B6_bands_frame)
resistor_6B_M_labelFrame.configure(style="bandTitle.TLabel", text=" M Band ")

# creating Option Menu widget ==================================
B6_M_bandColourSet = ['M','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White', 'Gold', 'Silver', 'Pink']

# setting variable for Integers and Strings ========================
B6_M_bandColour = StringVar()
B6_M_bandColour.set(B6_M_bandColourSet[0])
B6_M_bandColours = ttk.OptionMenu(
resistor_6B_M_labelFrame,
B6_M_bandColour,
*B6_M_bandColourSet,
command=B6_M_selected)
B6_M_bandColours.configure(style="bandColour.TLabel", width=7)
B6_M_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_6B_M_label_value = ttk.Label(master = resistor_6B_M_labelFrame, textvariable=B6_M_label_value)
resistor_6B_M_label_value.configure(style="bandValue.TLabel")
resistor_6B_M_label_value.pack(side="bottom", expand=True, fill="x")
resistor_6B_M_labelFrame.pack(side="left", expand=True, fill="y", pady=10)

B6_resistor_value = IntVar()
B6_resistor_value.set("")

resistor_6B_T_labelFrame = ttk.LabelFrame(master = B6_bands_frame)
resistor_6B_T_labelFrame.configure(style="bandTitle.TLabel", text=" T Band ")

# creating Option Menu widget ==================================
B6_T_bandColourSet = ['T','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White', 'Gold', 'Silver', 'Pink']

# setting variable for Integers and Strings ========================
B6_T_bandColour = StringVar()
B6_T_bandColour.set(B6_T_bandColourSet[0])
B6_T_bandColours = ttk.OptionMenu(
resistor_6B_T_labelFrame,
B6_T_bandColour,
*B6_T_bandColourSet,
command=B6_T_selected)
B6_T_bandColours.configure(style="bandColour.TLabel", width=7)
B6_T_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_6B_T_label_value = ttk.Label(master = resistor_6B_T_labelFrame, textvariable=B6_T_label_value)
resistor_6B_T_label_value.configure(style="bandValue.TLabel")
resistor_6B_T_label_value.pack(side="bottom", expand=True, fill="x")
resistor_6B_T_labelFrame.pack(side="left", expand=True, fill="y", pady=10)

resistor_6B_TCR_labelFrame = ttk.LabelFrame(master = B6_bands_frame)
resistor_6B_TCR_labelFrame.configure(style="bandTitle.TLabel", text=" TCR Band ")

# creating Option Menu widget ==================================
B6_TCR_bandColourSet = ['TCR','Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Gray', 'White', 'Gold', 'Silver', 'Pink']

# setting variable for Integers and Strings ========================
B6_TCR_bandColour = StringVar()
B6_TCR_bandColour.set(B6_TCR_bandColourSet[0])
B6_TCR_bandColours = ttk.OptionMenu(
resistor_6B_TCR_labelFrame,
B6_TCR_bandColour,
*B6_TCR_bandColourSet,
command=B6_TCR_selected)
B6_TCR_bandColours.configure(style="bandColour.TLabel", width=7)
B6_TCR_bandColours.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5, anchor="center")
resistor_6B_TCR_label_value = ttk.Label(master = resistor_6B_TCR_labelFrame, textvariable=B6_TCR_label_value)
resistor_6B_TCR_label_value.configure(style="bandValue.TLabel")
resistor_6B_TCR_label_value.pack(side="bottom", expand=True, fill="x")
resistor_6B_TCR_labelFrame.pack(side="left", expand=True, fill="y", pady=10)
B6_bands_frame.pack(side="top", expand=True, fill="both", padx=5, pady=5)
resistor_6B_value_label = ttk.Label(master=resistor_6B_Frame)
resistor_6B_value_label.configure(style="valueLabel.TLabel", text="")
resistor_6B_value_label.pack(side="top", expand=True, fill="both", padx=5, pady=5)
resistor_6B_Frame.pack(side="top", expand=True, fill="both", padx=5, pady=5)
# <<< End Six Band Resistor Frame >>>
# <<< End Six Band Frame >>>

r3cCalc_band_frame.grid(row=0, column=0, rowspan=4, columnspan=6, padx=5, pady=5, sticky="nsew")
r3cCalc_main_frame.grid(row=2, column=0, sticky="nsew", rowspan=4, columnspan=6, ipady=5)
copyright_label = ttk.Label(master = window)
copyright_label.configure(style="copyright.TLabel", text="dashWoorkZ Sovereign Society \u00A9 2024 - Since 2023")
copyright_label.grid(row=10, column=0, columnspan=6, sticky="nsew", ipady=5)
r3c_frame.grid(row=0, column=0, rowspan=10, columnspan=6, sticky="nsew")


def clearThreeBandTable():
        B3_M_bandColour.set(B3_M_bandColourSet[0])
        B3_M_bandColours.configure(style='bandColour.TLabel')
        B3_b1_bandColour.set(B3_b1_bandColourSet[0])
        B3_b1_bandColours.configure(style='bandColour.TLabel')
        B3_b2_bandColour.set(B3_b2_bandColourSet[0])
        B3_b2_bandColours.configure(style='bandColour.TLabel')
        B3_b1_label_value.set(" ")  
        B3_b2_label_value.set(" ") 
        B3_M_label_value.set(" ") 
        resistor_3B_M_label_value.configure(style="bandValue.TLabel")
        resistor_3B_b2_label_value.configure(style="bandValue.TLabel")
        resistor_3B_b1_label_value.configure(style="bandValue.TLabel")
        resistor_3B_value_label.configure(text=" ")   
        breakpoint



def clearFourBandTable():
        B4_T_bandColour.set(B4_T_bandColourSet[0])
        B4_T_bandColours.configure(style='bandColour.TLabel')
        B4_M_bandColour.set(B4_M_bandColourSet[0])
        B4_M_bandColours.configure(style='bandColour.TLabel')
        B4_b1_bandColour.set(B4_b1_bandColourSet[0])
        B4_b1_bandColours.configure(style='bandColour.TLabel')
        B4_b2_bandColour.set(B4_b2_bandColourSet[0])
        B4_b2_bandColours.configure(style='bandColour.TLabel')
        B4_b1_label_value.set(" ")  
        B4_b2_label_value.set(" ") 
        B4_M_label_value.set(" ") 
        B4_T_label_value.set(" ")
        resistor_4B_T_label_value.configure(style="bandValue.TLabel", text=" ")
        resistor_4B_M_label_value.configure(style="bandValue.TLabel")
        resistor_4B_b2_label_value.configure(style="bandValue.TLabel")
        resistor_4B_b1_label_value.configure(style="bandValue.TLabel")
        resistor_4B_value_label.configure(text=" ")   
        breakpoint


def clearFiveBandTable():
        B5_T_bandColour.set(B5_T_bandColourSet[0])
        B5_T_bandColours.configure(style='bandColour.TLabel')
        B5_M_bandColour.set(B5_M_bandColourSet[0])
        B5_M_bandColours.configure(style='bandColour.TLabel')
        B5_b1_bandColour.set(B5_b1_bandColourSet[0])
        B5_b1_bandColours.configure(style='bandColour.TLabel')
        B5_b2_bandColour.set(B5_b2_bandColourSet[0])
        B5_b3_bandColours.configure(style='bandColour.TLabel')
        B5_b3_bandColour.set(B5_b2_bandColourSet[0])
        B5_b2_bandColours.configure(style='bandColour.TLabel')
        B5_b1_label_value.set(" ")  
        B5_b2_label_value.set(" ")
        B5_b3_label_value.set(" ")  
        B5_M_label_value.set(" ") 
        B5_T_label_value.set(" ")
        resistor_5B_T_label_value.configure(style="bandValue.TLabel")
        resistor_5B_M_label_value.configure(style="bandValue.TLabel")
        resistor_5B_b3_label_value.configure(style="bandValue.TLabel")
        resistor_5B_b2_label_value.configure(style="bandValue.TLabel")
        resistor_5B_b1_label_value.configure(style="bandValue.TLabel")
        resistor_5B_value_label.configure(text=" ")   
        breakpoint    


def clearSixBandTable():
        B6_TCR_bandColour.set(B6_TCR_bandColourSet[0])
        B6_TCR_bandColours.configure(style='bandColour.TLabel')
        B6_T_bandColour.set(B6_T_bandColourSet[0])
        B6_T_bandColours.configure(style='bandColour.TLabel')
        B6_M_bandColour.set(B6_M_bandColourSet[0])
        B6_M_bandColours.configure(style='bandColour.TLabel')
        B6_b1_bandColour.set(B6_b1_bandColourSet[0])
        B6_b1_bandColours.configure(style='bandColour.TLabel')
        B6_b2_bandColour.set(B6_b2_bandColourSet[0])
        B6_b3_bandColours.configure(style='bandColour.TLabel')
        B6_b3_bandColour.set(B6_b2_bandColourSet[0])
        B6_b2_bandColours.configure(style='bandColour.TLabel')
        B6_b1_label_value.set(" ")  
        B6_b2_label_value.set(" ")
        B6_b3_label_value.set(" ")  
        B6_M_label_value.set(" ") 
        B6_T_label_value.set(" ")
        B6_TCR_label_value.set(" ")
        resistor_6B_TCR_label_value.configure(style="bandValue.TLabel")
        resistor_6B_T_label_value.configure(style="bandValue.TLabel")
        resistor_6B_M_label_value.configure(style="bandValue.TLabel")
        resistor_6B_b3_label_value.configure(style="bandValue.TLabel")
        resistor_6B_b2_label_value.configure(style="bandValue.TLabel")
        resistor_6B_b1_label_value.configure(style="bandValue.TLabel")
        resistor_6B_value_label.configure(text=" ")   
        breakpoint    


# ================================================================================================================================================================
# ================================================================ End Main Frame Layout =========================================================================
# ================================================================================================================================================================


# ================================================================================================================================================================
# =================================================== Start of Information Widgets ============================================================================
# ================================================================================================================================================================

        # Donation Window
def open_privacy_window():
        lawful_privacy_window = Toplevel(window)
        lawful_privacy_window.title("Lawful Privacy Statement")
        width = 300
        height = 540
        x = (lawful_privacy_window.winfo_screenwidth()//2)-(width//2)
        y = (lawful_privacy_window.winfo_screenheight()//2)-(height//2)
        lawful_privacy_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        lawful_privacy_window.configure(bg="#f0f0f0")
        # Lawful Privacy Statement
        lawful_privacy_frame = ttk.Frame(master=lawful_privacy_window)
        lawful_privacy_frame.configure(style="lawfulLight.TFrame")


       # ---------------------------------------------------------------#
        # ============= Logo to be put in a Canvas ======================
        privacy_frame = ttk.Frame(master=lawful_privacy_frame)
        privacy_frame.configure(style="privacyLight.TFrame")
        privacy_frame_label = ttk.Label(master=privacy_frame)
        privacy_frame_label.configure(style="privacyLight.TLabel", font=("Times New Roman", 10, "bold"), anchor="center", justify="center", wraplength=290, text="dashWoorkz Sovereign Society\n is a Private Society, we will not invade Your Privacy, or provide anyone any information we may have about you, any information we have about you will have been acquired with Your Consent, if we were to do anything with the information we have about you, it would be with Your Consent")
        privacy_frame_label.pack(fill="x", expand="True", side="top")
        privacy_frame.pack(fill="both", expand=True)
        lawful_frame = ttk.Frame(master=lawful_privacy_frame)
        lawful_frame.configure(style="lawfulLight.TFrame")
        lawful_frame_label = ttk.Label(master=lawful_frame)
        lawful_frame_label.configure(style="lawfulLight.TLabel", font=("Times New Roman", 10, "bold"), justify="center", anchor="center", wraplength=290, text="dashWoorkz Sovereign Society\nEstablished: 2023\nR3C Calc v1\nResistor Colour Code Calculator\nCalculates:\nThree Band, Four Band, Five Band and Six Band Resistors")
        lawful_frame_label.pack(fill="x", expand="True", side="top", ipady=5, ipadx=5)
        lawful_frame.pack(fill="both", expand=True)
        gpl_frame = ttk.Frame(master=lawful_privacy_frame)
        gpl_frame.configure(style="lawfulLight.TFrame")
        lawful_gpl_label = ttk.Label(master = gpl_frame)
        lawful_gpl_label.configure(justify="center", anchor="center", font=("Roboto, sans-serif", 8, "bold"), wraplength=290, background="#f7d4f6", foreground="#9370d8", text="    Resistor Colour Code Calculator\nCopyright (C) 2024\n  dashWoorkZ Sovereign Society\n\nThis program is free software: Resistor Colour Code Calculator\nCopyright (C) 2024\n  dashWoorkZ Sovereign Society\n\nThis program is free software: you can redistribute it modification to the program is expressly forbidden unless the author has granted permission.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.")
        lawful_gpl_label.grid(row=2, column=0, columnspan=4, sticky="nsew", ipady=5, ipadx=5)
        gpl_frame.pack(fill="both", expand="True", side="bottom", ipady=5, ipadx=5)
        lawful_privacy_frame.grid(row=0, column=0, columnspan=4, rowspan=3)
        
        lawful_privacy_frame.rowconfigure(0, weight = 1)
        lawful_privacy_frame.columnconfigure(0, weight = 1)
        lawful_privacy_frame.rowconfigure(1, weight = 1)
        lawful_privacy_frame.columnconfigure(1, weight = 1)
        lawful_privacy_frame.rowconfigure(2, weight = 1)
        lawful_privacy_frame.columnconfigure(2, weight = 1)
        lawful_privacy_frame.columnconfigure(3, weight = 1)

# End of Lawful Privacy Statement
# ===================

# Support Window
def open_support_window():
    support_window = Toplevel(window)
    support_window.title("Support")
    width = 400
    height = 350
    x = (support_window.winfo_screenwidth()//2)-(width//2)
    y = (support_window.winfo_screenheight()//2)-(height//2)
    support_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    support_window.configure(bg="#f0f0f0")
    support_label = Label(support_window)
    support_label.configure(font=("Times New Roman", 11, "bold"),highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True,  background="#ffe4c4", foreground="#5c3608", text="Donate:\nIf you enjoyed this program and would\n like to contribute to our work:\n\ndashWoorkz Sovereign Society:\ndashwoorkz@dashwoorkz.ca\n\nE-Transfer:\nLord :Dash: La Londe\nManaging Director:\ndash@dashwoorkz.ca\n\n Bitcoin:\nBTC:38YwKspQ8hdxAmGQUPP7LvXPRucdZURNu5\n\n Merchandise Online:\nhttp://everythingdash.creator-spring.com/")
    support_label.pack(fill="both", expand=True)
    
# End of Support Window
# ===================
# ===================

# Credits Window
def open_credits_window():
        donate_window = Toplevel(window)
        donate_window.title("Credits")
        donate_window.geometry("310x200")
        donate_window.configure(bg="#f0f0f0")
        donate_label = Label(donate_window)
        donate_label.configure(font=("Times New Roman", 11, "bold"),highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True,  background="#ffe4c4", foreground="#5c3608", text="\n'Praise Our lord God Almighty, \nbecause of who He is, \ni am able to be'\n R3C Calc v1\n dashwoorkZ Sovereign Society\nAuthor: Lord: Dash: La Londe\n \u00A9 2024\n All Rights Reserved \n Without Recourse - UCC 1-308")
        donate_label.pack(fill="both", expand=True)

# End of Donation Window
# ===================

# Contact Information Window
def open_contact_window():
        contact_window = Toplevel(window)
        contact_window.title("Contact Us")
        contact_window.geometry("310x200")
        contact_window.configure(bg="#f0f0f0")
        
        label_contact = Label(contact_window, text="Contact Information", foreground="#fd3adf", bg="#f7d4f6", font=("Helvetica", 12, "bold"))
        label_contact.pack(fill="both", expand=True)

        label_society = Label(contact_window, text="dashWoorkZ Sovereign Society", foreground="#4169e1", bg="#99cfe7", font=("Helvetica", 10, "bold"))
        label_society.pack(fill="both", expand=True)
        
        label_email = Label(contact_window, text="Email: dashwoorkz@dashwoorkz.ca", foreground="#4169e1", bg="#99cfe7", font=("Helvetica", 10))
        label_email.pack(fill="both", expand=True)
        
        label_mdirector = Label(contact_window, text="Managing Director:", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10, "bold"))
        label_mdirector.pack(fill="both", expand=True)
        
        label_mdName = Label(contact_window, text="Lord :Dash: La Londe", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10))
        label_mdName.pack(fill="both", expand=True)

        label_md_email = Label(contact_window, text="Email: dash@dashwoorkz.ca", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10, "bold"))
        label_md_email.pack(fill="both", expand=True)

        label_csDirector = Label(contact_window, text="Community Services Director:", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10, "bold"))
        label_csDirector.pack(fill="both", expand=True)
        
        label_csdName = Label(contact_window, text="Lady :Jeanette-Elizabeth: Hiuser", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10))
        label_csdName.pack(fill="both", expand=True)

        label_cs_email = Label(contact_window, text="Email: jeanette.elizabeth@dashwoorkz.ca", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10))
        label_cs_email.pack(fill="both", expand=True)




getMain()


window.configure(menu = menu)

window.mainloop()

