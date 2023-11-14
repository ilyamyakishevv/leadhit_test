from db import get_templates_from_database, fill_database
from fastapi import FastAPI, Form
from typing import Optional
from validation import *


app = FastAPI()


templates_table = get_templates_from_database()
fill_database()

def find_matching_template(submitted_fields: dict) -> Optional[str]:
    for template in templates_table:
        template_fields = template.get('fields', {})
        matching_fields = 0

        for field_name, field_value in submitted_fields.items():
            if field_name in template_fields and template_fields[field_name] == field_value:
                matching_fields += 1

        if matching_fields == len(submitted_fields):
            return template["fields"]

    return None




@app.post("/get_form")
def get_form(f_name1: str, f_name2: str):
    submitted_fields = {"f_name1": f_name1, "f_name2": f_name2}
    print(f"f_name1: {f_name1}, f_name2: {f_name2}") 

    matched_template = find_matching_template(submitted_fields)
    if matched_template:
        return {"form_name": matched_template}
    else:
        field_type_dict = {}
        for field_name, field_value in submitted_fields.items():
            for field_type in ["date", "phone", "email", "text"]:
                if validate_field_value(field_type, field_value):
                    field_type_dict[field_name] = field_type
                    break

        return field_type_dict