import streamlit as st

def show_deuxieme_page() :
    # Titre principal de la deuxième page
    st.title("Expériences Professionnelles")

    # Menu de sélection des expériences
    option = st.selectbox(
        'Choisissez une expérience professionnelle pour afficher les détails :',
        ('CDD Sinay', 'Stage Sinay', 'Stage CEREMA')
    )

    # Détails pour chaque expérience
    if option == 'CDD Sinay':
        st.header("1. Poste et Entreprise")
        st.write("""
        **Entreprise**: Sinay  
        **Spécialité**: Spécialisée dans la digitalisation et la préservation du secteur maritime grâce à l’utilisation d’outils Big Data        
        **Nom du poste**: Ingénieur Data & IA  
        **Période d'emploi**: Novembre 2022 - Mars 2023
        """)

        st.header("2. Contexte et Problématique")
        st.write("""
        Lors de mon CDD chez Sinay, j'ai occupé le poste d'ingénieur en IA au sein de l'équipe Tech & Data, où j'ai travaillé sur deux projets principaux : "OBSCAME" et un projet de prédiction du temps d'arrivée des navires.
        
        **Projet OBSCAME**:     
        OBSCAME est un programme scientifique visant à mieux comprendre les captures accidentelles dans les navires de pêche à l'aide de systèmes vidéo embarqués. J'avais déjà initié ce projet durant mon stage de fin d'études, où je m'étais concentré sur une problématique différente. Pendant cette période, j'ai poursuivi le travail sur les vidéos enregistrées, avec pour mission de garantir la conformité des données à la RGPD. En effet, il était possible d'identifier certains pêcheurs via les vidéos, ce qui n’était pas conforme à la réglementation. J'ai donc été chargé de mettre en place une solution pour assurer leur anonymat.

        **Projet ETA**:     
        Le projet ETA de Sinay vise à améliorer la précision des prévisions d'heure d'arrivée des navires. Mon rôle consistait à transformer des données brutes en formats exploitables pour les modèles de prédiction.
        """)

        st.header("3. Tâches Réalisées")
        st.subheader("a) OBSCAME")
        st.write("""
        **i) Préparation de la base de données**:     
        Collecte de vidéos sous différentes conditions (météo, horaires, angles de vue) afin d'évaluer l'algorithme de floutage dans divers contextes.
        
        **ii) Développement de l'algorithme de floutage**:        
        Conception d’un algorithme basé sur un modèle de Deep Learning pour flouter les visages.

        **iii) Optimisation du floutage**:    
        Mise au point de nouvelles approches pour améliorer le floutage, notamment pour les visages partiellement masqués lors des tests initiaux.

        **iv) Évaluation des performances** :  
        Analyse des performances du modèle selon trois niveaux de reconnaissance des visages :
        - Niveau 1 : Visage clairement identifiable.
        - Niveau 2 : Visage de profil partiellement identifiable.
        - Niveau 3 : Visage éloigné ou partiellement visible, rendant la reconnaissance difficile voire impossible.

        **v) Documentation** :  
        Rédaction de la documentation complète de la solution mise en place.
        """)
        st.subheader("b) ETA")
        st.write("""
        **i) Transformation des données :**     
        Conversion des données AIS depuis le format JSON vers un format CSV structuré, puis création d'un DataFrame pour faciliter l'analyse.  
        Étapes : 
        - Lecture des fichiers JSON
        - Extraction des champs pertinents
        - Organisation en CSV.

        **ii) Traitement des colonnes de listes :**
        Gestion des colonnes complexes comme celles contenant les positions des navires :
        - Décomposition : Séparation des éléments de liste en colonnes distinctes.
        - Nouvelles colonnes : Par exemple, transformation d'une colonne "positions" en "latitude" et "longitude".
        - Gestion des séries temporelles : Adaptation des données aux séries temporelles si les positions sont horodatées.

         **iii) Documentation** :  
        Rédaction de la documentation complète de la solution mise en place.
        """)

        st.subheader("4. Technologies Utilisées")
        st.write("""
        Infrastructure (GCP) :
        - Instance Linux équipée d'une carte graphique NVIDIA V100

        Frameworks de Deep Learning :  
        - Keras  
        - TensorFlow  
        - CUDA

        Langage de Programmation :  
        - Python

        Systèmes d'exploitation :  
        - Windows  
        - Linux

        Cloud Computing :  
        - Google Cloud Platform (GCP)

        Contrôle de Version :  
        - GitLab

        Environnements de Développement :  
        - Jupyter Notebook  
        - Visual Studio Code

        Gestion de Projet :  
        - Jira

        Accélération Matérielle :  
        - GPU
        """)

        st.header("5. Résultats")
        st.subheader("a) OBSCAME")
        st.write("""
                
        Développement d’un algorithme de floutage avec une précision supérieure à 95% pour tous les niveaux de reconnaissance faciale.
        """)
        st.subheader("b) ETA")
        st.write("""
        
        **i) DataFrame structuré** :    
        Création d'un DataFrame avec des colonnes bien définies, incluant des informations telles que :  
        - MMSI (identifiant unique du navire)
        - Dimensions (longueur, largeur)
        - Dernière position connue (latitude, longitude)
        - Vitesse actuelle
        - Direction (cap)
        - ...

        **ii) Données prêtes pour l’analyse** :  
        Le DataFrame final est optimisé pour diverses analyses, comme la prédiction des ETA, la détection d'anomalies, l'analyse des patterns de navigation, et l'évaluation de l'efficacité des routes maritimes.
        """)

    elif option == 'Stage Sinay':
        st.header("1. Poste et Entreprise")
        st.write("""
        **Entreprise**: Sinay  
        **Spécialité**: Spécialisée dans la digitalisation du secteur maritime et la préservation de l'environnement marin grâce à l’utilisation de technologies Big Data        
        **Nom du poste**: Ingénieur Data & IA  
        **Période d'emploi**: Mai 2022 - Octobre 2022
        """)

        st.header("2. Contexte et Problématique")
        st.write("""
        Lors de mon stage de fin d'études chez SINAY, j'ai occupé le poste d'ingénieur en IA au sein de l'équipe Tech & Data. Mon travail était principalement centré sur le projet OBSCAME, un programme visant à analyser les vidéos des activités de pêche, en particulier pour détecter les captures accidentelles de mammifères marins.
        L'objectif du stage était d'automatiser la détection des captures accidentelles en utilisant des modèles de réseaux de neurones basés sur l'intelligence artificielle. Mon rôle impliquait le développement et l'évaluation de ces modèles pour garantir leur efficacité dans diverses conditions de capture vidéo.
        """)

        st.header("3. Tâches Réalisées")
        st.write("""
       
        **a) État de l'art :**         
        Réalisation d'une étude comparative des outils existants pour la classification d'images et la détection d'objets.  
        
        **b) Préparation de la base de données :**   
        Découpage de vidéos en images, puis regroupement de ces images en ensembles spécifiques selon les groupes d'espèces étudiées. J'ai également mené une analyse des déséquilibres pour évaluer la répartition des données entre les différentes classes.  
       
        **c) Classification d'images :**   
        Déploiement de modèles de classification pour distinguer les mammifères marins des autres espèces présentes dans les vidéos.  
        
        **d) Détection d'objets :**    
        Mise en place d'un système de détection automatique des mammifères marins à la fois dans les images et les vidéos.  
        
        **e) Évaluation des modèles :**    
        Analyse des performances des modèles de classification d'images et de détection d'objets en fonction des conditions météorologiques, des moments de la journée et de l'angle de vue des caméras. 
        
        L'objectif était de déterminer dans quelles conditions les modèles étaient les plus efficaces et d'identifier les axes d'amélioration potentiels. 
        """)

        st.header("4. Technologies Utilisées")
        st.write("""
         Infrastructure (GCP) :
        - Instance Linux équipée d'une carte graphique NVIDIA V100

        Frameworks de Deep Learning :  
        - Keras  
        - TensorFlow  
        - CUDA

        Langage de Programmation :  
        - Python

        Systèmes d'exploitation :  
        - Windows  
        - Linux

        Cloud Computing :  
        - Google Cloud Platform (GCP)

        Contrôle de Version :  
        - GitLab

        Environnements de Développement :  
        - Jupyter Notebook  
        - Visual Studio Code

        Gestion de Projet :  
        - Jira

        Accélération Matérielle :  
        - GPU
        """)

        st.subheader("5. Résultats")
        st.write("Détection automatiquement des mammifères marins dans les vidéos avec une précision de 85% en utilisant des modèles d'intelligence artificielle récents déployés sur Google Cloud Platform (GCP).")

    elif option == 'Stage CEREMA':
        st.header("1. Poste et Entreprise")
        st.write("""
        **Organisme** : CEREMA Normandie Centre  
        **Spécialité** : 
        **Nom du poste**: Assistant chercheur  
        **Période d'emploi**: Mai 2021 - Août 2021
        """)

        st.header("2. Contexte et Problématique")
        st.write("""
        J'ai effectué mon stage chez CEREMA, un établissement public placé sous la tutelle du ministère de la Transition écologique et de la Cohésion des territoires. 

        Plus précisément, j'ai travaillé au sein de l'équipe ENDSUM, composée de techniciens et de chercheurs en géosciences, pour le projet "TélédéTac". Ce projet, soutenu par la Région Normandie, a pour objectif de développer des instruments de télédétection afin de surveiller, analyser et évaluer l'érosion côtière, dans le but d'améliorer la gestion et la préservation du littoral normand.

        Mon rôle au sein de l'équipe était de contribuer à ce projet en étudiant l'influence du sol et de la végétation sur les températures de surface des falaises des Vaches Noires.
        """)

        st.header("3. Tâches Réalisées")
        st.write("""
        **a) Participation à l'acquisition des données :**      
        Participation à l'acquisition des données qui a été assistée par un membre de l'équipe qui a supervisé un vol du drone équipé de capteurs sur les falaises des Vaches Noires. Ce vol a permis de capturer des images visibles, ainsi que des images thermiques grâce au LiDAR et à la caméra thermique. 
        
        Ces images ont ensuite été utilisées pour réaliser une photogrammétrie, ce qui a abouti à la création de modèles en 3D des Vaches Noires, ainsi que d'orthophotos visibles et thermiques que j'ai utilisé par la suite.
        
        **b)Annotation des données :**          
        Annotation des images à l'aide de l'outil d'annotation Labelme. Cela consiste à délimiter et annoter les zones de végétation sur les images des falaises des Vaches Noires.
        
        **c) État de l'art :**      
        État de l'art des techniques d'analyse des données thermiques et des modèles IA pour la segmentation d'objets.
        
        **d) Segmentation des zones chaudes :**        
        À partir de l'orthophoto thermique j'ai effectué une segmentation des zones chaudes en utilisant un seuillage avec l'aide de QGIS. Cette étape m'a permis d'identifier les zones présentant des températures élevées par rapport à un seuil. 
        
        Les zones chaudes sont généralement associées à la présence de végétation et parfois à la présence d'eau. En revanche, les zones froides sont principalement liées au sol nu.
        
        **e) Détection des zones de végétation :**          
        En utilisant une architecture de réseau de neurones UNET, les zones de végétation ont été segmentées sur les images visibles des falaises des Vaches Noires. Cette détection permet d'analyser la présence et la répartition de la végétation sur les falaises.

        """)

        st.subheader("4. Technologies Utilisées")
        st.write("""
        Langage de Programmation :
        - Python

        Deep Learning Frameworks :
        - Keras
        - Tensorflow
        
        Environnement de Développement :
        - Jupyter Notebook
        
        Annotation d'Images :
        - Labelme
        
        Système d'Information Géographique :
        - QGIS
        
        Accélération Matérielle :
        - GPU
        """)

        st.subheader("5. Résultats")
        st.write("""
        - Génération d'une carte de température en utilisant la technique de seuillage sur les ortho-images thermiques. Cette carte est en noir et blanc, où les zones blanches indiquent les régions dont la température dépasse un seuil fixé.
        - Segmentation des zones de végétation sur les images visibles des falaises des Vaches Noires en utilisant un réseau de neurones. Le résultat est une image en noir et blanc où les zones blanches indiquent la présence de végétation dans les falaises des Vaches Noires. Ensuite, j'ai procédé à une analyse et à une comparaison avec la carte de température pour identifier les zones chaudes qui ne sont pas liées à la végétation.
        """)
