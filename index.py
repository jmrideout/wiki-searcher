from flask import Flask
import utils


app = Flask(__name__)

@app.route("/", subdomain = "<query>", methods=["GET"])
def index(query):
    print(f"query: " + query)
    html = utils.get_wiki_page(query)
    modified_html = utils.remove_footer(html)
    links = utils.extract_links(modified_html)
    output = utils.package_links(links)
    return output


if __name__ == "__main__":
    website_url = "wiki-search.com:5000"
    app.config["SERVER_NAME"] = website_url
    app.run()
