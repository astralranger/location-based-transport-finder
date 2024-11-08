pip install overpy
pip install polyline
pip install geopy

import overpy
import pandas as pd
import json
import requests
from geopy.geocoders import Nominatim
import requests
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
import folium
import polyline


address = input("Enter your address") #input is needed for locality, address of buildings will give error
dest = input("enter your destination")
geolocator = Nominatim(user_agent= "address_geocoder") #Using the geopy liblaries function Nominatim to fetch the latitude and longitude from user location and destination
location = geolocator.geocode(address) #user source loaction
destloc = geolocator.geocode(dest) #user destination loaction
latitude_user = location.latitude
longitude_user = location.longitude
latitude_dest = destloc.latitude
longitude_dest = destloc.longitude
print(latitude_user,longitude_user)
print(latitude_dest,longitude_dest)


# Function to store the latitudes and longitudes user's input of source and destination locations
def get_input(): #this function will pe passed as an agrument as user_input while building queries to fetch the datasets.
    latitude = str(latitude_user) #converting(typecasting) the latitudes fetched to string
    longitude = str(longitude_user)
    print("\nEnter scan radius for target. (in meters) (EXAMPLE->'20000') >> ")
    search_radius = input()
    return [latitude, longitude, search_radius]


# Function to build Overpass QL query for metro stations
def get_metro_query(user_input):
    prefix = """[out:json][timeout:50];
(node["railway"="station"](around:"""
    suffix = """););out;
"""
    q = user_input[2] + ',' + user_input[0] + ',' + user_input[1]
    built_query = prefix + q + suffix
    return built_query


# Function to build Overpass QL query for taxi stands
def get_taxi_query(user_input):
    prefix = """[out:json][timeout:50];
(node["amenity"="taxi"](around:"""
    suffix = """););out;
"""
    q = user_input[2] + ',' + user_input[0] + ',' + user_input[1]
    built_query = prefix + q + suffix
    return built_query


# Function to build Overpass QL query for bus stops
def get_bus_query(user_input):
    prefix = """[out:json][timeout:50];
(node["highway"="bus_stop"](around:"""
    suffix = """););out;
"""
    q = user_input[2] + ',' + user_input[0] + ',' + user_input[1]
    built_query = prefix + q + suffix
    return built_query


# Function to extract data from Overpass API response and save as CSV
def extract_nodes_data_from_OSM(built_query, filename):
    api = overpy.Overpass()
    result = api.query(built_query)
    list_of_node_tags = []
    for node in result.nodes:
        node.tags['latitude'] = node.lat
        node.tags['longitude'] = node.lon
        node.tags['id'] = node.id
        list_of_node_tags.append(node.tags)
    data_frame = pd.DataFrame(list_of_node_tags)
    data_frame.to_csv(filename)
    print(f"\nCSV file created: '{filename}'. Check the file in the current directory.")
    return data_frame


# Function to extract raw JSON data from Overpass API response and save as JSON file
def extract_raw_data_from_OSM(built_query, filename):
    overpass_url = "http://overpass-api.de/api/interpreter"
    response = requests.get(overpass_url, params={'data': built_query})
    json_data = response.json()
    with open(filename, "w") as outfile:
        json.dump(json_data, outfile)
    print(f"Raw data extraction successful! Check '{filename}' file.")
    return json_data

# Plot the dataset points and user input location
def plot_data(user_lat, user_lon, transport_data):
    plt.figure(figsize=(8, 6))
    for label, coordinates_list in transport_data.items():
        coords = np.array(coordinates_list)
        plt.scatter(coords[:, 1], coords[:, 0], label=label)

    plt.scatter(user_lon, user_lat, color='red', label='User Input')
    plt.title("Transportation Mode Prediction")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to execute the program
def main():
    user_input = get_input()

    # Metro data
    metro_query = get_metro_query(user_input)
    extract_nodes_data_from_OSM(metro_query, 'metro_stations.csv')
    extract_raw_data_from_OSM(metro_query, 'metro_stations.json')

    # Taxi data
    taxi_query = get_taxi_query(user_input)
    extract_nodes_data_from_OSM(taxi_query, 'taxi_stands.csv')
    extract_raw_data_from_OSM(taxi_query, 'taxi_stands.json')

    # Bus data
    bus_query = get_bus_query(user_input)
    extract_nodes_data_from_OSM(bus_query, 'bus_stops.csv')
    extract_raw_data_from_OSM(bus_query, 'bus_stops.json')


