import tkinter as tk
from tkinter import messagebox
import requests

def get_exchange_rate(from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    data = response.json()
    if 'conversion_rate' in data:
        return data['conversion_rate']
    else:
        messagebox.showerror("Hata", "Döviz bilgisi alınamadı. Lütfen para birimlerini kontrol edin.")
        return None

def convert_currency(amount, from_currency, to_currency, api_key):
    rate = get_exchange_rate(from_currency, to_currency, api_key)
    return amount * rate if rate else 0

def on_convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_entry.get().upper()
        to_currency = to_currency_entry.get().upper()
        result = convert_currency(amount, from_currency, to_currency, api_key)
        if result:
            result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            result_label.config(text="Dönüşüm yapılamadı.")
    except ValueError:
        messagebox.showwarning("Uyarı", "Lütfen geçerli bir miktar giriniz.")


root = tk.Tk()
root.title("Döviz Çevirici")


api_key = "***********************"


tk.Label(root, text="Dönüştürülecek miktar:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Dönüştürülecek para birimi:").grid(row=1, column=0)
from_currency_entry = tk.Entry(root)
from_currency_entry.grid(row=1, column=1)

tk.Label(root, text="Hedef para birimi:").grid(row=2, column=0)
to_currency_entry = tk.Entry(root)
to_currency_entry.grid(row=2, column=1)


result_label = tk.Label(root, text="Sonuç burada görünecek")
result_label.grid(row=4, column=0, columnspan=2)


convert_button = tk.Button(root, text="Çevir", command=on_convert)
convert_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
