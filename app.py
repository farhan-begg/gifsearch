from flask import Flask, render_template, request
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()


TENOR_API_KEY = os.getenv("TENOR_API_KEY")


app = Flask(__name__)

# route the function
@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get("search_gif")
    payload = {
        "q": query,
        "key": "3OGJ9M5CUDUK",
        "limit" : "10"
    }
    data = None
#     # sets the apikey and limit

# request GET api, receive api, returns searched gifs
    r = requests.get("https://api.tenor.com/v1/search", params=payload)
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        data = r.json()
        data = data["results"]
    else:
        data = None
    return render_template("index.html", data=data)


    # get the top 10 GIFs for the search term
    # links to terminal
if __name__ == '__main__':
    app.run(debug=True)
