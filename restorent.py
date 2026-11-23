import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")

        self.menu_items = {
            "Pizza": 10.99,
            "Burger": 4.99,
            "Pasta": 7.99,
            "drinks": 0.99
        }
        self.exchange_rate = 89 # Default exchange rate
        self.setup_background(root)

        frame = ttk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="Restaurant order Management", font=("Helvetica", 16, "bold")).grid(row=0, columnspan=3, pady=10, padx=10)

        self.manu_label = {}
        self.manu_quantity = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text=f"{item} - ${price:.2f}", font=("Helvetica", 12))
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            self.manu_label[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)

            self.manu_quantity[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Select Currency:", font=("Helvetica", 12)).grid(row=len(self.menu_items)+1, column=0, sticky=tk.W, padx=10, pady=5)
        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, values=["USD", "INR"], state="readonly")
        currency_dropdown.grid(row=len(self.menu_items)+1, column=1, padx=10, pady=5)
        currency_dropdown.current(0)  
        self.currency_var.trace("w", self.update_prices)

        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items)+2, columnspan=3, padx=10, pady=10)

    def setup_background(self,root):
        bg_image = Image.open("background.jpg")
        bg_image = bg_image.resize((800, 600), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = ttk.Label(root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def update_prices(self, *args):
        currencey = self.currency_var.get()
        symbol = "$" if currencey == "USD" else "₹"
        rate = 1 if currencey == "USD" else self.exchange_rate

        for  item, price in self.menu_items.items():
            converted_price = price * rate
            self.manu_label[item].config(text=f"{item} - {symbol}{converted_price:.2f}")

    def place_order(self): 
        total_cost = 0
        order_summery = "Order Summary:\n\n"
        currencey = self.currency_var.get()
        symbol = "$" if currencey == "USD" else "₹"
        rate = 1 if currencey == "USD" else self.exchange_rate

        for item, entry in self.manu_quantity.items():
            quantity = entry.get()
            if quantity:
                total_cost += int(quantity) * self.menu_items[item]
                order_summery += f"{item}: {quantity} x ${self.menu_items[item]:.2f} = ${int(quantity) * self.menu_items[item]:.2f}\n"

        order_summery += f"\nTotal Cost: {symbol}{total_cost * rate:.2f}"
        messagebox.showinfo("Order Placed", order_summery)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.geometry("800x600")
    root.mainloop()