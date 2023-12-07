import os

from llm_initialization import init_llm, init_client
from utils import load_env

# env
_env = "TEST"  # TEST for gpt-4
load_env(_env)

# llm
llm = init_llm()

# client
client = init_client()
completion = client.chat.completions.create(
    messages=[{"role": "user",
               "content": "What are the differences between Azure Machine Learning and Azure AI services?"}],
    model=os.environ['OPENAI_DEPLOYMENT_NAME'],
    temperature=0
)
print(completion)

print()
