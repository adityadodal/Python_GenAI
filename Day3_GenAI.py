# In this session we will learn about Large Language Models (LLMs) and Generative AI.
#  We will explore how to use
# LLMs to generate text,
#  answer questions, and create content.
# We will also discuss the ethical considerations and potential applications
# of generative AI in various fields.


# Let's start by installing the necessary libraries for working with LLMs.
# We will use the Hugging Face Transformers library, which provides a wide range of pre-trained models for natural language processing tasks.

# Install the Transformers library
from transformers import pipeline
#!pip install transformers
# Now, let's import the necessary modules and load a pre-trained LLM.
# Load a pre-trained language model for text generation
generator = pipeline('text-generation', model='gpt2')
# Now that we have our generator set up, we can use it to generate text based on a given prompt. Let's try it out with a simple prompt.
prompt = "Once upon a time"
generated_text = generator(prompt, max_length=50, num_return_sequences=1)
# Print the generated text
print(generated_text[0]['generated_text'])
# As you can see, the model has generated a continuation of the prompt "Once upon a time". You can experiment with different prompts and parameters to see how the model responds.
# For example, you can change the max_length to generate longer or shorter text, or you can increase the num_return_sequences to get multiple variations of the generated text.
# Let's try generating multiple variations of the same prompt.
generated_texts = generator(prompt, max_length=50, num_return_sequences=3)
# Print the generated texts
for i, text in enumerate(generated_texts):
    print(f"Generated Text {i+1}: {text['generated_text']}\n")
# In addition to text generation, LLMs can also be used for other tasks such as question answering, summarization, and translation. Let's see how we can use a pre-trained model for question answering.
# Load a pre-trained model for question answering
qa_pipeline = pipeline(
    # Note: 'document-question-answering' is used for models that can handle longer contexts, while 'question-answering' is typically used for shorter contexts.
    'document-question-answering',
    # This is a smaller, faster model that is fine-tuned on the SQuAD dataset for question answering tasks.
    model='distilbert-base-cased-distilled-squad'
)
# Define a context and a question
# This is the context that the model will use to answer the question. It contains the information that the model needs to know in order to provide an answer.
context = "The capital of France is Paris."
# This is the question that we want the model to answer based on the provided context.
question = "What is the capital of France?"
# Use the model to answer the question based on the context
# The model will analyze the context and the question to generate an answer. The output will typically include the answer text and a confidence score indicating how confident the model is in its answer.
answer = qa_pipeline(question=question, context=context)
# Print the answer
print(f"Answer: {answer['answer']}")
# As you can see, the model correctly identified "Paris" as the answer to the question
# This is just a brief introduction to working with LLMs and generative AI. There are many more models and techniques to explore, and the field is rapidly evolving.
# It's important to keep in mind the ethical considerations when using generative AI, such as ensuring that the generated content is not harmful or misleading, and being transparent about the use of AI in content creation.
# With that said, I encourage you to experiment with different models and applications of generative AI to see how it can be used in various fields such as creative writing, customer service, and more.
