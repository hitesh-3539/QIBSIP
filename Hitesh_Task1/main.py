import datetime
import webbrowser
import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()
    
    # Using the microphone for input
    try:
        with sr.Microphone() as source:
            print("\n🎙️ Listening... Speak now (or type your command below if mic fails):")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
            
            print("🤖 Processing voice...")
            command = recognizer.recognize_google(audio).lower()
            print(f"👤 You said: '{command}'")
            return command
    except Exception:
        # Fallback to Text input if Microphone is not configured or fails
        print("\n⚠️ Microphone unavailable or silent. Switching to Text Mode.")
        fallback = input("⌨️ Enter your command here: ").lower()
        return fallback

def run_assistant():
    print("\n=========================================")
    print("      WELCOME TO YOUR VOICE ASSISTANT     ")
    print("=========================================")
    print("\n💡 Available Commands: 'hello', 'time', 'date', 'search [query]', or 'exit'")
    
    while True:
        command = listen_command()
        
        if 'hello' in command:
            print("🤖 Assistant: Hello! Hope you are having a wonderful day. How can I help you?")
            
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"🤖 Assistant: The current time is {current_time}.")
            
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            print(f"🤖 Assistant: Today's date is {current_date}.")
            
        elif 'search' in command:
            # Extract search query
            query = command.replace("search", "").replace("for", "").strip()
            if query:
                print(f"🤖 Assistant: Searching Google for '{query}'...")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                print("🤖 Assistant: What would you like me to search for?")
                
        elif 'exit' in command or 'stop' in command or 'quit' in command:
            print("🤖 Assistant: Goodbye! Have a great day ahead.")
            break
            
        else:
            print("🤖 Assistant: Command not recognized. Please try 'hello', 'time', 'date', or 'search [query]'.")

if __name__ == "__main__":
    run_assistant()