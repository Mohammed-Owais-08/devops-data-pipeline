def transform(data):
    return {
        "city": data["name"],
        "temp": round(data["main"]["temp"] - 273.15, 2),  # Kelvin → Celsius
        "weather": data["weather"][0]["description"]
    }