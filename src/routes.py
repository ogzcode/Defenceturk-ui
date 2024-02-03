from flask import render_template, request, redirect, url_for
from src import app
from src.parser import Parser, HomePageParser, TopicPageParser, PostPageParser, PaginateParser


@app.route("/")
def home():
    parser = Parser()
    parser.request_to_page("http://www.defenceturk.com/index.php")

    main_page_data = parser.get_home_page_data()

    home_page_parser = HomePageParser(main_page_data)
    data = home_page_parser.parse_table()

    return render_template("home_page.html", data=data)


@app.route("/topic", methods=["GET"])
def topic():

    url_for_parse = request.args.get("url")

    parser = Parser()
    parser.request_to_page(url_for_parse)

    paginate = parser.get_paginate()
    paginate_parser = PaginateParser(paginate)
    paginate_data = paginate_parser.get_parsed_paginate()


    topic_page_data = parser.get_topic_page_data()
    topic_page_parser = TopicPageParser(topic_page_data)
    data = topic_page_parser.parse_table()

    return render_template("topic_page.html", data=data, paginate=paginate_data)


@app.route("/post", methods=["GET"])
def post():
    url_for_parse = request.args.get("url")
    parser = Parser()
    parser.request_to_page(url_for_parse)

    paginate = parser.get_paginate()
    paginate_parser = PaginateParser(paginate)
    paginate_data = paginate_parser.get_parsed_paginate()

    post_page_data = parser.get_post_page_data()

    post_page_parser = PostPageParser(post_page_data)
    data = post_page_parser.get_parsed_post()

    return render_template("post_page.html", data=data, paginate=paginate_data)
