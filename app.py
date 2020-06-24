from flask import Flask, render_template, redirect
import scrape

# Create an instance of Flask
app = Flask(__name__)

engine = create_engine("postgresql://postgres:group5@35.226.24.243:5432/postgres")
conn = engine.connect()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    destination_data = engine(conn)
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    costa_weather = mongo.costa_db.costa_weather
    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!
    costa_data = scrape_costa.scrape_info()

    #Deactivate old data
    costa_weather.update_many(
        {'active': 1},
        {"$set":  {"active" : 0}
        }
    )

    # Update the Mongo database using update and upsert=True
    # @TODO: YOUR CODE HERE!
    #costa_weather.update({}, costa_data, upsert=True)
    costa_weather.insert_one(costa_data)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

