class TopicPageParser:
    def __init__(self, data):
        self.soup = data
        self.parsed_data = None

    def parse_table_body(self):
        data = []
        table_body = self.soup.find("tbody")

        table_body.find(class_="whos_viewing").decompose()

        for tr in table_body.find_all("tr"):
            subject = self.parse_subject(tr.find("td", class_="subject"))
            stats = self.parse_stats(tr.find("td", class_="stats"))
            last = self.parse_last(tr.find("td", class_="lastpost"))
            
            data.append({
                "subject": subject,
                "stats": stats,
                "last": last
            })
            
        self.parsed_data = data.copy()

    def parse_subject(self, td):
        if not td:
            return None
        
        parsed = None

        if td.find("div").find("strong"):
            parsed = td.find("div").find("strong").find("span").find("a")
        else:
            parsed = td.find("div").find("span").find("a")

        return {
            "title": parsed.text.strip(),
            "href": parsed.get("href")
        }
    
    def parse_stats(self, td):
        text = td.text.strip().replace("\n", " ").replace("\t", "").split("  ")
        return {
            "replies": text[0].split(" ")[0],
            "views": text[1].split(" ")[0]
        }
    
    def parse_last(self, td):
        for a in td.find_all("a"):
            a.decompose()
        
        text = td.text.strip().replace("\n", " ").replace("\t", "").split(",")

        return {
            "last_post": text[0],
        }

    def parse_table(self):
        self.parse_table_body()

        return self.parsed_data
