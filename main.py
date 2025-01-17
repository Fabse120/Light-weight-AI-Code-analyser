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
# instructions = ("Response should be short but include every error and in markdown format. "
               # "Adhere to the following format: Codesmells, best practices, security "
               # "vulnerabilities, suggested fixes; Analyze the given code for codesmells,"
               # " best practices, security vulnerabilities and suggest fixes for "
               # "those problems, give a corrected version of the code:")

instructions = """
Analyze the provided code thoroughly and deliver feedback in the following **exact structured format**, ensuring consistency, precision, and that all key aspects are addressed:

---

### 1. Codesmells
- **Definition**: Codesmells are patterns or structures in the code that indicate deeper issues, such as poor readability, duplicated logic, or overly complex methods.
- **Findings**: List and explain each identified codesmell. Provide specific examples from the code and detail the negative impact on maintainability, readability, or performance.

### 2. Best Practices
- **Definition**: Best practices refer to widely accepted coding standards and conventions that ensure high-quality, maintainable, and efficient code.
- **Findings**: Identify where the code deviates from best practices and explain why these deviations are suboptimal.
- **Recommendations**: Suggest actionable improvements to align the code with industry standards.

### 3. Security Vulnerabilities
- **Definition**: Security vulnerabilities are flaws in the code that attackers could exploit, such as weak input validation, improper authentication, or exposure of sensitive data.
- **Findings**: Highlight potential security vulnerabilities in the code and explain the risks.
- **Mitigation**: Offer specific fixes or strategies to eliminate the identified vulnerabilities.

### 4. Suggested Fixes
- **Summary of Changes**: Summarize the fixes for codesmells, best practices deviations, and security vulnerabilities.
- **Implementation**: Provide detailed suggestions or steps for applying these changes.

### 5. Corrected Code
- Deliver the final, corrected version of the code, formatted cleanly and incorporating all suggested improvements.
- Ensure the code is functional, optimized, and adheres to best practices.

---

### Additional Notes
- Use **markdown** formatting for clear and organized output.
- Always include examples referencing specific parts of the code for clarity.
- Explanations should be short but complete, avoiding ambiguity.
- The **corrected code** must reflect all suggested fixes and be ready to execute.

---

### Final Example Format:
#### Codesmells
- Issue 1: [Description, example, impact]
- Issue 2: [Description, example, impact]

#### Best Practices
- Issue 1: [Description, example, recommendation]
- ...

#### Security Vulnerabilities
- Issue 1: [Description, risk, mitigation]
- ...

#### Suggested Fixes
- [Summary of all recommended changes]

#### Corrected Code
```code
# Corrected and optimized code goes here
"""

code = """
public class Person {
public String full_Name;
public Integer age;
public String job;
public String preferredProgrammingLanguage;
public String ide;

public boolean database;
public String style;
public String preferredTestFramework;

public String getFirstName() {
    return full_Name.split(" ")[0];
}

public String getLastName() {
    return full_Name.split(" ")[1];
}

public boolean isOfLegalAge() {
    return age.compareTo(18) > 0;
}

public String getJobDescription() {
    switch(job) {
        case "Developer": return "Writes and tests code";
        case "Architect": return "Designs the project architecture";
        case "Tester": return "Tests code";
        default: return "";
    }
}


"""

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
logger.info(f"Response from server received.")

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
