from pathlib import Path


import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Onur Gumus"
PAGE_ICON = ":wave:"
NAME = "Onur Gumus"
DESCRIPTION = """
As a Data Analyst, 
I aid enterprises by leveraging data analysis to provide insights that support informed, 
data-driven decision-making processes.
"""
EMAIL = "gumus.onr@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/onur-gumus/",
    "GitHub": "https://github.com/onrgumus",
    "Medium": "https://medium.com/@gumus.onr",
    "Kaggle": "https://www.kaggle.com/onurgm"

}
PROJECTS = {
    "🏆 Updates on Completed Projects - Check it out on LinkedIn!": "https://www.linkedin.com/in/onur-gumus/details/projects/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
"""
Onur Gümüş is a Senior Implementation Engineer at Amadeus, with a strong background in IT project delivery, digital transformation, and data-driven solution development. He has over six years of experience across consulting, FMCG, and technology-driven industries, including roles at PwC, P&G, and Reckitt, where he worked on data analytics, business intelligence, and digital transformation initiatives.

At Amadeus, he contributes to the delivery of global airline technology solutions, focusing on customer experience and loyalty transformation projects. He works closely with cross-functional teams to ensure successful implementation of enterprise solutions and digital platforms. He has experience in end-to-end project delivery, including system integrations, data-driven reporting, and process optimization, supporting business stakeholders in improving operational efficiency and customer engagement.

His expertise includes digital transformation, business intelligence, data analytics, and enterprise IT project execution, with a strong focus on delivering scalable and impactful business solutions."""

"""His proficiency spans a range of specialties:

- ✔️ Industry 4.0 and Data Scientist specializing in Digital Transformation (Python, SQL, Power BI, Alteryx)
- ✔️ Expert in Data Analysis and Visualization
- ✔️ Proficient in IT Project Management & OEMS
- ✔️ Supply Chain Management
- ✔️ Business Analyst
- ✔️ Skilled in SAP S/4HANA, R/3, PLM Business Analyst for PLM system Implementation
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Alteryx, Sql ,Power BI
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Alteryx
- 📊 Data Visulization: Power Bi, MS Excel, Plotly,Tableau, Looker
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: Postgres, MongoDB, MySQL,SSIS, SQlite
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | PWC**")
st.write("04/2023 - 04/2024")
st.write(
    """
- ► Building interactive dashboards by connecting various data sources,
- ► Automating business processes to increase efficiency and decrease human error ratio,
- ► Cleansing, reshaping, transforming data and designing data models to enable more accurate analysis,
- ► Developing algorithms to resolve various business issues and create added value,
- ► Creating products with a proactive approach by using new generation technologies in the scope of Research & Development.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Supply Chain & Business System Analyst,CCAR&TURKEY | Procter & Gamble**")
st.write("03/2022 - 04/2023")
st.write(
    """
- ► Design, manufacturing and lifecycle management
- ► Led technical enhancements and process improvements, ensuring seamless system upgrades and optimizations while achieving 100% completion in project regression testing.
- ► Drove projects aligned with our annual Industry 4.0 and Digital Transformation goals, enhancing Logistics Center efficiency, productivity, and quality, including IT solutions, layout planning, and system integrations.
- ► Designed automated Business Intelligence solutions for recurrent reporting (daily/weekly/monthly).
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**SAP Data Cleansing Executive & EMEA | Reckitt**")
st.write("10/2021 - 03/2022")
st.write(
    """
- ► Perform Pre-Load Validation during Trial Loads and Production Cutover
- ► Perform Data Reconciliation during Trial Loads and Production Cutover 
- ► Support Business with Data Creation and Data team activities during go-live and hypercare
- ► Support collection of legacy data to be migrated for a specific deployment either from data extracts or manual construction for toolset population (ADM)
- ► Project lead in respective task area for new development of complex solutions for integration of SAP MM module and processes and interfaces in SAP SCM,SAP MDG
"""
)

#--- JOB 4
st.write('\n')
st.write('🚧', "**PLM Master Data Analyst | Reckitt**")
st.write("03/2021-10/2021")
st.write(
    """
- ► Design, manufacturing and lifecycle management
- ► To use the TDS (Technical Document System) and old product data, updating it to the new PLM system.
        Solving problems between JDE and PLM systems.
- ► To support in taking the unstructured data and re-qualifying it to specifications.
        To ensure documentation and data sources are formatted correctly.
- ► To support the PLM deployments to various sites and facilities by helping business teams prepare, cleanse and verify data for migration from source systems into the new PLM (OPTIVA) platform.
- ► I work hands on conducting data cleansing activities, working with business teams and their data.
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


