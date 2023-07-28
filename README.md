# InsightDocs : An API Which Helps You To Skim Research Papers 

# Contents

1. Introduction
2. Installation guide
3. Project Screen Shots
4. Endnotes

# Introduction

API that empowers users to upload PDF documents, like research papers, and interact with a personalized AI assistant. Users can ask queries related to the document, provides insightful responses and assistance.

## Tech stack used

`python`, `fastAPI`,`langchian`,` openai`,  `PyPDF2` etc...

# Installation guide

1. Clone the git repository using the link ```https://github.com/mechXsteam/InsightDocs.git``` or simply download
   the zip file.
2. Paste your openai secret key in the .env file.
   > Make sure you paste your openai secret key, otherwise the project will not work.
3. First navigate to the root directory (the one which contains the main.py file) and run
command `uvicorn main:app --reload` in the terminal, it will fire off a developement server at port:8000
on your local machine, simply click the link in the terminal. Navigate to http://localhost:8000/docs to view the project.

# Project screenshots

| Chat with personal AI chatbot [1/8]                                                   | Swagger docs [2/8]                                                                      |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![home page](https://i.pinimg.com/750x/ad/05/fa/ad05faa438893ba4079a771a14bc76e4.jpg) | ![working 2/2](https://i.pinimg.com/750x/a4/77/55/a4775552064b01b243003e68bac923f8.jpg) |

| Upload pdf file[3/8]                                                                  | Ask queries related to the document [4/8]                                               |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![home page](https://i.pinimg.com/750x/df/52/11/df521158866eab5ec5b5b17b8676f92b.jpg) | ![working 2/2](https://i.pinimg.com/750x/56/f4/94/56f4947c5ef66afa39584cae8932b3a6.jpg) |

# Endnotes

This project has been a challenging yet rewarding journey, as it taught me how to get started with langchian and openai. I've gained valuable insights into handling complex projects along the way. If you happen
to come across any flaws in the code or encounter errors, don't hesitate to get in touch with me. Your feedback is
highly
appreciated. Feel free to build a frontend around it. Please consider showing your support by giving this project a star. Thank you!
