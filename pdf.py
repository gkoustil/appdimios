import fpdf 
import os
import uuid

def pdf_names():
    return f"{uuid.uuid4()}.pdf"


def aitisi1_pdf(form_data, filename, entry_dir):

    pdf_path = os.path.join(entry_dir, filename)

    script_dir = os.path.dirname(__file__)

    #pdf_dir = os.path.join(script_dir, 'pdfs', 'aitisi1_sub')
    #os.makedirs(pdf_dir, exist_ok=True)
    #pdf_path = os.path.join(pdf_dir, filename)

    file_path = os.path.join(script_dir, 'templates', 'pdf_template_aitisi1.html')
    with open(file_path, "r", encoding='utf-8') as fl:
        template = fl.read()

    id_number_form = filename.replace('.pdf', '')
    template = template.replace("//IDNUMBER//", id_number_form)
    first_name = form_data.first_name.data
    template = template.replace("//FIRSTNAME//", first_name)
    last_name = form_data.last_name.data
    template = template.replace("//LASTNAME//", last_name)
    first_choice = form_data.first_choice.data
    template = template.replace("//CHOICEONE//", first_choice)
    second_choice = form_data.second_choice.data
    template = template.replace("//CHOICETWO//", second_choice)
    second_choice = form_data.second_choice.data
    template = template.replace("//CHOICETWO//", second_choice)
    kid_first_name = form_data.kid_first_name.data
    template = template.replace("//KIDFIRSTNAME//", kid_first_name)
    kid_last_name = form_data.kid_last_name.data
    template = template.replace("//KIDLASTNAME//", kid_last_name)
    birth_date = form_data.birth_date.data
    birth_date_str = birth_date.strftime("%d-%m-%Y")
    template = template.replace("//BIRTHDATE//", birth_date_str)
    mother_first_name = form_data.mother_first_name.data
    template = template.replace("//MOTHERFIRSTNAME//", mother_first_name)
    mother_last_name = form_data.mother_last_name.data
    template = template.replace("//MOTHERLASTNAME//", mother_last_name)
    mother_father_name = form_data.mother_father_name.data
    template = template.replace("//MOTHERFATHERNAME//", mother_father_name)
    mother_adt = form_data.mother_adt.data
    template = template.replace("//MOTHERADT//", mother_adt)
    family_status = form_data.family_status.data
    template = template.replace("//FAMILYSTATUS//", family_status)
    amea = form_data.amea.data
    template = template.replace("//AMEASTATUS//", amea)
    kids_number = form_data.kids_number.data
    template = template.replace("//KIDNUMBER//", kids_number)
    
    firstkidName = form_data.firstkidName.data
    template = template.replace("//FIRSTKIDNAME//", firstkidName)
    
    firstkid_birthdate = form_data.firstkid_birthdate.data
    firstkid_birthdate_str = firstkid_birthdate.strftime("%d-%m-%Y")
    template = template.replace("//FIRSTKIDBIRTHDATE//", firstkid_birthdate_str)
    
    secondkidName = form_data.secondkidName.data
    template = template.replace("//SECONDKIDNAME//", secondkidName)
    
    secondkid_birthdate = form_data.secondkid_birthdate.data
    secondkid_birthdate_str = secondkid_birthdate.strftime("%d-%m-%Y") if secondkid_birthdate else ""
    template = template.replace("//SECONDKIDBIRTHDATE//", secondkid_birthdate_str)

    thirdkidName = form_data.thirdkidName.data
    template = template.replace("//THIRDKIDNAME//", thirdkidName)
    
    thirdkid_birthdate = form_data.thirdkid_birthdate.data
    thirdkid_birthdate_str = thirdkid_birthdate.strftime("%d-%m-%Y") if secondkid_birthdate else ""
    template = template.replace("//THIRDKIDBIRTHDATE//", thirdkid_birthdate_str)

    fourthkidName = form_data.fourthkidName.data
    template = template.replace("//FOURTHKIDNAME//", fourthkidName)

    fourthkid_birthdate = form_data.fourthkid_birthdate.data
    fourthkid_birthdate_str = fourthkid_birthdate.strftime("%d-%m-%Y") if secondkid_birthdate else ""
    template = template.replace("//FOURTHKIDBIRTHDATE//", fourthkid_birthdate_str)

    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.add_font(fname='DejaVuSansCondensed.ttf')
    pdf.set_font('DejaVuSansCondensed', size=14)
    pdf.write_html(template)
    pdf.output(pdf_path)


