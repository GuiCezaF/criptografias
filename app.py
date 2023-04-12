from tkinter import *

def encrypt(key, plaintext):
    rail = [['\n' for i in range(len(plaintext))]
                for j in range(key)]
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(plaintext)):

        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = plaintext[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))

def decrypt(key, ciphertext):
    rail = [['\n' for i in range(len(ciphertext))]
                for j in range(key)]
     
    dir_down = None
    row, col = 0, 0
     
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == '*') and
            (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
         
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

def encrypt_text():
    plaintext = entry.get()
    key = int(key_entry.get())
    ciphertext = encrypt(key, plaintext)
    result_label['text'] = "Texto Encriptado: " + ciphertext

def decrypt_text():
    ciphertext = entry.get()
    key = int(key_entry.get())
    plaintext = decrypt(key, ciphertext)
    result_label['text'] = "Texto Desencriptado: " + plaintext

root = Tk()
root.title("Cifra de Trilho")

label = Label(root, text="Digite o texto:")
label.pack()

entry = Entry(root)
entry.pack()

key_label = Label(root, text="Digite a chave de encriptação:")
key_label.pack()

key_entry = Entry(root)
key_entry.pack()

encrypt_button = Button(root, text="Encriptar", command=encrypt_text)
encrypt_button.pack(side=LEFT)

decrypt_button = Button(root, text="Desencriptar", command=decrypt_text)
decrypt_button.pack(side=RIGHT)

result_label = Label(root, text="")
result_label.pack()


root.mainloop()