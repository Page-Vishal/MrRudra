import os
from dotenv import load_dotenv
from groq import Groq
import time

load_dotenv()
groq_client   = Groq  ( api_key = os.getenv("GROQ_KEY") )

sys_msg = (
    'You are a multi-modal AI voice assistant. Your user may or may not have attached a photo for context '
    '(either a screenshot or a webcam capture). Any photo has already been processed into a highly detailed '
    'text prompt that will be attached to their transcribed voice prompt. Generate the most useful and '
    'factual response possible, carefully considering all previous generated text in your response before '
    'adding new tokens to the response. Do not expect or request images, just use the context if added. '
    'Use all the context of this conversation so your response is relevant to the conversation. Make '
    'your responses clear and concise, avoiding any verbosity. Make sure to give short answers to requested prompt.'
)

convo = [ {'role': 'system', 'content': sys_msg} ]

def groq_prompt(prompt, img_context):
    if img_context:
        prompt = f'USER PROMPT: {prompt}\n\n    IMAGE CONTEXT:{img_context}'
    convo.append( {'role':'user', 'content': prompt} )

    chat_completion = groq_client.chat.completions.create(messages=convo, model = "gemma2-9b-it")
    response = chat_completion.choices[0].message
    print(response,"\n")
    convo.append(response)
    print("\n",convo,"\n")
    #return response

while True:
    prompt= input("Input: ")
    groq_prompt(prompt=prompt, img_context=None)
    time.sleep(1)