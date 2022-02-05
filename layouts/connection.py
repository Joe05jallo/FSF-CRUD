import tkinter as tk

def Connection():
    # Creation de la fenetre
    root = tk.Tk()
    root.title("FSF Administration")
    root.configure(background= 'light green')
    root.geometry("800x600")
    root.resizable(False, False)
    
    header = tk.Frame(root)
    header.pack()
    
    title = tk.Label(header, text="FSF Connection", font=("Arial", 21), bg='light green', fg="black", pady=30).pack()
    
    formulaire = tk.LabelFrame(root, text=" Formulaire de connection ", font=("Arial", 12), bg="light green", fg="black")
    formulaire.pack()
    
    usernameFrame = tk.Frame(formulaire, padx=20, bg='light green', pady=20)
    usernameFrame.pack()
    
    usernameLabel = tk.Label(usernameFrame, text="Nom d'utilisateur", font=("lato", 12), bg='light green', fg='black')
    usernameLabel.grid(row=1, column=0, padx=30)
    
    
    usernameEntryText = tk.StringVar()
    usernameEntry = tk.Entry(usernameFrame, textvariable=usernameEntryText)
    usernameEntryText.set("")
    usernameEntry.grid(row=1, column=1, padx=30)
    
    
    passwordFrame = tk.Frame(formulaire, padx=20, bg='light green', pady=20)
    passwordFrame.pack()
    
    passwordLabel = tk.Label(passwordFrame, text="Mot de passe", font=("lato", 12), bg='light green', fg='black')
    passwordLabel.grid(row=1, column=0, padx=30)
    
    
    passwordEntryText = tk.StringVar()
    passwordEntry = tk.Entry(passwordFrame, textvariable=passwordEntryText)
    passwordEntryText.set("")
    passwordEntry.grid(row=1, column=1, padx=30)
    
    
       
    
    
    
    
    
    
    root.mainloop()