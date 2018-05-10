from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.categories.models import Category
from application.categories.forms import CategoryForm, CategoryEditName
from application.works.models import Work

@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", categories = Category.query.all())

@app.route("/categories/delete/<category_id>/", methods=["POST"])
@login_required(role="ADMIN")
def category_delete(category_id):
    c = Category.query.get(category_id)
    db.session.delete(c)
    db.session().commit()

    return redirect(url_for("categories_index"))

@app.route("/categories/<category_id>/", methods=["GET"])
def category_view(category_id):
    return render_template("categories/category.html", category = Category.query.get(category_id), 
        works = Category.works_in_category(category_id))

@app.route("/categories/new/", methods=["GET"])
@login_required()
def categories_form():
    return render_template("categories/new.html", form = CategoryForm())

@app.route("/categories/new/", methods=["POST"])
@login_required()
def categories_create():
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("categories/new.html", form = form)

    c = Category(form.name.data)

    db.session().add(c)
    db.session().commit()
    
    return redirect(url_for("categories_index"))

@app.route("/categories/deletework/<category_id>/<work_id>/", methods=["POST"])
@login_required(role="ADMIN")
def category_work_delete(category_id, work_id):
    c = Category.query.get(category_id)
    w = Work.query.get(work_id)
    w.categories.remove(c)
    db.session().commit()

    return redirect(url_for("category_view", category_id=category_id))

@app.route("/categories/editname/<category_id>/", methods=["GET"])
@login_required(role="ADMIN")
def category_editnameform(category_id):  
    return render_template("categories/editname.html", form = CategoryEditName(), category_id=category_id)

@app.route("/categories/editname/<category_id>/", methods=["POST"])
@login_required(role="ADMIN")
def category_editname(category_id):
    form = CategoryEditName(request.form)
    
    if not form.validate():
        return render_template("categories/editname.html", form = form, category_id=category_id)

    c = Category.query.get(category_id)

    c.name = form.name.data

    db.session().commit()

    return redirect(url_for("category_view", category_id=category_id))