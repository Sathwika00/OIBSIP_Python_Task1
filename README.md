# Voice Assistant (Python)

A simple desktop voice assistant built in Python using speech recognition and text-to-speech. It listens for voice commands and responds accordingly — checking the time, opening YouTube, searching Google, or greeting the user.

> Built as part of the Oasis Infobyte Internship (OIBSIP) — Python Programming, Task 1.

✅ **Tested and confirmed working** — recognizes speech, tells time, opens YouTube, and performs Google searches via voice.

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

- Python 3.9 – 3.13 (⚠️ Python 3.14 is **not recommended** — `pyaudio` has no prebuilt wheel for it yet and will fail to build unless you install Microsoft C++ Build Tools. Python 3.13 or earlier works out of the box.)
- A working microphone
- Internet connection (Google Speech Recognition API is used for transcription)

**Tip:** If you have multiple Python versions installed on Windows, check which ones with:
```powershell
py -0
```
Then install dependencies and run the script using a specific version, e.g.:
```powershell
py -3.13 -m pip install -r requirements.txt
py -3.13 voice_assistant.py
```

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
   - **Windows:** `pip install pyaudio` usually works out of the box **on Python 3.9–3.13**. If you see an error like:
     ```
     error: Microsoft Visual C++ 14.0 or greater is required
     ```
     it means pip is trying to compile it from source because no prebuilt wheel exists for your Python version (commonly happens on brand-new versions like 3.14). The fix is to use an older Python version (3.13 or earlier) rather than installing the full Visual Studio Build Tools. See the version tip above for running with a specific Python version.
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
