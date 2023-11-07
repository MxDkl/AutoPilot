import os
import sys
import platform
from wrapper import wrapper
from screenshot import sc


MAKE_STEPS_PROMPT = """
You are now desktopGPT. 
You are a bot that can control this {} computer.
How would you go about navigating this computer?
How would you go about doing {}?
Output a list that contains the steps you would take to do {}.
Do not append or prepend anything else to the list.
An example of a list of steps to open firefox in windows would be:
open start menu, type 'firefox', press enter
"""

STEP_PROMPT = """
You will now exectute this step: {}. 
The step should be easy to complete given the screenshot provided. If it is not, you may improvise.
The screenshot is labeled with pixel coordinates. You can use these coordinates to click on the screen.
You will complete this step by outputing a python script that will do this step using the pyautogui library.
Your output should strictly only be the python script. 
Do not use code blocks or prepend or apend anything else to the code.
Dont write code comments.
The script should strictly folow this exact format:
import pyautogui
# more imports if needed

def step():
    # your code here
"""

def main(os_name):
    # get user input from cli
    instruction = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else sys.exit("No user input provided.")
    sc(os_name, "screenshot.png")
    list = wrapper.vision("screenshot.png", MAKE_STEPS_PROMPT.format(os_name,instruction, instruction)).split(",")
    print(list)

    # run through each step
    for step in list:
        sc(os_name, "screenshot.png")
        response = wrapper.vision("screenshot.png", STEP_PROMPT.format(instruction, step))
        print(response)
        # save response to a file
        with open("output.py", "w") as f:
            f.write(response)
        # run the file
        from output import step
        step()
        # remove the file
        os.remove("output.py")


if __name__ == "__main__":
    wrapper = wrapper()
    os_name = platform.system()
    main(os_name)
