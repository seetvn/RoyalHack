import openai
import os

secret_key="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"
openai.api_key = secret_key

def summ():
    with open('messages.csv') as f:
        lines = f.read()
    #print(f)
    
    model_engine = "text-davinci-002"
    prompt = lines + "\n Summarise this conversation in TLDR format"
    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=750,
        n=1,
        stop=None,
        temperature=0.3,
    )
    
    message = completion.choices[0].text
    return message

#print(summ())