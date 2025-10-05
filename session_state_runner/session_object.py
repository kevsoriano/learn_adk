import uuid
from google.adk.sessions import InMemorySessionService
import asyncio

async def main():
    temp_service = InMemorySessionService()
    example_session = await temp_service.create_session(
        app_name = "my_app",
        user_id = f"user{uuid.uuid4()}",
        state={"initial_key": "Hello World for State!"}
    )

    print(f"--- Examining Session Properties ---")
    print(f"ID (`id`):                {example_session.id}")
    print(f"Application Name (`app_name`): {example_session.app_name}")
    print(f"User ID (`user_id`):         {example_session.user_id}")
    print(
        f"State (`state`):           {example_session.state}"
    )  # Note: Only shows initial state here
    print(f"Events (`events`):         {example_session.events}")  # Initially empty
    print(f"Last Update (`last_update_time`): {example_session.last_update_time:.2f}")
    print(f"---------------------------------")

    # Clean up (optional for this example)
    temp_service = await temp_service.delete_session(
        app_name=example_session.app_name,
        user_id=example_session.user_id,
        session_id=example_session.id,
    )
    print("The final status of temp_service - ", temp_service)


if __name__ == "__main__":
    asyncio.run(main())