def get_recommendations(temperature, weather_condition):
    if temperature > 35:
        return {
            "wear": "Light cotton clothing, hats, sunglasses",
            "activities": "Indoor activities with air conditioning, swimming",
            "food_drink": "Cold beverages like coconut water, fresh juices, light meals"
        }
    elif 25 <= temperature <= 35:
        return {
            "wear": "Cotton shirts, light trousers, comfortable footwear",
            "activities": "Early morning or evening outdoor activities, visiting parks",
            "food_drink": "Hydrating foods, fresh fruits, salads"
        }
    elif temperature < 20:
        return {
            "wear": "Sweaters, shawls, full sleeves",
            "activities": "Outdoor activities like visiting markets, light sports",
            "food_drink": "Warm meals, soups, hot beverages"
        }
    elif 20 <= temperature <= 25:
        return {
            "wear": "Light jackets, comfortable clothing",
            "activities": "Hiking, picnics, outdoor sports",
            "food_drink": "Balanced meals, fresh juices"
        }
    
    if "rain" in weather_condition.lower():
        return {
            "wear": "Waterproof jackets, rubber sandals, umbrellas",
            "activities": "Indoor activities, visiting cafes, reading",
            "food_drink": "Hot beverages like chai, pakoras, soups"
        }
    
    # Default recommendations
    return {
        "wear": "Comfortable clothing suitable for the weather",
        "activities": "Check local events and attractions",
        "food_drink": "Stay hydrated and enjoy local cuisine"
    }