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
generator("Once upon a time", max_new_tokens=40)[0]['generated_text']

print(generator("Once upon a time", max_new_tokens=70)[0]['generated_text'])

print(generator("once upon a time in Germany during world war 2",
      max_new_tokens=70)[0]['generated_text'])

# We can also specify the temperature parameter to control the randomness of the output

print(generator("once upon a time in Germany during world war 2",
      max_new_tokens=70, temperature=0.9)[0]['generated_text'])

print(generator("History of Adolf Hitler during world war 2",
      max_new_tokens=99, temperature=0.9)[0]['generated_text'])


model = pipeline("text2text-generation", model="google/flan-t5-small")
result = model("Explain what is machine learning")
print(result)
