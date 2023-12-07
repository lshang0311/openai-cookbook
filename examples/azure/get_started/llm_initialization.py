import os

import openai
from langchain.chat_models import AzureChatOpenAI


def init_llm():
    OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
    OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

    openai.api_key = os.environ['OPENAI_API_KEY']
    openai.api_base = os.environ['OPENAI_API_BASE']
    openai.api_version = os.environ['OPENAI_API_VERSION']
    openai.api_type = os.environ['OPENAI_API_TYPE']

    temperature = 0
    max_tokens = 5000

    llm = AzureChatOpenAI(
        deployment_name=OPENAI_DEPLOYMENT_NAME,
        model=OPENAI_MODEL_NAME,
        temperature=temperature,
        max_tokens=max_tokens
    )

    return llm


def init_client():
    client = openai.AzureOpenAI(
        azure_endpoint=os.environ['OPENAI_API_BASE'],
        api_key=os.environ['OPENAI_API_KEY'],
        api_version=os.environ['OPENAI_API_VERSION']
    )

    return client
