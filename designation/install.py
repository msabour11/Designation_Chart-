import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def after_install():
    add_custom_fields()


def add_custom_fields():
    custom_fields = {
        "Designation": [
            dict(
                fieldname="parent_designation",
                label="Parent Designation",
                fieldtype="Link",
                options="Designation",
                insert_after="description",
            )
        ],
    }

    create_custom_fields(custom_fields, update=True)
