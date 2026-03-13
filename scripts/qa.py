
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def ask_question(text, question):
    result = qa_pipeline({
        "context": text,
        "question": question
    })
    return result["answer"]
