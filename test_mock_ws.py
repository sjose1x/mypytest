import pytest
from mock import MagicMock
from forecastor import ForeCaster, WeatherService

@pytest.fixture
def mock_ws():
    return MagicMock(spec=WeatherService)

def test_rain_when_barometer_rising(mock_ws):
    forecaster = ForeCaster(mock_ws)
    mock_ws.barometer.return_value = 'rising'
    assert forecaster.forecast() == 'Going to Rain'
#instead of two test cases for rising and falling
@pytest.mark.parametrize("reading, expected_forecast",
                         [('rising', 'Going to Rain'),
                          ('falling','Looks Clear')])
def test_forecast(reading, expected_forecast, mock_ws):
    forecaster = ForeCaster(mock_ws)
    mock_ws.barometer.return_value = reading
    assert forecaster.forecast() == expected_forecast
    
    
    