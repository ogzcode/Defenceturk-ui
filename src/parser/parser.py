from bs4 import BeautifulSoup
import requests

class Parser:
    def __init__(self):
        self.data = None
        self.res = None
        self.soup = None

    def request_to_page(self, url):
        self.res = requests.get(url)
        self.soup = BeautifulSoup(self.res.content, "html.parser")
        self.data = self.soup.find(id="glavni_okvir").find(id="wrapper").find(id="content_section").find(
            class_="frame").find(id="main_content_section")
        
    def get_home_page_data(self):
        return self.data.find(id="boardindex_table").find(class_="table_list")
    
    def get_topic_page_data(self):
        return self.data.find(id="messageindex").find(class_="table_grid")
    
    def get_paginate(self):
        return self.data.find(class_="pagesection")
    
    def get_post_page_data(self):
        return self.data.find(id="forumposts").find(id="quickModForm")
    
    def get_navigate_breadcrumb(self):
        return self.data.find(class_="navigate_section")


