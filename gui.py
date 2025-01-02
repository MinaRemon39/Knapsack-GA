import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as mbox
import requests
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry("820x420")
app.title("Knapsack problem")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app.resizable(width=False, height=False)

input_frame = ctk.CTkScrollableFrame(app,width=400)
input_frame.pack(side=tk.RIGHT, fill='y')
row_count = 0
name_entries = []
weight_entries = []
benefit_entries = []

def add_row():
    row_frame = ctk.CTkFrame(input_frame)
    row_frame.pack(pady=5, side=tk.TOP)

    name_entry = ctk.CTkEntry(row_frame, height=23,width=110, placeholder_text="Item Name")
    name_entry.pack(side="left", padx=5)
    name_entries.append(name_entry)

    weight_entry = ctk.CTkEntry(row_frame, height=23,width=110, placeholder_text="Weight")
    weight_entry.pack(side="left", padx=5)
    weight_entries.append(weight_entry)

    benefit_entry = ctk.CTkEntry(row_frame, height=23,width=110, placeholder_text="Benefit")
    benefit_entry.pack(side="left", padx=5)
    benefit_entries.append(benefit_entry)



knapsack_size_entry = ctk.CTkEntry(input_frame, height=23,width=110, placeholder_text="Max weight")
knapsack_size_entry.pack(side=tk.TOP, pady=10, padx=10)
add_row()
add_row_button = ctk.CTkButton(input_frame, width=100, text="Add Row", command=add_row)
add_row_button.pack(side=tk.BOTTOM, anchor="se", pady=10, padx=10)

left_frame = ctk.CTkFrame(app)
left_frame.pack(side="left", fill="both", expand=True)

image = Image.open("image.png")
image = image.resize((200, 200))
image_tk = ImageTk.PhotoImage(image)
image_label = ctk.CTkLabel(left_frame, image=image_tk,height=50)
image_label.pack(pady=10, padx=10, expand=True)

def submit_data():
    items = [entry.get() for entry in name_entries]
    try : 
        weights=[]
        benefits=[]
        for entry in weight_entries:
            if entry.get()!='':
                weights.append(int(entry.get()))
        for entry in benefit_entries:
            if entry.get()!='':
                benefits.append(int(entry.get()))
        knapsack_size = int(knapsack_size_entry.get())
    except:
        mbox.showerror("Error","Weights& benfit should be numerical only")
        clear_all()
    req = {"items":items,"size":knapsack_size,"weights":weights,"benfits":benefits}
    response=requests.post("http://127.0.0.1:5000/genetic",json=req)
    count =  response.json()["Count of items"]
    res_items= response.json()["Items"]
    total_benfit=response.json()["Total benfit"]
    mbox.showinfo("Resault",f"Count: {count}\nItems: {res_items}\nTotal benfit: {total_benfit}")

submit_button = ctk.CTkButton(left_frame, text="Submit", command=submit_data)
submit_button.pack(side=tk.BOTTOM, pady=10)

def clear_all():
    global knapsack_size_entry
    for widget in input_frame.winfo_children():
        widget.destroy()
    name_entries.clear()
    weight_entries.clear()
    benefit_entries.clear()
    knapsack_size_entry = ctk.CTkEntry(input_frame, height=23,width=110, placeholder_text="Max weight")
    knapsack_size_entry.pack(side=tk.TOP, pady=10, padx=10)
    add_row_button = ctk.CTkButton(input_frame, width=100, text="Add Row", command=add_row)
    add_row_button.pack(side=tk.BOTTOM, anchor="se", pady=10, padx=10)
    add_row()

clear_button = ctk.CTkButton(left_frame, text="Clear All", command=clear_all)
clear_button.pack(side=tk.BOTTOM, pady=10)
app.mainloop()