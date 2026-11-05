# LLM Fundamentals

A hands-on learning project exploring the fundamentals of Large Language Models (LLMs) using the OpenAI API and Python.

## 📚 Topics Covered

### 1. LLM Basics (`1.llm_basic.py`)
- Single-turn API calls with `gpt-4o`
- Multi-turn conversations (message history)
- System prompts, temperature, and max tokens
- Token usage tracking (input/output/total)
- Streaming responses with `gpt-4.1-mini`

### 2. Structured Output (`2.structured_output.py`)
- Getting plain text responses from the API
- Converting LLM output to structured JSON using **Pydantic** models
- Schema-constrained generation with `responses.parse()`

### 3. Tool Calling / Function Calling (`3.tool_call.py`)
- Role prompting with detailed system instructions
- Defining tools (functions) for the model to call
- Real-world integration: **OpenWeather API** for live weather data
- Tool call loop: model decides when to call a tool, processes the result, and generates a natural language answer
- Interactive CLI chat interface

## 🛠️ Setup

### Prerequisites
- Python 3.10+
- An [OpenAI API key](https://platform.openai.com/api-keys)
- An [OpenWeather API key](https://openweathermap.org/api) (for the weather tool demo)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/llm-fundamentals.git
   cd llm-fundamentals
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY="your-openai-api-key"
   OPENWEATHER_API_KEY="your-openweather-api-key"
   ```

## 🚀 Usage

Run any script directly:

```bash
python 1.llm_basic.py
python 2.structured_output.py
python 3.tool_call.py
```

The weather assistant (`3.tool_call.py`) runs as an interactive chat — type a city name to get live weather, or type `exit` to quit.

## 📦 Dependencies

- **openai** — Official OpenAI Python SDK
- **python-dotenv** — Load environment variables from `.env`
- **pydantic** — Data validation and structured output schemas
- **requests** — HTTP client for the OpenWeather API

## 📄 License

This project is for educational purposes.
