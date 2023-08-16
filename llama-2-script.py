# !pip install replicate

import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "" # Add your API key here. Get a key from: https://replicate.com/account
# Prompts
pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
prompt_input = "What is Python?"

# Generate LLM response
output = replicate.run('replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781', # LLM 2 70B model
                        input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})  # Model parameters


full_response = ""
# Add all text together to form a readable sentence
for item in output:
  full_response += item

print(full_response) #print full text
