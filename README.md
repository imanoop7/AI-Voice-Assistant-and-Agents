# LiveKit Voice Assistant

This project implements a voice assistant using LiveKit's agent framework, integrating with OpenAI for speech-to-text, language modeling, and text-to-speech capabilities.

## Features

- Voice-based interaction
- Temperature control for different zones in a home
- Integration with LiveKit for real-time communication
- Utilizes OpenAI's GPT-3.5 Turbo for natural language processing
- Silero VAD (Voice Activity Detection) for improved speech recognition

## Prerequisites

- Python 3.7+
- LiveKit account and API credentials
- OpenAI API key
- Groq API key (optional)
- Gemini API key (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/imanoop7/AI-Voice-Assistant-and-Agents
   cd AI-Voice-Assistant-and-Agents
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add the following:
   ```bash
   LIVEKIT_API_KEY=<your-livekit-api-key>
   LIVEKIT_URL=<your-livekit-url>
   LIVEKIT_API_SECRET=<your-livekit-api-secret>
   OPENAI_API_KEY=<your-openai-api-key>
   ```

## Usage

Run the main script to start the voice assistant:

```bash
python main.py
```

The assistant will connect to the LiveKit room and wait for voice commands. It can perform the following actions:

- Get the temperature of a specific room
- Set the temperature of a specific room

## Project Structure

- `main.py`: The entry point of the application, sets up the voice assistant
- `api.py`: Contains the `AssistantFuc` class with temperature control functions
- `requirements.txt`: Lists all the Python dependencies
- `.env`: Stores environment variables and API keys

## How It Works

1. The application uses LiveKit to establish a real-time audio connection.
2. Silero VAD is used for voice activity detection.
3. OpenAI's speech-to-text converts user's voice to text.
4. The text is processed by GPT-3.5 Turbo to understand the user's intent.
5. If temperature control is requested, it uses the functions in `AssistantFuc`.
6. The response is converted back to speech using OpenAI's text-to-speech.

## Customization

You can extend the `AssistantFuc` class in `api.py` to add more functionalities to your voice assistant.

## Troubleshooting

If you encounter any issues:
1. Ensure all environment variables are correctly set in the `.env` file.
2. Check that all required dependencies are installed.
3. Verify your LiveKit and OpenAI API credentials.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

