import os
from PyPDF2 import PdfMerger
import customtkinter as ctk
from tkinter import messagebox
import datetime

def get_current_date_formatted():
    current_date = datetime.datetime.now()
    return current_date.strftime("%d-%m-%Y")

def get_creation_time(file_path):# Obter o timestamp de criação do arquivo
    return os.path.getctime(file_path)

def merge_pdfs_in_folder(folder_path, output_file, order_by="date", reverse_order=False):
    merger = PdfMerger()
    pdf_files = [(get_creation_time(os.path.join(folder_path, f)), f) for f in os.listdir(folder_path) if f.endswith(".pdf")]

    if order_by == "Data":
        pdf_files.sort(key=lambda x: x[0], reverse=reverse_order)
    elif order_by == "Crescente":
        pdf_files.sort(key=lambda x: x[1], reverse=reverse_order)
    elif order_by == "Decrescente":
        pdf_files.sort(key=lambda x: x[1], reverse=not reverse_order)

    for timestamp, filename in pdf_files:
        pdf_path = os.path.join(folder_path, filename)
        merger.append(pdf_path)

    with open(output_file, "wb") as output_pdf:
        merger.write(output_pdf)

    messagebox.showinfo("ATENÇÃO","PDFs combinados com sucesso!")

def execute():
    diretory = entry_select.get()
    order = combobox_order.get()
    name_file = get_current_date_formatted()
    reverse_option = False

    if order == "Crescente":
        reverse_option = True
    if order == "Descrente":
        reverse_option = False

    if (diretory != "" and diretory != None and order != "" and order != None):
        folder_path = "C:\\Users\\Kevyn\\Documents\\origem"
        output_file = f"C:\\Users\\Kevyn\\Documents\\Destino\\{name_file}.pdf"
        merge_pdfs_in_folder(folder_path, output_file, order, reverse_option)


frame = ctk.CTk()
frame.geometry("250x200")
frame.title("BoardPDF")
frame.resizable(False, False)

button_select = ctk.CTkButton(master=frame, text= "Diretório origem", width=150, height=30)
button_select.place(x=50, y=10)

entry_select = ctk.CTkEntry(master=frame, width=200, height=30)
entry_select.place(x=25, y=50)

option_order = ["Data", "Crescente", "Decrescente"]  # Opções
combobox_order = ctk.CTkComboBox(master=frame, values=option_order, width=150, height=30, state="readonly")
combobox_order.set("Ordenação")  # Indica que precisa escolher um ordenação
combobox_order.configure(justify="center")  # Centraliza o texto na combobox
combobox_order.place(x=50, y=90)

button_execute = ctk.CTkButton(master=frame, text= "Executar", width=150, height=30)
button_execute.place(x=50, y=160)

if __name__ == "__main__":
    frame.mainloop()

