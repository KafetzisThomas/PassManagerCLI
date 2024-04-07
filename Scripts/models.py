#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class User:
    """Represent a user with a master username and password"""

    def __init__(self, master_username, master_password):
        self.master_username = master_username
        self.master_password = master_password


class Item:
    """Represent an item with a name, date posted, website, username, password, and notes"""

    def __init__(self, name, date_posted, website, username, password, notes):
        self.name = name
        self.date_posted = date_posted
        self.website = website
        self.username = username
        self.password = password
        self.notes = notes
