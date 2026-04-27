# In this session we are gonna learn more about the generator models and also we will try
# new types of models

# '''from transformers import pipeline

# model = pipeline("text-generation", model="gpt2")

# result = model("Explain what is machine learning")
# print(result)'''

from transformers import pipeline

llm = pipeline("text2text-generation", model="google/flan-t5-small")


def ask_question(query):
    docs = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm(prompt, max_length=200)
    return response[0]['generated_text']
