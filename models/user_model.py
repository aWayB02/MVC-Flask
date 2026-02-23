class UserModel:
    def __init__(self):
        # В реальном приложении здесь будет подключение к базе данных
        self.users = [
            {"id": 1, "name": "Иван Иванов", "email": "ivan@example.com"},
            {"id": 2, "name": "Мария Петрова", "email": "maria@example.com"},
        ]
        self.next_id = 3

    def get_all_users(self):
        """Получить всех пользователей"""
        return self.users

    def get_user_by_id(self, user_id):
        """Получить пользователя по ID"""
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def create_user(self, name, email):
        """Создать нового пользователя"""
        user = {"id": self.next_id, "name": name, "email": email}
        self.users.append(user)
        self.next_id += 1
        return user

    def update_user(self, user_id, name, email):
        """Обновить информацию о пользователе"""
        user = self.get_user_by_id(user_id)
        if user:
            user["name"] = name
            user["email"] = email
            return user
        return None

    def delete_user(self, user_id):
        """Удалить пользователя"""
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
