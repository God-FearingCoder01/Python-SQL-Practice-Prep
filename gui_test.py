import customtkinter

app = customtkinter.CTk()

app.geometry("400x180")
app.title("SQL PRacticeTool - Prototype")


def execute_sql(sql):
    return 0

# app.columnconfigure(0, 1)

txtSql = customtkinter.CTkTextbox(app)
query = txtSql.get("1.0", "end-1c") # start from line 1 character 0; got to the very end but ignore the invisible 'enter' key at the last character
txtSql.grid(row=0, column=0, padx=10, pady=10)
btnExecute = customtkinter.CTkButton(app, text="Run Query", command=execute_sql(query))
btnExecute.grid(row=1, column=0, padx= 10, pady=10,)
lblResult = customtkinter.CTkLabel(app, text="Result Area")
lblResult.grid(row=2, column=0, padx=10, pady=10)

app.mainloop()

