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
        return self.data.find(id="messageindex")
    
    def get_message_page_data(self):
        return self.data.find(id="forumposts")


