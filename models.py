from __init__ import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(256))
    password = db.Column(db.String(256))
    dota2 = db.Column(db.String(256))
    csgo = db.Column(db.String(256))
    rocket = db.Column(db.String(256))
    vk = db.Column(db.String(256))

    def __init__(self,login,vk, password, dota2, csgo, rocket):
        self.login = login
        self.password = password
        self.dota2 = dota2
        self.csgo = csgo
        self.rocket = rocket
        self.vk = vk

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def update_by_login(login, key, value):
        db.session.query(User).filter(User.login == login).update({key: value}, synchronize_session='evaluate')
        db.session.commit()

    # Сортировка юзеров по рангу в конкретной игре
    @staticmethod
    def get_sorted_dota():
        dota2 = User.get_all()
        sorted_users = sorted(dota2, key=lambda x: x.dota2, reverse=True)
        return sorted_users

    @staticmethod
    def get_sorted_cs():
        cs = User.get_all()
        sorted_users = sorted(cs, key=lambda x: x.csgo, reverse=True)
        return sorted_users

    @staticmethod
    def get_sorted_rocket():
        rocket = User.get_all()
        sorted_users = sorted(rocket, key=lambda x: x.rocket, reverse=True)
        return sorted_users


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    img = db.Column(db.String(256))
    count = db.Column(db.String(256))
    des = db.Column(db.String(256))


    def __init__(self,name, img, count, des):
        self.name = name
        self.img = img
        self.count = count
        self.des = des

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    @staticmethod
    def like(name, key, value):
        db.session.query(Game).filter(Game.name == name).update({key: value}, synchronize_session='evaluate')
        db.session.commit()

    @staticmethod
    def get_all():
        return Game.query.all()