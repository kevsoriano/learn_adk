import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search
# from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = "gemini-2.0-flash"

destination_research_agent = Agent(
    name="destination_research_agent",
    model=AGENT_MODEL,
    description=(
        "An agent that researches travel destinations and gathers essential information."
    ),
    instruction=(
        """
        You are a travel researcher. You will be given a destination and travel preferences, you will research:
        - Best time to visit and weather patterns
        - Top attractions and must-see locations
        - Local culture, customs, and etiquette tips
        - Transportation options within the destination
        - Safety considerations and travel requirements
        Provide comprehensive destination insights for trip planning.
        """
    ),
    tools=[google_search],
    output_key="destination_research"
)

itinerary_builder_agent = Agent(
    name="itinerary_builder_agent",
    model=AGENT_MODEL,
    description=(
        "An agent that creates structured travel itineraries with daily schedules"
    ),
    instruction=(
        """
        You are a professional travel planner. Using the research from "destination_research" output, create detailed itinerary that includes:
        - Day-by-day schedule with recommended activities
        - Suggested accommodation areas or districts
        - Estimated time requirements for each activity
        - Meal recommendations and dining suggestions
        - Budget estimates for major expenses
        Structure it logically for easy following during the trip.
        """
    ),
    output_key="travel_itinerary"
)

travel_optimizer_agent = Agent(
    name="travel_optimizer_agent",
    model=AGENT_MODEL,
    description=(
        "An agent that optimizes travel plans with practical advise and alternatives"
    ),
    instruction=(
        """
        You are a seasoned travel consultant. Using the research from "travel_itinerary" output, optimize it by adding:
        - Money-saving tips and budget alternatives
        - Packing recommendations specific to the destination
        - Backup plans for weather or unexpected situations
        - Local apps, websites, or resources to download
        - Cultural do's and don'ts for respectful travel

        Format the final output as:

        ITINERARY: {travel_itinerary}

        OPTIMIZATION TIPS: [your money-saving and practical tips here]

        TRAVEL ESSENTIALS: [packing and preparation advice here]

        BACKUP PLANS: [alternative options and contingencies here]
        """
    ),
    output_key="travel_itinerary"
)

root_agent = SequentialAgent(
    name="travel_planner_agent",
    description= "An agent that helps users plan their travel itineraries.",
    sub_agents=[destination_research_agent,itinerary_builder_agent,travel_optimizer_agent]
)