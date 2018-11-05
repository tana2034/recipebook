import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.validator import Validator

ALLOWED_EXTENSIONS = set(['pdf','jpeg','jpg','heif','png'])
UPLOAD_FOLDER = 'upload'

bp = Blueprint('recipe', __name__)
@bp.route('/')
def index():
    db = get_db()
    recipes = db.execute(
        'SELECT r.id, r.type, r.filename, r.title, r.description, r.url, r.created, r.author_id, u.username'
        ' FROM recipe r LEFT OUTER JOIN user u ON r.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('recipe/index.html', recipes=recipes)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    recipe = ()
    if request.method == 'POST':
        recipe = _generateRecipe(request)
        recipe.validate()
        recipe.regist()
        flash('regist successed')
        return redirect(url_for('recipe.index'))
    return render_template('recipe/edit.html', data=recipe)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    path = os.path.join(bp.root_path, UPLOAD_FOLDER, 'recipes', str(g.user['id']))
    return send_from_directory(path, filename)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    data = get_recipe(id)

    if request.method == 'POST':
        recipe = _generateRecipe(request, id)
        recipe.validate()
        recipe.update()
        flash('update successed')
        return redirect(url_for('recipe.index'))
    return render_template('recipe/edit.html', data=data)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    if request.method == 'POST':
        recipe = Recipe(None, id)
        recipe.delete()
        flash('deleted')
        return redirect(url_for('recipe.index'))


@bp.route('/<int:id>')
@login_required
def detail(id):
    data = get_recipe(id)
    return render_template('recipe/detail.html', data=data)


def get_recipe(id, check_author=True):
    recipe = get_db().execute(
        'SELECT r.id, r.title, r.type, r.url, r.description, r.filename, r.created, r.author_id, u.username'
        ' FROM recipe r JOIN user u ON r.author_id = u.id'
        ' WHERE r.id = ?',
        (id,)
    ).fetchone()

    if recipe is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and recipe['author_id'] != g.user.id:
        abort(403)

    return recipe


def _generateRecipe(request, id=None):
    type = request.form.getlist('type')[0]
    if type == '2' :
        recipe = Image(request, id)
    else:
        recipe = Webpage(request, id)
    return recipe


class Recipe():
    def __init__(self, request, id=None):
        self.request = request
        if not id == None:
            self.id = id


    def validate(self):
        pass


    def regist(self):
        pass
    

    def update(self):
        pass


    def delete(self):
        if not self.id is None:
            db = get_db()
            db.execute(
                'DELETE FROM recipe WHERE id = ?',
                (self.id,)
            )
            db.commit()


class Image(Recipe):
    def validate(self):
        request = self.request
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            self.filename = secure_filename(file.filename)
            self.title = request.form.getlist('title')[0]
            self.description = request.form.getlist('description')[0]


    def regist(self):
        self.upload_image()
        db = get_db()
        db.execute(
            'INSERT INTO recipe (type, title, description, filename, author_id)'
            ' VALUES (?, ?, ?, ?, ?)',
            (2, self.title, self.description, self.filename, g.user['id'])
        )
        db.commit()


    def update(self):
        self.upload_image()
        db = get_db()
        db.execute(
            'UPDATE recipe SET type = ?, title = ?, description = ?, filename = ?, author_id = ?'
            ' WHERE id = ?',
            (2, self.title, self.description, self.filename, g.user['id'], self.id)
        )
        db.commit()
        

    def upload_image(self):
        file = self.request.files['file']
        dirpath = os.path.join(bp.root_path , UPLOAD_FOLDER, 'recipes', str(g.user['id']))
        os.makedirs(dirpath, exist_ok=True)
        file.save(os.path.join(dirpath, self.filename))


class Webpage(Recipe):
    def validate(self):
        request = self.request
        self.url = request.form.getlist('url')[0]
        self.title = request.form.getlist('title')[0]
        self.description = request.form.getlist('description')[0]
        validator = Validator()
        if not validator.isUrl(self.url):
            flash('not url')
            return redirect(request.url)


    def regist(self):
        db = get_db()
        db.execute(
            'INSERT INTO recipe (type, title, description, url, author_id)'
            ' VALUES (?, ?, ?, ?, ?)',
            (1, self.title, self.description, self.url, g.user['id'])
        )
        db.commit()


    def update(self):
        db = get_db()
        db.execute(
            'UPDATE recipe SET type = ?, title = ?, description = ?, url = ?, author_id = ?'
            ' WHERE id = ?',
            (1, self.title, self.description, self.url, g.user['id'], self.id)
        )
        db.commit()