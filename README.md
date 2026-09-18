## Overview

Weather AI Assistant is a Streamlit-based application that provides current weather information for a selected city and generates an AI-based weather explanation using Hugging Face.

The project combines a weather API, Python, Streamlit, and Hugging Face to create a simple AI-powered weather application.

## Features

* Enter a city name
* Get current temperature
* Display humidity
* Display feels-like temperature
* Display wind speed
* Generate an AI-based weather explanation
* Simple Streamlit user interface
* Hugging Face access token integration

## Technologies Used

* Python
* Streamlit
* Open-Meteo Weather API
* Hugging Face
* OpenAI Python SDK
* Requests
* Python-dotenv

## Project Structure

```text
weather_ai/
│
├── app.py
├── test_token.py
├── requirements.txt
├── .env
└── venv/
```

## Working Process

```text
User enters city
        |
        v
Geocoding API
        |
        v
Latitude and Longitude
        |
        v
Weather API
        |
        v
Current Weather Data
        |
        v
Hugging Face AI Model
        |
        v
AI Weather Explanation
        |
        v
Streamlit Interface
```

## Installation

Create a virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

## Hugging Face Token Setup

Create a Hugging Face access token and add it to the `.env` file.

```text
HF_TOKEN=your_huggingface_token
```

The token is loaded in Python using `python-dotenv`.

## Run the Application

Run the following command:

```powershell
python -m streamlit run app.py
```

The application will open in the browser.

```text
http://localhost:8501
```

## Example

Enter a city name such as:

```text
Chennai
```

The application displays the current weather information including:

* Temperature
* Humidity
* Feels-like temperature
* Wind speed
* Weather condition

The Hugging Face AI model then generates a simple explanation based on the retrieved weather information.

## Security

The Hugging Face access token is stored in the `.env` file instead of directly inside the Python code.

The actual access token should not be shared publicly or uploaded to a public repository.

## Future Enhancements

* Weather forecast
* Rain probability
* Sunrise and sunset information
* Multiple city comparison
* Weather history
* Improved AI recommendations

## Conclusion

Weather AI Assistant demonstrates how weather APIs and Hugging Face AI can be integrated with Python and Streamlit.

It provides real-time weather information along with a simple AI-generated explanation through an easy-to-use interface.
