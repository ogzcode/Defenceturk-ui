class PostPageParser:
    def __init__(self, data):
        self.soup = data
        self.parsed_data = None

    def parse_post(self):
        data = []

        for div in self.soup.find_all("div", class_=["windowbg2", "windowbg"]):
            post_author = self.parse_post_author(
                div.find(class_="post_wrapper").find(class_="poster"))
            
            post_date = self.parse_post_date(
                div.find(class_="post_wrapper").find(class_="postarea"))
            
            post_content = self.parse_post_content(
                div.find(class_="post_wrapper").find(class_="postarea"))
            

            data.append({
                "author": post_author,
                "date": post_date,
                "content": post_content
            })
        
        self.parsed_data = data

    def parse_post_author(self, poster):
        data = poster.find("h4").find("a").text

        return data

    def parse_post_date(self, date_tag):
        data = date_tag.find(class_="flow_hidden").find(
            class_="keyinfo").find(class_="smalltext").text
        
        #«  : 20 Ağustos 2009, 13:06:56 »
        #« Yanıtla #1 : 20 Ağustos 2009, 13:44:13 »
        text = data.split(",")[0].split(":")[1]

        return text
    
    def parse_post_content(self, content):
        data = content.find(class_="post").find(class_="inner")

        if data.find_all("img", class_="smiley"):
            for img in data.find_all("img", class_="smiley"):
                img.decompose()

        return data

    def get_parsed_post(self):
        self.parse_post()
        return self.parsed_data