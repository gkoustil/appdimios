from models import Aitisi1_db, Aitisimetadimotefsis_db

def get_model_by_form_type(form_type):
    form_type_model_map = {
        'aitisi1': Aitisi1_db,
        'metadimotefsi': Aitisimetadimotefsis_db,
        # Add other form models here
    }
    return form_type_model_map.get(form_type)