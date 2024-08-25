import streamlit as st

def show_troisieme_page() :

    # Titre de la page
    st.title("Formations")

    # Menu déroulant pour choisir la formation
    option = st.selectbox("Choisissez une formation", ["DataScientest", "INSA Rouen", "Classe Préparatoire Université Internationale de Rabat"])

    if option == 'DataScientest':
        st.header("DataScientest")
        st.write("""
        **Organisme**: DataScientest  
        **Durée**: Mai 2024 - Août 2024  
        **Formation**: Data Engineer (POEI)
        """)

        st.subheader("Compétences acquises") 
        st.write("""
        - **Développement Python et Éthique** : 
        Compétence dans le développement en Python avec une prise en compte des aspects éthiques et réglementaires.
        
        - **Programmation Avancée et Outils de Développement** : 
        Expertise en programmation orientée objet, ainsi que dans l'utilisation des outils de gestion de versions et d'environnement de développement.
        
        - **Gestion et Traitement des Données** : 
        Maîtrise des techniques de gestion des données, y compris le traitement en batch et en streaming.
        
        - **Machine Learning et DevOps** : 
        Compétence en machine learning, avec une expérience dans l'intégration de solutions DevOps pour la virtualisation et l'orchestration des applications.
        - **CI/CD et Monitoring** : 
        Expertise en intégration continue, déploiement continu, et en surveillance des systèmes pour garantir leur performance et fiabilité.
        """)

        st.subheader("Programme")
        st.write("""
    
        **Introduction à Python :**
        - Python pour le Data Engineering (FR)
        - Éthique et RGPD

        **Programmation avancée pour les Data Engineers :**
        - Programmation orientée objet
        - Linux & Bash
        - Git & Github

        **Big Data Variété :**
        - Langage SQL
        - Base de données NoSQL (MongoDB)

        **Batch & Streaming :**
        - Kafka
        - PySpark
        - Streaming with Spark
        - Scala

        **Machine Learning :**
        - MLflow
        - Machine Learning pour Data Engineer
        - Drift Monitoring

        **DevOps - Virtualisation :**
        - Docker
        - FastApi
        - Kubernetes

        **CI / CD :**
        - Tests unitaires
        - GitLab
        - Airflow

        **Monitoring :**
        - Prometheus & Grafana
        """)

    elif option == 'INSA Rouen':
        st.header("INSA Rouen Normandie")
        st.write("""
        **Établissement**: INSA Rouen Normandie  
        **Durée**: 2019 - 2022  
        **Filière**: Génie Mathématique  
        **Spécialité**: Sciences des données
        """)
        
        st.subheader("Compétences acquises")
        st.write("""
        - **Maîtrise des outils mathématiques avancés** : 
        Compréhension approfondie des concepts tels que l'analyse fonctionnelle, les équations différentielles, et l'optimisation linéaire.
        
        - **Modélisation et simulation numérique** : 
        Capacité à résoudre des problèmes complexes en utilisant des méthodes numériques pour des équations aux dérivées partielles et des algorithmes d'approximation.
        
        - **Compétences en modélisation stochastique** : 
        Analyse et application des probabilités, statistiques, processus de Markov, et calcul stochastique pour modéliser l'incertitude dans divers systèmes.
        
        - **Expertise en sciences des données** : 
        Application des techniques de machine learning, traitement d'images, et statistiques descriptives. Utilisation de R et Python pour le machine learning et les statistiques, ainsi que gestion des bases de données avec MySQL pour analyser de grandes quantités de données.
        
        - **Développement et implémentation d'algorithmes** : 
        Programmation avancée en langages C, C++, Java, et Python ; conception et structuration d'algorithmes, ainsi que gestion de projets informatiques complexes.
        
        - **Résolution de problèmes complexes en IA** : 
        Conception et mise en œuvre de solutions en intelligence artificielle, en incluant l'IA explicable pour des systèmes plus transparents et interprétables.
        
        - **Compétences en cryptographie** : 
        Application des techniques cryptographiques pour sécuriser les données et les communications, en mettant en œuvre des méthodes de chiffrement et de déchiffrement robustes.
        """)

        st.subheader("Programme")
        st.write("""
        **Semestre 5**
        1. UE Modélisation Mathématique et Simulation Numérique (GM31_MMSN) - 8 ECTS
        - Calcul scientifique sous Unix (GMAT31-MMSN-CalSc) - 35h
        - Analyse Numérique (GMAT31-MMSN-AnaNum) - 35h
        - Analyse Fonctionnelle (GMAT31-MMSN-AnaFonc) - 43h

        2. UE Modélisation Stochastique et Recherche Opérationnelle (GM31_MSRO) - 7 ECTS
        - Probabilités (GMAT31-MSRO-Proba) - 35h
        - Optimisation Discrète (GMAT31-MSRO-OD) - 35h
        - Mesures et Intégrations (GMAT31-MSRO-Mesures) - 35h

        3. UE Informatique (GM31_INFO) - 6 ECTS
        - Soutien approfondissement "C" (GMAT31-Soutien-C) - 21h
        - Soutien approfondissement "Algo" (GMAT31-Soutien-Algo) - 21h
        - Langage "C" (GMAT31-INFO-C) - 35h
        - Algo. et structure de données (GMAT31-INFO-Algo) - 35h

        4. UE Projets (GM31_Proj) - 3 ECTS
        - PROJET 1er Semestre (GMAT31-PROJET1) - 72h

        5. UE Humanités (GM31_Hum) - 4 ECTS
        - Anglais GM (H-31-ANG-GM) - 18h
        - Gestion Stratégie Finance GM (H-31-GSF-GM) - 18h
        - Activités Physiques et Sportives GM (H-31-APS-GM) - 18h
        - Allemand débutant 1 (H-3451-ALL-DEB2) - 21h

        **Semestre 6**
        1. UE Modélisation Mathématique et Simulation Numérique (GM32_MMSN) - 9 ECTS
        - Analyse Numérique (GMAT32-MMSN-AnaNum) - 35h
        - Algorithmique Numérique et Arithmétique (GMAT32-MMSN-AlgoNum) - 35h
        - Équations Différentielles (GMAT32-MMSN-EqDif) - 35h

        2. UE Modélisation Stochastique et Recherche Opérationnelle (GM32_MSRO) - 9 ECTS
        - Analyse des Données (GMAT32-MSRO-AD) - 35h
        - Statistiques (GMAT32-MSRO-Stat) - 35h
        - Signal (GMAT32-MSRO-Sign) - 35h

        3. UE Informatique (GM32_Info) - 5 ECTS
        - Systèmes et réseaux (GMAT32-INFO-S&R) - 35h
        - Conception et Programmation par Objets (GMAT32-INFO-ProgObj) - 42h

        4. UE Humanités (GM32_Hum) - 4 ECTS
        - Divers cours similaires au semestre précédent (Langues, Gestion Stratégie Finance, etc.)

        **Semestre 7**
        1. UE Modélisation Mathématique et Simulation Numérique (GM41_MMSN) - 6 ECTS
        - Équations aux dérivées partielles (GMAT41-MMSN-EDP) - 30h
        - Méthodes Numériques pour les EDP1 (GMAT41-MMSN-MNEDP1) - 30h
        - Optimisation Linéaire (GMAT41-MMSN-OptLin) - 30h

        2. UE Modélisation Stochastique et Recherche Opérationnelle (GM41_MSRO) - 6 ECTS
        - Statistiques (GMAT41-MSRO-Stat) - 30h
        - Processus de Markov (GMAT41-MSRO-Mark) - 30h
        - Signal (GMAT41-MSRO-Sign) - 30h

        3. UE Informatique (GM41_Info) - 6 ECTS
        - Algo. et Structures de Données Avancées (GMAT41-INFO-AlStrD) - 30h
        - Génie Logiciel et Programmation Orientée-Objet Avancée (GMAT41-INFO-POA) - 36h

        4. UE Ouverture professionnelle (GM41_Ouvert.Pro) - 8 ECTS
        - PROJET 1er Semestre (GMAT41-PROJET1) - 88h
        - INSA JOB (GM41-INSAJOB) - 6h

        5. UE Humanités (GM41_Hum) - 4 ECTS
        - Anglais GM (H-41-ANG-GM) - 18h
        - Anglais Test TOEIC (H-41-ANG-TEST-TOEIC) - 3h
        - Gestion Stratégie Finance GM (H-41-GSF-GM) - 18h
        - Activités Physiques et Sportives GM (H-41-APS-GM) - 18h
        - Allemand débutant 2 (H-3451-ALL-DEB2) - 21h

        **Semestre 8**
        1. UE Modélisation Mathématique et Simulation Numérique (GM42_MMSN) - 4 ECTS
        - Approximation et Design Géométrique (GMAT42-MMSN-ADG) - 30h
        - Méthodes Numériques pour les EDP2 (GMAT42-MMSN-MNEDP2) - 30h

        2. UE Modélisation Stochastique et Recherche Opérationnelle (GM42_MSRO) - 6 ECTS
        - Optimisation Combinatoire (GMAT42-MSRO-OpCom) - 30h
        - Automatique (GMAT42-MSRO-Auto) - 30h
        - Machine Learning (GMAT42-MSRO-ML) - 30h

        3. UE Informatique (GM42_Info) - 6 ECTS
        - Base de Données (GMAT42-INFO-BdD) - 30h
        - Gestion de projet Info et C++ (GMAT42-INFO-C++) - 30h

        4. UE Ouverture professionnelle (GM42_Ouvert.Pro) - 10 ECTS
        - Calcul différentiel (GMAT42-MMSN-CalDif) - 30h
        - Analyse Lexicale et Syntaxique (GMAT42-INFO-AnLex) - 30h
        - PROJET 2ème Semestre (GMAT42-PROJET2) - 88h

        5. UE Humanités (GM42_Hum) - 4 ECTS
        - Anglais GM (H-42-ANG-GM) - 18h
        - Finance - EC de spécialité GM (H-42-ENV-FINAN-GM) - 18h
        - Initiation à la langue japonaise GM - 18h

        **Semestre 9 : Spécialité Sciences des données**
        1. UE Scientifique (GM51_Sc.) - 16 ECTS
        - Approximation et machine learning : application en traitement d'images et big data (GMAT51-Sc-AML) - 15h
        - Contrôle Optimal et applications (GMAT51-Sc-ContOpt) - 30h
        - Calcul Stochastique et Finance (GMAT51-Sc-SFin) - 30h
        - Méthodes itératives et algorithmes stochastiques pour le traitement en ligne de données (GMAT51-Sc-MIAS) - 15h
        - Méthodes variationnelles pour le traitement d'images (GMAT51-Sc-MetVar) - 15h
        - Cryptographie (GMAT51-Sc-Crypt) - 15h
        - Résolution de Problèmes en Intelligence Artificielle (GMAT51-Sc-PbIA) - 30h
        - Introduction à l'IA explicable (GMAT51-Sc-XAI) - 30h
        - Modélisation et simulation numérique : théorie et applications (GMAT51-Sc-MSN) - 15h
        - Optimisation en grande dimension (GMAT51-Sc-OptimGD) - 30h

        2. UE Humanités (GM51_Huma) - 2 ECTS
        - Finance (H-51-ENV-FINAN-GM) - 30h
        - Anglais (H-51-ANG-INSA5) - 21h

        3. UE Projet de fin d'études (GM51_PFE) - 12 ECTS
        - Projet de Fin d'Études (GMAT51-PROJETPFE) - 400h

        4. UE Stage de Spécialité (GM51_StageSpe) - 4 ECTS
        - Stage de Spécialité (GMAT51-Stage-Spe)

        **Semestre 10**
        1. UE Stage Ingénieur (GM52_StageIng) - 30 ECTS
        - Stage Ingénieur (GMAT52-Stage-Ing)
        """)


    elif option == 'Classe Préparatoire Université Internationale de Rabat':
        st.header("CPGE UIR")
        st.write("""
        **Établissement**: Université Internationale de Rabat  
        **Durée**: 2017 - 2019  
        **Filière**: MPSI - MP
        """)
        
        st.subheader("Compétences acquises")
        
        st.write("""
        - **Mathématiques** : 
        Résolution de problèmes complexes et modélisation mathématique. Maîtrise des concepts avancés tels que l'analyse, l'algèbre, et la géométrie.
        
        - **Physique** : 
        Compréhension approfondie des principes de la mécanique, de l'électromagnétisme, et de l'optique.
        
        - **Informatique (Python)** : 
        Programmation en Python, connaissance des structures de données, des algorithmes, et des concepts de base en informatique.
        
        - **Français** : 
        Compétences en rédaction, analyse littéraire, et expression écrite.
        
        - **Sciences de l'Ingénieur** : 
        Connaissance des principes fondamentaux de l'ingénierie, application de la théorie à des projets pratiques.
        
        - **Anglais** : 
        Compétence en communication écrite et orale, traduction et interprétation.
        
        - **Traduction** : 
        Maîtrise des techniques de traduction technique et littéraire, adaptation du contenu aux nuances culturelles et linguistiques.
        """)

        st.subheader("Programme")
        st.write("""
        **Mathématiques**
        - Résolution de problèmes complexes et modélisation mathématique.
        - Maîtrise des concepts avancés tels que l'analyse, l'algèbre, et la géométrie.
        - Développement de compétences en calculs différentielles et intégrales, ainsi que en probabilités et statistiques.

        **Physique**
        - Compréhension approfondie des principes de la mécanique, de l'électromagnétisme, et de l'optique.
        - Application de concepts théoriques à des problèmes pratiques et réalisation d'expériences en laboratoire.
        - Développement de compétences en analyse expérimentale et en résolution de problèmes physiques complexes.

        **Informatique (Python)**
        - Programmation en Python, y compris la création de scripts, le traitement de données, et le développement d'algorithmes.
        - Connaissance des structures de données, des algorithmes, et des concepts de base en informatique.
        - Capacité à résoudre des problèmes de programmation et à concevoir des solutions efficaces.

        **Français**
        - Compétences avancées en rédaction, analyse littéraire, et expression écrite.
        - Capacité à argumenter, critiquer, et discuter des textes littéraires et des œuvres culturelles.
        - Maîtrise des techniques de communication et de structuration des idées.

        **Sciences de l'Ingénieur**
        - Connaissance des principes fondamentaux de l'ingénierie, y compris les méthodes de conception et d'analyse des systèmes techniques.
        - Application de la théorie à des projets pratiques, tels que la conception de systèmes mécaniques ou électroniques.
        - Développement de compétences en résolution de problèmes techniques et en gestion de projet.

        **Anglais**
        - Compétence en communication écrite et orale en anglais, y compris la compréhension de textes techniques et littéraires.
        - Capacité à rédiger à participer à des discussions en anglais.
        - Développement de compétences en traduction et en interprétation de documents.

        **Traduction**
        - Maîtrise des techniques de traduction y compris la traduction technique et littéraire.
        - Compétences en adaptation du contenu en tenant compte des nuances culturelles et linguistiques.
        """)
        
        

