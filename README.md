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


# Used LLM: StarCoder

## Why StarCoder is Perfectly Fitted for a Code Analyzer

### Specialization in Code
StarCoder is specifically trained on a vast amount of code from various programming languages. This specialization allows it to understand the syntax, semantics, and structure of code better than general-purpose language models.

### Multilingual Support
StarCoder supports multiple programming languages, making it versatile for developers working in different languages. This broad support ensures that the model can provide meaningful analysis across a wide range of codebases.

### Advanced Code Understanding
StarCoder can perform complex code understanding tasks, such as code completion, error detection, code refactoring, and generating documentation. Its ability to comprehend and generate code makes it a powerful tool for code analysis.

### Integration Capabilities
StarCoder can be easily integrated into various development environments, including VS Codium and JetBrains IDEs. This integration allows developers to leverage the model's capabilities directly within their preferred coding environment.

### Performance and Accuracy
StarCoder is designed to be performant and accurate, providing reliable and precise code analysis. Its large parameter size and extensive training data contribute to its robust performance in understanding and generating code.

### Customizability
Developers can fine-tune StarCoder for specific tasks or domains, making it adaptable to different coding styles and project requirements. This customizability ensures that the model can provide tailored analysis for various use cases.

### Community and Support
Being part of the Hugging Face ecosystem, StarCoder benefits from a large community of developers and researchers. This community support ensures continuous improvements, updates, and a wealth of resources for integrating and using the model effectively.

### Summary
StarCoder's specialization in code, multilingual support, advanced code understanding, integration capabilities, performance, customizability, and community support make it an ideal choice for a code analyzer. Its ability to understand and generate code accurately and efficiently makes it a valuable tool for developers seeking to enhance their coding workflow.

https://huggingface.co/bigcode/starcoder/tree/main


## Further ideas for this project
Creation of a VSCodium plugin that automatically analyzes the written Code.
