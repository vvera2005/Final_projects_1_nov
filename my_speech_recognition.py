import subprocess
import webbrowser

def install_library(library_name):
    """This is to install a library"""
    try:
        subprocess.check_call(['pip', 'install', library_name])
        print(f"Successfully installed {library_name}.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {library_name}.")

try:
    import speech_recognition as sr
except ImportError:
    install_library("SpeechRecognition")
    import speech_recognition as sr
try:
    from youtubesearchpython import VideosSearch
except ImportError:
    install_library("youtube-search-python")
    from youtubesearchpython import VideosSearch

def get_command():
    """Gets command after running when you speak"""
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(source=mic, duration=0.5)
        try:
            audio = recognizer.listen(source=mic)
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak again.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    return None  

def open_application(app_name):
    """This function opens an application"""
    try:
        subprocess.Popen(app_name)
        print(f"Opening {app_name}...")
    except FileNotFoundError:
        print(f"Error: {app_name} not found. Make sure the app name is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

def close_application(app_name):
    """This function closes an application"""
    try:
        subprocess.run(['pkill', '-f', app_name], check=True)
        print(f"Closed {app_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to close {app_name}. Error: {e}")

def open_youtube_video(query):
    """This function opens a YouTube video"""
    videos_search = VideosSearch(query, limit = 1)
    results = videos_search.result()

    if results['result']:
        first_video = results['result'][0]
        video_url = first_video['link']
        webbrowser.open(video_url)
        print(f"Opening the first YouTube video for '{query}': {video_url}")
    else:
        print(f"No YouTube video found for '{query}'.")

def run_terminal_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)
        print("Command output (stderr):", e.stderr)

def main():
    """This is the main part where the commands are processed"""
    app_dir = {
        "firefox": "firefox",
        "terminal": "gnome-terminal",
        "text editor": "gedit",
        "task manager": "gnome-system-monitor"
    }

    terminal_dict = {
        "directory": "mkdir",
        "list": "ls -l",
        "file": "touch",
        "": "vim"
    }

    command = get_command()
    while command != "finish":
        if command:
            print(command)
            lcom = command.split()

            if command.startswith("open "):
                app_name = command[5:]
                if app_name in app_dir:
                    open_application(app_dir[app_name])
                else:
                    print(f"Unknown application: {app_name}")
            elif command.startswith("close "):
                app_name = command[6:]
                if app_name in app_dir:
                    close_application(app_dir[app_name])
            elif "youtube search" in command:
                query = command.replace("youtube search ", "")
                open_youtube_video(query)
            elif lcom[0] in terminal_dict:
                command = command.replace(lcom[0], terminal_dict[lcom[0]])
                run_terminal_command(command) 
            else:
                print(f"Unknown command: {command}")
        
        command = get_command()


    print("Voice Assistant: The end.")

if __name__ == "__main__":
    main()
