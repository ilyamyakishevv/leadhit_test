from enum import Enum
from tinydb import TinyDB


class FieldType(str, Enum):
    date = "date"
    phone = "phone"
    email = "email"
    text = "text"


def create_database():
    db = TinyDB("templates_db.json")
    templates_table = db.table("templates")
    return templates_table

def fill_database():
    templates_data = [
        {
            "template_name": "Contact Data",
            "fields": [
                {"field_name": "phone", "field_type": FieldType.phone.value},
                {"field_name": "email", "field_type": FieldType.email.value}
            ]
        },
        {
            "template_name": "Order Data",
            "fields": [
                {"field_name": "text", "field_type": FieldType.text.value},
                {"field_name": "date", "field_type": FieldType.date.value}
            ]
        }
    ]
    templates_table = create_database()
    templates_table.truncate() 
    templates_table.insert_multiple(templates_data)

def get_templates_from_database():
    templates_table = create_database()
    templates_data = templates_table.all()
    return templates_data

