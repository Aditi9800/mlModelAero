***************************  app.js of frontend  ***************************


import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [mainTemp, setMainTemp] = useState('');
  const [visibility, setVisibility] = useState('');
  const [windSpeed, setWindSpeed] = useState('');
  const [pressure, setPressure] = useState('');
  const [humidity, setHumidity] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setPrediction(null);

    try {
      const response = await axios.post('http://localhost:8000/predict', {
        main_temp: parseFloat(mainTemp),
        visibility: parseFloat(visibility),
        wind_speed: parseFloat(windSpeed),
        pressure: parseFloat(pressure),
        humidity: parseFloat(humidity)
      });

      setPrediction(response.data.prediction);
    } catch (err) {
      console.error('Error making prediction:', err);
      setError('Error making prediction. Please try again.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Weather Prediction</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Main Temperature: </label>
            <input
              type="number"
              value={mainTemp}
              onChange={(e) => setMainTemp(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Visibility (meters): </label>
            <input
              type="number"
              value={visibility}
              onChange={(e) => setVisibility(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Wind Speed (m/s): </label>
            <input
              type="number"
              value={windSpeed}
              onChange={(e) => setWindSpeed(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Pressure (hPa): </label>
            <input
              type="number"
              value={pressure}
              onChange={(e) => setPressure(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Humidity (%): </label>
            <input
              type="number"
              value={humidity}
              onChange={(e) => setHumidity(e.target.value)}
              required
            />
          </div>
          <button type="submit">Predict</button>
        </form>
        {error && <p className="error">{error}</p>}
        {prediction !== null && <p className="prediction">Prediction: {prediction}</p>}
      </header>
    </div>
  );
}

export default App;
