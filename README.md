<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Smart Transport Mode Predictor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 0;
        }
        h1 {
            color: #2c3e50;
        }
        h2 {
            color: #34495e;
        }
        p {
            font-size: 1.1em;
            color: #7f8c8d;
        }
        code {
            background-color: #ecf0f1;
            padding: 5px 10px;
            font-family: Courier, monospace;
        }
        .code-block {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            font-family: Courier, monospace;
            overflow: auto;
        }
        ul {
            margin-left: 20px;
        }
        .highlight {
            color: #e74c3c;
        }
    </style>
</head>
<body>

    <h1>Smart Transport Mode Predictor</h1>

    <p>Welcome to the <strong>Smart Transport Mode Predictor</strong> project! This Python-based tool helps users find the best transportation mode (metro, bus, or taxi) based on their current location and a destination.</p>

    <h2>Project Overview</h2>
    <p>The Smart Transport Mode Predictor provides transportation recommendations using geolocation data and machine learning. The system predicts the best transportation mode based on your location and destination and visualizes the route on a map.</p>

    <h2>Features</h2>
    <ul>
        <li>Geolocation-based transportation prediction (Metro, Bus, Taxi).</li>
        <li>Route planning with GraphHopper's routing API.</li>
        <li>Data visualization using <strong>Folium</strong> for interactive maps.</li>
        <li>Machine learning model using K-Nearest Neighbors for transportation mode classification.</li>
    </ul>

    <h2>Setup and Installation</h2>
    <p>To get started, you will need to install the required libraries. You can do this using the following pip commands:</p>
    
    <div class="code-block">
        <code>pip install overpy</code><br>
        <code>pip install polyline</code><br>
        <code>pip install geopy</code><br>
        <code>pip install folium</code><br>
        <code>pip install scikit-learn</code><br>
    </div>

    <h2>How to Use</h2>
    <ol>
        <li>Clone the repository: <code>git clone <a href="https://github.com/yourusername/smart-transport-mode-predictor">https://github.com/yourusername/smart-transport-mode-predictor</a></code></li>
        <li>Install the required dependencies (as shown above).</li>
        <li>Run the Python script <code>smart_transport_finder.py</code>.</li>
        <li>Input your location and destination when prompted.</li>
        <li>The system will predict the best transportation mode and show you the route on an interactive map.</li>
    </ol>

    <h2>Data Sources</h2>
    <ul>
        <li><strong>Overpass API</strong>: Used for fetching transportation data (metro stations, bus stops, and taxi stands).</li>
        <li><strong>GraphHopper Routing API</strong>: Provides route coordinates for the predicted transportation mode.</li>
    </ul>

    <h2>How It Works</h2>
    <p>The program first uses the <strong>geopy</strong> library to fetch the latitude and longitude of the user's location and destination. It then builds queries to fetch transportation data (e.g., metro stations, taxi stands, bus stops) using the <strong>Overpass API</strong>.</p>
    <p>Once transportation data is gathered, a machine learning model (K-Nearest Neighbors) is used to predict the best transportation mode based on the user's location. The best route is then fetched using the <strong>GraphHopper API</strong> and displayed on an interactive map using <strong>Folium</strong>.</p>

    <h2>Project Structure</h2>
    <ul>
        <li><strong>smart_transport_finder.py</strong> - Main script that executes the program.</li>
        <li><strong>metro_stations.csv</strong> - Stores metro station data fetched from Overpass API.</li>
        <li><strong>bus_stops.csv</strong> - Stores bus stop data fetched from Overpass API.</li>
        <li><strong>taxi_stands.csv</strong> - Stores taxi stand data fetched from Overpass API.</li>
        <li><strong>transportation_map.html</strong> - Map displaying the route and transportation mode.</li>
    </ul>

    <h2>Future Improvements</h2>
    <ul>
        <li>Enhance the machine learning model for better accuracy.</li>
        <li>Include more transportation modes (e.g., bicycles, ride-sharing).</li>
        <li>Integrate real-time traffic data for better route optimization.</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the <span class="highlight">MIT License</span> - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
