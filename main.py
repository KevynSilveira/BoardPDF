import os
from PyPDF2 import PdfMerger
import customtkinter as ctk

def get_creation_time(file_path):
    # Obter o timestamp de criação do arquivo
    return os.path.getctime(file_path)


def merge_pdfs_in_folder(folder_path, output_file, order_by="date", reverse_order=False):
    merger = PdfMerger()
    pdf_files = [(get_creation_time(os.path.join(folder_path, f)), f) for f in os.listdir(folder_path) if f.endswith(".pdf")]

    if order_by == "date":
        pdf_files.sort(key=lambda x: x[0], reverse=reverse_order)
    elif order_by == "crescente":
        pdf_files.sort(key=lambda x: x[1], reverse=reverse_order)
    elif order_by == "decrescente":
        pdf_files.sort(key=lambda x: x[1], reverse=not reverse_order)

    for timestamp, filename in pdf_files:
        pdf_path = os.path.join(folder_path, filename)
        merger.append(pdf_path)

    with open(output_file, "wb") as output_pdf:
        merger.write(output_pdf)

    print("PDFs combinados com sucesso!")

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
    # Substitua "caminho/da/pasta" pelo caminho real da pasta que contém os arquivos PDF
    folder_path = "C:\\Users\\Kevyn\\Documents\\origem"
    # Substitua "caminho/do/arquivo_completo.pdf" pelo caminho do arquivo que será gerado
    output_file = "C:\\Users\\Kevyn\\Documents\\Destino\\arquivo_completo.pdf"
    frame.mainloop()
    #merge_pdfs_in_folder(folder_path, output_file)
