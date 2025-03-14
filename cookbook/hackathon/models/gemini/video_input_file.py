from pathlib import Path

from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

# Run: `wget https://storage.googleapis.com/generativeai-downloads/images/GreatRedSpot.mp4` to download a sample video
video_path = Path(__file__).parent.joinpath("sample_video.mp4")

agent.print_response("Tell me about this video?", videos=[Video(filepath=video_path)])
