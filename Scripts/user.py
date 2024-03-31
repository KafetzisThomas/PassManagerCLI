
class User:

    def __init__(self, master_username, master_password):
        self.master_username = master_username
        self.master_password = master_password

    def check_input(self):
        if self.master_username != '' and self.master_password != '':
            return True
        else:
            return False

class Item:

    def __init__(self, name, date_posted, website, username, password, notes):
        self.name = name
        self.date_posted = date_posted
        self.website = website
        self.username = username
        self.password = password
        self.notes = notes
