import os
from dotenv import load_dotenv
from google import genai

# 1. Load configuration variables
load_dotenv()

# 2. Initialize the Gemini API client
client = genai.Client()

def generate_digest(file_path: str) -> str:
    """
    Uploads a PDF file to the Gemini File API, requests a structured
    research digest summary, and cleans up the uploaded file afterwards.
    """
    # 3. Safety Check: Verify file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
        
    print(f"Uploading {file_path} to Gemini File API...")
    
    # 4. Upload the PDF file
    uploaded_file = client.files.upload(file=file_path)
    
    # 5. Define the extraction prompt
    prompt = """
    You are an expert scientific researcher. Analyze the uploaded PDF document and compile a high-density Research Digest.
    Filter out all fluff, introductory history, and standard boilerplate. Extract only the key operational facts.
    
    Structure your response using the following Markdown sections:
    
    # Research Digest: [Document Title]
    
    ## 1. Core Objective & Hypothesis
    - What is the primary problem being solved?
    - What is the main hypothesis or objective?
    
    ## 2. Methodology & Experimental Setup
    - How did the authors test their hypothesis? 
    - Detail the models, datasets, physical setups, or experimental parameters used (include key numbers/sizes).
    
    ## 3. Key Findings & Quantitative Results
    - What are the major outcomes? 
    - List specific metrics, percentages, coefficients, or comparative improvements (e.g., "Accuracy increased by 14.2%").
    
    ## 4. Crucial Data Points & Tables Summary
    - Summarize any key charts, graphs, or tables present in the document.
    
    ## 5. Limitations & Future Work
    - What are the stated limitations of this research?
    - What future directions do the authors propose?
    """
    
    try:
        print("Analyzing document and generating digest...")
        # 6. Request generation from the Gemini model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[uploaded_file, prompt]
        )
        return response.text
        
    finally:
        # 7. Clean up the file from Google's servers
        print(f"Cleaning up: deleting {uploaded_file.name} from Gemini API storage...")
        client.files.delete(name=uploaded_file.name)