# AI Research Agent 

A conversational AI research assistant built with Python, LangChain, and a locally running Ollama model. The agent uses web search and Wikipedia to gather information, generates research-based responses, and automatically saves each conversation to a local text file.

## Overview

This project explores the development of an AI agent capable of combining a language model with external tools to perform research tasks. Instead of relying exclusively on the model's existing knowledge, the agent can retrieve information from external sources and use it to formulate responses.

The application provides a Gradio chat interface where users can submit research questions and receive responses from the agent.

## Features

- **Conversational research:** Ask questions on a variety of topics through an interactive chat interface.
- **Web search:** Uses DuckDuckGo to retrieve information from the web.
- **Wikipedia integration:** Searches Wikipedia and retrieves relevant article content through the Wikipedia API.
- **Tool-calling agent:** Uses LangChain to connect the language model with external tools and coordinate their execution.
- **Automatic research logging:** Saves each question and its final answer to `research_output.txt`, including a timestamp.
- **Local language model:** Uses Ollama with the `llama3.2:1b` model, allowing the language model to run locally without requiring a paid LLM API.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| LangChain | Agent creation, tool integration, and execution |
| Ollama (Llama 3.2 1B) | Local language model |
| DuckDuckGo Search | Web information retrieval |
| Wikipedia API | Encyclopedia search and article retrieval |
| Gradio | Interactive chat interface |
| Pydantic | Structured research response schema |
| python-dotenv | Environment variable management |

## Architecture

The application follows a tool-augmented agent architecture:

1. **User input:** The user submits a question through the Gradio interface.
2. **Agent reasoning and tool selection:** The LangChain agent, powered by the local Ollama model, determines which available tools to call.
3. **Information retrieval:** The agent can use DuckDuckGo Search and Wikipedia to gather relevant information.
4. **Response generation:** The model uses the information returned by the tools to formulate its answer.
5. **Automatic logging:** The final response and original question are appended to `research_output.txt` with a timestamp.
6. **User output:** The generated answer is displayed in the Gradio chat interface.

## Project Structure

```text
AI Agent Tutorial/
├── main.py              # Agent configuration and Gradio interface
├── tools.py             # Search, Wikipedia, and file-saving tools
├── requirements.txt     # Python dependencies
├── .gitignore           # Excludes local and sensitive files
└── research_output.txt  # Generated research history (local)
```

The research output file is generated automatically when the application processes a question. It is intended to remain local and is excluded from version control.

## Installation and Setup

### Prerequisites

- Python 3.13 (or a compatible Python version)
- Ollama installed on your machine
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the repository URL with your own GitHub repository URL.

### 2. Create and activate a virtual environment

On Windows:

```cmd
python -m venv venv
venv\Scripts\activate
```

On macOS or Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

Ensure that the dependencies for Ollama integration and Gradio are installed as well.

### 4. Set up Ollama

Pull the model used by the application:

```bash
ollama pull llama3.2:1b
```

Make sure the Ollama service is running before starting the agent.

### 5. Run the application

From the project directory, execute:

```bash
python main.py
```

Open the local Gradio URL displayed in the terminal to access the chat interface.

## Example Research Questions

- What makes a great CV?
- Explain quantum computing simply.
- What are the main applications of artificial intelligence?

These examples are also available in the Gradio interface.

## Research Output

Every processed question and its corresponding answer are automatically appended to `research_output.txt`.

Each entry contains:
- Timestamp
- Original research question
- Generated answer

The file uses UTF-8 encoding and is created in the application's working directory.

## Limitations and Future Improvements

Potential extensions include:

- Improving the structured output pipeline using the Pydantic research response schema.
- Adding persistent conversational memory.
- Improving source attribution and citations in generated answers.
- Enhancing error handling and tool-selection reliability.
- Exporting research results to Markdown or PDF.

## Author

Developed as a personal hands-on project to explore AI agents, local language models, tool calling, information retrieval, and LLM-powered applications.
