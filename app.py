from flask import Flask, render_template, redirect, request, url_for
from search_city_weather import get_city_weather
app = Flask(__name__)


@app.route('/')
def index():
    default_city = get_city_weather("北京")
    return render_template('index.html', c=default_city["city_info"], td=default_city["today"],
                           five_day=[default_city["yesterday"], default_city["today"], default_city["tomorrow"],
                                     default_city["ht"], default_city["dht"], default_city["ddht"]])


@app.route('/search', methods=["POST"])
def search():
    # city_name = request.form["city_name"]
    city_weather = get_city_weather(request.form["city_name"])
    if type(city_weather) == str:
        return f"{city_weather}"
    elif type(city_weather) == dict:
        return render_template("index.html", c=city_weather["city_info"], td=city_weather["today"],
                               five_day=[city_weather["yesterday"], city_weather["today"],city_weather["tomorrow"],
                                         city_weather["ht"],city_weather["dht"], city_weather["ddht"]])



if __name__ == '__main__':
    app.run()
