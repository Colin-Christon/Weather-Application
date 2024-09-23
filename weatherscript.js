const apiKey = `e56bf621b4fa8f4143caaee9fff0f2b4`; // Replace with your OpenWeatherMap API key

// Function to get weather data
function getWeather() {
    const city = document.getElementById('city-input').value;
    if (!city) {
        alert('Please enter a place name.');
        return;
    }

    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
    console.log(url)
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.cod === 200) {
                console.log(data)
                // Display weather info
                document.getElementById('city-name').innerText = "City: ${data.name}";
                document.getElementById('temperature').innerText = `Temperature: ${data.main.temp} °F`;
                document.getElementById('weather').innerText = `Weather: ${data.weather[0].description}`;
                document.getElementById('humidity').innerText = `Humidity: ${data.main.humidity} %`;
                document.getElementById('wind-speed').innerText = `Wind Speed: ${data.wind.speed} m/s`;

                document.getElementById('weather-info').classList.remove('hidden');
            } else {
                alert('City not found!');
            }
        })
        .catch(error => {
            alert('Error fetching weather data.');
            console.error('Error:', error);
        });
}
