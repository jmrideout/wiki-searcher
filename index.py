# Flask application
# June 2, 2021
# Jason Rideout


from flask import Flask, jsonify
import utils


app = Flask(__name__)

@app.route("/", subdomain = "<query>", methods=["GET"])
def index(query):
    print(f"query: " + query)
    try:
        html = utils.get_wiki_page_html(query)
    except utils.RequestsResponseException as rre:
        return rre + "Unable to process request."
    html = utils.remove_footer(html)
    links = utils.extract_links(html)
    return jsonify(utils.package_links(links))

@app.route("/")
def home():
    return "Use the sub-domain to search."


if __name__ == "__main__":
    website_url = "wiki-search.com:5000"
    app.config["SERVER_NAME"] = website_url
    app.run(debug=True)
