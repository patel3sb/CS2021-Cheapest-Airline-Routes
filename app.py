
# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

#import json module to parse incoming requests to json
import json

#import Dijsktra's algorithm 
from getShortestPath import shortestPath, graph

# Initialize the Flask application
app = Flask(__name__)

# list of cities to display on the form
cityList = ['Addis Ababa', 'Aden', 'Ankara', 'Athens', 'Auckland', 'Bangkok', 'Beijing', 'Berlin', 'Bogota', 'Brisbane', 'Buenos Aires', 'Cairo', 'Cape Town', 'Caracas', 'Chennai', 'Chicago', 'Christchurch', 'Colombo', 'Dakar', 'Dallas', 'Dhaka', 'Dubai', 'Fairbanks', 'Frankfurt', 'Georgetown', 'Hong Kong', 'Houston', 'Irkutsk', 'Jakarta', 'Karachi', 'Kathmandu', 'Kinshasa', 'Kolkata', 'Kuwait', 'Lagos', 'Lahore', 'Leningrad', 'Lima', 'Lisbon', 'London', 'Los Angeles', 'Manila', 'Melbourne', 'Mexico', 'Miami', 'Mombasa', 'Moscow', 'Mumbai', 'Nairobi', 'New Delhi', 'New York', 'Omsk', 'Oslo', 'Ottawa', 'Panama', 'Paris', 'Perm', 'Perth', 'Port Louis', 'Pretoria', 'Quito', 'Rabat', 'Reykjavik', 'Rio de Janeiro', 'Rome', 'San Francisco', 'Santiago', 'Sao Paulo', 'Seoul', 'Shanghai', 'Singapore', 'Stockholm', 'Sydney', 'Tehran', 'Tokyo', 'Vancouver', 'Washington DC', 'Wellington', 'Winnipeg']


# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    # on path "/", render html template to show an input form
    return render_template('form_submit.html', cityList = cityList)