if __name__ == "__main__":
    main()



import matplotlib.pyplot as plt
# Read metro data from CSV
metro_df = pd.read_csv("/content/metro_stations.csv")
metro_data = metro_df[['latitude', 'longitude']].values.tolist()

# Read bus data from CSV
bus_df = pd.read_csv("/content/bus_stops.csv")
bus_data = bus_df[['latitude', 'longitude']].values.tolist()

# Read taxi data from CSV
taxi_df = pd.read_csv("/content/taxi_stands.csv")
taxi_data = taxi_df[['latitude', 'longitude']].values.tolist()

# Combine all transport data into a single dictionary
transport_data = {
    "Metro": metro_data,
    "Bus": bus_data,
    "Taxi": taxi_data
}

# Convert dataset to feature and label arrays
X = []
y = []
for label, coordinates_list in transport_data.items():
    for coord in coordinates_list:
        X.append(coord)
        y.append(label)

X = np.array(X)
y = np.array(y)

# Encode labels so that the non numeric values if any may be converted to numeric ones,
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train K-Nearest Neighbors classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Function to get route coordinates using GraphHopper Routing API
def get_route_coordinates(user_lat, user_lon, destination_lat, destination_lon):
    try:
        # initializing the GraphHopper api key
        api_key = "52f24a7e-ab3a-4cc3-b6f8-f9dcfaff296a"
        url = f"https://graphhopper.com/api/1/route?point={user_lat},{user_lon}&point={destination_lat},{destination_lon}&vehicle=car&key={api_key}"

        # Send GET(request for any data source) request to GraphHopper Routing API
        response = requests.get(url)
        data = response.json()

        # Extract the polyline from the response
        polyline_points = data['paths'][0]['points']

        # Decode the polyline to get the route coordinates
        route_coordinates = polyline.decode(polyline_points)

        return route_coordinates
    except Exception as e:
        print("Error retrieving route coordinates:", e)
        return None

# User input for current location
try:
    user_lat = float(latitude_user)
    user_lon = float(longitude_user)

    # Predict transportation mode
    prediction = knn.predict([[user_lat, user_lon]])
    predicted_transport = label_encoder.inverse_transform(prediction)

    # Find the nearest transport location for the predicted mode this is done by calculating the euclidean dist
    nearest_location = min(transport_data[predicted_transport[0]], key=lambda x: np.linalg.norm(np.array(x) - np.array([user_lat, user_lon])))

    # Get route coordinates
    route_coordinates = get_route_coordinates(user_lat, user_lon, nearest_location[0], nearest_location[1])

    if route_coordinates:
        # Create a map centered at the user's input location
        mymap = folium.Map(location=[user_lat, user_lon], zoom_start=12)

        # Define marker colors for each transportation mode
        marker_colors = {
            "Metro": "blue",
            "Bus": "green",
            "Taxi": "red"
        }

        # Add markers for the dataset points with different colors for each transportation mode
        for label, coordinates_list in transport_data.items():
            for coord in coordinates_list:
                folium.Marker(location=coord, popup=label, icon=folium.Icon(color=marker_colors[label])).add_to(mymap)

        # Add a marker for the user's input location
        folium.Marker(location=[user_lat, user_lon], popup="Your Location", icon=folium.Icon(color='red')).add_to(mymap)

        # Add the route to the map
        if route_coordinates:
            folium.PolyLine(route_coordinates, color="blue", weight=2.5, opacity=1).add_to(mymap)

        # Add popup for predicted transport mode and destination
        folium.Marker(location=nearest_location, popup=f"Predicted Transport: {predicted_transport[0]}").add_to(mymap)

        # Save the map as an HTML file
        mymap.save("transportation_map.html")

        print("Based on your location, the predicted transportation mode is:", predicted_transport[0])
    else:
        print("Failed to retrieve route coordinates. Please check your input coordinates and try again.")
except ValueError as ve:
    print("Invalid latitude or longitude value. Latitude values should be in the range [-90, 90] and longitude values should be in the range [-180, 180].")
transport_data = {
        "Metro": pd.read_csv("/content/metro_stations.csv")[['latitude', 'longitude']].values.tolist(),
        "Bus": pd.read_csv("/content/bus_stops.csv")[['latitude', 'longitude']].values.tolist(),
        "Taxi": pd.read_csv("/content/taxi_stands.csv")[['latitude', 'longitude']].values.tolist()
    }
plot_data(latitude_user, longitude_user, transport_data)
