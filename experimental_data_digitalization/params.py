from pathlib import Path
import os


repo_path = Path(__file__).parent.parent

LOCAL_DATA_PATH = repo_path.joinpath('data')

LANGCHAIN_API_KEY= os.environ.get('LANGCHAIN_API_KEY')
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY')
