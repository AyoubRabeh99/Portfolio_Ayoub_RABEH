import streamlit as st

def show_premiere_page():

    # Main CV title
    st.title("Ayoub RABEH")
    st.subheader("Data Engineer - AI Engineer")

    # Personal Information
    st.write("### PERSONAL INFORMATION")
    st.write("""
    - **Location**: France  
    - **Phone**: +33665001243  
    """)

    # Education
    st.write("### EDUCATION")
    st.write("""
    **POEI Datascientest, Data Engineer**  
    **May 2024 – August 2024**  
    
    **Programming and Big Data:** Python, SQL, NoSQL, OOP, Linux & Bash, PySpark.  
    **Machine Learning and DevOps:** Statistics, Machine Learning Concepts, Data Visualization, MLflow, Docker, FastAPI.  
    **CI/CD and Monitoring:** GitLab, Airflow, Prometheus & Grafana.

    **INSA de Rouen, Saint Etienne du Rouvray**  
    **2019 – 2022**  
    
    **Mathematical Engineering** - Data Science (Data Analysis, Machine Learning, AI)

    **International University of Rabat, Rabat**  
    **2017 – 2019**  
    **Preparatory Class** - Specialty: Mathematics - Physics.
    """)

    # Professional Experience
    st.write("### PROFESSIONAL EXPERIENCE")
    st.write("""
    **Data & AI Engineer at Sinay, Caen (Fixed-term contract)**  
    **November 2022 – March 2023**  
  
    - Implemented ETL pipelines to optimize maritime data processing and improve vessel Estimated Time of Arrival (ETA) at ports.
    - Developed an AI algorithm to blur faces with 95% precision using Google Cloud Platform (GCP).
    
    **Data & AI Engineer at Sinay, Caen (Internship)**  
    **May 2022 – October 2022**  
    
    - Collected, transformed, processed, and stored data in GCP (Google Cloud Platform) related to marine species from fishing activities.
    - Automated detection of marine mammals in videos with 85% precision, using AI models on Google Cloud Platform (GCP).

    **Research Assistant at CEREMA, Le Grand-Quevilly (Internship)**     
    **May 2021 – August 2021**  

    - Analyzed and processed environmental data to explain temperature variations on a cliff, using advanced AI techniques.
    """)

    # Skills
    st.write("### SKILLS")
    st.write("""
    - **Project Management**: Agile  
    - **Cloud**: GCP, Microsoft Azure  
    - **Languages**: Python, SQL (MySQL, PostgreSQL), NoSQL (MongoDB), C, C++, Java  
    - **Containerization**: Docker, Kubernetes  
    - **Data Science**: PySpark, ETL, FastAPI, MLflow, Deep Learning (Keras, TensorFlow, PyTorch)  
    - **Data Visualization**: Tableau, Power BI  
    - **DevOps & CI/CD**: Airflow, Prometheus, Grafana, GitLab, JIRA  
    - **Operating Systems**: Windows, Linux
    """)

    # Languages
    st.write("### LANGUAGES")
    st.write("""
    - **Arabic**: ★★★★★  
    - **French**: ★★★★☆  
    - **English**: ★★★★☆
    """)

    # Hobbies
    st.write("### HOBBIES")
    st.write("""
    - **Astronomy**  
    - **Music**: Classical, Pop, and Jazz  
    - **Japanese Anime**: Action, Psychological Thriller, Detective
    """)
