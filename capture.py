from __future__ import annotations
import mss
from PIL import Image  

def take_screenshot() -> Image.Image:
    """
    Captures a screenshot of the primary monitor and returns it as a PIL Image object.

    This function uses the `mss` library to capture the screen and the `PIL` library to convert
    the raw screenshot data into an image object. The screenshot is not saved to disk; it is
    returned directly as a PIL Image for further processing or saving as needed.

    Returns:
        Image.Image: Screenshot as a PIL Image object.
    """
    # Create a screen capture object using mss
    with mss.mss() as sct:
        # Select the primary monitor (index 1 in mss)
        monitor = sct.monitors[1]
        # Capture the screen contents of the primary monitor
        screenshot = sct.grab(monitor)

        # Convert the raw screenshot data to a PIL Image object (RGB format)
        # Return the PIL Image object
        return Image.frombytes("RGB", screenshot.size, screenshot.rgb)