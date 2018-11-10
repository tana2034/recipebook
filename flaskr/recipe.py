import os
from enum import Enum
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.validator import Validator

from flaskr.model import db, Recipe, User

ALLOWED_EXTENSIONS = {'pdf', 'jpeg', 'jpg', 'heif', 'png'}
UPLOAD_FOLDER = 'upload'

bp = Blueprint('recipe', __name__)


@bp.route('/')
def index():
    recipes = Recipe.query.order_by(Recipe.id.desc()).all()
    return render_template('recipe/index.html', recipes=recipes)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    recipe = None
    if request.method == 'POST':
        recipe = _generateRecipe(request)
        if not recipe.validate():
            return redirect(request.url)
        recipe.regist()
        flash('regist successed')
        return redirect(url_for('recipe.index'))
    return render_template('recipe/edit.html', data=recipe)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    path = os.path.join(bp.root_path, UPLOAD_FOLDER, 'recipes', str(g.user.id))
    return send_from_directory(path, filename)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    data = get_recipe(id)

    if request.method == 'POST':
        recipe = _generateRecipe(request, id)
        if not recipe.validate():
            return redirect(request.url)
        recipe.update()
        flash('update successed')
        return redirect(url_for('recipe.index'))
    return render_template('recipe/edit.html', data=data)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    if request.method == 'POST':
        recipe = Recipe.query.filter_by(id=id).first()
        db.session.delete(recipe)
        db.session.commit()
        flash('deleted')
        return redirect(url_for('recipe.index'))


@bp.route('/<int:id>')
@login_required
def detail(id):
    data = get_recipe(id)
    return render_template('recipe/detail.html', data=data)


def get_recipe(id, check_author=True):
    recipe = Recipe.query.filter_by(id=id).first()

    if recipe is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and recipe.author_id != g.user.id:
        abort(403)

    return recipe


class RecipeType(Enum):
    WEBPAGE = 1
    IMAGE = 2


def _generateRecipe(request, id=None):
    type = request.form.getlist('type')[0]
    if int(type) == RecipeType.IMAGE.value:
        recipe = Image(request, id)
    else:
        recipe = Webpage(request, id)
    return recipe


class Detail():
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
            db.session.delete(Recipe(id=self.id))
            db.session.commit()


class Image(Detail):
    def validate(self):
        request = self.request

        if 'file' not in request.files:
            flash('No file part')
            return False
        file = request.files['file']
        if not file:
            flash('No file data')
            return False
        if file.filename == '':
            flash('No selected file')
            return False
        if allowed_file(file.filename):
            self.filename = secure_filename(file.filename)
            self.title = request.form.getlist('title')[0]
            self.description = request.form.getlist('description')[0]
            return True

    def regist(self):
        self.upload_image()
        recipe = Recipe(type=RecipeType.IMAGE.value, title=self.title, description=self.description,
                        filename=self.filename, author_id=g.user.id)
        db.session.add(recipe)
        db.session.commit()

    def update(self):
        self.upload_image()
        recipe = db.session.query(Recipe).filter_by(id=self.id).first()
        recipe.type = RecipeType.IMAGE.value
        recipe.title = self.title
        recipe.description = self.description
        recipe.filename = self.filename
        db.session.commit()

    def upload_image(self):
        file = self.request.files['file']
        dirpath = os.path.join(bp.root_path, UPLOAD_FOLDER,
                               'recipes', str(g.user.id))
        os.makedirs(dirpath, exist_ok=True)
        file.save(os.path.join(dirpath, self.filename))


class Webpage(Detail):
    def validate(self):
        request = self.request
        self.url = request.form.getlist('url')[0]
        self.title = request.form.getlist('title')[0]
        self.description = request.form.getlist('description')[0]
        validator = Validator()
        if not validator.isUrl(self.url):
            flash('not url')
            return False
        return True

    def regist(self):
        recipe = Recipe(type=RecipeType.WEBPAGE.value, title=self.title,
                        description=self.description, url=self.url, author_id=g.user.id)
        db.session.add(recipe)
        db.session.commit()

    def update(self):
        recipe = db.session.query(Recipe).filter_by(id=self.id).first()
        recipe.type = RecipeType.WEBPAGE.value
        recipe.title = self.title
        recipe.description = self.description
        recipe.url = self.url
        db.session.commit()
