import tkinter as tk
from tkinter import messagebox, ttk

class Menu:
    def __init__(self):
        self.categories = {}

    def add_dish(self, category, dish):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(dish)

    def remove_dish(self, category, dish_index):
        if category in self.categories and dish_index < len(self.categories[category]):
            self.categories[category].pop(dish_index)
            if not self.categories[category]:
                del self.categories[category]

    def get_dishes(self, category):
        return self.categories.get(category, [])
    
class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, dish, quantity=1):
        self.items.append({"dish": dish, "quantity": quantity})

    def remove_item(self, index):
        if index < len(self.items):
            self.items.pop(index)

    def print_order(self):
        total_cost = 0
        print("Заказ:")
        for item in self.items:
            dish = item["dish"]
            quantity = item["quantity"]
            total_cost += dish.price * quantity
            print(f"- {dish.name} x{quantity}: {dish.price * quantity} руб.")
        print(f"Итого: {total_cost} руб.")

# Создание меню
menu = Menu()
menu.add_dish("Первое", Dish("Борщ", 250))
menu.add_dish("Первое", Dish("Суп фрикадельковый", 250))
menu.add_dish("Первое", Dish("Харчо", 350))
menu.add_dish("Первое", Dish("Солянка", 250))
menu.add_dish("Первое", Dish("Суп гороховый", 250))
menu.add_dish("Первое", Dish("Окрошка", 250))
menu.add_dish("Второе", Dish("Паста", 250))
menu.add_dish("Второе", Dish("Овощное рагу", 300))
menu.add_dish("Второе", Dish("Запеканка", 250))
menu.add_dish("Второе", Dish("Ребрышки", 350))
menu.add_dish("Второе", Dish("Плов", 250))
menu.add_dish("Второе", Dish("Печень в сметане", 200))
menu.add_dish("Салаты", Dish("Оливье", 150))
menu.add_dish("Салаты", Dish("Цезарь", 200))
menu.add_dish("Салаты", Dish("Крабовый", 150))
menu.add_dish("Салаты", Dish("Овощной салат", 150))
menu.add_dish("Напитки", Dish("Вода", 50))
menu.add_dish("Напитки", Dish("Кола", 80))
menu.add_dish("Напитки", Dish("Компот", 50))
menu.add_dish("Напитки", Dish("Кофе", 50))
menu.add_dish("Напитки", Dish("Молочный коктейль", 50))
menu.add_dish("Десерты", Dish("Торт Наполеон", 250))
menu.add_dish("Десерты", Dish("Торт Пьяная вишня", 300))
menu.add_dish("Десерты", Dish("Пирожные", 150))
menu.add_dish("Десерты", Dish("Чизкейк", 250))
menu.add_dish("Десерты", Dish("Тирамису", 250))
menu.add_dish("Десерты", Dish("Творожная запеканка", 250))

