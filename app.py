import streamlit as st
from transformers import pipeline

# --- Global Model Loading (Cached for efficiency) ---
# This function will only run once, even if Streamlit reruns the script.
# This is crucial for performance as models are large and take time to load.
@st.cache_resource
def load_summarizer_model():
    print("Loading summarization pipeline... (This happens once)")
    # Initialize the summarization pipeline with a pre-trained model.
    # 'facebook/bart-large-cnn' is a good general-purpose choice.
    # It will download the model the first time it's run.
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("Summarizer model loaded.")
    return summarizer

# Load the summarizer model when the app starts
summarizer = load_summarizer_model()

# --- Streamlit UI Components ---

st.set_page_config(page_title="Text Summarizer", page_icon="📝")

st.title("📝 Text Summarizer")
st.markdown("""
    Enter any long text below, and I will generate a concise summary for you!.
""")

# Text area for user input
input_text = st.text_area(
    "Enter your text here:",
    height=300,
    placeholder="Paste your article, blog post, or any long text here...",
    key="input_text_area"
)

# Sliders for min_length and max_length
st.subheader("Summary Length Controls")
col1, col2 = st.columns(2)

with col1:
    min_len = st.slider(
        "Minimum Summary Length (words):",
        min_value=10,
        max_value=100,
        value=30,
        step=5,
        key="min_len_slider"
    )
with col2:
    max_len = st.slider(
        "Maximum Summary Length (words):",
        min_value=50,
        max_value=300,
        value=150,
        step=10,
        key="max_len_slider"
    )

# Summarize button
if st.button("Summarize Text", key="summarize_button"):
    if input_text:
        with st.spinner("Generating summary... This might take a moment."):
            try:
                # Call the summarizer model
                # The min_length and max_length here refer to tokens, not strict word counts.
                # 1 token is roughly 1 word, but can vary.
                summary_output = summarizer(
                    input_text,
                    min_length=min_len,
                    max_length=max_len,
                    do_sample=False  # Makes the output more consistent
                )
                generated_summary = summary_output[0]['summary_text']

                st.subheader("✨ Generated Summary")
                st.success(generated_summary) # Display summary in a success box

                st.markdown("---")
                st.subheader("Original Text (for reference)")
                st.expander("Click to view original text").write(input_text) # Allows hiding long text

            except Exception as e:
                st.error(f"An error occurred during summarization: {e}")
                st.warning("Please ensure your input text is not too short or too long for the selected lengths.")
    else:
        st.warning("Please enter some text to summarize!")

st.markdown("---")
st.caption("Powered by Hugging Face Transformers and Streamlit")