class HomePageParser:
    def __init__(self, data):
        self.soup = data
        self.parsed_data = None

    def parse_table_header(self):
        data = []
        for tbody in self.soup.find_all("tbody"):
            if tbody.get("class") == ["header"]:
                data.append({
                    "type": "header",
                    "title": tbody.find("tr").find("td").find("div").find("h3").text.strip(),
                    "content": []
                })

        self.parsed_data = data.copy()

    def parse_table_content(self):
        for tbody_index, tbody in enumerate(self.soup.find_all("tbody", class_="content")):
            for tr in tbody.find_all("tr"):
                info_tag = tr.find("td", class_="info")
                stats_tag = tr.find("td", class_="stats")

                info_data = self.parse_info_data(info_tag)
                stats_data = self.parse_stats_data(stats_tag)

                self.parsed_data[tbody_index]["content"].append({
                    "info": info_data,
                    "stats": stats_data,
                })

    def parse_info_data(self, link_tag):
        if not link_tag:
            return None

        return {
            "link_content": link_tag.find("a").text.strip(),
            "link_href": link_tag.find("a").get("href"),
            "description": link_tag.find("p").text.strip(),
        }

    def parse_stats_data(self, stats_tag):
        if not stats_tag:
            return None

        text_list = stats_tag.find("p").text.strip().replace(
            "\n", "").replace("\t", "").split(" ")

        return {
            "post_count": text_list[0] + " " + text_list[1],
            "topic_count": text_list[2] + " " + text_list[3],
        }
        

    def parse_table(self):
        self.parse_table_header()
        self.parse_table_content()

        return self.parsed_data
