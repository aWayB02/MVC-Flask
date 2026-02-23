class View:
    def show_items(self, items):
        print("Список элементов:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

    def show_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)
