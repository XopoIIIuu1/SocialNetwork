from _sha256 import sha256
from __init__ import db,app
from flask import Flask, render_template, session,redirect
from forms import RegForm, LoginForm, ChangeDota, ChangeCS, ChangeRocket, CreateGame, Like
from models import User, Game


@app.route('/')
def start():
    return render_template("main.html")

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        same_login = User.query.filter(User.login == form.login.data).count()
        error = False
        if same_login:
            return render_template('reg.html', form=form, error_text='Пользователь с таким логином уже существует.',
                                   error=True)

        secret_pass = sha256(form.password.data.encode()).hexdigest()

        user = User( form.login.data, form.vk.data ,secret_pass , 0 , 0, 0,)
        user.save()
        session['logged_in'] = True
        session['username'] = form.login.data
        user_info = db.session.query(User).filter(User.login == session['username']).first()
        session['id'] = user_info.id
        return redirect('/')
    return render_template('reg.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = False
    if form.validate_on_submit():
        password = sha256(form.password.data.encode()).hexdigest()
        user_count = User.query.filter(User.login == form.login.data).filter(User.password == password)
        if user_count.count():
            session['username'] = form.login.data
            session['id'] = user_count[0].id
            session['logged_in'] = True
            return redirect('/')
        return render_template('login.html', form=form, error_text='Неправильный логин или пароль.', error=True)
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return redirect('/')

@app.route('/account', methods=['GET', 'POST'])
def account():
    if (session['logged_in']):
        user = User.query.filter(User.login == session['username']).first()
    else:
        user = {"login": "Гость"}
    return render_template('account.html', user=user)

@app.route('/users', methods=['GET', 'POST'])
def us():
    user = User.query.filter(User.login == session['username']).first()
    return render_template('users.html', user=user)

@app.route('/change/dota2', methods=['GET', 'POST'])
def change_dota():
    form = ChangeDota()
    error = False
    success = False
    user = User.query.filter(User.login == session['username']).first()
    if form.validate_on_submit():
        login = session['username']
        password_form = sha256(form.password.data.encode()).hexdigest()
        user_count = User.query.filter(User.login == session['username']).filter(User.password == password_form)
        if user_count.count():
            User.update_by_login(login, 'dota2', form.newrank.data)
            return render_template('dota2.html', form=form, success_text='Ваш ранг успешно изменен!',
                                   success=True, user=user)
        # Проверка на уникальность
        return render_template('dota2.html', form=form, error_text='Вы ввели неправильный пароль.', error=True,
                               user=user)
    return render_template('dota2.html', form=form, user=user)


@app.route('/change/cs', methods=['GET', 'POST'])
def change_cs():
    form = ChangeCS()
    error = False
    success = False
    user = User.query.filter(User.login == session['username']).first()
    if form.validate_on_submit():
        login = session['username']
        password_form = sha256(form.password.data.encode()).hexdigest()
        user_count = User.query.filter(User.login == session['username']).filter(User.password == password_form)
        if user_count.count():
            User.update_by_login(login, 'csgo', form.newrank.data)
            return render_template('cs.html', form=form, success_text='Ваш ранг успешно изменен!',
                                   success=True, user=user)
        # Проверка на уникальность
        return render_template('cs.html', form=form, error_text='Вы ввели неправильный пароль.', error=True,
                               user=user)
    return render_template('cs.html', form=form, user=user)

@app.route('/change/rocket', methods=['GET', 'POST'])
def change_r():
    form = ChangeRocket()
    error = False
    success = False
    user = User.query.filter(User.login == session['username']).first()
    if form.validate_on_submit():
        login = session['username']
        password_form = sha256(form.password.data.encode()).hexdigest()
        user_count = User.query.filter(User.login == session['username']).filter(User.password == password_form)
        if user_count.count():
            User.update_by_login(login, 'rocket', form.newrank.data)
            return render_template('rocket.html', form=form, success_text='Ваш ранг успешно изменен!',
                                   success=True, user=user)
        # Проверка на уникальность
        return render_template('rocket.html', form=form, error_text='Вы ввели неправильный пароль.', error=True,
                               user=user)
    return render_template('rocket.html', form=form, user=user)

@app.route('/users/dota2', methods=['GET'])
def all_dota2():
    users = User.get_sorted_dota()
    user = User.query.filter(User.login == session['username']).first()
    return render_template('users_dota2.html', users = users,user = user)

@app.route('/users/cs', methods=['GET'])
def all_cs():
    users = User.get_sorted_cs()
    user = User.query.filter(User.login == session['username']).first()
    return render_template('users_cs.html', users = users,user = user)

@app.route('/users/rocket', methods=['GET'])
def all_rocket():
    users = User.get_sorted_rocket()
    user = User.query.filter(User.login == session['username']).first()
    return render_template('users_rocket.html', users = users, user = user)

@app.route('/user/<int:id>', methods=['GET'])
def user(id):
    user = User.query.filter(User.id == id).first()
    if user.login == session['username']:
        return redirect('/account')
    return render_template('user.html', user=user)

@app.route('/allgames/<name>', methods=['GET', 'POST'])
def game(name):
    form = Like()
    user = User.query.filter(User.login == session['username']).first()
    game = Game.query.filter(Game.name == name).first()
    if form.validate_on_submit():
        Game.like(name,'count', str(int(game.count)+1))
        return redirect('/allgames')
    return render_template('game.html', user=user,game = game, form = form)

@app.route('/allgames', methods=['GET'])
def all_games():
    games = Game.get_all()
    user = User.query.filter(User.login == session['username']).first()
    return render_template('allGames.html', games = games, user = user)

@app.route('/allgames/add', methods = ['GET','POST'])
def add_game():
    form = CreateGame()
    user = User.query.filter(User.login == session['username']).first()
    error = False
    success = False
    if form.validate_on_submit():
        login = session['username']
        password = sha256(form.password.data.encode()).hexdigest()
        user_count = User.query.filter(User.login == login).filter(User.password == password)
        game1 = Game(form.name.data,form.img.data, 0, form.des.data)
        game1.save()
        return redirect('/allgames')
    return render_template('addGame.html', user = user,form = form)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404






