
import os
import sys
import shutil
sys.path.append("/content/pdf_qa_project/scripts")

from extract import extract_text_from_pdf
from qa import ask_question

import gradio as gr

def qa_from_pdf(pdf_file, question):  
    try:  
        import io  
  
        # Support both Gradio file types: UploadedFile or file path  
        pdf_path = "/content/pdf_qa_project/pdfs/uploaded.pdf"  
  
        if isinstance(pdf_file, str):  
            # It's a path string  
            shutil.copy(pdf_file, pdf_path)  
        else:  
            # It's a file-like object  
            with open(pdf_path, "wb") as f:  
                f.write(pdf_file.read())  
  
        # Extract text  
        text_path = extract_text_from_pdf(pdf_path, "/content/pdf_qa_project/extracted_text")  
        with open(text_path, "r", encoding="utf-8") as f:  
            context = f.read()  
  
        if not context.strip():  
            return "❌ PDF has no readable text. Try another file."  
  
        if not question.strip():  
            return "❌ Please enter a valid question."  
  
        # Get answer  
        answer = ask_question(context, question)  
        return f"✅ Answer: {answer}"  
  
    except Exception as e:  
        return f"❌ Error: {str(e)}"

ui = gr.Interface(
    fn=qa_from_pdf,
    inputs=[
        gr.File(label="Upload PDF"),
        gr.Textbox(label="Ask a Question")
    ],
    outputs=gr.Textbox(label="Answer"),
    title="📄 AI PDF Q&A System",
    description="Upload a PDF and ask a question based on its content."
)

ui.launch(share=True, debug=True)
