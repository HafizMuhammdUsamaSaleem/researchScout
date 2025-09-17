import streamlit as st
from src.search_agent import SearchAgent
from src.researcher_info_agent import ResearchInfoAgent
from src.article_agent import ArticleAgent
from src.utils import filter_results
st.set_page_config(page_title="🧠 AI Research Assistant", page_icon="📚")
st.title("📚 AI Research Assistant")
st.write("Ask about a research topic and choose whether to search **academic papers** or **popular articles**.")

# --- User Input ---
query = st.text_input("🔍 Enter your research topic/question:")
search_type = st.selectbox("📂 What do you want to search?", ["Research Papers", "Popular Articles"])

# --- Run button ---
if st.button("Run Search"):
    if not query.strip():
        st.warning("⚠️ Please enter a query.")
    else:
        if search_type == "Research Papers":
            with st.spinner("🔎 Searching for research papers..."):
                search_agent = SearchAgent()
                search_results = search_agent.search_papers(query)
                search_results = filter_results(search_results)
                if not search_results:
                    st.warning("⚠️ No valid open-access papers found.")
                else:
                    st.success("✅ Found relevant papers")
                    for r in search_results:
                        st.markdown(f"- [{r['title']}]({r['url']})")
            with st.spinner("👤 Gathering researcher info..."):
                researcher_agent = ResearchInfoAgent()
                researcher_info = researcher_agent.researcher_info(search_results, query)
            st.success("✅ Researcher insights ready")
            st.markdown("### 👨‍🔬 Researcher Info")
            st.markdown(researcher_info)

        elif search_type == "Popular Articles":
            with st.spinner("📰 Searching for popular articles..."):
                article_agent = ArticleAgent()
                article_results = article_agent.search_articles(query)
                article_results = filter_results(article_results)
                if not article_results:
                    st.warning("⚠️ No valid open-access papers found.")
                else:
                    st.success("✅ Found relevant articles")
                    for r in article_results:
                        st.markdown(f"- [{r['title']}]({r['url']})")

