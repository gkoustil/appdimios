from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aitisi1_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    kid_first_name = db.Column(db.String(20), nullable=False)
    kid_last_name = db.Column(db.String(20), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    first_choice = db.Column(db.String(20), nullable=False)
    second_choice = db.Column(db.String(20), nullable=False)
    pdf_filename = db.Column(db.String(100), nullable=True)
   

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.kid_first_name}', '{self.kid_last_name}', '{self.birth_date}', '{self.first_choice}', '{self.second_choice}', '{self.pdf_filename}')"
    
class Aitisimetadimotefsis_db(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    father_fullname = db.Column(db.String(20), nullable=False)
    mother_fullname = db.Column(db.String(20), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    pdf_filename = db.Column(db.String(100), nullable=False)
    pdf_dieti_katikia = db.Column(db.String(100), nullable=False)
    pdf_dilosi_epanadimotefsi = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.father_fullname}', '{self.mother_fullname}', '{self.birth_date}', '{self.pdf_filename}', '{self.pdf_dieti_katikia}'), '{self.pdf_dieti_katikia}')"
    
