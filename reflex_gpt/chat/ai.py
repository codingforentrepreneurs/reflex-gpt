from decouple import config
from openai import OpenAI

OPENAI_API_KEY= config("OPENAI_API_KEY", cast=str, default=None)
OPENAI_MODEL="gpt-4o-mini"

def get_client():
    return OpenAI(api_key=OPENAI_API_KEY)

def get_llm_response(gpt_messages):
    client = get_client()
    completion = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=gpt_messages
    )
    return completion.choices[0].message.content