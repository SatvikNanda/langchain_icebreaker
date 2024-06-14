import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain")
    print(os.environ['OPEN_AI_KEY'])