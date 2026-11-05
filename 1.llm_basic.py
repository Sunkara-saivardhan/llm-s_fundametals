
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

'''result = client.responses.create(
    model="gpt-4o",
    input="What is AI?"
)

print(result.output_text)'''

#---multi-turn conversation (passing a list of messages)---
'''result=client.responses.create(
    model="gpt-4o",
    instructions="you are a helpful assistant.",
    input=[
        {'role':'user','content':"my name is sai vardhan"},
        {'role':'assistant','content':'nice to meet you saivardhan'},
        {'role':'user','content':'what is my name'}
    ]
)

print(result.output_text)'''

#---now add system prompt, temperature and, max tokens
result= client.responses.create(
    model="gpt-4o",
    instructions=" your are a useful assisatant who makes jokes",
    input="what is the square root of 49",
    temperature=0.7,
    max_output_tokens=1000
)

print(result.output_text)

#--token_usage--
print(f"Input tokens:{result.usage.input_tokens}")# total number of tokens that we send to llm
print(f"Output tokens:{result.usage.input_tokens}")# total number of tokens that we got from llm
print(f"Total tokens:{result.usage.input_tokens+ result.usage.input_tokens}")# total input+total output


#----streaming----
stream = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain transformer architecture in simple words.",
    stream=True
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)