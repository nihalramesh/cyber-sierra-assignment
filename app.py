import streamlit as st
import pandas as pd
from pandasai.smart_dataframe import SmartDataframe
from pandasai.llm.openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Data Explorer", layout="wide")
st.title("AI-Powered Data Explorer")
st.caption("Upload Excel or CSV files, preview your data, and ask natural language questions.")

if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []

if "user_query" not in st.session_state:
    st.session_state.user_query = ""

st.divider()

# ------------------ File Upload ------------------
uploaded_files = st.file_uploader("Upload CSV or Excel files", type=["csv", "xls", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    file_names = [file.name for file in uploaded_files]
    selected_file = st.selectbox("Select a file", file_names)
    selected_index = file_names.index(selected_file)
    file = uploaded_files[selected_index]

    n_rows = st.slider("Number of top rows to preview", min_value=1, max_value=100, value=5)

    try:
        df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
        st.markdown(f"### Top {n_rows} rows from `{file.name}`")
        st.dataframe(df.head(n_rows), use_container_width=True)

        # ------------------ Ask Question ------------------
        st.divider()
        st.markdown("## Ask a question about the data")
        user_query = st.text_input("Your question", value=st.session_state.get("user_query", ""))

        if user_query:
            st.session_state.user_query = user_query
            llm = OpenAI(api_token=OPENAI_API_KEY)
            sdf = SmartDataframe(df, config={"llm": llm})

            with st.spinner("Running analysis..."):
                try:
                    answer = sdf.chat(user_query)
                    st.success("Answer:")
                    st.write(answer)

                    # Save to prompt history
                    st.session_state.prompt_history.append({
                        "prompt": user_query,
                        "response": str(answer),
                        "feedback": None
                    })

                    # Feedback
                    st.markdown("Was this helpful?")
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button("Yes", key="fb_yes"):
                            st.toast("Thanks for your feedback!")
                            st.session_state.prompt_history[-1]["feedback"] = "Yes"
                    with col2:
                        if st.button("No", key="fb_no"):
                            st.toast("We'll use that to improve.")
                            st.session_state.prompt_history[-1]["feedback"] = "No"

                except Exception as e:
                    st.error(f"Error: {e}")

    except Exception as e:
        st.error(f"Could not read file: {e}")

# ------------------ Sidebar: Prompt History ------------------
with st.sidebar:
    st.header("Prompt History")

    if st.button("Clear History"):
        st.session_state.prompt_history = []
        st.success("History cleared.")
        st.stop()

    if st.session_state.prompt_history:
        for idx, entry in enumerate(reversed(st.session_state.prompt_history)):
            if st.button(f"{entry['prompt'][:50]}", key=f"reuse_{idx}"):
                st.session_state["user_query"] = entry["prompt"]
            if entry.get("feedback"):
                st.caption(f"Feedback: {entry['feedback']}")
    else:
        st.caption("No previous prompts yet.")
