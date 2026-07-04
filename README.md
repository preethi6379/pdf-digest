# PDF Research Digest AI

An elegant, automated web application that leverages Google Gemini's large context capabilities to compress 50+ page PDF documents (research papers, legal briefs, financial reports) into highly structured, high-density key fact sheets.

---

## 🎨 Color Palette & Theme System

This application utilizes a strict, custom **8-color palette** built using Streamlit's style configurations and advanced CSS injections. It features a bold, high-contrast cyber-neon-crimson theme with absolutely **no blue, no black, and no pastel colors**:

1. **Deep Maroon (`#5A001C`)**: App background canvas (a rich, saturated dark burgundy).
2. **Dark Burgundy (`#3E0010`)**: Secondary card backgrounds and sidebar panels.
3. **Ruby Red (`#9E0031`)**: Borders, dividers, and secondary details.
4. **Hot Pink (`#FF007F`)**: Active accents, highlights, and uploader borders.
5. **Vibrant Orange (`#FF7700`)**: Header gradients and primary action buttons.
6. **Neon Yellow (`#FFFF00`)**: Primary readable text (glowing high-density text).
7. **Neon Green (`#00FF00`)**: Success elements, download buttons, and hover highlights.
8. **Saturated Red (`#D90429`)**: Error warning messages and exception labels.

---

## 📂 Folder Structure

```text
pdf-digest/
├── .env                   # Environment config (stores GEMINI_API_KEY)
├── requirements.txt       # Project python package requirements
├── app.py                 # Streamlit UI, visual styles, and user flow
├── summarizer.py          # Gemini API client initialization & prompts
└── README.md              # Project documentation (this file)
```

---

## ⚡ Setup & Installation

Follow these steps to configure the project on your machine:

### 1. Prerequisites
Make sure you have **Python 3.9 or higher** installed.

### 2. Clone/Move to Directory
Navigate to your project directory:
```bash
cd C:\Users\HP\Desktop\pdf-digest
```

### 3. Initialize Virtual Environment
Create and activate an isolated Python environment:
```bash
# Create the environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate it (Windows Command Prompt)
.\venv\Scripts\activate.bat
```

### 4. Install Dependencies
Install all required dependencies with pip:
```bash
pip install -r requirements.txt
```

### 5. Setup Environment Variables
Create a file named `.env` in the root folder of the project and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🚀 Running the Application

To launch your development server, run the following command in your active terminal:

```bash
streamlit run app.py
```

Streamlit will launch a local development server and open a window in your default browser at `http://localhost:8501`.

---

## 🔬 How It Works Under the Hood

1. **Ingestion**: The user uploads a PDF file which Streamlit buffers into memory.
2. **Local Buffer**: The app creates a temporary directory to save the file locally, generating a file path pointer.
3. **Gemini Upload**: Using the `google-genai` SDK, the PDF is uploaded directly to the Gemini File API. This allows Gemini to parse text, formatting, tables, and images natively rather than relying on messy local OCR parsers.
4. **Structured Inference**: Gemini 2.5 Flash is invoked with a custom system prompt that acts as a structural guide to extract core objectives, methodologies, quantitative outputs, and key data points.
5. **Clean Up**: The temporary local file and the remote Gemini API file are deleted immediately after processing to respect user privacy and security guidelines.
6. **Rendering & Export**: The final structured markdown text is rendered inside a beautiful customized UI container along with a file download handler.
