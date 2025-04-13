import frappe


def after_uninstall():
    # Remove custom fields or any other cleanup operations
    remove_custom_fields()
    # Add any other cleanup operations here


def remove_custom_fields():
    # Define the custom fields to be removed
    custom_fields = {
        "Designation": [
            "parent_designation",
        ],
    }

    # Loop through each DocType and remove the specified custom fields
    for doctype, fields in custom_fields.items():
        for field in fields:
            try:
                # Delete the custom field from the database
                frappe.db.delete("Custom Field", {"dt": doctype, "fieldname": field})
                # Commit the changes to the database
                frappe.db.commit()
                # Optionally, you can also remove the field from the DocType

                print(f"Removed custom field '{field}' from '{doctype}'")
            except Exception as e:
                print(f"Error removing custom field '{field}' from '{doctype}': {e}")
