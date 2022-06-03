const express = require("express");
const app = express();

let weatherData = { temperature: [], humidity: [] };
let diseaseData = {
  /*1: [], 2: [], 3: []*/
};

app.use(express.json());

app.get("/weather-history", (req, res) => {
  res.status(200).json(weatherData);
});

app.get("/weather", (req, res) => {
  const latestTemperature =
    weatherData.temperature[weatherData.temperature.length - 1];
  const latestHumidity = weatherData.humidity[weatherData.humidity.length - 1];

  res
    .status(200)
    .json({ temperature: latestTemperature, humidity: latestHumidity });
});

app.post("/weather", (req, res) => {
  if (req.body === null) {
    res.status(400).send("error");
    return;
  }
  console.log(req.body);
  console.log(req.body, req.body.humidity);
  temperature = [...weatherData.temperature, req.body.temperature];
  humidity = [...weatherData.humidity, req.body.humidity];
  weatherData = {
    ...weatherData,
    temperature: temperature,
    humidity: humidity,
  };
  res.send("done");
});

app.post("/disease", (req, res) => {
  if (req.body === null) {
    res.status(400).send("error");
    return;
  }
  const { plantId, disease, diseaseProbability } = req.body;
  if (!diseaseData[plantId]) {
    diseaseData[plantId] = [];
  }
  diseaseData[plantId].push({
    disease: disease,
    diseaseProbability: diseaseProbability,
    time: new Date(),
  });
  res.send("done");
});

app.get("/disease-history", (req, res) => {
  res.status(200).json(diseaseData);
});

app.get("/disease", (req, res) => {
  const latestDisease = {};
  if (Object.keys(diseaseData).length === 0) {
    res.status(200).json(latestDisease);
  }
  console.log(Object.keys(diseaseData));
  Object.keys(diseaseData).map((key) => {
    latestDisease[key] = diseaseData[key][diseaseData[key].length - 1];
  });
  res.status(200).json(latestDisease);
});

app.listen(3000, () => {
  console.log("server active at port 3000");
});
