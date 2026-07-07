# Voice Assistant (Python)

A simple desktop voice assistant built in Python using speech recognition and text-to-speech. It listens for voice commands and responds accordingly — checking the time, opening YouTube, searching Google, or greeting the user.

> Built as part of the Oasis Infobyte Internship (OIBSIP) — Python Programming, Task 1.

## Features

- 🎙️ Listens to voice commands via microphone
- 🕒 Tells the current time
- ▶️ Opens YouTube
- 🔍 Searches Google for a spoken query
- 👋 Responds to greetings
- 🛑 Exits gracefully on the "bye" command

## Demo Commands

| Say this...          | Assistant does...                          |
|-----------------------|---------------------------------------------|
| "What time is it"     | Speaks the current time                     |
| "Open YouTube"         | Opens youtube.com in your browser           |
| "Search Google"        | Asks what to search, then opens the results |
| "Hello"                | Greets you back                             |
| "Bye"                  | Says goodbye and exits                      |

## Requirements

- Python 3.7+
- A working microphone
- Internet connection (Google Speech Recognition API is used for transcription)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Note on PyAudio:** `pyaudio` can fail to install directly via pip on some systems because it needs the PortAudio library.
   - **Windows:** `pip install pyaudio` usually works out of the box, or use `pipwin install pyaudio` if it fails.
   - **macOS:** `brew install portaudio` then `pip install pyaudio`
   - **Linux (Debian/Ubuntu):** `sudo apt-get install python3-pyaudio` or `sudo apt-get install portaudio19-dev` then `pip install pyaudio`

## Usage

Run the assistant:
```bash
python voice_assistant.py
```

Speak clearly into your microphone after you see `Listening...` in the console. Say **"bye"** at any time to exit.

## Project Structure

```
├── voice_assistant.py   # Main application script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## How It Works

1. **Speech-to-Text:** `speech_recognition` captures audio from the microphone and sends it to Google's Speech Recognition API to convert it to text.
2. **Command Matching:** The recognized text is checked against a set of keywords (`time`, `youtube`, `google`, `hello`, `bye`).
3. **Text-to-Speech:** `pyttsx3` converts the assistant's replies into spoken audio, offline.

## Possible Future Improvements

- Add more commands (weather, news, reminders, music playback)
- Wrap recognition errors more specifically (e.g. `sr.UnknownValueError`, `sr.RequestError`) instead of a bare `except`
- Add a wake word (e.g. "Hey Assistant") instead of continuous listening
- Support offline speech recognition for use without internet

## License

This project is open source and available for learning purposes.
