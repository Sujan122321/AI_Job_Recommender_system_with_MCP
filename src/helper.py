import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from openai import OpenAI




load_dotenv()  # Load environment variables from .env file for api keys


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")      # Get OpenAI API key from environment variables
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY      # Set the OpenAI API key in the environment

client = OpenAI(api_key=OPENAI_API_KEY)  # Initialize OpenAI client with the API key



# Extract the content from the pdf
def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text = page.get_text()
    return text

# Large language function to interact with OpenAPI service
def ask_openai(prompt,max_tokens=500):
    """
    Function to interact with the OpenAPI service.

    Args:
        prompt (str): The prompt to send to the OpenAPI service.
        max_tokens (int): The maximum number of tokens to return.

    Returns:
        str: The response from the OpenAPI service.
    """
    
    response =client.chat.completions.create(
        model ="gpt-4o",
        messages=[
            {"role": "user",
             "content": prompt
             }
        ],
        temperature=0.5,
        max_tokens=max_tokens    
    )
    
    return response.choices[0].message.content  # Return the content of the response  


