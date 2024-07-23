import os
from flask import Flask, render_template, redirect, url_for, flash, abort, request
from config import Config
from flask_migrate import Migrate
from models import db, Aitisi1_db
from werkzeug.utils import secure_filename
from pdf import pdf_names, aitisi1_pdf, aitisi_metad_pdf
from forms import AitisiEna, AitisiMetadimotefsis

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.before_request
def create_tables():
    if not hasattr(app, 'tables_created'):
        db.create_all()
        app.tables_created = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aitisi-1", methods=['GET'])
def aitisi1():
    form = AitisiEna()
    return render_template('aitisi1.html', form=form)

@app.route("/aitisi-1", methods=['POST'])
def aitisi1_submit():
    form = AitisiEna()
    if form.validate_on_submit():
        pdf_random_name = pdf_names()

        user = Aitisi1_db(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            kid_first_name=form.kid_first_name.data,
            kid_last_name=form.kid_last_name.data,
            birth_date=form.birth_date.data,
            first_choice=form.first_choice.data,
            second_choice=form.second_choice.data,
            pdf_filename=pdf_random_name
        )
        db.session.add(user)
        db.session.commit() 
        
        aitisi1_pdf(form, pdf_random_name)

        flash('Η φόρμα υποβλήθηκε επιτυχώς!', 'success')
        return redirect(url_for('index'))
    else:
        flash(str(form.errors))
        return render_template('aitisi1.html', form=form)
    
@app.route('/ipovoles')
def users():
    all_users = Aitisi1_db.query.all()
    return render_template('ipovoles.html', users=all_users)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_row(id):
    row = Aitisi1_db.query.get(id)
    if row:
        db.session.delete(row)
        db.session.commit()
        flash('Επιτυχής Διαγραφή', 'success')  
    else:
        flash('Σφάλμα κατά τη διαγραφή', 'error')

    return redirect(url_for('users'))


@app.route("/aitisi-metadimotefsis", methods=['GET'])
def aitisimetadimotefsis():
    form = AitisiMetadimotefsis()
    return render_template('aitisimetadimotefsis.html', form=form)

@app.route("/aitisi-metadimotefsis", methods=['POST'])
def aitisimetadimotefsis_submit():
    form = AitisiMetadimotefsis()
    if form.validate_on_submit():
        pdf_random_name = pdf_names()
        aitisi_metad_pdf(form, pdf_random_name)
        for field_name in ['dilosi_dieti_katikia', 'dilosi_epanadimotefsi', 'astinomiki_tautothta', 'antigrafo_e1', 'antigrafo_logariasmou']:
            file = getattr(form, field_name).data 
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
        flash('Η φόρμα υποβλήθηκε επιτυχώς!', 'success')
        return redirect(url_for('index'))
    else:
        flash(str(form.errors))
        return render_template('aitisimetadimotefsis.html', form=form)

@app.route("/aitisi-3")
def aitisi3():
    return render_template("aitisi3.html")


app.run(debug=True)
