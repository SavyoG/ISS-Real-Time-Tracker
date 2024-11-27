import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder  # type: ignore

# Write astronaut data to file
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

with open("iss.txt", "w") as file:
    file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")
    for person in result["people"]:
        file.write(person["name"] + " - on board\n")
    
    # Get user's latitude and longitude
    g = geocoder.ip("me")
    file.write("\nYour current latitude/longitude is: " + str(g.latlng))

webbrowser.open("iss.txt")

# Set up the world map in turtle
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load map and ISS images
screen.bgpic("C:/Users/glyan/OneDrive/Documents/Space Projects/ISS Tracking Project/map.gif")
screen.register_shape("C:/Users/glyan/OneDrive/Documents/Space Projects/ISS Tracking Project/iss.gif")

iss = turtle.Turtle()
iss.shape("C:/Users/glyan/OneDrive/Documents/Space Projects/ISS Tracking Project/iss.gif")
iss.setheading(45)
iss.penup()  # Corrected method call

# Function to fetch ISS location
def fetch_iss_location():
    try:
        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url, timeout=5)
        result = json.loads(response.read())
        location = result["iss_position"]
        lat = float(location["latitude"])
        lon = float(location["longitude"])
        return lat, lon
    except Exception as e:
        print(f"Error fetching ISS location: {e}")
        return None, None

# Continuously update ISS location
try:
    while True:
        lat, lon = fetch_iss_location()
        if lat is not None and lon is not None:
            print(f"\nLatitude: {lat}")
            print(f"Longitude: {lon}")

            # Update the ISS location on the map
            iss.goto(lon, lat)

        # Refresh every 5 seconds
        time.sleep(5)

except turtle.Terminator:
    print("Turtle graphics closed.")
except KeyboardInterrupt:
    print("Program stopped by user.")
