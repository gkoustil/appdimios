import os
from flask import Flask, render_template, redirect, url_for, flash, abort, request, send_from_directory
from dotenv import load_dotenv
from config import Config
import shutil
from flask_migrate import Migrate
from models import db, Aitisi1_db, Aitisimetadimotefsis_db
from models_utils import get_model_by_form_type
from werkzeug.utils import secure_filename
from pdf import pdf_names, aitisi1_pdf, aitisi_metad_pdf
from forms import AitisiEna, AitisiMetadimotefsis

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
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
        submission_id = pdf_random_name.replace('.pdf', '')

        entry = Aitisi1_db(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            kid_first_name=form.kid_first_name.data,
            kid_last_name=form.kid_last_name.data,
            birth_date=form.birth_date.data,
            first_choice=form.first_choice.data,
            second_choice=form.second_choice.data,
            pdf_filename=pdf_random_name
        )
        db.session.add(entry)
        db.session.commit() 

        script_dir = os.path.dirname(__file__)
        entry_dir = os.path.join(script_dir, 'pdfs', 'aitisi1_sub', submission_id)
        os.makedirs(entry_dir, exist_ok=True)
        
        aitisi1_pdf(form, pdf_random_name, entry_dir)

        flash('Η φόρμα υποβλήθηκε επιτυχώς!', 'success')
        return redirect(url_for('index'))
    else:
        flash(str(form.errors))
        return render_template('aitisi1.html', form=form)
    
@app.route('/aitisi1_entries')
def aitisi1_entries():
    entries = Aitisi1_db.query.all()
    return render_template('aitisi1_entries.html', entries=entries)

@app.route('/pdfs/<subdir>/<entry_dir>/<filename>')
def serve_pdf(subdir, entry_dir, filename):
    script_dir = os.path.dirname(__file__)
    directory = os.path.join(script_dir, 'pdfs', subdir, entry_dir)
    if os.path.exists(os.path.join(directory, filename)):
        return send_from_directory(directory, filename)
    else:
        abort(404)

#@app.route('/pdfs/<subdir>/<path:filename>')
#def serve_pdf(subdir, filename):
    #pdf_base_dir = os.path.join(os.path.dirname(__file__), 'pdfs')
    #pdf_dir = os.path.join(pdf_base_dir, subdir)
    #return send_from_directory(pdf_dir, filename)

#@app.route('/delete/<int:id>', methods=['POST'])
#def delete_row(id):
    #row = Aitisi1_db.query.get(id)
    #if row:
        #db.session.delete(row)
        #db.session.commit()
        #flash('Επιτυχής Διαγραφή', 'success')  
    #else:
        #flash('Σφάλμα κατά τη διαγραφή', 'error')

    #return redirect(url_for('users'))

@app.route("/aitisi-metadimotefsis", methods=['GET'])
def aitisimetadimotefsis():
    form = AitisiMetadimotefsis()
    return render_template('aitisimetadimotefsis.html', form=form)

@app.route("/aitisi-metadimotefsis", methods=['POST'])
def aitisimetadimotefsis_submit():
    form = AitisiMetadimotefsis()
    if form.validate_on_submit():
        pdf_random_name = pdf_names()
        submission_id = pdf_random_name.replace('.pdf', '')

        file_names = {}

        # Check if each file is uploaded and generate a filename if it is
        # DO I REALLY NEED A RANDOM NAME FOR UPLOADS?? -  MAYBE A SET NAME
        for field_name in ['dilosi_dieti_katikia', 'dilosi_epanadimotefsi', 'astinomiki_tautothta', 'antigrafo_e1', 'antigrafo_logariasmou']:
            file = getattr(form, field_name).data
            if file:
                file_names[field_name] = pdf_names()
            else:
                file_names[field_name] = None

        entry = Aitisimetadimotefsis_db(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            father_fullname=form.father_fullname.data,
            mother_fullname=form.mother_fullname.data,
            birth_date=form.birth_date.data,
            pdf_filename=pdf_random_name,
            pdf_dieti_katikia=file_names['dilosi_dieti_katikia'],
            pdf_dilosi_epanadimotefsi=file_names['dilosi_epanadimotefsi']
            )
        db.session.add(entry)
        db.session.commit() 

        script_dir = os.path.dirname(__file__)
        entry_dir = os.path.join(script_dir, 'pdfs', 'metadimotefsi_sub', submission_id)
        os.makedirs(entry_dir, exist_ok=True)

        aitisi_metad_pdf(form, pdf_random_name, entry_dir)

        for field_name, filename in file_names.items():
            file = getattr(form, field_name).data 
            if file:
                file_path = os.path.join(entry_dir, filename)
                file.save(file_path)

        flash('Η φόρμα υποβλήθηκε επιτυχώς!', 'success')
        return redirect(url_for('index'))
    else:
        flash(str(form.errors))
        return render_template('aitisimetadimotefsis.html', form=form)

@app.route('/metadimotefsi_entries')
def metadimotefsi_entries():
    entries = Aitisimetadimotefsis_db.query.all()
    return render_template('metadimotefsi_entries.html', entries=entries)

@app.route("/aitisi-3")
def aitisi3():
    return render_template("aitisi3.html")

#@app.route('/delete/<string:form_type>/<int:id>', methods=['POST'])
#def delete_entry(form_type, id):
    #model = get_model_by_form_type(form_type)
    #if not model:
        #flash('Invalid form type', 'error')
        #return redirect(url_for(f'{form_type}_entries'))

    #row = model.query.get(id)
    #if row:
        #db.session.delete(row)
        #db.session.commit()
        #flash('Επιτυχής Διαγραφή', 'success')  
    #else:
        #flash('Σφάλμα κατά τη διαγραφή', 'error')

    #return redirect(url_for(f'{form_type}_entries'))
    
def get_pdf_file_path(form_type, filename):
    script_dir = os.path.dirname(__file__)
    if form_type == 'aitisi1':
        return os.path.join(script_dir, 'pdfs', 'aitisi1_sub', filename.replace('.pdf', ''), filename)
    elif form_type == 'metadimotefsi':
        return os.path.join(script_dir, 'pdfs', 'metadimotefsi_sub', filename.replace('.pdf', ''), filename)
    # Add other form types as needed
    return None

@app.route('/delete/<string:form_type>/<int:id>', methods=['POST'])
def delete_entry(form_type, id):
    model = get_model_by_form_type(form_type)
    if not model:
        flash('Invalid form type', 'error')
        return redirect(url_for(f'{form_type}_entries'))

    row = model.query.get(id)
    if row:

        pdf_dir_path = os.path.dirname(get_pdf_file_path(form_type, row.pdf_filename))
        
        db.session.delete(row)
        db.session.commit()

        if pdf_dir_path and os.path.exists(pdf_dir_path):
            try:
                shutil.rmtree(pdf_dir_path)
            except Exception as e:
                flash(f'Σφάλμα κατά την διαγραφή του PDF: {e}', 'error')

        flash('Επιτυχής Διαγραφή', 'success')
    else:
        flash('Σφάλμα κατά τη διαγραφή', 'error')

    return redirect(url_for(f'{form_type}_entries'))

app.run(debug=True)
