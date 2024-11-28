Features
🧑‍🚀 Astronaut Information: Retrieves and displays a list of astronauts currently aboard the ISS.
🌎 Real-Time ISS Location: Fetches the live location (latitude and longitude) of the ISS using the Open Notify API.
🗺️ World Map Visualization: Shows the ISS's position on a world map using Python’s Turtle graphics.
📍 User Geolocation: Detects and displays the user's current latitude and longitude.
🔄 Continuous Updates: Automatically updates the ISS position in real-time, refreshing every second.
📂 File Output: Saves astronaut information and user geolocation data into a text file for reference.
How It Works
Astronaut Information:

The astros.json API provides the number of astronauts and their names.
The data is saved to a file (iss.txt) and opened automatically.
ISS Location Tracking:

The iss-now.json API provides the live coordinates of the ISS.
The location is updated on the map using the Turtle library.
Geolocation:

The script uses geocoder to fetch the user's approximate location based on their IP address.
World Map Display:

A custom world map image is used as the background for the Turtle graphics window.
The ISS is represented as a custom icon (iss.gif), dynamically moving across the map.
