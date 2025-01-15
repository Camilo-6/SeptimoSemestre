import functools
import os

# Cambio import de flash from flask
from flask import (render_template, Blueprint, g, redirect, request, session, url_for, flash)

# Upload files secure
from werkzeug.utils import secure_filename
from src.controller.auth import requires_login

# Cambio para usar generate_password_hash
from werkzeug.security import generate_password_hash

# Maped rows to objects
from src.model.user import User
from src.model.post import Post
# import querys
from src.model.repo import *
from src import app

# Endpoint para la función de autenticación y registro de usuarios
profile = Blueprint('profile', __name__, url_prefix='/profile')

@profile.route('/<user>', methods=['GET', 'POST'])
@requires_login
def main(user):
    # Cambio para evitar que un usuario vea el perfil de otro usuario
    current_user = session.get('user')
    if current_user != user:
        flash('No puedes hacer esto >:(')
        return redirect(url_for('home.main'))
    '''Gets the user information and can update info when update'''
    user = get_user(user)
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        second_name = request.form.get('second_name')
        birthday = request.form.get('birthday')
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        # Cambio para usar generate_password_hash
        password_hash = generate_password_hash(new_password)
        # Cambio para actualizar los datos del usuario
        """
        user.first_name = first_name
        user.second_name = second_name
        user.birthday = birthday
        """
        # Cambio para actualizar la contrasenia
        """
        if old_password and new_password:
            if old_password == user.password:
                user.password = new_password
            else:
                flash('Las contraseñas no coinciden')
        """
        if old_password and new_password:
            if check_password_hash(user[1], old_password):
                # Cambio para actualizar los datos del usuario
                cambio = User.update(User, user[0], first_name, second_name, birthday, password_hash)
                if cambio == None:
                    flash('Error al actualizar los datos')
                else:
                    flash('Datos actualizados')
            else:
                flash('Contrasenia incorrecta')    
        # Cambio para actualizar los datos del usuario
        #add(user)
    return render_template('blog/profile.html',
                           user = user)

@profile.route('/create', methods=['GET', 'POST'])
@requires_login
def create():
    '''This person creates a post'''
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text').strip()
        img = request.files['img']
        access = 'access' in request.form

        post = Post(title, text, access)
        post.author = session['user']#:)

        if img:
            filename = secure_filename(img.filename)
            abs_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img.save(abs_path)
            post.img = abs_path[5+8:] #LMAO

        add(post)
        return redirect(url_for('home.main'))

    return render_template('blog/create.html')

@profile.route('/update/<int:id_post>', methods=['GET', 'POST'])
@requires_login
def update(id_post):
    # Cambio implementacion para poder editar un post
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text').strip()
        img = request.files['img']
        access = 'access' in request.form
        if img:
            filename = secure_filename(img.filename)
            abs_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img.save(abs_path)
            post_img = abs_path[5+8:]
            cambio = Post.update(Post, id_post, title, text, access, post_img)
        else:
            cambio = Post.update(Post, id_post, title, text, access, None)
        if cambio == None:
            flash('Error al actualizar el post')
        else:
            flash('Post actualizado')
        return redirect(url_for('home.main'))
    '''Updates a post by this user'''
    post = get_post_by_id(id_post)
    # Cambio para evitar que un usuario actualice un post de otro usuario
    current_user = session.get('user')
    if current_user != post.author:
        flash('No puedes hacer esto >:(')
        return redirect(url_for('home.main'))
    return render_template('blog/update.html', post = post)

@profile.route('/delete/<int:id_post>', methods=['GET', 'POST'])
@requires_login
def delete(id_post):
    '''Deletes a post by this user'''
    post = get_post_by_id(id_post)
    # Cambio para evitar que un usuario elimine un post de otro usuario
    current_user = session.get('user')
    if current_user != post.author:
        flash('No puedes hacer esto >:(')
        return redirect(url_for('home.main'))
    remove(post)
    # Cambio para redirigir a home.main en lugar de profile.main y agregar el mensaje de confirmacion
    #return redirect(url_for('profile.main', user = post.author))
    flash('Post eliminado')
    return redirect(url_for('home.main'))
