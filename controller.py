class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item(self, item):
        self.model.add_item(item)
        self.view.show_message(f"Элемент '{item}' добавлен")

    def show_items(self):
        items = self.model.get_items()
        if items:
            self.view.show_items(items)
        else:
            self.view.show_message("Список пуст")

    def remove_item(self, item):
        self.model.remove_item(item)
        self.view.show_message(f"Элемент '{item}' удален")

    def run(self):
        while True:
            self.view.show_message("\n1. Добавить элемент")
            self.view.show_message("2. Показать элементы")
            self.view.show_message("3. Удалить элемент")
            self.view.show_message("4. Выход")

            choice = self.view.get_input("Выберите действие: ")

            if choice == "1":
                item = self.view.get_input("Введите элемент: ")
                self.add_item(item)
            elif choice == "2":
                self.show_items()
            elif choice == "3":
                item = self.view.get_input("Введите элемент для удаления: ")
                self.remove_item(item)
            elif choice == "4":
                break
            else:
                self.view.show_message("Неверный выбор")
