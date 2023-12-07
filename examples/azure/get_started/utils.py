import os

from dotenv import load_dotenv


def load_env(env: str):
    env_path = ''
    if env == 'TEST-35':
        env_path = os.getenv('ENVIRONMENT', '.env.test.35')
    elif env == 'TEST':
        env_path = os.getenv('ENVIRONMENT', '.env.test')
    else:
        pass

    dotenv_path = f'{env_path}'
    load_dotenv(dotenv_path=dotenv_path)

    return True
