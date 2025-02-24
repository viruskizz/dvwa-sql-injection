from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from .models import User
from . import DbConnect

# Low
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
# Meduim
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
# High
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";

def index(request):
    users_count = User.objects.count()
    error_message = ""
    rows = []
    form = UserForm()
    if request.method == "GET":
        form = UserForm(request.GET)
        if form.is_valid():
            id = form['id'].value()
            query  = f"SELECT first_name, last_name FROM {User.__table_name__} WHERE id = '{id}'"
            ### psycopg
            try:
                db_connect = DbConnect()
                db_connect.cur.execute(query)
                rows = db_connect.cur.fetchall()
                print(rows)
            except Exception as e:
                error_message = str(e)
    return render(request, "pgsql/display.html", {
        "form": form,
        "users_count": users_count,
        "rows": rows,
        "error_message": error_message
    })

def login(request):
    form = LoginForm()
    error_message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        query  = f"SELECT * FROM {User.__table_name__} WHERE username = '{username}' and password = '{password}' LIMIT 1"
        # users = User.objects.raw(query)
        try:
            db_connect = DbConnect()
            db_connect.cur.execute(query)
            row = db_connect.cur.fetchone()
            print(row)
            if row:
                return redirect('/pgsql')
            else:
                error_message = "user or password not correct"
        except Exception as e:
            error_message = str(e)
    return render(request, "pgsql/login.html", { 'form': form, "error_message": error_message })