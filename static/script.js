const apiKey = "api-key goes here";
const resultDiv = document.getElementById("result");
const searchInput = document.getElementById("city-input");
const searchButton = document.getElementById("search-button");

searchButton.addEventListener("click", () => {
  const city = searchInput.value.trim();
  if (!city) return;

  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  resultDiv.innerHTML = "Loading...";

  fetch(url)
    .then(response => {
      if (!response.ok) throw new Error("City not found");
      return response.json();
    })
    .then(data => {
      resultDiv.innerHTML = `
        <div class="weather-box">
          <h1>The weather in ${data.name} is:</h1>
          <p>Temperature: ${data.main.temp}°C</p>
          <p>Description: ${data.weather[0].description}</p>
        </div>
      `;
    })
    .catch(error => {
      resultDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    });
});