def aitisi_metad_pdf(form_data, filename, entry_dir):

    pdf_path = os.path.join(entry_dir, filename)

    script_dir = os.path.dirname(__file__)

    #pdf_dir = os.path.join(script_dir, 'pdfs', 'metadimotefsi_sub')
    #os.makedirs(pdf_dir, exist_ok=True)
    #pdf_path = os.path.join(pdf_dir, filename)

    file_path = os.path.join(script_dir, 'templates', 'pdf_template_aitisi_metadim.html')
    with open(file_path, "r", encoding='utf-8') as fl:
        template = fl.read()

    id_number_form = filename.replace('.pdf', '')
    template = template.replace("//IDNUMBER//", id_number_form)
    first_name = form_data.first_name.data
    template = template.replace("//FIRSTNAME//", first_name)
    last_name = form_data.last_name.data
    template = template.replace("//LASTNAME//", last_name)
    father_fullname = form_data.father_fullname.data
    template = template.replace("//FATHERFULLNAME//", father_fullname)
    mother_fullname = form_data.mother_fullname.data
    template = template.replace("//MOTHERFULLNAME//", mother_fullname)
    partner_first_name = form_data.partner_first_name.data
    template = template.replace("//PARTNERFIRSTNAME//", partner_first_name)
    birth_date = form_data.birth_date.data
    birth_date_str = birth_date.strftime("%d-%m-%Y")
    template = template.replace("//BIRTHDATE//", birth_date_str)
    home_address = form_data.home_address.data
    template = template.replace("//HOMEADDRESS//", home_address)
    taxidromiki_thirida = form_data.taxidromiki_thirida.data
    template = template.replace("//POBOX//", taxidromiki_thirida)
    cell_number = form_data.cell_number.data
    template = template.replace("//CELLNUMBER//", cell_number)
    afm = form_data.afm.data
    template = template.replace("//AFM//", afm)
    email = form_data.email.data
    template = template.replace("//EMAIL//", email)
    email = form_data.email.data
    template = template.replace("//EMAIL//", email)
    monimi_egkatastasi = form_data.monimi_egkatastasi.data
    monimi_egkatastasi_str = str(form_data.monimi_egkatastasi.label.text) if monimi_egkatastasi else ""
    template = template.replace("//PERMANENTRESIDENCE//", monimi_egkatastasi_str)
    gamos_dimoti = form_data.gamos_dimoti.data
    gamos_dimoti_str = str(form_data.gamos_dimoti.label.text) if gamos_dimoti else ""
    template = template.replace("//MARRIAGETOMUNICIPALRESIDENT//", gamos_dimoti_str)
    epanadimotefsi = form_data.epanadimotefsi.data
    epanadimotefsi_str = str(form_data.epanadimotefsi.label.text) if epanadimotefsi else ""
    template = template.replace("//REREGISTRATION//", epanadimotefsi_str)
    arxiki_dimotikotita = form_data.arxiki_dimotikotita.data
    arxiki_dimotikotita_str = str(form_data.arxiki_dimotikotita.label.text) if arxiki_dimotikotita else ""
    template = template.replace("//INITIALMUNICIPALREGISTRATION//", arxiki_dimotikotita_str)
    luseos_gamou = form_data.luseos_gamou.data
    luseos_gamou_str = str(form_data.luseos_gamou.label.text) if luseos_gamou else ""
    template = template.replace("//DISSOLUTIONOFMARRIAGE//", luseos_gamou_str)
    upopsifiotita = form_data.upopsifiotita.data
    upopsifiotita_str = str(form_data.upopsifiotita.label.text) if upopsifiotita else ""
    template = template.replace("//CANDIDACYFORUPCOMINGELECTIONS//", upopsifiotita_str)
    municipality = form_data.municipality.data
    template = template.replace("//MUNICIPALITY//", municipality)


    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.add_font(fname='DejaVuSansCondensed.ttf')
    pdf.set_font('DejaVuSansCondensed', size=14)
    pdf.write_html(template)
    pdf.output(pdf_path)
