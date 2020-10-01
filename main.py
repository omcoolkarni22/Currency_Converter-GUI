from tkinter import *
from forex_python.converter import CurrencyRates
from tkinter import messagebox


def run():
    from_ = variable_form.get()
    to_ = variable_to.get()
    try:
        amo = float(value_ent.get())
        c = CurrencyRates()
        # print(from_, to_, amo)
        convert = c.convert(from_, to_, amo)
        value_c.delete(0, END)
        value_c.insert(0, convert)
    except:
        messagebox.showinfo("Invalid Argument", 'Please Check the Amount')


def main():
    global variable_form, variable_to, value_ent, value_c
    root = Tk()
    root.geometry("500x300")
    root.title("Currency Converter")
    root.configure(bg="gray")

    label_from = Label(root, text="From", font=("Arial Bold", 15), height=1, width=10,
                       justify="left", fg="white", bg="gray")
    label_to = Label(root, text="To", font=("Arial Bold", 15), height=1, width=10,
                     justify="left", fg="white", bg="gray")
    value = Label(root, text="Amount", font=("Arial Bold", 15), height=1, width=10,
                  justify="left", fg="white", bg="gray")
    value_cl = Label(root, text="Converted", font=("Arial Bold", 15), height=1, width=10,
                  justify="left", fg="white", bg="gray")

    value_ent = Entry(root, font=("Arial Bold", 18))
    value_c = Entry(root,font=("Arial Bold", 18))

    button = Button(root, text="Convert", command=run, height=1, width=15,
                    font=("Arial Bold", 12), fg="white", bg="#383837")
    OPTIONS = [
        "USD",
        "GBP",
        "INR",
        "EUR",
        "CAD",
        "HDK",
        'SGD',
        "AUD",
        "NZD"
    ]

    variable_form = StringVar(root)
    variable_to = StringVar(root)

    variable_form.set(OPTIONS[0])
    variable_to.set(OPTIONS[1])

    w_form = OptionMenu(root, variable_form, *OPTIONS)
    w_to = OptionMenu(root, variable_to, *OPTIONS)

    label_from.grid(row=0, column=1, padx=5, pady=5)
    w_form.grid(row=0, column=2, padx=5, pady=5)
    label_to.grid(row=1, column=1, padx=5, pady=5)
    w_to.grid(row=1, column=2, padx=5, pady=5)
    value.grid(row=2, column=1, padx=5, pady=5)
    value_ent.grid(row=2, column=2, padx=5, pady=5)
    button.grid(row=3, column=2, padx=5, pady=5)
    value_cl.grid(row=4, column=1, padx=5, pady=5)
    value_c.grid(row=4, column=2, padx=5, pady=5)
    root.mainloop()


if __name__ == "__main__":
    main()
