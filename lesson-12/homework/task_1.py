from bs4 import BeautifulSoup

# Loading HTML file
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the table and extract rows
table = soup.find("table")
rows = table.find_all("tr")[1:]

# Parse the weather data
weather_data = []
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temperature = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    weather_data.append((day, temperature, condition))

# Display
print("Weather Forecast:")
for day, temp, cond in weather_data:
    print(f"{day}: {temp}°C, {cond}")

# The highest temperature
max_temp = max(weather_data, key=lambda x: x[1])
print(f"\nHottest Day: {max_temp[0]} with {max_temp[1]}°C")

# Find days with 'Sunny' condition
sunny_days = [day for day, temp, cond in weather_data if cond == "Sunny"]
print("\nSunny Days:", ", ".join(sunny_days))

# Average temperature
avg_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)
print(f"\nAverage Temperature: {avg_temp:.2f}°C")
