document.addEventListener('DOMContentLoaded', () => {
    const cityInput = document.getElementById('cityInput');
    const getWeatherBtn = document.getElementById('getWeatherBtn');
    const weatherInfo = document.getElementById('weatherInfo');
    const recommendations = document.getElementById('recommendations');

    getWeatherBtn.addEventListener('click', () => {
        const city = cityInput.value.trim();
        if (city) {
            fetchWeatherData(city);
        } else {
            alert('Please enter a city name');
        }
    });

    function fetchWeatherData(city) {
        fetch(`http://localhost:5000/weather?city=${encodeURIComponent(city)}`)
            .then(response => response.json())
            .then(data => {
                displayWeatherInfo(data);
                displayRecommendations(data.recommendations);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Unable to fetch weather data. Please try again.');
            });
    }

    function displayWeatherInfo(data) {
        document.getElementById('cityName').textContent = data.city;
        document.getElementById('temperature').textContent = `Temperature: ${data.temperature}°C`;
        document.getElementById('weatherCondition').textContent = `Weather: ${data.weather_condition}`;
        weatherInfo.style.display = 'block';
    }

    function displayRecommendations(recs) {
        document.getElementById('wear').textContent = `Wear: ${recs.wear}`;
        document.getElementById('activities').textContent = `Activities: ${recs.activities}`;
        document.getElementById('foodDrink').textContent = `Food/Drink: ${recs.food_drink}`;
        recommendations.style.display = 'block';
    }
});