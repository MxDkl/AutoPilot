import pyautogui


def sc(os, filename):
    if os == "Windows":
        # Perform actions for Windows
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

    elif os == "Darwin":
        # Perform actions for macOS (Darwin is the core of macOS)
        import subprocess
        subprocess.run(["screencapture", filename])

    elif os == "Linux":
        # Perform actions for Linux
        from PIL import ImageGrab
        screenshot = ImageGrab.grab()
        screenshot.save(filename)

    else:
        # Handle other or unknown operating systems
        print("Operating system not recognized")
        exit(1)

    from PIL import Image, ImageDraw, ImageFont
    
    image = Image.open(filename)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Get the dimensions of the image
    image_width, image_height = image.size

    # Draw the horizontal scale
    for x in range(0, image_width + 1, 100):  # Adjust the step size as needed
        draw.line([(x, image_height - 20), (x, image_height)], fill=(255, 0, 0), width=2)
        draw.text((x, image_height - 35), str(x), fill=(255, 0, 0))

    # Draw the vertical scale
    for y in range(0, image_height + 1, 100):  # Adjust the step size as needed
        draw.line([(image_width - 20, y), (image_width, y)], fill=(0, 255, 0), width=2)
        draw.text((image_width - 50, y), str(y), fill=(0, 255, 0))

    # Save the image with the graph/scale (overwrite the original)
    image.save(filename)


if __name__ == "__main__":
    sc("Windows", "test.png")