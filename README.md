# Smart Transport Mode Predictor

Welcome to the **Smart Transport Mode Predictor** project! This Python-based tool helps users find the best transportation mode (metro, bus, or taxi) based on their current location and a destination.

## Project Overview

The Smart Transport Mode Predictor provides transportation recommendations using geolocation data and machine learning. The system predicts the best transportation mode based on your location and destination and visualizes the route on a map.

## Features

- Geolocation-based transportation prediction (Metro, Bus, Taxi).
- Route planning with GraphHopper's routing API.
- Data visualization using **Folium** for interactive maps.
- Machine learning model using K-Nearest Neighbors for transportation mode classification.

## Setup and Installation

To get started, you will need to install the required libraries. You can do this using the following pip commands:

pip install overpy
pip install polyline
pip install geopy
pip install folium
pip install scikit-learn

## How to Use

1. **Clone the repository:**

    ```bash
    git clone https://github.com/astralranger/location-based-transport-finder
    ```

2. Install the required dependencies (as shown above).

3. Run the Python script `smart_transport_finder.py`.

4. Input your location and destination when prompted.

5. The system will predict the best transportation mode and show you the route on an interactive map.

## Data Sources

- **Overpass API**: Used for fetching transportation data (metro stations, bus stops, and taxi stands).
- **GraphHopper Routing API**: Provides route coordinates for the predicted transportation mode.

## How It Works

The program first uses the **geopy** library to fetch the latitude and longitude of the user's location and destination. It then builds queries to fetch transportation data (e.g., metro stations, taxi stands, bus stops) using the **Overpass API**.

Once transportation data is gathered, a machine learning model (K-Nearest Neighbors) is used to predict the best transportation mode based on the user's location. The best route is then fetched using the **GraphHopper API** and displayed on an interactive map using **Folium**.

## Project Structure

- `smart_transport_finder.py` - Main script that executes the program.
- `metro_stations.csv` - Stores metro station data fetched from Overpass API.
- `bus_stops.csv` - Stores bus stop data fetched from Overpass API.
- `taxi_stands.csv` - Stores taxi stand data fetched from Overpass API.
- `transportation_map.html` - Map displaying the route and transportation mode.

