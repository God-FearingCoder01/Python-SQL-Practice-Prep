import customtkinter
import sqlite3

app = customtkinter.CTk()

app.geometry("400x400")
app.title("SQL PRacticeTool - Prototype")

def clear_textbox():
    sqlTextbox.delete("0.0", "end")
    resultTextbox.delete("0.0", "end")

def execute_sql():
    inputText = sqlTextbox.get("1.0", "end-1c")
    # print(f"Executing: {inputText}")
    try:
        db_conn = sqlite3.connect('school.db')
        db_curosr = db_conn.cursor()

        rows = db_curosr.execute(inputText)

        # [f"{i}.0", row for i in range(len(rows-1))]
        if rows:
            i = 1 
            for row in rows:
                resultTextbox.insert(f"{i}.0", row)
                i += 1
        else:
            resultTextbox.insert("1.0", "No data was found!")

        db_conn.close()
    except sqlite3.Error as e:
        resultTextbox.insert("1.0", e)
    except Exception as e:
        app.title = type(e).__name__
        resultTextbox.insert("1.0", e)

app.grid_columnconfigure(0, weight=1)

sqlTextbox = customtkinter.CTkTextbox(app)
sqlTextbox.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
btnExecute = customtkinter.CTkButton(app, text="Run Query", command=execute_sql)
btnExecute.grid(row=1, column=0, padx= 10, pady=10)
btnClear = customtkinter.CTkButton(app, text="CLEAR", command=clear_textbox)
btnClear.grid(row=1, column=1, padx=10, pady=10, sticky="e")
lblResult = customtkinter.CTkLabel(app, text="Result Area")
lblResult.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
resultTextbox = customtkinter.CTkTextbox(app, width=250)
resultTextbox.grid(row=3, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
# resultTextbox.configure(state="disabled")

app.mainloop()


