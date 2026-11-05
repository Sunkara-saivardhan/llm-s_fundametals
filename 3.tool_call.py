from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Load environment variables
load_dotenv()

# 2. Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 3. Define the system prompt with role prompting
system_prompt = """
You are a senior AI engineer and an expert teacher.
Your role is to teach AI concepts to beginners.
Follow these rules:
- Explain concepts in simple English.
- Explain step by step.
- Use practical examples.
- Explain technical terms before using them.
- Use Python examples when relevant.
- Avoid unnecessary complexity.
"""

# 4. Define the user prompt
user_prompt = """
Explain Retrieval-Augmented Generation (RAG).
Explain:
1. What RAG is.
2. Why RAG is needed.
3. How RAG works step by step.
4. A practical example.
"""

# 5. Call the Responses API
result = client.responses.create(
    model="gpt-4o",
    instructions=system_prompt,
    input=user_prompt,
    max_output_tokens=500,
    temperature=0.3
)

# 6. Print the generated response
print(result.output_text)


#weather api
import os
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI(api_key=(os.getenv("OPENAI_API_KEY")))

def weather(city:str):
    try:
        api_key=os.getenv("OPENWEATHER_API_KEY")

        if not api_key:
              return {"error": "Missing OpenWeather API key."}
          
        url = "https://api.openweathermap.org/data/2.5/weather"
        params={
            'q':city,
            "appid":api_key,
            "units": "metric"
        }
        response=requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data=response.json()
    
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

    
    except requests.RequestException as error:
        return {"error": f"Weather API error: {error}"}
    
tools = [
    {
        "type": "function",
        "name": "weather",
        "description": "Get current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
                "discription":"name of the city"
            },
            "required": ["city"],
            "additionalProperties": False
        },
        "strict": True
    }
]

SYSTEM_PROMPT= """
You are a helpful weather assistant.

Rules:
1. For current weather questions, call the weather tool.
2. Never invent temperature, humidity, or weather conditions.
3. Use only the returned tool data to answer.
4. If the city is missing, ask the user which city.
5. If the tool returns an error, explain it honestly.
6. Answer in simple English.
7. Include the city, temperature in Celsius, and
   other available weather details.
"""

def ask_weather_assistant(user_prompt: str):
    
    input_items=[
        {"role":"system","content": SYSTEM_PROMPT},
        {"role":"user","content": user_prompt}
    ]
    
    result= client.responses.create(
        model="gpt-4",
        input=input_items,
        tools=tools,
        tool_choice="auto",
        temperature=0.3,
        max_output_tokens=500
        
    )
    
    while True:
        function_calls=[]
        for item in result.output:
            if item.type=="function_call":
                function_calls.append(item)
        if not function_calls:
            return result.output_text
        
        # Preserve the model's response, including its tool calls
        input.extend(result.output)

        for call in function_calls:
            if call.name != "weather":
                tool_result = {"error": "Unknown tool requested."}
            else:
                try:
                    arguments = json.loads(call.arguments)
                    city = arguments["city"]
                    # Execute the real Python function
                    tool_result = weather(city)
                except (json.JSONDecodeError, KeyError, TypeError):
                    tool_result = {
                        "error": "Invalid arguments supplied to the weather tool."
                    }
            # Step 6: Send the function result back to the model
            input.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": json.dumps(tool_result)
            })
        # Step 7: Model processes tool results and generates its answer
        result = client.responses.create(
            model="gpt-4o-mini",
            input=input_items,
            tools=tools,
            tool_choice="auto",
            temperature=0.3,
            max_output_tokens=500
        )
        
# Step 8: Run the assistant
if __name__ == "__main__":

    while True:
        user_prompt = input("\nYou: ").strip()

        if user_prompt.lower() in ["exit", "quit", "stop"]:
            print("Assistant: Goodbye!")
            break

        if not user_prompt:
            continue

        try:
            answer = ask_weather_assistant(user_prompt)
            print("\nAssistant:", answer)

        except Exception as error:
            print(f"\nAn unexpected error occurred: {error}")
            
            
