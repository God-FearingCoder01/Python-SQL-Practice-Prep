import customtkinter

app = customtkinter.CTk()

app.geometry("400x180")
app.title("SQL PRacticeTool - Prototype")

def execute_sql():
    inputText = sqlTextbox.get("1.0", "end-1c")
    print(f"Executing: {inputText}")

app.grid_columnconfigure(0, weight=1)

sqlTextbox = customtkinter.CTkTextbox(app)
sqlTextbox.grid(row=0, column=0, padx=10, pady=10)
btnExecute = customtkinter.CTkButton(app, text="Run Query", command=execute_sql)
btnExecute.grid(row=1, column=0, padx= 10, pady=10,)
lblResult = customtkinter.CTkLabel(app, text="Result Area")
lblResult.grid(row=2, column=0, padx=10, pady=10)

app.mainloop()


