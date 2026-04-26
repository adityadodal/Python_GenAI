# In this session we will learn about GenAI in Python
#

# We will learn how to use already existing llm and also hpw to fine tune the response according to our requirements
#

#


#
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

output = generator("Artificial Intelligence is",
                   max_new_tokens=40, num_return_sequences=1)
print(output[0]['generated_text'])
