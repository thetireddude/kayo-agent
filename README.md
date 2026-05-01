# 🤖 Kayo - Your AI Coding Sidekick

> **Because coding alone is so 2023.** Meet Kayo, the AI agent that actually *gets* your codebase.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-4285F4?logo=google)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 What is Kayo?

Kayo is an **agentic AI coding assistant** powered by Google's Gemini API that can autonomously interact with your codebase. Unlike traditional chatbots that just *talk* about code, Kayo can:

- 📂 **Browse** your project structure
- 📖 **Read** your files
- ✍️ **Write** new code or modify existing files
- 🏃 **Execute** Python scripts with arguments
- 🔄 **Iterate** through complex multi-step tasks

Think of it as having a junior developer who never sleeps, never complains, and works entirely from the command line.

### 🎬 Proof It Works 

https://github.com/user-attachments/assets/1e0b43b4-dc25-4d29-a6c9-4f13c13a4907

> A fully functional website generated entirely by Kayo

---

## ✨ Features

### 🧠 **Intelligent Function Calling**
Kayo uses Gemini's function calling capabilities to autonomously decide which operations to perform:

| Function | What It Does |
|----------|--------------|
| `get_files_info` | Lists directory contents with file sizes |
| `get_file_content` | Reads file contents (with smart truncation) |
| `write_file` | Creates or overwrites files (auto-creates directories) |
| `run_python_file` | Executes Python scripts with optional CLI arguments |

### 🔒 **Sandboxed Execution**
All operations are restricted to a configured working directory. Kayo can't accidentally `rm -rf /` your system (we've all been there).

### 🔁 **Agentic Loop**
Kayo doesn't just respond once—it iterates through tasks, making multiple function calls until the job is done or the loop limit is reached.

### 🎛️ **Configurable & Verbose**
- Set your working directory, read limits, and execution timeouts
- Enable verbose mode to see exactly what Kayo is thinking (and doing)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- A Google Gemini API key ([Get one here](https://aistudio.google.com/api-keys))


### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/kayo.git
   cd kayo
   ```

2. **Set up a virtual environment** (optional but recommended)
   ```bash
   python -m venv kayo
   source kayo/Scripts/activate  # On Windows
   # source kayo/bin/activate    # On Unix/macOS
   ```

3. **Install dependencies**
   ```bash
   pip install google-genai python-dotenv
   ```

4. **Configure your environment**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
   Gemma 4 31B is recommended, as it provides the most flexible rate limits right now. This could change in the future.

5. **Update your working directory**
   
   Edit `config.py` to set your target project path:
   ```python
   WORKING_DIRECTORY = "/path/to/your/project"
   ```

### Usage

Run Kayo with a natural language prompt:

```bash
python main.py "Create a hello world script in Python"
```

Enable verbose mode to see the magic happen:

```bash
python main.py "List all Python files and show me the main.py content" --verbose
```

---

## 🎮 Example Commands

```bash
# File exploration
python main.py "What files are in the src directory?"

# Code generation
python main.py "Create a FastAPI endpoint for user authentication"

# Code execution
python main.py "Run the test_suite.py file with the --verbose flag"

# Multi-step tasks
python main.py "Find all TODO comments in Python files and create a summary markdown file"
```

---

## ⚙️ Configuration

Edit `config.py` to customize Kayo's behavior:

```python
WORKING_DIRECTORY = "C:\\path\\to\\your\\project"  # Target project directory
READ_MAX_CHARS = 10000                             # Max characters to read from files
EXECUTION_TIMEOUT = 30                             # Timeout for Python execution (seconds)
FUNCTION_CALL_VERBOSE = False                      # Show detailed function call logs
AGENTIC_LOOP_LIMIT = 20                            # Max iterations per request
```

### Configuration Details

| Setting | Purpose | Default | Notes |
|---------|---------|---------|-------|
| `WORKING_DIRECTORY` | Root directory for all file operations | `"C:\Tired-Stash\..."` | All paths are relative to this. Kayo cannot access files outside this directory for security. |
| `READ_MAX_CHARS` | Maximum characters to read from a single file | `10000` | Files larger than this are truncated with a notice. Prevents memory issues with large files. |
| `EXECUTION_TIMEOUT` | Maximum seconds a Python script can run | `30` | Prevents infinite loops or long-running processes from blocking Kayo. |
| `FUNCTION_CALL_VERBOSE` | Enable detailed function call logging | `False` | Shows function arguments when enabled. Useful for debugging. |
| `AGENTIC_LOOP_LIMIT` | Maximum function call iterations per request | `20` | Should match or slightly exceed your Gemini API rate limit (RPM). Prevents infinite loops. |

---

## 🧪 Testing

Kayo comes with test files for each function:

```bash
python test_get_files_info.py
python test_get_file_content.py
python test_write_file.py
python test_run_python_file.py
```

---

## 🏗️ Project Structure

```
kayo/
├── main.py                    # Entry point & agentic loop
├── config.py                  # Configuration settings
├── prompts.py                 # System prompt for the AI
├── call_function.py           # Function calling orchestration
├── functions/                 # Function implementations
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── test_*.py                  # Test files
└── .env                       # API keys (not in repo)
```

---

## 🤔 How It Works

1. **You provide a prompt** via command line
2. **Kayo analyzes** the request using Gemini's reasoning
3. **Function calls are made** autonomously (read files, write code, etc.)
4. **Results are fed back** to the model for the next iteration
5. **The loop continues** until the task is complete or limit is reached
6. **Final response** is displayed to you

```
User Prompt → Gemini → Function Call → Result → Gemini → ... → Final Answer
```

---

## 🛡️ Security Features

- **Path validation**: All file operations are restricted to the working directory
- **Execution timeout**: Python scripts can't run indefinitely
- **Read limits**: Large files are truncated to prevent memory issues
- **Error handling**: Graceful handling of API errors and invalid operations

---

## 🐛 Known Limitations

- Currently only supports Python file execution (not other languages)
- File reading is truncated at 10,000 characters by default
- Requires manual configuration of working directory
- API rate limits apply (adjust `AGENTIC_LOOP_LIMIT` accordingly)

---

## 🙏 Acknowledgments

- Built with [Google Gemini API](https://ai.google.dev/)
- Inspired by the agentic AI revolution
- Powered by caffeine and curiosity

---

## 📬 Contact

Questions? Ideas? Found a bug? Open an issue or reach out!

**Happy coding with Kayo! 🚀**

---

<div align="center">
  <sub>Made with ❤️ by developers, for developers</sub>
</div>
