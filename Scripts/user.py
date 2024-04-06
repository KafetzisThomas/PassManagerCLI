#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class User:
    def __init__(self, master_username, master_password):
        self.master_username = master_username
        self.master_password = master_password

class Item:
    def __init__(self, name, date_posted, website, username, password, notes):
        self.name = name
        self.date_posted = date_posted
        self.website = website
        self.username = username
        self.password = password
        self.notes = notes
