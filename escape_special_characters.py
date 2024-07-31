import re
import pyperclip

# Define the input string
input_string = "https://echonax07.github.io/Automatic_Whale_detection_Thesis_figures/#:~:text=Figure%202.16%20%3A%20Predictions%20on%20images%20overlooked%20by%20DFO%20but%20found%20by%20our%20best%20model."

# Perform the replacements
output_string = re.sub(r'([#%])', r'\\\1', input_string)

# Copy the result to the clipboard
pyperclip.copy(output_string)

# Print the result
print(output_string)
