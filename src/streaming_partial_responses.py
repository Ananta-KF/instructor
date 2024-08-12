import instructor
from pydantic import BaseModel
from openai import OpenAI

# our desired output structure
class UserInfo(BaseModel):
    name: str
    age: int

# our OpenAI  details
api_key = 'YOUR_API_KEY'
openai_client = OpenAI(api_key=api_key)

client = instructor.from_openai(openai_client)

user_stream = client.chat.completions.create_partial(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "John Doe is 30 years old."}],
    response_model=UserInfo,
)

for user_info in user_stream:
    print(user_info)
