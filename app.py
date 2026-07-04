import streamlit as st
import os
import tempfile
from summarizer import generate_digest

# 1. Page Configuration
st.set_page_config(
    page_title="PDF Research Digest",
    page_icon="📄",
    layout="centered"
)

# 2. Inject Custom CSS for Colorful Styling (Maximum 8 Colors - No Blue, No Black, No Pastels)
# Color Palette:
# 1. #5A001C (Deep Maroon - main app background)
# 2. #3E0010 (Dark Burgundy - sidebar & card backgrounds)
# 3. #9E0031 (Ruby Red - borders & dividers)
# 4. #FF007F (Hot Pink - accents & highlights)
# 5. #FF7700 (Vibrant Orange - primary buttons & header gradients)
# 6. #FFFF00 (Neon Yellow - main high-contrast text)
# 7. #00FF00 (Neon Green - hover effects, success messages, download button)
# 8. #D90429 (Saturated Red - error states)
st.markdown("""
    <style>
    /* Main App Background & Text */
    .stApp {
        background: radial-gradient(circle at top left, #5A001C, #3E0010) !important;
        color: #FFFF00 !important;
        font-family: 'Inter', -apple-system, sans-serif !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #3E0010 !important;
        border-right: 2px solid #9E0031 !important;
    }
    [data-testid="stSidebar"] * {
        color: #FFFF00 !important;
    }
    
    /* Header/Title gradients */
    h1, h2, h3 {
        background: linear-gradient(135deg, #FF007F, #FF7700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }
    
    /* Input & Upload container styling */
    [data-testid="stFileUploader"] {
        background-color: #3E0010 !important;
        border: 2px dashed #FF007F !important;
        border-radius: 12px !important;
        padding: 25px !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #00FF00 !important;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.15) !important;
    }
    
    /* Custom button styling */
    div.stButton > button {
        background: linear-gradient(135deg, #FF7700, #FF007F) !important;
        color: #3E0010 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 28px !important;
        font-weight: bold !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 10px rgba(255, 119, 0, 0.2) !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #00FF00, #FF7700) !important;
        color: #3E0010 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(0, 255, 0, 0.4) !important;
    }
    div.stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    /* Alert cards custom styles */
    div.stAlert {
        border-radius: 8px !important;
        border: 1px solid #9E0031 !important;
        background-color: #3E0010 !important;
    }
    
    /* Download button */
    div.stDownloadButton > button {
        background-color: transparent !important;
        color: #00FF00 !important;
        border: 2px solid #00FF00 !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
    }
    div.stDownloadButton > button:hover {
        background-color: #00FF00 !important;
        color: #3E0010 !important;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.3) !important;
    }
    
    /* JSON elements and file info boxes */
    pre, code {
        background-color: #5A001C !important;
        border: 1px solid #9E0031 !important;
        border-radius: 6px !important;
        color: #00FF00 !important;
    }
    
    /* Streamlit divider line styling */
    hr {
        border-top: 1px solid #9E0031 !important;
        opacity: 0.5;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Info & Setup Instructions
with st.sidebar:
    st.title("Settings & Info")
    st.write("This application compresses long PDF documents into structured research digests.")
    st.write("### Powered by:")
    st.markdown("- **Google Gemini 2.5 Flash**")
    st.markdown("- **Streamlit UI**")
    
    st.divider()
    
    # Check if API Key is configured in the environment
    api_key_check = os.getenv("GEMINI_API_KEY")
    if api_key_check:
        st.success("API Key Status: Configured ✓")
    else:
        st.error("API Key Status: Missing ✗")
        st.info("Please set the GEMINI_API_KEY in your `.env` file.")

# 4. Main Dashboard Header
st.title("📄 PDF Research Digest")
st.subheader("Auto-compress 50+ page PDFs into structured key facts.")
st.write("Upload a research paper, business report, or document below to generate a high-density summary.")

# 5. File Uploader Component
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    # Display details of the uploaded file
    file_details = {
        "Filename": uploaded_file.name, 
        "FileType": uploaded_file.type, 
        "FileSize": f"{uploaded_file.size / (1024*1024):.2f} MB"
    }
    st.write("File Details:")
    st.json(file_details)
    
    # 6. Trigger Button
    if st.button("🚀 Generate Fact Sheet Digest"):
        # Create a secure temporary directory to hold the file
        with tempfile.TemporaryDirectory() as temp_dir:
            # Construct a safe path within the temp directory
            temp_file_path = os.path.join(temp_dir, uploaded_file.name)
            
            # 7. Save the uploaded file to disk
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Show a progress spinner while generating the summary
            with st.spinner("Analyzing document structure and extracting key facts..."):
                try:
                    # 8. Call the summarizer function
                    digest_text = generate_digest(temp_file_path)
                    
                    st.success("Analysis Complete!")
                    st.divider()
                    
                    # 9. Render the Markdown Output
                    st.markdown(digest_text)
                    
                    st.divider()
                    
                    # 10. Add a Download Button
                    st.download_button(
                        label="📥 Download Digest (Markdown)",
                        data=digest_text,
                        file_name=f"{os.path.splitext(uploaded_file.name)[0]}_digest.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {e}")