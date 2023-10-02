from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
import re

pattern = r'^[A-Za-z0-9_-]*$'


def latinica_only(form, field):
    if not re.match(pattern, str(field.data)):
        raise ValidationError('Символы могут включать в себя латинские буквы, номера, или - _')


class RegForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(message='Это поле обязательно.'), latinica_only])
    vk = StringField('Ссылка на личную страницу', validators=[DataRequired(message='Это поле обязательно.'), latinica_only])
    password = PasswordField('Придумайте пароль', validators=[DataRequired(message='Это обязательное поле.'),
                                                                Length(8, message='Количество символов должно превышать 8.')])
    confirmpass = PasswordField('Пароль для подтверждения',
                                validators=[DataRequired(message='Это обязательное поле.'),
                                            Length(8, message='Количество символов должно превышать 8.'),
                                            EqualTo('password', message='Пароли должны совпадать.')])

class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(message='Это поле обязательно.')])
    password = PasswordField('Пароль', validators=[DataRequired(message='Это поле обязательно.')])

class ChangeDota(FlaskForm):
    newrank = SelectField('Новый ранг',choices = [("Herald","Herald (0 - 650 mmr)"),("Guardian","Guardian (650 - 1400 mmr)"),
                                                  ("Crusader","Crusader (1400 - 2200 mmr)"),("Archon","Archon (2200 - 3000 mmr)"),
                                                  ("Legand","Legend (3000 - 3700 mmr)"), ("Ancient","Ancient(3700 - 4500)"),
                                                  ("Divine","Divine (4500 - 5500 mmr)"), ("Divine Elite","Divine Elite (4500+ mmr)"),
                                                  ("Divine TOP 100"," Divine TOP 100"),("Divine TOP 10","Divine TOP 10")],validators=[DataRequired(message='Это поле обязательно.')])

    password = PasswordField('Пароль', validators=[DataRequired(message='Это обязательное поле.'),
                                                              Length(8,
                                                                     message='Количество символов должно превышать 8.')])


class ChangeCS(FlaskForm):
    newrank = SelectField('Новый ранг',choices = [("Silver 1","Silver 1"),
                                        	  ("Silver 2","Silver 2"),("Silver 3","Silver 3") , ("Silver 4","Silver 4"), ("Silver 5","Silver 5"), ("Silver 6", "Silver 6"),
                                                  ("Gold nova 1","Gold nova 1"), ("Gold nova 2","Gold nova 2"), ("Gold nova 3","Gold nova 3"),("Gold nova Master","Gold nova Master"),
                                                  ("Master Guardian 1","Master Guardian 1"),("Master Guardian 2","Master Guardian 2"),("Master Guardian Elite","Master Guardian Elite"),
                                                  ("Distiguished Master Guardian","Distiguished Master Guardian"),("Legendary Eagle","Legendary Eagle"), ("Legendary Eagle Mater","Legendary Eagle Master"),
                                                  ("Supreme Master First Class","Supreme Master First Class"), ("The Global Elite","The Global Elite")],validators=[DataRequired(message='Это поле обязательно.')])

    password = PasswordField('Пароль', validators=[DataRequired(message='Это обязательное поле.'),
                                                              Length(8,
                                                                     message='Количество символов должно превышать 8.')])

class ChangeRocket(FlaskForm):
    newrank = SelectField('Новый ранг',choices = [("Bronze 1","Bronze 1"),("Bronze 2", "Bronze 2"), ("Bronze 3","Bronze 3"), ("Silver 1","Silver 1"),
                                                  ("Silver 2","Silver 2"),("Silver 3","Silver 3") ,
                                                  ("Gold 1","Gold 1"), ("Gold 2","Gold 2"), ("Gold 3","Gold 3"),
                                                  ("Platinum 1","Platinum 1"),("Platinum 2","Platinum 2"),("Platinum 3","Platinum 3"),
                                                  ("Diamond 1","Diamond 1"),("Diamond 2","Diamond 2"), ("Diamond 3","Diamond 3"),
                                                  ("Champion 1","Champion 1"), ("Champion 2","Champion 2"), ("Champion 3","Champion 3"),
                                                  ("GRAND CHAMPION","GRAND CHAMPION")], validators=[DataRequired(message='Это поле обязательно.')])

    password = PasswordField('Пароль', validators=[DataRequired(message='Это обязательное поле.'),
                                                              Length(8,
                                                                     message='Количество символов должно превышать 8.')])


class CreateGame(FlaskForm):
    name = StringField('Название игры', validators=[DataRequired(message='Это поле обязательно.'), latinica_only])

    img = StringField('Ссылка на логотип', validators=[DataRequired(message='Это поле обязательно.')])

    des = StringField('Описание ', validators=[DataRequired(message='Это поле обязательно.')])

    password = PasswordField('Пароль', validators=[DataRequired(message='Это обязательное поле.'),
                                                              Length(8,
                                                                     message='Количество символов должно превышать 8.')])

class Like(FlaskForm):
    des = StringField()



