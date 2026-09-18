import requests
import streamlit as st

st.set_page_config(
    page_title="Weather App",
    layout="centered"
)

st.title("Weather App")

city = st.text_input("Enter city name")

if st.button("Get Weather"):

    if not city.strip():
        st.warning("Please enter a city name.")
        st.stop()

    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

    geocode_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    try:
        location_response = requests.get(
            geocode_url,
            params=geocode_params,
            timeout=10
        )

        location_response.raise_for_status()

        location_data = location_response.json()

        if "results" not in location_data:
            st.error("City not found.")
            st.stop()

        location = location_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "")

        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "wind_speed_10m"
            ],
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()
        current = weather_data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        feels_like = current["apparent_temperature"]
        wind_speed = current["wind_speed_10m"]

        st.success("Weather found")

        st.write("City:", city_name)
        st.write("Country:", country)
        st.write("Temperature:", temperature, "°C")
        st.write("Humidity:", humidity, "%")
        st.write("Feels Like:", feels_like, "°C")
        st.write("Wind Speed:", wind_speed, "km/h")

    except requests.exceptions.RequestException:
        st.error("Unable to connect to the weather API.")

    except Exception as e:
        st.error("Error:", e)