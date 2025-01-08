import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "contacts.html")
contacts_html = os.path.abspath(rel_file_path)
