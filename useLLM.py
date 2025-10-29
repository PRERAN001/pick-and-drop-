from dotenv import load_dotenv
import os
from groq import Groq
load_dotenv()
api_key=os.getenv('groq_api')
client = Groq(api_key=api_key)
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "user",
        "content": "hi"
      }
      ,{
          "role":"System",
          "content":"act like a general llm"
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_format="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
