import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the URL where the local Ollama server is running
url = "http://localhost:11434/api/generate"

# instructions = "Give a response in markdown format and in maximum 20 lines and adhere to the format given: Analyze Codesmells, check for best practices, check security vulnerabilities and suggest fixes for the provided code: "
# instructions = "Erstelle eine Rückmeldung in maximal 20 Zeilen und achte auf die vorgegebene Reihenfolge: Analysiere Codesmells, prüfe den Code auf best practices und prüfe den Code auf Sicherheitslücken. Schlage ausserdem Lösungen für die gefundenen Probleme vor:"
instructions = ("Response should be short but include every error and in markdown format. "
                "Adhere to the following format: Codesmells, best practices, security "
                "vulnerabilities, suggested fixes; Analyze the given code for codesmells,"
                " best practices, security vulnerabilities and suggest fixes for "
                "those problems, give a corrected version of the code:")
code = ("""

""")

# Define the payload for the request
payload = {
    "model": "codellama",
    "prompt": f"{instructions} {code}",
    "max_tokens": 100,
    "temperature": 0.7
}

# Make a POST request to the LLM
logger.info("Waiting for response...")
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Split the response text into individual JSON objects
        json_objects = response.text.strip().split('\n')
        # Initialize an empty string to accumulate the generated text
        generated_text = ""

        # Parse each JSON object and accumulate the generated text
        for json_str in json_objects:
            if json_str.strip():  # Ensure the string is not empty
                json_obj = json.loads(json_str)
                generated_text += json_obj.get('response', '')

        # Write the generated text to a Markdown file
        with open("output.md", "w") as md_file:
            md_file.write(generated_text)

        logger.info("Generated text has been written to output.md")
    except json.JSONDecodeError as e:
        logger.error("JSON Decode Error: %s", e)
    except Exception as e:
        logger.error("An error occurred: %s", e)
else:
    logger.error("Failed to get a response from the LLM. Status code: %d", response.status_code)
