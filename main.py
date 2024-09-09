import tkinter
from tkinter import messagebox

from cryptography.fernet import Fernet
import base64

#main window
root = tkinter.Tk()
root.title("Secret Notes")
root.config(padx=50, pady=50)
#top-secret logo
image = tkinter.PhotoImage(file="topsecret.png")
image_label = tkinter.Label(root, image=image)
image_label.pack()

#note's title
title_label = tkinter.Label(root, text="Enter your title.")
title_label.pack(padx=5, pady=5)
title_entry = tkinter.Entry(root)
title_entry.pack(padx=5, pady=5)

#secret note content
title_label2 = tkinter.Label(root, text="Enter your secret note.")
title_label2.pack(padx=5, pady=5)
note_text = tkinter.Text(root)
note_text.pack(padx=5, pady=5)

#master key box
pass_label = tkinter.Label(root, text="Enter master key.")
pass_label.pack(padx=5, pady=5)
pass_entry = tkinter.Entry(root)
pass_entry.pack(padx=5, pady=5)

#Saving, encryption, decryption buttons and their functions
def save():


  def encrypt():
    entered_pw = pass_entry.get()
    key = base64.b64encode(f"{entered_pw:<32}".encode("utf-8"))
    encryptor = Fernet(key=key)
    encrypted = encryptor.encrypt(
      note_text.get(1.0, tkinter.END).encode("utf-8")
    ).decode("utf-8")

    return encrypted


  with open(file="secretNotes.txt", mode="a",encoding="UTF-8") as file:
    file.write(f"\n{title_entry.get()}")
    encrypted_message= encrypt()
    file.write(f"\n{encrypted_message}")
  title_entry.delete("0", tkinter.END)
  note_text.delete("1.0", tkinter.END)
  pass_entry.delete("0", tkinter.END)
  return

def decrypt():
  try:
    entered_pw = pass_entry.get()
    key = base64.b64encode(f"{entered_pw:<32}".encode("utf-8"))
    encryptor = Fernet(key=key)
    decrypted = encryptor.decrypt(note_text.get("1.0",tkinter.END)).decode("utf-8")
    note_text.delete("1.0", tkinter.END)
    note_text.insert(tkinter.END, f"{decrypted}")
  except:
    messagebox.showwarning(title="Invalid Key", message="Please enter the correct master key.", parent=root)
  return

#buttons
encrypt_button = tkinter.Button(root, text="Save&Encrypt", command=save)
encrypt_button.pack(padx=5, pady=5)

decrypt_button = tkinter.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(padx=5, pady=5)

root.mainloop()