import os

# fast api imports
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse

title = "InsightDocs"
description = "1. Feel free to inquire about anything from our personal assistant (try asking about their name and " \
              "what they do).\n" \
              "2. Easily upload a PDF document from which you wish to extract insights and information.\n" \
              "3. Post queries related to the uploaded document (try requesting a summary or ask specific questions" \
              "about the content)."

app = FastAPI(title=title, description=description)

# langchain imports
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the secret key using the key name from the .env file
secret_key = os.getenv("OPENAI_SECRET_KEY")

chat_model = ChatOpenAI(openai_api_key=secret_key)

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
)


@app.post("/", description="Your personal assistant with a personality")
async def personalAssistant(query: str = Form(...)):
    try:
        pdfreader = PdfReader("fastAPI bot.pdf")
        raw_text = ""
        for i, page in enumerate(pdfreader.pages):
            content = page.extract_text()
            if content:
                raw_text += content
        texts = text_splitter.split_text(raw_text)
        embeddings = OpenAIEmbeddings(openai_api_key=secret_key)
        document_search = FAISS.from_texts(texts, embeddings)
        chain = load_qa_chain(OpenAI(openai_api_key=secret_key), chain_type="stuff")
        docs = document_search.similarity_search(query)
        output = chain.run(input_documents=docs, question=query)
        return JSONResponse(content={"content": output})
    except:
        return JSONResponse(content={"message:": "Something went wrong"})


@app.post("/uploadfile")
def uploadFile(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


desc = 'Please provide the exact filename and query you wish to execute. Make sure the filename matches the uploaded ' \
       'file. For example, if the uploaded file is named "shopping_earth.pdf," ensure that you specify the filename as ' \
       '"shopping_earth.pdf." Using incorrect filenames may lead to inaccurate results.'


@app.post("/queries", description=desc)
async def askQueries(filename: str = Form(...), query: str = Form(...)):
    try:
        pdfreader = PdfReader(filename)
        raw_text = ""
        for i, page in enumerate(pdfreader.pages):
            content = page.extract_text()
            if content:
                raw_text += content
        texts = text_splitter.split_text(raw_text)
        embeddings = OpenAIEmbeddings(openai_api_key=secret_key)
        document_search = FAISS.from_texts(texts, embeddings)
        chain = load_qa_chain(OpenAI(openai_api_key=secret_key), chain_type="stuff")
        docs = document_search.similarity_search(query)
        output = chain.run(input_documents=docs, question=query)
        return JSONResponse(content={"content": output})
    except:
        return JSONResponse(content={"message:": f"No such files and directory found with filename: {filename}"})
