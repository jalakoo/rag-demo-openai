from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from secrets_manager import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

LLM = ChatOpenAI(temperature=0)
EMBEDDINGS = OpenAIEmbeddings()