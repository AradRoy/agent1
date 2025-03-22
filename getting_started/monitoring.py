from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
import dotenv

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


agent = Agent(
    markdown=True,
    monitoring=True,
    model=OpenAIChat(id="gpt-4o", api_key=OPENAI_API_KEY),
)
agent.print_response("Share a 2 sentence horror story")
