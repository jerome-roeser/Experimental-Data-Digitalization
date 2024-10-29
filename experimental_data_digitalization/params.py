from pathlib import Path
import os


repo_path = Path(__file__).parent.parent

PDF_CATEGORY= os.environ.get('PDF_CATEGORY')
LOCAL_DATA_PATH = repo_path.joinpath('data', 'pdfs', f"{PDF_CATEGORY}")


LANGCHAIN_API_KEY= os.environ.get('LANGCHAIN_API_KEY')
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY')
