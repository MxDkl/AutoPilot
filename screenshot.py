import platform



def sc(filename):
    # Get the operating system name
    os_name = platform.system()

    if os_name == "Windows":
        # Perform actions for Windows
        import pyautogui
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

    elif os_name == "Darwin":
        # Perform actions for macOS (Darwin is the core of macOS)
        import subprocess
        subprocess.run(["screencapture", filename])


    elif os_name == "Linux":
        # Perform actions for Linux
        from PIL import ImageGrab
        screenshot = ImageGrab.grab()
        screenshot.save(filename)


    else:
        # Handle other or unknown operating systems
        print("Operating system not recognized")
        exit(1)