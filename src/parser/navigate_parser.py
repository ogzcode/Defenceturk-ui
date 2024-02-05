class NavigateParser:
    def __init__(self, data):
        self.soup = data
        self.parsed_data = None

    def get_navigate_breadcrumb(self):
        nav = self.soup.find("ul")
        data = []

        for li in nav.find_all("li"):
            link = li.find("a")

            if link:
                data.append({
                        "title": link.text,
                        "href": link.get("href")
                    })
            
        
        self.parsed_data = data

    def parse_navigate(self):
        self.get_navigate_breadcrumb()
        return self.parsed_data