# Refactoring a Weather Forecast Application into Classes and Modules
# Objective: The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more 
# structured, object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated 
# into classes and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

# Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities 
# that can be encapsulated into classes. Create classes that represent different aspects of the weather 
# forecast application, such as fetching data, parsing data, and user interaction.

# Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization.

# Code Example: Before Refactoring:

# Weather Forecast Application Script

class WeatherForecast:
    def __init__(self,weather_data):
        self.weather_data = weather_data

    def city_weather(self, city):
        if city in self.weather_data.keys():
            print(f"Here is the weather report for {city}:")
            print(f"{self.weather_data[city]["temperature"]} degrees, {self.weather_data[city]["condition"]}, Humidity: {self.weather_data[city]["humidity"]}%")
        else:
            print("Weather data is not available for that city.")
    
    def display_all_weather(self):
        for key, value in self.weather_data.items():
            print(f"Weather in {key}: {value["temperature"]} degrees, {value["condition"]}, Humidity: {value["humidity"]}%")


weather_data = {
        "New York": {"temperature": 50, "condition": "Rainy", "humidity": 80, "city": "New York"},
        "London": {"temperature": 80, "condition": "Sunny", "humidity": 45, "city": "London"},
        "Tokyo": {"temperature": 70, "condition": "Foggy", "humidity": 80, "city": "Tokyo"}
    }

current_weather = WeatherForecast(weather_data)

print("Welcome to the Weather Forecast System.")
while True: 
    print("Please select from the following options:\n")
    action = input("1. Check weather data is a specific city\n2. Check all weather data\n3. Exit\n")
    if action == "1":
        city = input("Please enter the city name you want to check: ").title()
        current_weather.city_weather(city)
    elif action == "2":
        current_weather.display_all_weather()
    elif action == "3":
        print("Thank you for using the Weather Forecast System, have a good day!")
        break


# def fetch_weather_data(city):
#     # Simulated function to fetch weather data for a given city
#     print(f"Fetching weather data for {city}...")
#     # Simulated data based on city
    # weather_data = {
    #     "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
    #     "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
    #     "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    # }
#     return weather_data.get(city, {})

# def parse_weather_data(data):
#     # Function to parse weather data
#     if not data:
#         return "Weather data not available"
#     city = data["city"]
#     temperature = data["temperature"]
#     condition = data["condition"]
#     humidity = data["humidity"]
#     return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# def get_detailed_forecast(city):
#     # Function to provide a detailed weather forecast for a city
#     data = fetch_weather_data(city)
#     return parse_weather_data(data)

# def display_weather(city):
#     # Function to display the basic weather forecast for a city
#     data = fetch_weather_data(city)
#     if not data:
#         print(f"Weather data not available for {city}")
#     else:
#         weather_data = parse_weather_data(data)
#         print(weather_data)

# def main():
#     while True:
#         city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
#         if city.lower() == 'exit':
#             break
#         detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
#         if detailed == 'yes':
#             forecast = get_detailed_forecast(city)
#         else:
#             forecast = display_weather(city)
#         print(forecast)

# if __name__ == "__main__":
#     main()