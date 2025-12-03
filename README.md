# HakkoAI: Terminal AI Assistant

✨ **HakkoAI** is a beautiful, feature-rich AI assistant designed to run directly in your terminal, optimized for **Termux** and **Kali Linux** environments. It leverages the power of OpenRouter's API to bring powerful LLMs (e.g., GPT-3.5) right to your command line.

## 🚀 Features

* **Multi-Mode Interaction:** Specialized modes for chat, coding (`/code`), research (`/search`), and creative writing (`/creative`).
* **Beautiful UI:** Optimized color scheme and animations for a smooth terminal experience.
* **Conversation History:** Maintains context across interactions (up to 30 messages).
* **Easy Setup:** Simple dependency management with Python's `requests` library.

## 🛠️ Installation & Setup

### Prerequisites

* Python 3
* `requests` library (`pip install requests`)

### Running the Script

**Execute the script:**
    ```
    python3 hakko.py
    ```

## 🎯 Usage Commands

| Command | Description | Mode |
| :--- | :--- | :--- |
| **`/chat`** | Standard, friendly conversation. | Chat |
| **`/code`** | Expert programming and hacking assistant. | Code |
| **`/search`** | Research and information gathering mode. | Search |
| **`/creative`** | Creative writing, brainstorming, and ideas. | Creative |
| **`/clear`** | Clears the entire conversation history. | Utility |
| **`/stats`** | Displays current session statistics. | Utility |
| **`/help`** | Shows the command menu. | Utility |
| **`/exit`** | Closes HakkoAI. | Utility |

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
