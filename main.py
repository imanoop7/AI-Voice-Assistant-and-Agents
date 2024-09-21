import asyncio
from dotenv import load_dotenv

from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant

from livekit.plugins import openai, silero, deepgram

load_dotenv()

async def entrypoint(ctx: JobContext):
    intial_ctx = llm.ChatContext().append(
        role = "system",
        text = (
            "You are a voice assistant created by livekit. your interface with user will be voice."
            "You should use sjprt and concise response, and avoiding usage of unpronouncable punctuation. "
        ),
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    assistant = VoiceAssistant(
        vad = silero.VAD.load(),
        stt=deepgram.STT(),
        llm=openai.LLM(model="phi3", base_url="http://localhost:11434/"),
        tts= openai.TTS(),
        chat_ctx= intial_ctx

    )
    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say("Hey, How can I help you today!", allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))