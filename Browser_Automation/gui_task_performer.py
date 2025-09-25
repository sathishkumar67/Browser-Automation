from __future__ import annotations
import pyautogui
from gradio_client import Client, handle_file
from .capture import take_screenshot
from .model_api import get_instructions

client = Client("")

def perform_task(task_description):
    result = client.predict(
        image=handle_file(take_screenshot()),
        task=task_description,
        api_name="/predict"
)
    return result


while True:
		task = input("Enter a task description (or 'exit' to quit): ")
		if task.lower() == 'exit':
			break
		# output = perform_task(task)
		lines = get_instructions(task)
		for i in range(len(lines)-1): 
			output = perform_task(lines[i])
			pyautogui.moveTo(output['x'], output['y'], duration=0.25)
			pyautogui.click()