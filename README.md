# LangSmith Observability Quick Start

This project demonstrates how to use LangSmith for observability in your LLM applications.

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API keys:**

   You need to set the `OPENAI_API_KEY` environment variable. You can do this in several ways:

   **Option 1: Export in terminal (temporary)**

   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

   **Option 2: Add to your shell profile (permanent)**
   Add this line to your `~/.zshrc` or `~/.bashrc`:

   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

   **Option 3: Create a .env file (recommended for development)**
   Create a `.env` file in the project root:

   ```
   OPENAI_API_KEY=your-openai-api-key-here
   LANGSMITH_API_KEY=your-langsmith-api-key-here  # Optional
   ```

3. **Run the script:**
   ```bash
   python 01-observability-quick-start.py
   ```

## What this does

The script demonstrates a simple RAG (Retrieval-Augmented Generation) pipeline with LangSmith observability:

1. A mock retriever that returns predefined results
2. An OpenAI chat completion wrapped with LangSmith for tracing
3. Automatic logging of inputs, outputs, and metadata

## Getting API Keys

- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **LangSmith API Key**: Get from [LangSmith](https://smith.langchain.com/) (optional for basic tracing)

## Files

- `01-observability-quick-start.py`: Main script demonstrating RAG with observability
- `config.py`: Configuration utilities for API keys
- `requirements.txt`: Python dependencies
- `README.md`: This file
