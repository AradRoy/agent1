import os
import dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

agent = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=OPENAI_API_KEY),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=True,
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
