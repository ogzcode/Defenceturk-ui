from flask import render_template, request
from src import app
from src.parser import Parser, HomePageParser, TopicPageParser, PostPageParser, PaginateParser, NavigateParser

def get_navigate_data(parser):
    navigate_breadcrumb = parser.get_navigate_breadcrumb()
    navigate_parser = NavigateParser(navigate_breadcrumb)
    return navigate_parser.parse_navigate()

def get_paginate_data(parser):
    paginate = parser.get_paginate()
    paginate_parser = PaginateParser(paginate)
    return paginate_parser.get_parsed_paginate()


@app.route("/")
def home():
    parser = Parser()
    parser.request_to_page("http://www.defenceturk.com/index.php")

    navigate_data = get_navigate_data(parser)

    main_page_data = parser.get_home_page_data()

    home_page_parser = HomePageParser(main_page_data)
    data = home_page_parser.parse_table()

    return render_template("home_page.html", data=data, breadcrumb=navigate_data)


@app.route("/topic", methods=["GET"])
def topic():

    url_for_parse = request.args.get("url")

    parser = Parser()
    parser.request_to_page(url_for_parse)

    navigate_data = get_navigate_data(parser)
    paginate_data = get_paginate_data(parser)

    topic_page_data = parser.get_topic_page_data()
    topic_page_parser = TopicPageParser(topic_page_data)
    data = topic_page_parser.parse_table()

    return render_template("topic_page.html", data=data, paginate=paginate_data, breadcrumb=navigate_data)


@app.route("/post", methods=["GET"])
def post():
    url_for_parse = request.args.get("url")
    parser = Parser()
    parser.request_to_page(url_for_parse)

    navigate_data = get_navigate_data(parser)
    paginate_data = get_paginate_data(parser)

    post_page_data = parser.get_post_page_data()

    post_page_parser = PostPageParser(post_page_data)
    data = post_page_parser.get_parsed_post()

    return render_template("post_page.html", data=data, paginate=paginate_data, breadcrumb=navigate_data)

@app.route("/about")
def about():
    return render_template("about.html")
