# streamlit_app.py

import streamlit as st
from src.search_agent import SearchAgent
from src.summarizer_agent import SummarizerAgent
from src.relevance_checker_agent import RelevanceCheckerAgent
# from pdf.generator import generate_pdf  # 👈 New import

st.set_page_config(page_title="🧠 AI Research Assistant", page_icon="📚")
st.title("📚 AI Research Assistant")
st.write("Ask any research topic and get relevant papers with summaries and relevance scores!")

query = st.text_input("🔍 Enter your research topic/question:")

if st.button("Run Research"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("🔎 Searching for papers..."):
            search_agent = SearchAgent()
            search_results = search_agent.search_papers(query)
        st.success("✅ Found relevant papers")
        st.markdown(search_results)

        with st.spinner("📝 Summarizing papers..."):
            summarizer_agent = SummarizerAgent()
            summary_results = summarizer_agent.summarize_papers(search_results)
        st.success("✅ Summaries ready")
        st.markdown(summary_results)

        with st.spinner("📌 Evaluating relevance..."):
            relevance_agent = RelevanceCheckerAgent()
            relevance_results = relevance_agent.check_relevance(summary_results, query)
        st.success("✅ Relevance check complete")
        st.markdown("### 🧾 Relevance Evaluation")
        st.markdown(relevance_results)

        # PDF download
        # Your existing code works as-is
        # pdf_bytes = generate_pdf(query, search_results, summary_results, relevance_results)
        # st.download_button(
        #     label="📄 Download Report as PDF",
        #     data=pdf_bytes,
        #     file_name="research_report.pdf",
        #     mime="application/pdf"
        # )
