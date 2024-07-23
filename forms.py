from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, DateField, BooleanField, EmailField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional

class AitisiEna(FlaskForm):

    first_name = StringField('Όνομα' , validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Επίθετο' , validators=[DataRequired(), Length(min=2, max=20)])
    first_choice = SelectField(
        'Πρώτη Επιλογή Βρεφ/κού Σταθμού',
        choices=[
            ('', 'Επιλογή...'),
            ('Δημοτικός Βρεφ/κός Σταθμός Θέρμης', 'Δημοτικός Βρεφ/κός Σταθμός Θέρμης'),
            ('Δημοτικός Βρεφονηπιακός Σταθμός Βασιλικών', 'Δημοτικός Βρεφονηπιακός Σταθμός Βασιλικών'),
            ('Δημοτικός Βρεφονηπιακός Σταθμός Ελαφακια', 'Δημοτικός Βρεφονηπιακός Σταθμός Ελαφακια'),
            ('Παιδικός Σταθμός Καρδίας Γλυκές Μελωδίες', 'Παιδικός Σταθμός Καρδίας Γλυκές Μελωδίες'),
            ('Βρεφονηπιακός Σταθμός Μελισσόπουλα', 'Βρεφονηπιακός Σταθμός Μελισσόπουλα'),
            ('Βρεφονηπιακός Σταθμός Πλαγιαρίου Νότες Στοργής', 'Βρεφονηπιακός Σταθμός Πλαγιαρίου Νότες Στοργής')
        ],
        validators=[DataRequired(message="Παρακαλώ επιλέξτε μία επιλογή")])

    second_choice = SelectField(
        'Δεύτερη Επιλογή Βρεφ/κού Σταθμού',
        choices=[
            ('', 'Επιλογή...'),
            ('Δημοτικός Βρεφ/κός Σταθμός Θέρμης', 'Δημοτικός Βρεφ/κός Σταθμός Θέρμης'),
            ('Δημοτικός Βρεφονηπιακός Σταθμός Βασιλκών', 'Δημοτικός Βρεφονηπιακός Σταθμός Βασιλκών'),
            ('Δημοτικός Βρεφονηπιακός Σταθμός Ελαφακια', 'Δημοτικός Βρεφονηπιακός Σταθμός Ελαφακια'),
            ('Παιδικός Σταθμός Καρδίας Γλυκές Μελωδίες', 'Παιδικός Σταθμός Καρδίας Γλυκές Μελωδίες'),
            ('Βρεφονηπιακός Σταθμός Μελισσόπουλα', 'Βρεφονηπιακός Σταθμός Μελισσόπουλα'),
            ('Βρεφονηπιακός Σταθμός Πλαγιαρίου Νότες Στοργής', 'Βρεφονηπιακός Σταθμός Πλαγιαρίου Νότες Στοργής')
        ],
        validators=[DataRequired(message="Παρακαλώ επιλέξτε μία επιλογή")])

    kid_first_name = StringField('Όνομα', validators=[DataRequired(), Length(min=2, max=20)])
    kid_last_name = StringField('Επίθετο', validators=[DataRequired(), Length(min=2, max=20)])
    birth_date = DateField('Ημερομηνία γέννησης', validators=[DataRequired()])
    mother_first_name = StringField('Όνομα', validators=[DataRequired(), Length(min=2, max=20)])
    mother_last_name = StringField('Εππιθετο', validators=[DataRequired(), Length(min=2, max=20)])
    mother_father_name = StringField('Όνομα Πατέρα', validators=[DataRequired(), Length(min=2, max=20)])
    mother_adt = StringField('Α.Δ.Τ.', validators=[DataRequired(), Length(min=2, max=20)])

    family_status = SelectField(
        'Οικογενειακή Κατάσταση',
        choices=[
            ('', 'Επιλογή...'),
            ('Μονογονεϊακή Οικογένεια', 'Μονογονεϊακή Οικογένεια'),
            ('Τρίτεκνη Οικογένεια', 'Τρίτεκνη Οικογένεια'),
            ('Πολύτεκνη Οικογένεια', 'Πολύτεκνη Οικογένεια')
        ],
        validators=[DataRequired(message="Παρακαλώ κάντε μία επιλογή")])

    amea = SelectField(
        'Οικογένεια με μέλος ΑΜΕΑ 67% ή περισσότερο:',
        choices=[ 
            ('', 'Επιλογή...'),         
            ('Ναι', 'Ναι'),
            ('Όχι', 'Όχι')
        ],
        validators=[DataRequired(message="Παρακαλώ κάντε μία επιλογή")])

    kids_number = SelectField(
        'Επιλογή...',
        choices=[
            ('', 'Επιλογή...'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
        ],
        validators=[DataRequired(message="Παρακαλώ επιλέξτε μία επιλογή")])
    firstkidName = StringField('Όνομα Παιδιού (1):', validators=[DataRequired()])
    firstkid_birthdate = DateField('Ημερομηνία γέννησης', validators=[DataRequired()])
    secondkidName = StringField('Όνομα Παιδιού (2):', validators=[Optional()])
    secondkid_birthdate = DateField('Ημερομηνία γέννησης', validators=[Optional()])
    thirdkidName = StringField('Όνομα Παιδιού (3):', validators=[Optional()])
    thirdkid_birthdate = DateField('Ημερομηνία γέννησης', validators=[Optional()])
    fourthkidName = StringField('Όνομα Παιδιού (4):', validators=[Optional()])
    fourthkid_birthdate = DateField('Ημερομηνία γέννησης', validators=[Optional()])
    Check_dilosi = BooleanField('Δηλώνω υπεύθυνα ότι τα στοιχεία που παρείχα παραπάνω είναι ακριβή και αληθή.', validators=[DataRequired()])
    submit = SubmitField('Υποβολή')

class AitisiMetadimotefsis(FlaskForm):

    first_name = StringField('Όνομα', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Επίθετο', validators=[DataRequired(), Length(min=2, max=20)])
    father_fullname = StringField('Ονομ/μο Πατρός', validators=[DataRequired(), Length(min=2, max=20)])
    mother_fullname = StringField('Ονομ/μο Μητρός', validators=[DataRequired(), Length(min=2, max=20)])
    partner_first_name = StringField('Όνομα Συζύγου', validators=[DataRequired(), Length(min=2, max=20)])
    birth_date = DateField('Ημερομηνία γέννησης', validators=[DataRequired()])
    home_address = StringField('Διεύθυνση Κατοικίας', validators=[DataRequired(), Length(min=2, max=20)])
    taxidromiki_thirida = StringField('Τ.Θ.', validators=[DataRequired(), Length(min=2, max=20)])
    cell_number = StringField('Τηλέφωνο', validators=[DataRequired(), Length(min=2, max=20)])
    afm = StringField('Α.Φ.Μ.', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Ηλεκτρονική Διεύθυνση', validators=[DataRequired(), Email()])
    monimi_egkatastasi = BooleanField('Λόγω μονίμου εγκατάστασης', validators=[Optional()])
    gamos_dimoti = BooleanField('Λόγω γάμου με δημότη/-ισσα', validators=[Optional()])
    epanadimotefsi = BooleanField('Λόγω επαναδημότευσης', validators=[Optional()])
    arxiki_dimotikotita = BooleanField('Λόγω απόκτησης αρχικής δημοτικότητας του πατέρα ή της μητέρας ή των γονέων μου', validators=[Optional()])
    luseos_gamou = BooleanField('Λόγω λύσεως του γάμου μου', validators=[Optional()])
    upopsifiotita = BooleanField('Λόγω υποψηφιότητας στις επικείμενες Δημοτικές & Περιφερειακές Εκλογές', validators=[Optional()])
    municipality = StringField('Δήμος', validators=[DataRequired()])
    dilosi_dieti_katikia = FileField('dilosi_dieti_katikia', validators=[
        Optional(),
        FileAllowed(['pdf', 'png'], 'Επιλέξτε αρχείο')
    ])
    dilosi_epanadimotefsi = FileField('dilosi_epanadimotefsi', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'png'], 'Επιλέξτε αρχείο')
    ])
    astinomiki_tautothta = FileField('astinomiki_tautothta', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'png'], 'Επιλέξτε αρχείο')
    ])
    antigrafo_e1 = FileField('antigrafo_e1', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'png'], 'Επιλέξτε αρχείο')
    ])   
    antigrafo_logariasmou = FileField('antigrafo_logariasmou', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'png'], 'Επιλέξτε αρχείο')
    ])  
    Check_dilosi = BooleanField('Δηλώνω υπεύθυνα ότι τα στοιχεία που παρείχα παραπάνω είναι ακριβή και αληθή.', validators=[DataRequired()]) 
    Check_prosopika_dedomena = BooleanField('Συμφωνώ με τους Ορους Προστασίας Προσωπικών Δεδομένων της ιστοσελίδας του Δήμου Θέρμης.', validators=[DataRequired()]) 
    submit = SubmitField('Υποβολή')
