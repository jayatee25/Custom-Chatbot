!pip install langchain
!pip install openai

!pip install langchain_community

from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.question_answering import load_qa_chain

!pip install tiktoken

!pip install PyPDF2

!pip install python-docx

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS

#this is a function that will read pdf

def pdf_reader(file):
  pdfreader = PdfReader(file);
  text = ''
  for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
      text = text + content
  text = text.replace('\n', ' ')
  return text

import pandas as pd

# functions to read XLSX and CSV files

def excel_reader(file):
  df = pd.read_excel(file)
  return df.to_string()

def csv_reader(file):
  df = pd.read_csv(file)
  return df.to_string()

#function to read DOC files

from docx import Document

def doc_reader(file):
  doc = Document(file)
  content = []
  for paragraph in doc.paragraphs:
    content.append(paragraph.text)

  con = ''.join(content)
  return con

# finding out the file extension
def file_reader(file):

  split = os.path.splitext(file)
  file_extension = split[1]

  if file_extension == '.pdf':
    return pdf_reader(file)
  elif file_extension == 'xlsx':
    return excel_reader(file)
  elif file_extension == '.csv':
    return csv_reader(file)
  elif file_extension == '.docx':
    return doc_reader(file)
  else:
    return 'File type not supported'

import os
import openai

openai.api_key =  "<OPENAI-API-KEY>"

def create_code(prompt):
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = prompt,
        temperature = 0.9,
        max_tokens = 250,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.5
    )

    answer = response.choices[0].text
    return answer

from math import *

def execute_code(code):
  ans = exec(code)
  return ans

"""Putting everything together"""

user_prompt = input('User prompt: ')

text = file_reader('test file.pdf')
prompt = user_prompt + '\n' + text

prompt = prompt.replace('\n', ': ')

required_code = create_code(prompt)
print(required_code)

answer = execute_code(required_code)
print(answer)

# this is to check for docx files

text = file_reader('test file doc.docx')

user_prompt = input('User prompt: ')
prompt = user_prompt + '\n' + text

prompt = prompt.replace('\n', ': ')

prompt

required_code = create_code(prompt)
print(required_code)

answer = execute_code(required_code)
print(answer)

df = file_reader('test file csv.csv')
df

user_prompt = input('User prompt: ')
prompt = user_prompt + '\n' + df

prompt = prompt.replace('\n', ': ')

prompt

required_code = create_code(prompt)
print(required_code)

answer = execute_code(required_code)
print(answer)

