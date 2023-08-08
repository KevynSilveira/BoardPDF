import os
from PyPDF2 import PdfMerger
import customtkinter as ctk
from tkinter import messagebox
import datetime
from tkinter import filedialog
import tkinter as tk
from natsort import natsorted

def select():
    diretorio = filedialog.askdirectory()
    entry_select.delete(0, tk.END)
    entry_select.insert(0, diretorio)
def get_current_date_formatted():
    current_date = datetime.datetime.now()
    return current_date.strftime("%d-%m-%Y")

def get_creation_time(file_path):# Obter o timestamp de criação do arquivo
    return os.path.getctime(file_path)

def merge_pdfs_in_folder(folder_path, output_file):
    merger = PdfMerger()
    pdf_files = natsorted([f for f in os.listdir(folder_path) if f.endswith(".pdf")])

    for filename in pdf_files:
        pdf_path = os.path.join(folder_path, filename)
        merger.append(pdf_path)

    with open(output_file, "wb") as output_pdf:
        merger.write(output_pdf)

    messagebox.showinfo("ATENÇÃO", "PDFs combinados com sucesso!")


def execute():
    directory = entry_select.get()

    if directory:
        folder_path = directory
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile=f"{get_current_date_formatted()}.pdf")
        if output_file:
            merge_pdfs_in_folder(folder_path, output_file)

frame = ctk.CTk()
frame.geometry("250x200")
frame.title("BoardPDF")
frame.resizable(False, False)

button_select = ctk.CTkButton(master=frame, text= "Diretório origem", width=150, height=30, command=select)
button_select.place(x=50, y=10)

entry_select = ctk.CTkEntry(master=frame, width=200, height=30)
entry_select.place(x=25, y=50)

button_execute = ctk.CTkButton(master=frame, text= "Executar", width=150, height=30, command=execute)
button_execute.place(x=50, y=160)

if __name__ == "__main__":
    frame.mainloop()

