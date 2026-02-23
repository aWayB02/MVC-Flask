from flask import Flask, render_template, request, redirect, url_for
from models.user_model import UserModel
from controllers.user_controller import UserController

app = Flask(__name__)

# Инициализация модели и контроллера
user_model = UserModel()
user_controller = UserController(user_model)


@app.route("/")
def index():
    return user_controller.index()


@app.route("/users")
def users():
    return user_controller.list_users()


@app.route("/users/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        return user_controller.create_user(request)
    else:
        return user_controller.new_user_form()


@app.route("/users/<int:user_id>")
def show_user(user_id):
    return user_controller.show_user(user_id)


@app.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        return user_controller.update_user(request, user_id)
    else:
        return user_controller.edit_user_form(user_id)


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    return user_controller.delete_user(user_id)


if __name__ == "__main__":
    app.run(debug=True)