# dictionary with preprocessed values of the respective city's coordinates
cityDict = {'Fairbanks': {'lat': 64.8377778, 'lng': -147.7163888}, 'Winnipeg': {'lat': 49.895136, 'lng': -97.13837439999999}, 'Vancouver': {'lat': 49.2827291, 'lng': -123.1207375}, 'San Francisco': {'lat': 37.7749295, 'lng': -122.4194155}, 'Los Angeles': {'lat': 34.0522342, 'lng': -118.2436849}, 'Ottawa': {'lat': 45.4215296, 'lng': -75.69719309999999}, 'Chicago': {'lat': 41.8781136, 'lng': -87.6297982}, 'Dallas': {'lat': 32.7766642, 'lng': -96.79698789999999}, 'New York': {'lat': 40.7127753, 'lng': -74.0059728}, 'Washington DC': {'lat': 38.9071923, 'lng': -77.0368707}, 'Houston': {'lat': 29.7604267, 'lng': -95.3698028}, 'Miami': {'lat': 25.7616798, 'lng': -80.1917902}, 'Mexico': {'lat': 23.634501, 'lng': -102.552784}, 'Panama': {'lat': 8.537981, 'lng': -80.782127}, 'Bogota': {'lat': 4.710988599999999, 'lng': -74.072092}, 'Caracas': {'lat': 10.4805937, 'lng': -66.90360629999999}, 'Georgetown': {'lat': 38.9097057, 'lng': -77.06535650000001}, 'Quito': {'lat': -0.1806532, 'lng': -78.4678382}, 'Lima': {'lat': -12.0463731, 'lng': -77.042754}, 'Rio de Janeiro': {'lat': -22.9068467, 'lng': -43.1728965}, 'Sao Paulo': {'lat': -23.5505199, 'lng': -46.63330939999999}, 'Buenos Aires': {'lat': -34.6036844, 'lng': -58.3815591}, 'Santiago': {'lat': -33.4488897, 'lng': -70.6692655}, 'Reykjavik': {'lat': 64.12652059999999, 'lng': -21.8174392}, 'Rabat': {'lat': 33.9715904, 'lng': -6.8498129}, 'Dakar': {'lat': 14.716677, 'lng': -17.4676861}, 'Lagos': {'lat': 6.5243793, 'lng': 3.3792057}, 'Cairo': {'lat': 30.0444196, 'lng': 31.2357116}, 'Kinshasa': {'lat': -4.4419311, 'lng': 15.2662931}, 'Pretoria': {'lat': -25.7478676, 'lng': 28.2292712}, 'Cape Town': {'lat': -33.9248685, 'lng': 18.4240553}, 'Addis Ababa': {'lat': 8.9806034, 'lng': 38.7577605}, 'Nairobi': {'lat': -1.2920659, 'lng': 36.8219462}, 'Mombasa': {'lat': -4.0434771, 'lng': 39.6682065}, 'Port Louis': {'lat': -20.1608912, 'lng': 57.5012222}, 'Tehran': {'lat': 35.6891975, 'lng': 51.3889736}, 'Kuwait': {'lat': 29.31166, 'lng': 47.481766}, 'Dubai': {'lat': 25.2048493, 'lng': 55.2707828}, 'Karachi': {'lat': 25.0700428, 'lng': 67.2847875}, 'Aden': {'lat': 12.7854969, 'lng': 45.0186548}, 'Lahore': {'lat': 31.5203696, 'lng': 74.35874729999999}, 'Mumbai': {'lat': 19.0759837, 'lng': 72.8776559}, 'New Delhi': {'lat': 28.6139391, 'lng': 77.2090212}, 'Kathmandu': {'lat': 27.7172453, 'lng': 85.3239605}, 'Dhaka': {'lat': 23.810332, 'lng': 90.4125181}, 'Chennai': {'lat': 13.0826802, 'lng': 80.2707184}, 'Colombo': {'lat': 6.9270786, 'lng': 79.861243}, 'Kolkata': {'lat': 22.572646, 'lng': 88.36389500000001}, 'Omsk': {'lat': 54.9884804, 'lng': 73.3242361}, 'Irkutsk': {'lat': 52.28697409999999, 'lng': 104.3050183}, 'Beijing': {'lat': 39.90419989999999, 'lng': 116.4073963}, 'Shanghai': {'lat': 31.2303904, 'lng': 121.4737021}, 'Hong Kong': {'lat': 22.396428, 'lng': 114.109497}, 'Bangkok': {'lat': 13.7563309, 'lng': 100.5017651}, 'Singapore': {'lat': 1.352083, 'lng': 103.819836}, 'Jakarta': {'lat': -6.17511, 'lng': 106.8650395}, 'Manila': {'lat': 14.5995124, 'lng': 120.9842195}, 'Tokyo': {'lat': 35.6894875, 'lng': 139.6917064}, 'Seoul': {'lat': 37.566535, 'lng': 126.9779692}, 'Perth': {'lat': -31.9505269, 'lng': 115.8604572}, 'Brisbane': {'lat': -27.4697707, 'lng': 153.0251235}, 'Melbourne': {'lat': -37.8136276, 'lng': 144.9630576}, 'Sydney': {'lat': -33.8688197, 'lng': 151.2092955}, 'Auckland': {'lat': -36.8484597, 'lng': 174.7633315}, 'Wellington': {'lat': -41.2864603, 'lng': 174.776236}, 'Christchurch': {'lat': -43.5320544, 'lng': 172.6362254}, 'London': {'lat': 51.5073509, 'lng': -0.1277583}, 'Lisbon': {'lat': 38.7222524, 'lng': -9.1393366}, 'Paris': {'lat': 48.856614, 'lng': 2.3522219}, 'Berlin': {'lat': 52.52000659999999, 'lng': 13.404954}, 'Frankfurt': {'lat': 50.1109221, 'lng': 8.6821267}, 'Rome': {'lat': 41.9027835, 'lng': 12.4963655}, 'Athens': {'lat': 37.9838096, 'lng': 23.7275388}, 'Oslo': {'lat': 59.9138688, 'lng': 10.7522454}, 'Stockholm': {'lat': 59.32932349999999, 'lng': 18.0685808}, 'Leningrad': {'lat': 59.9342802, 'lng': 30.3350986}, 'Moscow': {'lat': 55.755826, 'lng': 37.6172999}, 'Perm': {'lat': 58.02968129999999, 'lng': 56.2667916}, 'Ankara': {'lat': 39.9333635, 'lng': 32.8597419}}

# pick coordinates and add them to the shortest path cities
def initializeCityList(shortestPathList):
  shortestPathDict = []

  #recreating a dict with only coordinates for shortest path values
  for city in shortestPathList:
    cityDict[city]["name"] = city
    shortestPathDict.append(cityDict[city])

  return shortestPathDict

# define route for /get_route url that is called when POST request is invoked
@app.route('/get_route/', methods=['POST'])
def get_route():

    #get data from the submitted form
    start = request.form['start']
    end = request.form['end'];
    if start != end:
      res = shortestPath(graph, start, end)
    
      # return template to show results
      #pass on variables to template to show to user
      return render_template('form_action.html', shortestPath= initializeCityList(res[1]), totalCost = res[0])
    return render_template('error.html')  
# Run the app on port 5000 
if __name__ == '__main__':
  app.run(
        host="localhost",
        port=int("5000")
  )
