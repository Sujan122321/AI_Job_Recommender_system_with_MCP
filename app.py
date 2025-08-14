import streamlit as st
from src.helper import extract_text_from_pdf,ask_gemini
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs


st.set_page_config(
    page_title="Job Recommender",
    layout="wide"
)
st.title("📃AI Based Job Recommender System")
st.markdown("Upload your resume and get job recommendations based on your skills and experience from linkedin and naukri.")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])
if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        
    with st.spinner("Summerizing resume..."):
        summary = (f"Summarize the following resume highlighting the skills, education, training and expericence:\n\n{resume_text}")
    
    with st.spinner("Finding skill gaps..."):
        skill_gap = ask_gemini(f"Analyze this resume and highlight missing skills,  certifications and experiences need for better job opportunity:\n\n{resume_text} ")
        
    with st.spinner("Creating future roadmap..."):
        roadmap = ask_gemini(f"Based on this resume suggest a  future roadmap to improve this person's carrer prospects (skills and certification needed, industry exposure):\n\n{resume_text}")\
    
    # Display nicely formatted results
    st.markdown(ask_gemini("-----------"))
    st.header("📑Resume Summary")  
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; color:white;'>{summary}</div>", unsafe_allow_html=True)      
    
    st.markdown("-----------")
    st.header("🔍Skill Gap and Missing Areas")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; color:white;'>{skill_gap}</div>", unsafe_allow_html=True)
    
    st.markdown("-----------")
    st.header("🚀Future Roadmap")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; color:white;'>{roadmap}</div>", unsafe_allow_html=True)
    
    st.success("✅Analysis Completed successfully!")
    
    
    if st.button("Get Job Recommendations"):
        with st.spinner("Fetching job recommendations..."):
            keywords = ask_gemini(
                f"Based on this resummary, suggest the best job titles and keywords for searching jobs. Give a comma-sepearted list only, no explination.\n\nSummary: {summary}"
            )
            search_keywords_clean = keywords.replace("\n", "").strip()
        st.success(f"Extracted job keywords: {search_keywords_clean}")
        
        with st.spinner("Fetching jobs from LinkedIn and Nakuri..."):
            linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=60)
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean, rows=60)
            
            
            
        st.markdown("-----------") 
        st.header("🔗Job Recommendations from LinkedIn")
        
        if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"***{job.get('title')} ** at * {job.get('companyName')}")
                st.markdown(f"Location: {job.get('location')}")
                st.markdown(f"Posted on: {job.get('datePosted')}")
                st.markdown(f"[View Job]({job.get('link')})")
                st.markdown("---")
        else:
            st.warning("No job recommendations found on LinkedIn.")
            
        st.markdown("-----------")
        st.header("🔗Job Recommendations from Naukri")
        if naukri_jobs:
            for job in naukri_jobs:
                st.markdown(f"***{job.get('title')} ** at * {job.get('company')}")
                st.markdown(f"Location: {job.get('location')}")
                st.markdown(f"Posted on: {job.get('date')}")
                st.markdown(f"[View Job]({job.get('link')})")
                st.markdown("---")
        else:
            st.warning("No job recommendations found on Naukri.")
            