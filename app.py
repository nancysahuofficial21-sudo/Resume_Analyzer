import streamlit as st
import requests

st.title("🚀 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

job_desc = st.text_area("Paste Job Description (optional)")

if st.button("Analyze Resume"):

    if uploaded_file is not None:

        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue())
        }

        data = {
            "job_description": job_desc
        }

        response = requests.post(
            "http://127.0.0.1:5050/upload",
            files=files,
            data=data
        )

        result = response.json()
        st.json(result)
        st.subheader("🎯 Job Match Score")
        st.progress(result["match"]["match_percentage"] / 100)

        st.success(f"Matched Skills: {', '.join(result['match']['matched_skills'])}")
        st.error(f"Missing Skills: {', '.join(result['match']['missing_skills'])}")

    else:
        st.error("Please upload a file")
