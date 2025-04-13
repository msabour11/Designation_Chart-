# import frappe


# @frappe.whitelist()
# def get_children(parent=None, exclude_node=None, company=None):
#     filters = []

#     if parent:
#         filters.append({"parent_designation": parent})
#     else:
#         filters.append({"parent_designation": ["in", [None, ""]]})

#     if exclude_node:
#         filters.append({"name": ["!=", exclude_node]})

#     print("Filters used:", filters)  # Debugging statement

#     designations = frappe.get_all(
#         "Designation",
#         fields=[
#             "name",
#             "name as id",
#             "parent_designation as reports_to",
#             # "custom_is_group as is_group",
#             # "designation_name as title",
#         ],
#         filters=filters,
#         order_by="name",
#     )

#     print("Designations fetched:", designations)  # Debugging statement

#     for designation in designations:
#         designation["connections"] = get_child_count(designation["id"])
#         designation["expandable"] = designation["connections"] > 0
#         print(
#             f"Designation: {designation['name']}, Connections: {designation['connections']}"
#         )  # Debugging statement

#     return designations


# def get_child_count(designation_id):
#     count = frappe.db.count(
#         "Designation", filters={"parent_designation": designation_id}
#     )
#     print(f"Child count for {designation_id}: {count}")  # Debugging statement
#     return count


# ###############################3


import frappe



@frappe.whitelist()
def get_children(parent=None, exclude_node=None, company=None):
    filters = []

    if parent:
        filters.append({"parent_designation": parent})
    else:
        filters.append({"parent_designation": ["in", [None, ""]]})

    if exclude_node:
        filters.append({"name": ["!=", exclude_node]})

    print("Filters used:", filters)  # Debugging statement

    designations = frappe.get_all(
        "Designation",
        fields=[
            "name",
            "name as id",
            "parent_designation as reports_to",
            # "custom_is_group as is_group",
            # "designation_name as title",
        ],
        filters=filters,
        order_by="name",
    )

    print("Designations fetched:", designations)  # Debugging statement

    for designation in designations:
        designation["connections"] = get_child_count(designation["id"])
        designation["expandable"] = designation["connections"] > 0
        print(
            f"Designation: {designation['name']}, Connections: {designation['connections']}"
        )  # Debugging statement

    return designations


def get_child_count(designation_id):
    count = frappe.db.count(
        "Designation", filters={"parent_designation": designation_id}
    )
    print(f"Child count for {designation_id}: {count}")  # Debugging statement
    return count
