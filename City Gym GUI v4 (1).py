# I installed the module with "pip3 install customtkinter" (pip3 install customtkinter --upgrade, if existing)
# Libraries i have imported to create this GUI 
import tkinter as Tk
from tkinter import *
from tkinter import messagebox
import customtkinter
import re
from tkinter import ttk
import os


# This is the window parameters
root = customtkinter.CTk()
root.title("City Gym Member Registration App")
root.geometry("985x700")
# root.state("zoomed")
root.configure(background='Black')


# This is the class that holds the GUI and all its functions  
class registration:
    

    def __init__(self, master):
    
        # Frames that make up the background, foreground, highlight headers, categories and progress bars  
        self.frame_top = customtkinter.CTkFrame(master=root, width=985, height=690, fg_color= "#262626", corner_radius=30, bg_color="#262626")
        self.frame_top.pack(fill='both', expand=True)

        self.frame_top1 = customtkinter.CTkFrame(self.frame_top, width=985, height=690, fg_color= "#262626", corner_radius=30, bg_color="#262626", border_color="#FFE4C4", border_width=3)
        self.frame_top1.pack()

        self.frame_top_left = customtkinter.CTkFrame(self.frame_top1, width=475, height=260, fg_color= "#383838", corner_radius=30, bg_color="#262626", border_width=3)
        self.frame_top_left.place(x=10, y=70)

        self.frame_bottom_left = customtkinter.CTkFrame(self.frame_top1, width=475, height=335, fg_color= "#383838", corner_radius=30,bg_color="#262626", border_width=3)
        self.frame_bottom_left.place(x=10, y=340)

        self.frame_top_right = customtkinter.CTkFrame(self.frame_top1, width=475, height=260, fg_color=	"#383838", corner_radius=30, bg_color="#262626", border_width=3)
        self.frame_top_right.place(x=500, y=70)

        self.frame_Bottom_right = customtkinter.CTkFrame(self.frame_top1, width=475, height=335, fg_color= "#383838", corner_radius=30, bg_color="#262626", border_width=3)
        self.frame_Bottom_right.place(x=500, y=340)
        
        
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("moving.Horizontal.TProgressbar", background="#1E90FF", troughcolor= "#383838")

        self.progress_bar = ttk.Progressbar(self.frame_top_left, orient="horizontal", length=300, mode="determinate", style= "moving.Horizontal.TProgressbar")
        self.progress_bar.place(x=20, y=32)
        
        self.progress_bar1 = ttk.Progressbar(self.frame_bottom_left, orient="horizontal", length=300, mode="determinate", style="moving.Horizontal.TProgressbar")
        self.progress_bar1.place(x=20, y=32)

        # Heading for form (Top Center)=============================================================================================================
        self.frame_heading4 = customtkinter.CTkFrame(self.frame_top1, width=600, height=50, fg_color="#383838", corner_radius=30, bg_color="#262626", border_color="#FFE4C4", border_width=3)
        self.frame_heading4.place(x=180, y= 10)
        
        self.form_heading = customtkinter.CTkLabel(self.frame_heading4, text='City GYM New Member Registration', font=("italic",20), fg_color="#383838", text_color="#1E90FF")
        self.form_heading.place(x=130, y=10)

        # Category heading (Customer Information) (Top Left)=============================================================================================

        self.catcategory_name1 = customtkinter.CTkLabel(master=self.frame_top_left, text="Customer Details - Step 1", font=("italic", 16),fg_color="#383838", text_color="#1E90FF")
        self.catcategory_name1.place(x=20, y=4)

        # Labels (Customer Information) (Top Left)==========================================================================================================
        self.fname = customtkinter.CTkLabel(master=self.frame_top_left, text="First Name", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.fname.place(x=20, y=50)

        self.sname = customtkinter.CTkLabel(master=self.frame_top_left, text="Last Name", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.sname.place(x=20, y=100)

        self.mnumber = customtkinter.CTkLabel(master=self.frame_top_left, text="Mobile Number", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.mnumber.place(x=20, y=150)

        self.address = customtkinter.CTkLabel(master=self.frame_top_left, text="Full Address", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.address.place(x=20, y=200)

        # Entry box (Customer Information) (Top Left)==========================================================================================================
        self.fname_textb = customtkinter.CTkEntry(master=self.frame_top_left, width=437, fg_color= "#333333", text_color="#FFFAF0")
        self.fname_textb.place(x=20, y=75)
        self.fname_var = StringVar()

        self.sname_textb = customtkinter.CTkEntry(master=self.frame_top_left, width=437, fg_color= "#333333", text_color="#FFFAF0")
        self.sname_textb.place(x=20, y=125)
        self.sname_var = StringVar()

        self.mnumber_textb = customtkinter.CTkEntry(master=self.frame_top_left, width=437, fg_color= "#333333", text_color="#FFFAF0")
        self.mnumber_textb.place(x=20, y=175)
        self.mnumber_var = StringVar()

        self.address_textb = customtkinter.CTkEntry(master=self.frame_top_left, width=437, fg_color= "#333333", text_color="#FFFAF0")
        self.address_textb.place(x=20, y=225)
        self.address_var = StringVar()

        # This is grouping all Text entries and binding an event and progress bar function to increase the progress bar every time data is entered into an Entry Field 
        for entry in [self.fname_textb, self.sname_textb, self.mnumber_textb, self.address_textb]:
            entry.bind("<KeyRelease>", self.change_progress)

        # Category heading (Membership Information) (Bottom left)==========================================================================================================
        self.catcategory_name2 = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Membership Payment Details - Step 2", font=("italic", 16), fg_color=	"#383838", text_color="#1E90FF")     
        self.catcategory_name2.place(x=20, y=4)

        # Labels (Membership Type) (Bottom Left)==========================================================================================================
        self.membership_types = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Membership Type", font=("italic", 14), fg_color="#383838", bg_color="transparent", text_color="#FFFAF0")
        self.membership_types.place(x=20, y=50)
        
        self.frame_heading1 = Frame(master=self.frame_bottom_left, width=250, height=0, highlightbackground="#F8F8FF", highlightthickness=2)
        self.frame_heading1.place(x=20, y=72)

        self.membership_types1 = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Basic Membership: ", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_types1.place(x=20, y=75)

        self.membership_types2 = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Regular Membership: ", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_types2.place(x=20, y=100)

        self.membership_types2 = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Premium Membership: ", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_types2.place(x=20, y=125)

        # Check box (Membership Types) (Bottom Left)===================================================================================================================================================================================================================================================
        self.membership_type_choice = StringVar()
        self.membership_type_default = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.membership_type_choice, value="Default")
        self.membership_type_choice.set("Default")
        #This is the variable that keeps track of where the second progress bar is % wise
        self.bar = 0

        self.membership_basic_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.membership_type_choice, value="Basic Membership", text="$10pw/$43.30pm", font=("italic", 14), text_color_disabled="#1E90FF", bg_color="#383838" , command=self.change_progress1, text_color="#FFFAF0")
        self.membership_basic_check.place(x=280, y=75)
         
        self.membership_regular_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.membership_type_choice, value="Regular Membership", text="$15pw/$65.60pm", font=("italic", 14), text_color_disabled="1E90FF", bg_color="#383838", command=self.change_progress1, text_color="#FFFAF0")
        self.membership_regular_check.place(x=280, y=100)
        
        self.membership_premium_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.membership_type_choice, value="Premium Membership", text="$20pw/$86.60pm", font=("italic", 14), text_color_disabled="1E90FF", bg_color="#383838", command=self.change_progress1, text_color="#FFFAF0")
        self.membership_premium_check.place(x=280, y=125)
        
        # Labels (Membership Duration) (Bottom Left)===================================================================================================================================================================================================================================================
        self.membership_duration = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Membership Duration", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_duration.place(x=20, y=150)

        self.frame_heading2 = Frame(master=self.frame_bottom_left, width=250, height=0, highlightbackground="#F8F8FF", highlightthickness=2)
        self.frame_heading2.place(x=20, y=172)

        self.membership_duration1 = customtkinter.CTkLabel(master=self.frame_bottom_left, text="3 Months                   ", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_duration1.place(x=20, y=175)

        self.membership_duration2 = customtkinter.CTkLabel(master=self.frame_bottom_left, text="12 Months                 ", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_duration2.place(x=20, y=200)

        self.membership_duration2 = customtkinter.CTkLabel(master=self.frame_bottom_left, text="24 Months                ", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_duration2.place(x=20, y=225)

        # Check box (Membership Duration) (Bottom Left)===================================================================================================================================================================================================================================================
        # I have created a non-placed radio button to set an unselected as the default 
        self.membership_duration_choice = StringVar()     
        self.membership_duration_default = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.membership_duration_choice, value="Default", )
        self.membership_duration_choice.set("Default")

        self.membership_duration_3_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.membership_duration_choice, value="3 Months", text="", bg_color="#383838", width=5, command=self.change_progress2)
        self.membership_duration_3_check.place(x=280, y=175)

        self.membership_duration_12_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.membership_duration_choice, value="12 Months", text="", bg_color="#383838", width=5, command=self.change_progress2)
        self.membership_duration_12_check.place(x=280, y=200)

        self.membership_duration_24_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.membership_duration_choice, value="24 Months", text="", bg_color="#383838", width=5, command=self.change_progress2)
        self.membership_duration_24_check.place(x=280, y=225)

        # Label (Payment Options) (Bottom Left)===================================================================================================================================================================================================================================================
        self.payment_option = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Payment options", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.payment_option.place(x=20, y=250)

        self.frame_heading3 = Frame(master=self.frame_bottom_left, width=250, height=0, highlightbackground="#F8F8FF", highlightthickness=2)
        self.frame_heading3.place(x=20, y=272)

        self.payment_option_direct_debit = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Direct debit: ", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.payment_option_direct_debit.place(x=20, y=275)

        # Check box (Payment Options) (Bottom Left)===================================================================================================================================================================================================================================================
        # I have created a non-placed radio button to set an unselected as the default  
        self.debit_payment_choice = StringVar()
        self.membership_payment_default = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.debit_payment_choice, value="Default")
        self.debit_payment_choice.set("Default")

        self.debit_payment_yes_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.debit_payment_choice, value="Yes", text="Yes", font=("italic", 14), text_color_disabled="FFFAF0", bg_color="#383838", command=self.change_progress3, text_color="#FFFAF0")
        self.debit_payment_yes_check.place(x=280, y=275)

        self.debit_payment_no_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.debit_payment_choice, value="No", text="No", font=("italic", 14), text_color_disabled="FFFAF0", bg_color="#383838", width=10, command=self.change_progress3, text_color="#FFFAF0")
        self.debit_payment_no_check.place(x=370, y=275)

        # Label (Payment Frequency) (Bottom Left)===================================================================================================================================================================================================================================================
        self.frequency_option = customtkinter.CTkLabel(master=self.frame_bottom_left, text="Frequency of payment: ", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.frequency_option.place(x=20, y=300)

        # Check box (Payment Fequency) (Bottom Left)===================================================================================================================================================================================================================================================
        # I have created a non-placed radio button to set an unselected as the default 
        self.payment_frequency_choice = StringVar()
        self.membership_frequency_default = Radiobutton(master=self.frame_bottom_left, variable=self.payment_frequency_choice, value="Default")
        self.payment_frequency_choice.set("Default")

        self.payment_frequency1_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.payment_frequency_choice, value="Weekly", text="Weekly", font=("italic", 14), text_color_disabled="1E90FF", bg_color="#383838", width=7, command=self.change_progress4, text_color="#FFFAF0")
        self.payment_frequency1_check.place(x=280, y=300)

        self.payment_frequency2_check = customtkinter.CTkRadioButton(master=self.frame_bottom_left, variable=self.payment_frequency_choice, value="Monthly", text="Monthly", font=("italic", 14), text_color_disabled="1E90FF", bg_color="#383838", width=7, command=self.change_progress4, text_color="#FFFAF0")
        self.payment_frequency2_check.place(x=370, y=300)
        
        # Category heading (Membership Extras) (Top Right)===================================================================================================================================================================================================================================================
        self.catcategory_name3 = customtkinter.CTkLabel(master=self.frame_top_right, text="Membership Extras - Step 3", font=("italic", 16), fg_color="#383838", text_color="#1E90FF")
        self.catcategory_name3.place(x=20, y=4)
            
        # Labels (Membership Extras) (Top Right)===================================================================================================================================================================================================================================================================
        self.membership_extra_header = customtkinter.CTkLabel(master=self.frame_top_right, text="Membership Extras", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_extra_header.place(x=20, y=50)

        self.frame_heading3 = Frame(master=self.frame_top_right, width=250, height=0, highlightbackground="#F8F8FF", highlightthickness=2)
        self.frame_heading3.place(x=20, y=72)

        self.membership_extra1 = customtkinter.CTkLabel(master=self.frame_top_right, text="24/7 Access", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_extra1.place(x=20, y=75)

        self.membership_extra2 = customtkinter.CTkLabel(master=self.frame_top_right, text="Personal Trainer", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_extra2.place(x=20, y=100)

        self.membership_extra3 = customtkinter.CTkLabel(master=self.frame_top_right, text="Diet Consultation", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_extra3.place(x=20, y=125)

        self.membership_extra4 = customtkinter.CTkLabel(master=self.frame_top_right, text="Access To Online Fitness Videos", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_extra4.place(x=20, y=150)

        # Check Box (Membership Extra) (Top Right)===================================================================================================================================================================================================================================================
        # I have .set all the check boxes to the offvalue of 0
        self.membership_extra1_box = StringVar()
        self.membership_extra1_check = customtkinter.CTkCheckBox(master=self.frame_top_right, variable=self.membership_extra1_box, onvalue="24/7 Access", offvalue=0, text="$1.00 pw", font=("italic", 14), bg_color="#383838", width=10, text_color="#FFFAF0")
        self.membership_extra1_box.set(0)
        self.membership_extra1_check.place(x=280, y=75)
        
        self.membership_extra2_box = StringVar()
        self.membership_extra2_check = customtkinter.CTkCheckBox(master=self.frame_top_right, variable=self.membership_extra2_box, onvalue="Personal Trainer", offvalue=0, text="$20.00 pw", font=("italic", 14), width=10, bg_color="#383838", text_color="#FFFAF0")
        self.membership_extra2_box.set(0)
        self.membership_extra2_check.place(x=280, y=100)

        self.membership_extra3_box = StringVar()
        self.membership_extra3_check = customtkinter.CTkCheckBox(master=self.frame_top_right, variable=self.membership_extra3_box, onvalue="Diet Consultation", offvalue=0, text="$20.00 pw", font=("italic", 14), width=10, bg_color="#383838", text_color="#FFFAF0")
        self.membership_extra3_box.set(0)
        self.membership_extra3_check.place(x=280, y=125)

        self.membership_extra4_box = StringVar()
        self.membership_extra4_check = customtkinter.CTkCheckBox(master=self.frame_top_right, variable=self.membership_extra4_box, onvalue="Access To Online Fitness Videos", offvalue=0, text="$2.00 pw", font=("italic", 14), width=10, bg_color="#383838", text_color="#FFFAF0")
        self.membership_extra4_box.set(0)
        self.membership_extra4_check.place(x=280, y=150)

        # Calculate Button (All Data) (Top Right)===================================================================================================================================================================================================================================================
        self.calculate = customtkinter.CTkButton(master=self.frame_top_right, text="Calculate", command=lambda: self.calculate_costs(), font=("italic", 16), fg_color="#1E90FF", text_color="#FFFAF0")
        self.calculate.place(x=20, y=220)

        # Category heading (Membership Form Input Summary) (Bottom Right)===================================================================================================================================================================================================================================================
        self.catcategory_name3 = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="Membership Form Summary - Step 4", font=("italic", 16), fg_color="#383838", text_color="#1E90FF")
        self.catcategory_name3.place(x=20, y=4)

        # Label (Membership Form Input Sumamary)===================================================================================================================================================================================================================================================
        self.membership_total_cost = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="Membership Cost:", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_total_cost.place(x=20, y=50)

        self.membership_total_extras = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="Extra Charges:", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_total_extras.place(x=20, y=75)

        self.membership_total_discount = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="Discount Total:", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_total_discount.place(x=20, y=100)

        self.membership_total_net = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="Net Membership:", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_total_net.place(x=20, y=125)

        self.membership_total__regular_payment = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="Regular Payment Total:", font=("italic", 14), fg_color="#383838", text_color="#FFFAF0")
        self.membership_total__regular_payment.place(x=20, y=150)

        # Discount Infromation (Bottom Right)===================================================================================================================================================================================================================================================
        self.frame_heading4 = Frame(master=self.frame_Bottom_right, width=445, height=0, highlightbackground="#F8F8FF", highlightthickness=2)
        self.frame_heading4.place(x=20, y=190)
        
        self.membership_total_extras = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type.", font=("italic", 10), fg_color="#383838", text_color="#FFFAF0")
        self.membership_total_extras.place(x=20, y=200)

        self.membership_total_discount = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="Sign up for 24 months to receive a $5 per week discount on any membership type.", font=("italic", 10), fg_color="#383838", text_color="#FFFAF0")
        self.membership_total_discount.place(x=20, y=230)

        self.membership_total_net = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="For direct debits, there is a 1% discount on the base membership cost.", font=("italic", 10), fg_color="#383838", text_color="#FFFAF0")
        self.membership_total_net.place(x=20, y=255)

        self.membership_cost_total_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="", width=32, text_color="#FFFAF0")
        self.membership_cost_total_output.place(x=200, y=50)

        self.extra_charges_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="", width=32, text_color="#FFFAF0")
        self.extra_charges_output.place(x=200, y=75)

        self.total_discount_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="", width=32, text_color="#FFFAF0")
        self.total_discount_output.place(x=200, y=100)

        self.net_membership_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="", width=32, text_color="#FFFAF0")
        self.net_membership_output.place(x=200, y=125)

        self.regular_payments_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text="", width=32, text_color="#FFFAF0")
        self.regular_payments_output.place(x=200, y=150)

        # Save Data to Txt File Button (Bottom Right)===================================================================================================================================================================================================================================================
        self.submit = customtkinter.CTkButton(master=self.frame_Bottom_right, text="Submit", command=lambda: self.save_to_file(), font=("italic", 16), fg_color="#1E90FF", text_color="#FFFAF0")
        self.submit.place(x=20, y=295)

        # Reset Button (Bottom Right)===================================================================================================================================================================================================================================================
        self.reset = customtkinter.CTkButton(master=self.frame_Bottom_right, text="Reset", command=lambda: self.reset_button(), font=("italic", 16), fg_color="#1E90FF", text_color="#FFFAF0")
        self.reset.place(x=170, y=295)

        # Exit Button (Exit Form) (Bottom Right)===================================================================================================================================================================================================================================================
        self.exit = customtkinter.CTkButton(master=self.frame_Bottom_right, text="Exit", command=root.quit, font=("italic", 16), fg_color="#1E90FF", text_color="#FFFAF0")
        self.exit.place(x=320, y=295)
        #======================================================== ** End of GUI Frame ** ===============================================================================================================================================================================================================================================================================================================
    
    # This function updates a progress bar based on the number of text box entries filled.
    def change_progress(self, event):
        self.entries_filled = 0
        for entry in [self.fname_textb, self.sname_textb, self.mnumber_textb, self.address_textb]:
            if entry.get() == "": 
                pass
            else:  
                self.entries_filled += 1
                self.progress_bar["value"] = self.entries_filled * 25  


    # This function updates the progress bar by 25% when the membership type is not set to "Default".
    def change_progress1(self): 
        
        self.change_progress1_flag = False
        
        if self.membership_type_choice == "Default":
            pass  
        elif self.change_progress1_flag == True:
            pass
        else: 
             if self.bar == 0:
                self.progress_bar1["value"] = self.bar + 25
                self.progress_bar1.update()
                self.bar = self.progress_bar1["value"]
                self.change_progress1_flag = True


    # This function updates the progress bar by 25% when the membership type is not set to "Default".      
    def change_progress2(self):
        
        self.change_progress2_flag = False

        if self.membership_duration_choice == "Default":
            pass
        elif self.change_progress2_flag == True:
            pass
        else:  
              if self.bar <= 25:
                self.progress_bar1["value"] = self.bar + 25
                self.progress_bar1.update()
                self.bar = self.progress_bar1["value"]
                self.change_progress2_flag == True


    # This function updates the progress bar by 25% when the membership type is not set to "Default".      
    def change_progress3(self):
        self.change_progress3_flag = False

        if self.debit_payment_choice == "Default":
            pass
        elif self.change_progress3_flag == True:
            pass
        else:  
            if self.bar <= 50:  
                self.progress_bar1["value"] = self.bar + 25
                self.progress_bar1.update()
                self.bar = self.progress_bar1["value"]
                self.change_progress3_flag == True
            
    # This function updates the progress bar by 25% when the membership type is not set to "Default".          
    def change_progress4(self):
        self.change_progress4_flag = False

        if self.payment_frequency_choice == "Default":
            pass
        elif self.change_progress4_flag == True:
            pass
        else:  
            if self.bar <= 75:  
                self.progress_bar1["value"] = self.bar + 25
                self.progress_bar1.update()
                self.bar = self.progress_bar1["value"]
                self.change_progress4_flag = True


    # Display an error popup with detailed descriptions when user input is invalid.
    def popup_entry_error(self):
        
        message1 = "Please review Step 2, the following errors have occured: \n"
        membership_details_blank_fail = False
        self.proceed_to_calculate = False

        if self.membership_type_choice.get() == "Default" or self.membership_duration_choice.get() =="Default" or self.debit_payment_choice.get() == "Default" or self.payment_frequency_choice.get() == "Default":
            message1 += "\n Unselected items in Step 2 "
            membership_details_blank_fail = True


        if  membership_details_blank_fail:
            messagebox.showerror(title="error", message=message1, ) 
            membership_details_blank_fail = False
            message1 = "\nPlease review Step 2, the following errors have occured: "
            
        else:
            self.proceed_to_calculate = True
            pass


    # This function resets all the elements on the page to their default values.
    def reset_button(self):
        self.bar = 0
        self.entries_filled = 0

        self.progress_bar1["value"] = self.bar
        self.progress_bar1.update()

        self.progress_bar["value"] = self.entries_filled
        self.progress_bar.update()

        self.change_progress1_flag = False
        self.change_progress2_flag = False
        self.change_progress3_flag = False
        self.change_progress4_flag = False

        boxes = [self.membership_extra1_check, self.membership_extra2_check, self.membership_extra3_check,
        self.membership_extra4_check]

        elements = [self.fname_textb, self.sname_textb, self.mnumber_textb, self.address_textb, 
            self.membership_type_choice, self.membership_duration_choice, self.debit_payment_choice, 
            self.payment_frequency_choice, self.membership_extra1_box, self.membership_extra2_box, 
            self.membership_extra3_box, self.membership_extra4_box]
        
        outputs = [self.membership_cost_total_output, self.extra_charges_output, self.total_discount_output, self.net_membership_output,
             self.regular_payments_output]

        for element in elements:
            if isinstance(element, customtkinter.CTkEntry):
                element.delete(0, END)
            else:
                element.set("Default")

        for box in boxes:
            box.deselect()

        for output in outputs:
            output.configure(text="")


    # This function is used to calculate the cost of the membership based on the user's chosen options
    def calculate_costs(self):
        

        self.popup_entry_error()

        if self.proceed_to_calculate:    

            # Variables used thoughout this function
            self.membership_type = []
            self.membership_type_result = []
            self.membership_type_discount = []
            self.total_extras = []
            self.discount1 = []
            self.discount1.append(0)

            # This code assigns the appropriate amount to the membership_type list depending on the membership type chosen by the user.
            if (self.membership_type_choice.get() == "Basic Membership"):
                
                self.membership_type.append(10.00)

            elif (self.membership_type_choice.get() == "Regular Membership"):
                
                self.membership_type.append(15.00)

            else:
                (self.membership_type_choice.get() == "Premium Membership")
                
                self.membership_type.append(20.00)

            # This code calculates the total amount for the membership type chosen by the user and prints it
            
            self.membership_t = 0
            self.membership_t = sum(self.membership_type)     
            print(self.membership_t)
                 
            # This is where we are applying the 1% discount for a debit or no discount 
            if (self.debit_payment_choice.get() == "Yes"):

                self.membership_type_result = [item * 0.01 for item in self.membership_type]
                
                self.discount1[0] = self.membership_type_result[0]
                self.membership_type_result[0] = self.membership_type[0] - self.membership_type_result[0]
                
            else:
                (self.debit_payment_choice.get() == "No")

                self.membership_type_result = self.membership_type

            # This is where we are applying the discount associated with the membership duration 
            if(self.membership_duration_choice.get() == "3 Months"):
                self.membership_type_result = self.membership_type_result
            
            elif (self.membership_duration_choice.get() == "12 Months"):
                self.membership_type_discount.append(2.00)
                self.membership_type_result[0] = self.membership_type_result[0] - self.membership_type_discount[0]

            else:
                (self.membership_duration_choice.get() == "24 Months")
                self.membership_type_discount.append(5.00)
                self.membership_type_result[0] = self.membership_type_result[0] - self.membership_type_discount[0]

            # This is the variable that houses the total discount (membership type chosen minus any applied discounts)
            self.total_d = self.discount1 + self.membership_type_discount
            self.total_discount = sum(self.total_d)
            print(self.total_discount)

            if (self.membership_extra1_box.get() == "24/7 Access"):
                self.membership_type_result.append(1.00) 
                self.total_extras.append(1.00)
                
            if (self.membership_extra2_box.get() == "Personal Trainer"):
                self.membership_type_result.append(20.00) 
                self.total_extras.append(20.00)

            if (self.membership_extra3_box.get() == "Diet Consultation"):
                self.membership_type_result.append(20.00) 
                self.total_extras.append(20.00)
            
            if (self.membership_extra4_box.get() == "Access To Online Fitness Videos"):
                self.membership_type_result.append(2.00)
                self.total_extras.append(2.00)
            
            # This is the varaible that houses the total extras 
            self.total_extra_sum = sum(self.total_extras)
            print(self.total_extra_sum) 
            
            # This is the varaible that houses the total net membership cost 
            self.membership_cost_output = sum(self.membership_type_result)
            print(self.membership_cost_output)

            # This is validating what payment frequency has been chosen and displaying the relevant cost associated (after deductions)
            if (self.payment_frequency_choice.get() == "Weekly"):
                self.reg_membership_cost = self.membership_cost_output
                print(self.reg_membership_cost)
 
            else:
                (self.payment_frequency_choice.get() == "Monthly")
                self.reg_membership_cost = self.membership_cost_output * 4
                print(self.reg_membership_cost)
                

            # This is displaying the costs per field based on chosen options 
            self.membership_cost_total_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text=(f"$ {self.membership_t}"), width=32, text_color="#FFFAF0")
            self.membership_cost_total_output.place(x=200, y=50)

            self.extra_charges_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text=(f"$ {self.total_extra_sum}"), width=32, text_color="#FFFAF0")
            self.extra_charges_output.place(x=200, y=75)

            self.total_discount_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text=(f"$ {self.total_discount}"), width=32, text_color="#FFFAF0")
            self.total_discount_output.place(x=200, y=100)

            self.net_membership_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text=(f"$ {self.membership_cost_output}"), width=32, text_color="#FFFAF0")
            self.net_membership_output.place(x=200, y=125)

            self.regular_payments_output = customtkinter.CTkLabel(master=self.frame_Bottom_right, text=(f"$ {self.reg_membership_cost}"), width=32, text_color="#FFFAF0")
            self.regular_payments_output.place(x=200, y=150)

            #This resets the proceed to calculate variable so that it can resart the functions use 
            self.proceed_to_calculate = False

    # This function first validates all inputs and the following:    
    # This is then used to create/append the data into a file called "membersdatasaved.txt"
    def save_to_file(self):
        
        message1 = "Please review Step 1 & Step 2, the following errors have occured: \n"
        first_name_fail = False
        last_name_fail = False
        mobile_num_fail = False
        full_address_fail = False
        membership_details_blank_fail = False
        global proceed_to_calculate 
        proceed_to_calculate = False


        if not re.match(r'^[a-zA-Z ]+$', self.fname_textb.get()) or self.fname_textb.get() == "":
            message1 += "\n First name can't be blank and should contain character letters only \n"
            first_name_fail = True

        if not re.match(r'^[a-zA-Z ]+$', self.sname_textb.get()) or self.fname_textb.get() == "":
            last_name_fail = True
            message1 += "\n Last name can't be blank and should contain character letters only \n"
            

        if not re.match(r'^[0-9 ]+$', self.mnumber_textb.get()) or self.mnumber_textb.get() == "":
            mobile_num_fail = True
            message1 += "\n Invalid mobile number entered\n"

        if self.address_textb.get() == "":
            message1 += "\n Full address can't be black and should contain a valid address \n"
            full_address_fail = True

        if self.membership_type_choice.get() == "Default" or self.membership_duration_choice.get() =="Default" or self.debit_payment_choice.get() == "Default" or self.payment_frequency_choice.get() == "Default":
            message1 += "\n Unselected items in Step 2 "
            membership_details_blank_fail = True


        if first_name_fail or last_name_fail or mobile_num_fail or full_address_fail or membership_details_blank_fail:
            messagebox.showerror(title="error", message=message1, ) 
            first_name_fail = False
            last_name_fail = False
            mobile_num_fail = False
            full_address_fail = False
            membership_details_blank_fail = False
            message1 = "\nPlease review Step 1 & Step 2, the following errors have occured: "
            
        else:
            proceed_to_calculate = True
            pass
            
            # file = open("membersdatasaved", "a+")# Open the txt file in append mode
            with open(r'C:\Temp\membersdatasaved.txt', 'a+') as f:
        
            # Write the info of the user to the txt file
                f.write("\n")
                f.write("First Name: " + self.fname_textb.get())
                f.write("\n")
                f.write("Last Name: " + self.sname_textb.get())
                f.write("\n")
                f.write("Mobile number: " + self.mnumber_textb.get())
                f.write("\n")
                f.write("Full Address: " + self.address_textb.get())
                f.write("\n")
                
                # Write the membership type of the user to the txt file
                self.membership_type = self.membership_type_choice.get()
                f.write("Membership Type: " + self.membership_type)
                f.write("\n")

                # Write the cost details to the txt file
                f.write("Base Memebership cost: $" + str(self.membership_t))
                f.write("\n")
                f.write("Extra cost : $" + str(self.total_extra_sum))
                f.write("\n")
                f.write("Total discount: $" + str(self.total_discount))
                f.write("\n")
                f.write("Net membership cost: $" + str(self.membership_cost_output))
                f.write("\n")

                # Write the payment details to the txt file
                self.payment_frequency = self.payment_frequency_choice.get()
                if (self.payment_frequency == "Weekly"):
                    f.write("Regular Payment: " + str(self.reg_membership_cost))
                    f.write("\n") 
                    f.write("Payment Frequency: " + self.payment_frequency)
                    f.write("\n")       

                # payment_frequency == "Monthly"
                else: 
                    f.write("Regular Payment: " + str(self.reg_membership_cost))
                    f.write("\n") 
                    f.write("Payment Frequency: " + self.payment_frequency)
                    f.write("\n")

                self.payment_type = self.debit_payment_choice.get()
                if (self.debit_payment_choice.get() == "Yes"):
                    f.write("Payment By Direct Debit: " + self.payment_type)
                    f.write("\n")
            
                else:
                    (self.debit_payment_choice.get() == "No")
                    f.write("Payment By Direct Debit: " + self.payment_type)
                    f.write("\n")
                
                f.close() 

reg_form = registration(root)
root.mainloop()