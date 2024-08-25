import streamlit as st

def show_troisieme_page() :

    # Page title
    st.title("Training")

    # Dropdown menu to choose the training
    option = st.selectbox("Choose a training", ["DataScientest", "INSA Rouen", "Preparatory Class International University of Rabat"])

    if option == 'DataScientest':
        st.header("DataScientest")
        st.write("""
        **Organization**: DataScientest  
        **Duration**: May 2024 - August 2024  
        **Training**: Data Engineer (POEI)
        """)

        st.subheader("Skills Acquired") 
        st.write("""
        - **Python Development and Ethics**: 
        Proficiency in Python development with consideration of ethical and regulatory aspects.
        
        - **Advanced Programming and Development Tools**: 
        Expertise in object-oriented programming, as well as in using version control and development environment tools.
        
        - **Data Management and Processing**: 
        Mastery of data management techniques, including batch and streaming processing.
        
        - **Machine Learning and DevOps**: 
        Skills in machine learning, with experience in integrating DevOps solutions for application virtualization and orchestration.
        
        - **CI/CD and Monitoring**: 
        Expertise in continuous integration, continuous deployment, and system monitoring to ensure performance and reliability.
        """)

        st.subheader("Program")
        st.write("""
    
        **Introduction to Python:**
        - Python for Data Engineering (FR)
        - Ethics and GDPR

        **Advanced Programming for Data Engineers:**
        - Object-oriented programming
        - Linux & Bash
        - Git & Github

        **Big Data Variety:**
        - SQL Language
        - NoSQL Database (MongoDB)

        **Batch & Streaming:**
        - Kafka
        - PySpark
        - Streaming with Spark
        - Scala

        **Machine Learning:**
        - MLflow
        - Machine Learning for Data Engineers
        - Drift Monitoring

        **DevOps - Virtualization:**
        - Docker
        - FastApi
        - Kubernetes

        **CI / CD:**
        - Unit tests
        - GitLab
        - Airflow

        **Monitoring:**
        - Prometheus & Grafana
        """)

    elif option == 'INSA Rouen':
        st.header("INSA Rouen Normandie")
        st.write("""
        **Institution**: INSA Rouen Normandie  
        **Duration**: 2019 - 2022  
        **Department**: Mathematical Engineering  
        **Specialty**: Data Science
        """)
        
        st.subheader("Skills Acquired")
        st.write("""
        - **Mastery of Advanced Mathematical Tools**: 
        Deep understanding of concepts such as functional analysis, differential equations, and linear optimization.
        
        - **Modeling and Numerical Simulation**: 
        Ability to solve complex problems using numerical methods for partial differential equations and approximation algorithms.
        
        - **Skills in Stochastic Modeling**: 
        Analysis and application of probabilities, statistics, Markov processes, and stochastic calculus to model uncertainty in various systems.
        
        - **Expertise in Data Science**: 
        Application of machine learning techniques, image processing, and descriptive statistics. Use of R and Python for machine learning and statistics, as well as database management with MySQL to analyze large datasets.
        
        - **Development and Implementation of Algorithms**: 
        Advanced programming in C, C++, Java, and Python; design and structuring of algorithms, as well as management of complex IT projects.
        
        - **Solving Complex Problems in AI**: 
        Design and implementation of artificial intelligence solutions, including explainable AI for more transparent and interpretable systems.
        
        - **Cryptography Skills**: 
        Application of cryptographic techniques to secure data and communications, implementing robust encryption and decryption methods.
        """)

        st.subheader("Program")
        st.write("""
        **Semester 5**
        1. Mathematical Modeling and Numerical Simulation (GM31_MMSN) - 8 ECTS
        - Scientific Computing under Unix (GMAT31-MMSN-CalSc) - 35h
        - Numerical Analysis (GMAT31-MMSN-AnaNum) - 35h
        - Functional Analysis (GMAT31-MMSN-AnaFonc) - 43h

        2. Stochastic Modeling and Operations Research (GM31_MSRO) - 7 ECTS
        - Probability (GMAT31-MSRO-Proba) - 35h
        - Discrete Optimization (GMAT31-MSRO-OD) - 35h
        - Measures and Integrations (GMAT31-MSRO-Mesures) - 35h

        3. Computer Science (GM31_INFO) - 6 ECTS
        - Advanced Support "C" (GMAT31-Soutien-C) - 21h
        - Advanced Support "Algo" (GMAT31-Soutien-Algo) - 21h
        - "C" Language (GMAT31-INFO-C) - 35h
        - Algorithms and Data Structures (GMAT31-INFO-Algo) - 35h

        4. Projects (GM31_Proj) - 3 ECTS
        - Project 1st Semester (GMAT31-PROJET1) - 72h

        5. Humanities (GM31_Hum) - 4 ECTS
        - English GM (H-31-ANG-GM) - 18h
        - Strategy Finance Management GM (H-31-GSF-GM) - 18h
        - Physical and Sports Activities GM (H-31-APS-GM) - 18h
        - Beginner German 1 (H-3451-ALL-DEB2) - 21h

        **Semester 6**
        1. Mathematical Modeling and Numerical Simulation (GM32_MMSN) - 9 ECTS
        - Numerical Analysis (GMAT32-MMSN-AnaNum) - 35h
        - Numerical Algorithms and Arithmetic (GMAT32-MMSN-AlgoNum) - 35h
        - Differential Equations (GMAT32-MMSN-EqDif) - 35h

        2. Stochastic Modeling and Operations Research (GM32_MSRO) - 9 ECTS
        - Data Analysis (GMAT32-MSRO-AD) - 35h
        - Statistics (GMAT32-MSRO-Stat) - 35h
        - Signal (GMAT32-MSRO-Sign) - 35h

        3. Computer Science (GM32_Info) - 5 ECTS
        - Systems and Networks (GMAT32-INFO-S&R) - 35h
        - Object-Oriented Design and Programming (GMAT32-INFO-ProgObj) - 42h

        4. Humanities (GM32_Hum) - 4 ECTS
        - Various courses similar to the previous semester (Languages, Strategy Finance, etc.)

        **Semester 7**
        1. Mathematical Modeling and Numerical Simulation (GM41_MMSN) - 6 ECTS
        - Partial Differential Equations (GMAT41-MMSN-EDP) - 30h
        - Numerical Methods for PDEs1 (GMAT41-MMSN-MNEDP1) - 30h
        - Linear Optimization (GMAT41-MMSN-OptLin) - 30h

        2. Stochastic Modeling and Operations Research (GM41_MSRO) - 6 ECTS
        - Statistics (GMAT41-MSRO-Stat) - 30h
        - Markov Processes (GMAT41-MSRO-Mark) - 30h
        - Signal (GMAT41-MSRO-Sign) - 30h

        3. Computer Science (GM41_Info) - 6 ECTS
        - Advanced Algorithms and Data Structures (GMAT41-INFO-AlStrD) - 30h
        - Software Engineering and Advanced Object-Oriented Programming (GMAT41-INFO-POA) - 36h

        4. Professional Development (GM41_Ouvert.Pro) - 8 ECTS
        - Project 1st Semester (GMAT41-PROJET1) - 88h
        - INSA JOB (GM41-INSAJOB) - 6h

        5. Humanities (GM41_Hum) - 4 ECTS
        - English GM (H-41-ANG-GM) - 18h
        - TOEIC Test English (H-41-ANG-TEST-TOEIC) - 3h
        - Strategy Finance Management GM (H-41-GSF-GM) - 18h
        - Physical and Sports Activities GM (H-41-APS-GM) - 18h
        - Beginner German 2 (H-3451-ALL-DEB2) - 21h

        **Semester 8**
        1. Mathematical Modeling and Numerical Simulation (GM42_MMSN) - 4 ECTS
        - Approximation and Geometric Design (GMAT42-MMSN-ADG) - 30h
        - Numerical Methods for PDEs2 (GMAT42-MMSN-MNEDP2) - 30h

        2. Stochastic Modeling and Operations Research (GM42_MSRO) - 6 ECTS
        - Combinatorial Optimization (GMAT42-MSRO-OpCom) - 30h
        - Control Systems (GMAT42-MSRO-Auto) - 30h
        - Machine Learning (GMAT42-MSRO-ML) - 30h

        3. Computer Science (GM42_Info) - 6 ECTS
        - Databases (GMAT42-INFO-BdD) - 30h
        - Project Management Info and C++ (GMAT42-INFO-C++) - 30h

        4. Professional Development (GM42_Ouvert.Pro) - 10 ECTS
        - Differential Calculus (GMAT42-MMSN-CalDif) - 30h
        - Lexical and Syntactic Analysis (GMAT42-INFO-AnLex) - 30h
        - Project 2nd Semester (GMAT42-PROJET2) - 88h

        5. Humanities (GM42_Hum) - 4 ECTS
        - English GM (H-42-ANG-GM) - 18h
        - Finance - Specialty EC GM (H-42-ENV-FINAN-GM) - 18h
        - Introduction to Japanese Language GM - 18h

        **Semester 9: Data Science Specialty**
        1. Scientific (GM51_Sc.) - 16 ECTS
        - Approximation and Machine Learning: Application in Image Processing and Big Data (GMAT51-Sc-AML) - 15h
        - Optimal Control and Applications (GMAT51-Sc-ContOpt) - 30h
        - Stochastic Calculus and Finance (GMAT51-Sc-SFin) - 30h
        - Iterative Methods and Stochastic Algorithms for Online Data Processing (GMAT51-Sc-MIAS) - 15h
        - Variational Methods for Image Processing (GMAT51-Sc-MetVar) - 15h
        - Cryptography (GMAT51-Sc-Crypt) - 15h
        - Problem Solving in Artificial Intelligence (GMAT51-Sc-PbIA) - 30h
        - Introduction to Explainable AI (GMAT51-Sc-XAI) - 30h
        - Modeling and Numerical Simulation: Theory and Applications (GMAT51-Sc-MSN) - 15h
        - High-Dimensional Optimization (GMAT51-Sc-OptimGD) - 30h

        2. Humanities (GM51_Huma) - 2 ECTS
        - Finance (H-51-ENV-FINAN-GM) - 30h
        - English (H-51-ANG-INSA5) - 21h

        3. Final Study Project (GM51_PFE) - 12 ECTS
        - Final Study Project (GMAT51-PROJETPFE) - 400h

        4. Specialty Internship (GM51_StageSpe) - 4 ECTS
        - Specialty Internship (GMAT51-Stage-Spe)

        **Semester 10**
        1. Engineering Internship (GM52_StageIng) - 30 ECTS
        - Engineering Internship (GMAT52-Stage-Ing)
        """)


    elif option == 'Preparatory Class International University of Rabat':
        st.header("CPGE UIR")
        st.write("""
        **Institution**: International University of Rabat  
        **Duration**: 2017 - 2019  
        **Department**: MPSI - MP
        """)
        
        st.subheader("Skills Acquired")
        
        st.write("""
        - **Mathematics**: 
        Solving complex problems and mathematical modeling. Mastery of advanced concepts such as analysis, algebra, and geometry.
        
        - **Physics**: 
        Deep understanding of principles of mechanics, electromagnetism, and optics.
        
        - **Computer Science (Python)**: 
        Programming in Python, knowledge of data structures, algorithms, and basic computer science concepts.
        
        - **French**: 
        Skills in writing, literary analysis, and written expression.
        
        - **Engineering Sciences**: 
        Knowledge of fundamental engineering principles, application of theory to practical projects.
        
        - **English**: 
        Proficiency in written and oral communication, translation, and interpretation.
        
        - **Translation**: 
        Mastery of technical and literary translation techniques, adaptation of content to cultural and linguistic nuances.
        """)

        st.subheader("Program")
        st.write("""
        **Mathematics**
        - Solving complex problems and mathematical modeling.
        - Mastery of advanced concepts such as analysis, algebra, and geometry.
        - Development of skills in differential and integral calculus, as well as in probability and statistics.

        **Physics**
        - Deep understanding of principles of mechanics, electromagnetism, and optics.
        - Application of theoretical concepts to practical problems and conducting laboratory experiments.
        - Development of skills in experimental analysis and solving complex physical problems.

        **Computer Science (Python)**
        - Programming in Python, including script creation, data processing, and algorithm development.
        - Knowledge of data structures, algorithms, and basic computer science concepts.
        - Ability to solve programming problems and design effective solutions.

        **French**
        - Advanced skills in writing, literary analysis, and written expression.
        - Ability to argue, critique, and discuss literary texts and cultural works.
        - Mastery of communication techniques and structuring of ideas.

        **Engineering Sciences**
        - Knowledge of fundamental engineering principles, including design and analysis methods for technical systems.
        - Application of theory to practical projects, such as designing mechanical or electronic systems.
        - Development of skills in solving technical problems and project management.

        **English**
        - Proficiency in written and oral communication in English, including understanding technical and literary texts.
        - Ability to write and participate in discussions in English.
        - Development of skills in translation and interpretation of documents.

        **Translation**
        - Mastery of translation techniques including technical and literary translation.
        - Skills in adapting content considering cultural and linguistic nuances.
        """)
