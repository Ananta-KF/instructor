import instructor
from pydantic import BaseModel
from openai import OpenAI

# our desired output structure
class UserInfo(BaseModel):
    name: str
    age: int

# our OpenAI details
api_key = 'YOUR_API_KEY'
openai_client = OpenAI(api_key=api_key)

client = instructor.from_openai(openai_client)

user_info = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=UserInfo,
    messages=[{"role": "user", "content": "John Doe is 30 years old."}],
)

print(user_info.name)  # expected output: John Doe
print(user_info.age)   # expected output: 30
