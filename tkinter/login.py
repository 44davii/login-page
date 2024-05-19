from customtkinter import*

maicou = CTk()
maicou.geometry("500x400")

title = CTkLabel(maicou, text="Login", font=("Arial", 20)).pack(pady=20)
user = CTkEntry(maicou, placeholder_text="User name...", width=300).pack(pady=20)
password = CTkEntry(maicou, placeholder_text="Password...", width=300, show="*").pack()
CTkCheckBox = CTkCheckBox(maicou, text="Lembrar de mim").place(x=100, y=180)
button = CTkButton(maicou, text="Login", width=300).pack(pady=70)

maicou.mainloop()
