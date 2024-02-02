from flask import render_template
from src import app
from src.parser import Parser, HomePageParser


@app.route("/")
def home():
    parser = Parser()
    parser.request_to_page("http://www.defenceturk.com/index.php")

    main_page_data = parser.get_home_page_data()

    home_page_parser = HomePageParser(main_page_data)
    data = home_page_parser.parse_table()

    return render_template("home_page.html", data=data)

