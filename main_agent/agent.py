import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
# from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = "gemini-2.0-flash"

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict:   A dictionary containing the weather information.
                Includes a 'status' key ('success' or 'error').
                if 'success', includes a 'report' key with weather details.
                if 'error', includes an 'error_message' key.
    """
    print(f"--- Tool: get_weather called for city: {city} ---")
    city_normalized = city.lower().replace(" ", "")

    # mock weather data
    mock_weather_db = {
        "newyork": {
            "status": "success",
            "report": "The weather in New York is sunny."
        },
        "london": {
            "status": "success",
            "report": "It's cloudy in London with a temperature of 15 degree Celsius"
        }
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {
            "status": "error",
            "error_message": "Sorry, I don't have weather information for '{city}'."
        }

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}

root_agent = Agent(
    name="travel_planner_agent",
    # model=LiteLlm(AGENT_MODEL), # Use if not using gemini or vertex ai
    model=AGENT_MODEL,
    description=(
        "An agent that helps users plan their travel itineraries."
    ),
    instruction=(
        "You are a travel planner agent. Help the user plan their trip."
    ),
    tools=[get_weather,get_current_time]
)