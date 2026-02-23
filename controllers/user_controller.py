from flask import render_template, redirect, url_for


class UserController:
    def __init__(self, user_model):
        self.user_model = user_model

    def index(self):
        """Главная страница"""
        return render_template("index.html")

    def list_users(self):
        """Отобразить список всех пользователей"""
        users = self.user_model.get_all_users()
        return render_template("users/index.html", users=users)

    def new_user_form(self):
        """Отобразить форму создания нового пользователя"""
        return render_template("users/new.html")

    def create_user(self, request):
        """Создать нового пользователя"""
        name = request.form["name"]
        email = request.form["email"]

        if name and email:
            self.user_model.create_user(name, email)

        return redirect(url_for("users"))

    def show_user(self, user_id):
        """Отобразить информацию о конкретном пользователе"""
        user = self.user_model.get_user_by_id(user_id)
        if user:
            return render_template("users/show.html", user=user)
        else:
            return "Пользователь не найден", 404

    def edit_user_form(self, user_id):
        """Отобразить форму редактирования пользователя"""
        user = self.user_model.get_user_by_id(user_id)
        if user:
            return render_template("users/edit.html", user=user)
        else:
            return "Пользователь не найден", 404

    def update_user(self, request, user_id):
        """Обновить информацию о пользователе"""
        name = request.form["name"]
        email = request.form["email"]

        if name and email:
            self.user_model.update_user(user_id, name, email)

        return redirect(url_for("users"))

    def delete_user(self, user_id):
        """Удалить пользователя"""
        self.user_model.delete_user(user_id)
        return redirect(url_for("users"))
