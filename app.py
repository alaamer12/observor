# Define the Observer interface
class Observer:
    def update(self, temperature, humidity, pressure):
        pass

# Define the Subject interface
class Subject:
    def register_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self):
        pass

# Define Concrete Observer: DisplayElement
class DisplayElement(Observer):
    def display(self):
        pass

# Define Concrete Subject: WeatherData
class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

# Define Concrete Observer: CurrentConditionsDisplay
class CurrentConditionsDisplay(DisplayElement):
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: {:.1f}F degrees and {:.1f}% humidity".format(self.temperature, self.humidity))

# Define Concrete Observer: StatisticsDisplay
class StatisticsDisplay(DisplayElement):
    def __init__(self, weather_data):
        self.temperatures = []
        self.humidities = []
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperatures.append(temperature)
        self.humidities.append(humidity)
        self.display()

    def display(self):
        avg_temp = sum(self.temperatures) / len(self.temperatures)
        avg_humidity = sum(self.humidities) / len(self.humidities)
        print("Avg Temperature: {:.1f}F, Avg Humidity: {:.1f}%".format(avg_temp, avg_humidity))

# Define Concrete Observer: ForecastDisplay
class ForecastDisplay(DisplayElement):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.forecast = "No forecast yet"
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        if pressure < 1000:
            self.forecast = "Expect rainy weather"
        elif pressure > 1000:
            self.forecast = "Expect sunny weather"
        else:
            self.forecast = "More of the same"

        self.display()

    def display(self):
        print("Forecast: {}".format(self.forecast))

# Usage
if __name__ == "__main__":
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
