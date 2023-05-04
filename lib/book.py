#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print('Flipping the page...wow, you read fast!')
    
    def get_count(self):
        return self._page_count # create a private parameter
    
    def set_count(self, value):
        if type(value) == int:
            self._page_count = value # create a private parameter
        
        print("page_count must be an integer")
    page_count = property(get_count, set_count) # property()
