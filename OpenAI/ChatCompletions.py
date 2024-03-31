from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key=os.getenv('OPENAI_API_KEY')
completions = openai.chat.completions.create(
    model='gpt-3.5-turbo',
    messages= [{'role':'User', 'content': 'Write an efficient program for sorting numbers with respect to Time complexity.'}]
)
response = completions.choices[0].content
print(response)