from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
client= OpenAI()

result=client.responses.create(
    model='gpt-4',
    instructions='your a helpul assistant',
    input='give me a name, age and city of a fictional character'
)

print(result.output_text)
''' in the above we get output in string format but when we want our output in json format
we have use pydantic'''

#---------what is pydantic-------------
#pydantic lets you define the exact "shape" and "size" and data you expect
#each field has a type (str,int, float, bool, list etc..)

#when we pass a text_format =person, SDK converts it pass into a
#json schema and sends it to openAI servers. the model is contreained
#at the sever level to only return data that matches this schema

class person(BaseModel):
    name:str
    age:int
    city:str
    
result=client.responses.parse(
    model='gpt-4',
    instructions='you are helpful assistant',
    input='give me a name, age and city of a fictional character',
    text_format=person
)

person=result.output_parsed
print(person)