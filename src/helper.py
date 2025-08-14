import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
import google.generativeai as genai 

load_dotenv()  # Load environment variables from .env file

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)  # Correct configuration for Gemini

# Initialize model (Gemini 1.5 Flash is the current name as of July 2024)
model = genai.GenerativeModel('gemini-1.5-flash')

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file: File object or bytes of the PDF
        
    Returns:
        str: The extracted text from the PDF
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()  # Fixed: Accumulate text from all pages
    return text

def ask_gemini(prompt):
    """
    Function to interact with Gemini AI
    
    Args:
        prompt (str): The prompt to send to Gemini
        
    Returns:
        str: The response from Gemini
    """
    response = model.generate_content(prompt)
    return response.text  # Get the text from Gemini's response