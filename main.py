import wrapper from wrapper
from screenshot import sc

wrapper = wrapper()

prompt = """
You are
"""

def main():
    # take a screenshot
    # run vision on screenshot
    sc("screenshot.png")
    response = wrapper.vision("screenshot.png", "?")