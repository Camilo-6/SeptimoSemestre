import datetime as dt

from sqlalchemy import func, or_
from sqlalchemy.sql import text
from src.model.user import User
from src.model.post import Post

# Cambio para usar check_password_hash
from werkzeug.security import check_password_hash


from src import db

def get_user(username):
    # Cambio para evitar SQL Injection al iniciar sesion
    # En lugar de usar f-strings, usamos placeholders para los valores
    '''Returns the username as python object'''
    """
    session = db.session()
    query = text(f"SELECT * FROM user WHERE username = '{username}'")
    cursor = session.execute(query).cursor
    return cursor.fetchone()
    """
    session = db.session()
    query = text("SELECT * FROM user WHERE username = :username")
    result = session.execute(query, {'username': username})
    return result.fetchone()

def get_all_public_posts():
    '''Returns all public posts'''
    return Post.query.filter(Post.access == 1)

def get_post_by_id(id_post):
    return Post.query.get(id_post)

def get_posts_by_access(user, access):
    return Post.query.filter(Post.access == access, Post.author == user)

def get_birthdays(days):
    '''Gets all birthdays within the range days '''
    dateFrom = dt.date.today()
    dateTo = dt.date.today() + dt.timedelta(days=days)
    thisYear = dateFrom.year
    nextYear = dateFrom.year +1
    return User.query.filter(
        or_(
            func.STR_TO_DATE(func.concat(func.DATE_FORMAT(User.birthday, "%d%m"), thisYear), "%d%m%Y").between(dateFrom, dateTo),
            func.STR_TO_DATE(func.concat(func.DATE_FORMAT(User.birthday, "%d%m"), nextYear), "%d%m%Y").between(dateFrom, dateTo)
        )
    )

def validate_user_and_password(username, password):
    # Cambio para evitar SQL Injection al iniciar sesion
    # En lugar de usar f-strings, usamos placeholders para los valores
    # Cambio para usar check_password_hash
    # En lugar de usar las contrasenias en texto plano, usamos hash
    session = db.session()
    #query = text(f"SELECT * FROM user WHERE username='{username}' AND password='{password}'")
    query = text("SELECT * FROM user WHERE username = :username")
    try:
        #cursor = session.execute(query).cursor
        result = session.execute(query, {'username': username})
        user = result.fetchone()
        pass
        if user:
            password1 = user.password
            resultado = check_password_hash(password1, password)
            if resultado:
                return True
    except:
        return False
    #return cursor.fetchone()
    return False


def add(entity):
    '''Adds the model to its respective table'''
    db.session.add(entity)
    db.session.commit()

def remove(entity):
    '''Removes the model to its respective table'''
    db.session.delete(entity)
    db.session.commit()