# Функция редактирования меню
def edit_menu():
    def save_new_dish():
        category = new_category_entry.get()
        name = new_name_entry.get()
        price = int(new_price_entry.get())
        if category and name and price:
            menu.add_dish(category, Dish(name, price))
            update_category_combobox()
            update_menu_listbox()
        else:
            messagebox.showwarning("Ошибка", "Заполните все поля")

    def delete_dish():
        selected_category = category_combobox.get()
        selected_dish_index = menu_listbox.curselection()
        if selected_dish_index and selected_category in menu.categories:
            menu.remove_dish(selected_category, selected_dish_index[0])
            update_category_combobox()
            update_menu_listbox()

    def update_dish():
        selected_category = category_combobox.get()
        selected_dish_index = menu_listbox.curselection()
        if selected_dish_index and selected_category in menu.categories:
            new_name = new_name_entry.get()
            new_price = int(new_price_entry.get())
            if new_name and new_price:
                menu.categories[selected_category][selected_dish_index[0]] = Dish(new_name, new_price)
                update_category_combobox()
                update_menu_listbox()
            else:
                messagebox.showwarning("Ошибка", "Заполните все поля")

    def update_menu_listbox():
        selected_category = category_combobox.get()
        menu_listbox.delete(0, tk.END)
        if selected_category in menu.categories:
            for dish in menu.categories[selected_category]:
                menu_listbox.insert(tk.END, f"{dish.name} ({dish.price} руб.)")

        
    edit_menu_window = tk.Toplevel(root)
    edit_menu_window.title("Редактировать меню")
    edit_menu_window.geometry("500x550")

    tk.Label(edit_menu_window, text="Категория").pack()
    category_combobox = ttk.Combobox(edit_menu_window, values=list(menu.categories.keys()))
    category_combobox.bind("<<ComboboxSelected>>", lambda event: update_menu_listbox())
    category_combobox.pack()

    # Создание контейнера для списка блюд с ограниченными размерами
    menu_listbox_frame = tk.Frame(edit_menu_window, width=400, height=300)
    menu_listbox_frame.pack_propagate(False)  # Отключить автоматическое изменение размера
    menu_listbox_frame.pack()

    menu_listbox = tk.Listbox(menu_listbox_frame)
    menu_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(menu_listbox_frame, orient="vertical")
    scrollbar.config(command=menu_listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    menu_listbox.config(yscrollcommand=scrollbar.set)

    tk.Label(edit_menu_window, text="Категория").pack()
    new_category_entry = tk.Entry(edit_menu_window, width=40)
    new_category_entry.pack()

    tk.Label(edit_menu_window, text="Наименование").pack()
    new_name_entry = tk.Entry(edit_menu_window, width=40)
    new_name_entry.pack()

    tk.Label(edit_menu_window, text="Цена").pack()
    new_price_entry = tk.Entry(edit_menu_window, width=40)
    new_price_entry.pack()

    # Создание контейнера для кнопок
    button_frame = tk.Frame(edit_menu_window)
    button_frame.pack(pady=(10, 0))  # Расположить контейнер в окне

    # Создание кнопок и их размещение в строку
    save_button = tk.Button(button_frame, text="Добавить", command=save_new_dish)
    save_button.grid(row=5, column=0, padx=15)

    update_button = tk.Button(button_frame, text="Обновить", command=update_dish)
    update_button.grid(row=5, column=1, padx=15)

    delete_button = tk.Button(button_frame, text="Удалить", command=delete_dish)
    delete_button.grid(row=5, column=2, padx=15)

# Обновление списка категорий в комбобоксе
def update_category_combobox():
    category_combobox['values'] = list(menu.categories.keys())

# Функция для добавления блюда в заказ
def add_to_order():
    selected_category = category_combobox.get()
    selected_dish_index = dish_listbox.curselection()
    if selected_dish_index and selected_category in menu.categories:
        selected_dish = menu.categories[selected_category][selected_dish_index[0]]
        quantity = int(quantity_spinbox.get())
        order.add_item(selected_dish, quantity)
        update_order_list()

# Функция для удаления блюда из заказа
def remove_from_order():
    selected_order_index = order_treeview.selection()
    if selected_order_index:
        order.remove_item(int(selected_order_index[0]))
        update_order_list()

# Функция для обновления списка заказа
def update_order_list():
    for row in order_treeview.get_children():
        order_treeview.delete(row)
    total_cost = 0
    for index, item in enumerate(order.items):
        dish = item["dish"]
        quantity = item["quantity"]
        cost = dish.price
        cost = dish.price * quantity
        total_cost += cost
        order_treeview.insert("", "end", iid=index, values=(dish.name, quantity, dish.price, cost))
    total_label.config(text=f"Итого: {total_cost} руб.")

# Обновление списка блюд в зависимости от выбранной категории
def update_dish_listbox(event):
    selected_category = category_combobox.get()
    dish_listbox.delete(0, tk.END)
    if selected_category in menu.categories:
        for dish in menu.categories[selected_category]:
            dish_listbox.insert(tk.END, f"{dish.name} ({dish.price} руб.)")

# Создание главного окна
root = tk.Tk()
root.title("Меню ресторана")

# Создание виджетов меню
menu_frame = tk.Frame(root, width=300, height=400)
menu_frame.pack_propagate(False)
menu_frame.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(menu_frame, text="Категория").pack()
category_combobox = ttk.Combobox(menu_frame, values=list(menu.categories.keys()))
category_combobox.bind("<<ComboboxSelected>>", update_dish_listbox)
category_combobox.pack()

tk.Label(menu_frame, text="Меню").pack()

dish_listbox = tk.Listbox(menu_frame)
dish_listbox.pack(fill=tk.BOTH, expand=True)

tk.Label(menu_frame, text="Количество").pack()
quantity_spinbox = tk.Spinbox(menu_frame, from_=1, to=10)
quantity_spinbox.pack()

button_frame = tk.Frame(menu_frame)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Добавить в заказ", command=add_to_order)
add_button.grid(row=0, column=1, padx=10)

edit_menu_button = tk.Button(button_frame, text="Редактировать меню", command=edit_menu)
edit_menu_button.grid(row=0, column=0, padx=10)

# Создание виджетов заказа
order_frame = tk.Frame(root, width=900, height=400)
order_frame.pack_propagate(False)
order_frame.pack(side=tk.RIGHT, padx=10, pady=10)

tk.Label(order_frame, text="Заказ").pack()

columns = ("name", "quantity", "price_per_item", "total_price")
order_treeview = ttk.Treeview(order_frame, columns=columns, show="headings")
order_treeview.heading("name", text="Наименование")
order_treeview.heading("quantity", text="Количество")
order_treeview.heading("price_per_item", text="Цена за единицу")
order_treeview.heading("total_price", text="Итоговая цена")
order_treeview.pack(fill=tk.BOTH, expand=True)

# Центрирование текста в столбцах
order_treeview.column("quantity", anchor="center")
order_treeview.column("price_per_item", anchor="center")
order_treeview.column("total_price", anchor="center")

total_label = tk.Label(order_frame, text="Итого: 0 руб.")
total_label.pack()

remove_button = tk.Button(order_frame, text="Удалить из заказа", command=remove_from_order)
remove_button.pack()

# Создание заказа
order = Order()

# Запуск главного цикла программы
root.mainloop()
