import streamlit as st
import google.generativeai as genai
import os

# Get Gemini API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# Sample elements list
elements = [
    "H", "O", "Na", "Cl", "C", "N", "Fe", "Cu", "Zn", "S"
]

st.title("🔬 Chemical Reaction Generator (Text-Based) By Pratik 😎")
st.markdown("Select elements from the periodic table to generate chemical reactions using Google Gemini.")

selected_elements = st.multiselect("Choose Elements", elements)

if selected_elements:
    prompt = (
        f"Generate 3 balanced chemical reactions involving the following elements: {', '.join(selected_elements)}.\n"
        f"Provide only the reactions in chemical equation format (e.g., H2 + O2 → H2O)."
    )

    st.info("Generating reactions...")

    try:
        response = model.generate_content(prompt)
        st.success("Here are the generated reactions:")
        st.markdown(f"```\n{response.text.strip()}\n```")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please select at least one element.")
