import streamlit as st

def show_premiere_page():

    # Titre principal du CV
    st.title("Ayoub RABEH")
    st.subheader("Data Engineer - Ingénieur IA")

    # Informations personnelles
    st.write("### INFORMATIONS PERSONNELLES")
    st.write("""
    - **Localisation**: France  
    - **Téléphone**: +33665001243  
    """)

    # Éducation
    st.write("### ÉDUCATION")
    st.write("""
    **POEI Datascientest, Data Engineer**  
    **Mai 2024 – Août 2024**  
    
    **Programmation et Big Data :** Python, SQL, NoSQL, POO, Linux & Bash, PySpark.  
    **Machine Learning et DevOps :** Statistiques, Concepts de Machine Learning, Data Visualisation, MLflow, Docker, FastAPI.  
    **CI/CD et Monitoring :** GitLab, Airflow, Prometheus & Grafana.

    **INSA de Rouen, Saint Etienne du Rouvray**  
    **2019 – 2022**  
    
    **Génie Mathématique** - Science des données (Analyse des données, Machine Learning, IA)

    **Université Internationale de Rabat, Rabat**  
    **2017 – 2019**  
    **Classe préparatoire** - Spécialité : Mathématique - Physique.
    """)

    # Expérience professionnelle
    st.write("### EXPÉRIENCE PROFESSIONNELLE")
    st.write("""
    **Ingénieur Data & IA à Sinay, Caen (CDD)**  
    **Novembre 2022 – Mars 2023**  
  
    - Mise en place de pipelines ETL pour optimiser le traitement des données maritimes et améliorer l'estimation des délais d'arrivée (ETA) des navires dans les ports.
    - Développement d'un algorithme d'intelligence artificielle pour flouter les visages avec une précision de 95 % en utilisant Google Cloud Platform (GCP).
    
    **Ingénieur Data & IA à Sinay, Caen (Stage)**  
    **Mai 2022 – Octobre 2022**  
    
    - Collecte, transformation, traitement et stockage des données dans le Cloud GCP (Google Cloud Platform) concernant des espèces maritimes issues des activités de pêche.
    - Détection automatique des mammifères marins dans les vidéos avec une précision de 85%, en utilisant des modèles IA sur Google Cloud Platform (GCP).

    **Assistant chercheur à CEREMA, Le Grand-Quevilly (Stage)**     
    **Mai 2021 – Août 2021**  

    - Analyse et traitement des données environnementales pour expliquer les variations de température sur une falaise, utilisant des techniques avancées de l'IA.
    """)

    # Compétences
    st.write("### COMPÉTENCES")
    st.write("""
    - **Gestion de projet**: Agile  
    - **Cloud**: GCP, Microsoft Azure  
    - **Langages**: Python, SQL (MySQL, PostgreSQL), NoSQL (MongoDB), C, C++, Java  
    - **Conteneurisation**: Docker, Kubernetes  
    - **Data Science**: PySpark, ETL, FastAPI, MLflow, Deep Learning (Keras, Tensorflow, Pytorch)  
    - **Data Visualization**: Tableau, Power BI  
    - **DevOps & CI/CD**: Airflow, Prometheus, Grafana, GitLab, JIRA  
    - **Systèmes d'exploitation**: Windows, Linux
    """)

    # Langues
    st.write("### LANGUES")
    st.write("""
    - **Arabe**: ★★★★★  
    - **Français**: ★★★★☆  
    - **Anglais**: ★★★★☆
    """)

    # Hobbies
    st.write("### Centres d'intérêts")
    st.write("""
    - **Astronomie**  
    - **Musique**: Classique, Pop et Jazz  
    - **Animés japonais**: Action, Thriller psychologique, Policier
    """)
