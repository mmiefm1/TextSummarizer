import streamlit as st
from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

# Cache the model
@st.cache_resource
def load_model():
    return PredictionPipeline()

st.title("📝 Text Summarizer")

text_input = st.text_area("Enter Text to Summarize", height=300)

if st.button("Summarize"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            st.info("Loading model...")
            summarizer = load_model()
            st.info("Generating summary...")
            summary = summarizer.predict(text_input)
            st.subheader("Summary:")
            st.success(summary)
        except Exception as e:
            st.error("An error occurred.")
            st.exception(e)
