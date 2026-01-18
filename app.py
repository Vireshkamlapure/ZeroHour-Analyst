import streamlit as st
import pandas as pd
import google.generativeai as genai
import io
import time

# --- 1. Setup & Configuration ---
# layout="wide" sets the page to full screen width (no margins)
st.set_page_config(page_title="ZeroHour Analyst", layout="wide")

try:
    API_KEY = st.secrets["general"]["gemini_api_key"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("⚠️ API Key not found. Please check Step 1 setup.")
    st.stop()

# --- 2. The Logic Functions ---

def get_dataset_info(file):
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return None, None, "Error: Unsupported file type."

        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()

        summary = f"""
        DATASET METADATA:
        - Filename: {file.name}
        - Columns: {list(df.columns)}
        - Shape: {df.shape}
        - Column Details:
        {info_str}
        
        SAMPLE DATA:
        {df.head(3).to_markdown(index=False)}
        """
        return df, summary, None
    except Exception as e:
        return None, None, str(e)

def analyze_with_ai(summary_text, project_context):
    """
    Hybrid Prompt: Combines 'Senior Data Scientist' (Strategy) + 'Professor' (Theory).
    """
    models_to_try = ['gemini-2.0-flash', 'gemini-2.0-flash-lite', 'gemini-flash-latest']
    
    prompt = f"""
    You are a Senior Lead Data Scientist who also mentors students.
    
    Context: I am a student working on: "{project_context}"
    My Dataset Metadata:
    {summary_text}
    
    Provide a "Hybrid Analysis" that balances professional strategy with educational theory.
    Structure your response exactly like this:

    ### 1. 🌍 Industry & Theoretical Context
    - **The Domain:** Briefly explain the industry (e.g., Precision Agriculture, Fintech).
    - **The "Why":** Explain theoretically why this specific data helps solve the problem.

    ### 2. 🔬 The Data Scientist's Assessment
    - **Quality Check:** Critique the columns. Are there nulls? Wrong types?
    - **Technical Warning:** If something is missing (like coordinates or timestamps), explain *why* that is a risk for modeling.

    ### 3. 🧪 Key Hypotheses (Scientific Questions)
    - Propose 3 specific questions to test.
    - *Format:* "Question: [Question] -> Theory: [Why this matters]"

    ### 4. 🚀 Execution Roadmap (Step-by-Step)
    - **Phase 1: EDA:** What specific plots should I make?
    - **Phase 2: Pre-processing:** How should I handle the specific columns in this file?
    - **Phase 3: Modeling:** Which algorithms fit this data type (e.g., Random Forest vs. ARIMA) and why?
    
    Output Format: Clean Markdown. Keep it professional but encouraging.
    """

    last_error = None
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            last_error = e
            continue
            
    return f"⚠️ Analysis failed. Error: {str(last_error)}"

def stream_text(text):
    """Simulates the 'Typing' effect"""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

# --- 3. The User Interface ---

st.title("⏱️ ZeroHour Analyst")
st.caption("Senior Data Science Mentor | Powered by Gemini 2.0 Flash")
st.caption("Developed by : Viresh Kamlapure | Git-ID : Vireshkamlapure")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Project Setup")
    project_context = st.text_area("Project Goal", height=150, placeholder="e.g. Predicting Crop Yield based on soil")
    uploaded_file = st.file_uploader("Upload Dataset", type=['csv', 'xlsx'])
    analyze_btn = st.button("✨ Run Analysis", type="primary", disabled=not (uploaded_file and project_context))

# Main Area
if uploaded_file and project_context and analyze_btn:
    df, summary, error = get_dataset_info(uploaded_file)
    
    if error:
        st.error(error)
    else:
        # 1. Data Snapshot (Full Width)
        st.subheader("1. Data Snapshot")
        st.dataframe(df.head(), use_container_width=True)
        
        # 2. AI Analysis
        st.subheader("2. Mentor's Analysis")
        
        with st.spinner("🧠 Synthesizing theory and strategy..."):
            ai_response = analyze_with_ai(summary, project_context)
            
            # Streaming Effect
            response_placeholder = st.empty()
            streamed_text = ""
            for chunk in stream_text(ai_response):
                streamed_text += chunk
                response_placeholder.markdown(streamed_text)
            
            # Copy Button (Hidden in Expander)
            st.markdown("---")
            with st.expander("📋 Copy Full Report"):
                st.code(ai_response, language="markdown")

elif not analyze_btn:
    st.info("👈 Upload your dataset and tell me about your project to start.")
