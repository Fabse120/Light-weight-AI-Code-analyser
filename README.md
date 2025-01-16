# Code Analysis Tool with Local LLM

## Goal
Create a Python tool that checks code for code smells, best practices, and security vulnerabilities, and provides active improvement suggestions. This tool will use a local LLM like Llama to perform the analysis.

## Features

### Code Smells Detection
- **Identify Long Functions, Deep Nesting, Unused Variables, and Poorly Named Code Elements**
  - Provide suggestions for better structuring.

### Best Practices
- **Check for Adherence to Clear Naming Conventions and Documentation (Docstrings)**
  - Provide suggestions to improve code readability and maintainability.

### Security Analysis
- **Check for Common Security Vulnerabilities like Unsafe Input Handling and Unsafe Functions (eval(), exec())**
  - Provide recommendations for secure handling of user inputs and error handling.

### Active Improvement Suggestions
- **The Tool Provides Concrete Suggestions on How to Refactor the Code to Fix Errors, Code Smells, and Security Vulnerabilities**


# Used LLM: Codelama with Ollama
