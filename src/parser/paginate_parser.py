class PaginateParser:
    def __init__(self, data):
        self.soup = data
        self.parsed_data = None

    def parse_paginate(self):
        data = []
        paginate = self.soup.find(class_="pagelinks")

        active_page = paginate.find("strong").text

        data.append({
            "text": int(active_page),
            "href": "",
            "active": True
        })

        for page in paginate.find_all("a", class_="navPages"):
            data.append({
                "text": int(page.text),
                "href": page["href"],
                "active": False
            })

        data.sort(key=lambda x: x["text"])

        self.parsed_data = data

    def get_parsed_paginate(self):
        self.parse_paginate()
        return self.parsed_data
    
        