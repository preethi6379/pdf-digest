# PDF Research Digest AI

An elegant, end-to-end AI-powered document compression pipeline that utilizes Large Language Models (LLMs) to ingest 50+ page PDF documents (scientific papers, technical manuals, financial briefs) and synthesize them into structured, high-density key fact sheets.

---

## 🧠 AI/ML Architecture & Pipeline

Unlike traditional RAG (Retrieval-Augmented Generation) setups that chunk documents and lose context, this project leverages native **large-context multimodal models** to read entire files in their native visual and semantic format.

```
   [ Upload PDF ]
         │
         ▼
[ Gemini File API ] ──► Extracts text, tables, figures, & visual layouts natively
         │
         ▼
[ Gemini 2.5 Flash ] ──► System Instructions: Zero-shot structured compression
         │
         ▼
 [ MD Fact Sheet ] ──► Rendered beautifully on the dashboard UI
```

### 1. Multimodal Document Ingestion
By uploading the PDF directly to Google's **Gemini File API**, the model analyzes the document's layout natively. This retains crucial tables, graphs, equations, and visual relationships that standard text-only OCR parsers (like PyPDF or PDFMiner) destroy.

### 2. Large-Context LLM Inference
* **Model**: `gemini-2.5-flash`
* **Context Capacity**: 1 Million+ tokens (equivalent to roughly 700,000 words, easily handling 50+ page documents).
* **Benefits**: Prevents context fragmentation. The model processes the entire document in a single attention window, ensuring that correlations between early hypotheses and late results are preserved.

### 3. Saturated Prompt Engineering
The system utilizes a structured zero-shot compression prompt designed to strip academic noise and force the model to output a strictly formatted markdown schema:
* **Objective/Hypothesis Extraction**: Isolate main claims.
* **Methodology Details**: Quantify dataset sizes, baseline models, and parameters.
* **Results & Findings**: Synthesize percentages, metrics, and comparisons.
* **Limitations**: Capture crucial edge cases and boundary conditions.

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

### 1. Prerequisites
Make sure you have **Python 3.9 or higher** installed.

### 2. Setup Directory & Environment
Clone or navigate to your project directory, then initialize your virtual environment:
```bash
cd C:\Users\HP\Desktop\pdf-digest

# Create the environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate it (Windows Command Prompt)
.\venv\Scripts\activate.bat
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
Create a `.env` file in the root folder of the project and add your Google Gemini API key:
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
