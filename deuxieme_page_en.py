import streamlit as st

def show_deuxieme_page():
    # Main title of the second page
    st.title("Professional Experience")

    # Experience selection menu
    option = st.selectbox(
        'Choose a professional experience to view details:',
        ('Sinay Fixed-term Contract', 'Sinay Internship', 'CEREMA Internship')
    )

    # Details for each experience
    if option == 'Sinay Fixed-term Contract':
        st.header("1. Position and Company")
        st.write("""
        **Company**: Sinay  
        **Specialty**: Specializes in the digitalization and preservation of the maritime sector through the use of Big Data tools        
        **Position**: Data & AI Engineer  
        **Employment Period**: November 2022 - March 2023
        """)

        st.header("2. Context and Issue")
        st.write("""
        During my fixed-term contract at Sinay, I worked as an AI engineer within the Tech & Data team on two main projects: "OBSCAME" and a vessel ETA prediction project.
        
        **OBSCAME Project**:     
        OBSCAME is a scientific program aimed at better understanding bycatch in fishing vessels using onboard video systems. I had previously initiated this project during my end-of-studies internship, focusing on a different issue. During this period, I continued working on recorded videos, with the mission of ensuring data compliance with GDPR. It was possible to identify some fishermen via the videos, which was not compliant with regulations. I was therefore tasked with implementing a solution to ensure their anonymity.

        **ETA Project**:     
        The Sinay ETA project aims to improve the accuracy of vessel Estimated Time of Arrival predictions. My role was to transform raw data into actionable formats for prediction models.
        """)

        st.header("3. Tasks Completed")
        st.subheader("a) OBSCAME")
        st.write("""
        **i) Database Preparation**:     
        Collected videos under various conditions (weather, times, viewing angles) to evaluate the blurring algorithm in different contexts.
        
        **ii) Blurring Algorithm Development**:        
        Designed an algorithm based on a Deep Learning model to blur faces.

        **iii) Blurring Optimization**:    
        Developed new approaches to improve blurring, especially for partially masked faces during initial tests.

        **iv) Performance Evaluation**:  
        Analyzed the model's performance according to three levels of face recognition:
        - Level 1: Clearly identifiable face.
        - Level 2: Profile face partially identifiable.
        - Level 3: Distant or partially visible face, making recognition difficult or impossible.

        **v) Documentation**:  
        Wrote comprehensive documentation of the implemented solution.
        """)
        st.subheader("b) ETA")
        st.write("""
        **i) Data Transformation**:     
        Converted AIS data from JSON format to a structured CSV format, then created a DataFrame to facilitate analysis.  
        Steps: 
        - Read JSON files
        - Extract relevant fields
        - Organize into CSV.

        **ii) Handling List Columns**:
        Managed complex columns like those containing ship positions:
        - Decomposition: Split list elements into separate columns.
        - New Columns: For example, transforming a "positions" column into "latitude" and "longitude".
        - Time Series Management: Adjusted data to time series if positions were timestamped.

        **iii) Documentation**:  
        Wrote comprehensive documentation of the implemented solution.
        """)

        st.subheader("4. Technologies Used")
        st.write("""
        Infrastructure (GCP):
        - Linux instance equipped with an NVIDIA V100 graphics card

        Deep Learning Frameworks:  
        - Keras  
        - TensorFlow  
        - CUDA

        Programming Language:  
        - Python

        Operating Systems:  
        - Windows  
        - Linux

        Cloud Computing:  
        - Google Cloud Platform (GCP)

        Version Control:  
        - GitLab

        Development Environments:  
        - Jupyter Notebook  
        - Visual Studio Code

        Project Management:  
        - Jira

        Hardware Acceleration:  
        - GPU
        """)

        st.header("5. Results")
        st.subheader("a) OBSCAME")
        st.write("""
                
        Developed a blurring algorithm with over 95% accuracy for all levels of facial recognition.
        """)
        st.subheader("b) ETA")
        st.write("""
        
        **i) Structured DataFrame**:    
        Created a DataFrame with well-defined columns, including information such as:  
        - MMSI (vessel unique identifier)
        - Dimensions (length, width)
        - Last known position (latitude, longitude)
        - Current speed
        - Direction (course)
        - ...

        **ii) Data Ready for Analysis**:  
        The final DataFrame is optimized for various analyses, such as ETA prediction, anomaly detection, navigation pattern analysis, and evaluation of maritime route efficiency.
        """)

    elif option == 'Sinay Internship':
        st.header("1. Position and Company")
        st.write("""
        **Company**: Sinay  
        **Specialty**: Specializes in the digitalization of the maritime sector and the preservation of the marine environment through the use of Big Data technologies        
        **Position**: Data & AI Engineer  
        **Employment Period**: May 2022 - October 2022
        """)

        st.header("2. Context and Issue")
        st.write("""
        During my end-of-studies internship at SINAY, I worked as an AI engineer within the Tech & Data team. My work was mainly focused on the OBSCAME project, a program aimed at analyzing videos of fishing activities, specifically to detect accidental captures of marine mammals.
        The goal of the internship was to automate the detection of accidental captures using AI-based neural network models. My role involved developing and evaluating these models to ensure their effectiveness under various video capture conditions.
        """)

        st.header("3. Tasks Completed")
        st.write("""
       
        **a) State of the Art:**         
        Conducted a comparative study of existing tools for image classification and object detection.  
        
        **b) Database Preparation:**   
        Split videos into images, then grouped these images into specific sets according to the studied species groups. I also performed a balance analysis to assess data distribution among different classes.  
       
        **c) Image Classification:**   
        Deployed classification models to distinguish marine mammals from other species present in the videos.  
        
        **d) Object Detection:**    
        Implemented an automatic detection system for marine mammals in both images and videos.  
        
        **e) Model Evaluation:**    
        Analyzed the performance of image classification and object detection models based on weather conditions, times of day, and camera angles. 
        
        The goal was to determine under which conditions the models were most effective and to identify potential areas for improvement.
        """)

        st.header("4. Technologies Used")
        st.write("""
         Infrastructure (GCP):
        - Linux instance equipped with an NVIDIA V100 graphics card

        Deep Learning Frameworks:  
        - Keras  
        - TensorFlow  
        - CUDA

        Programming Language:  
        - Python

        Operating Systems:  
        - Windows  
        - Linux

        Cloud Computing:  
        - Google Cloud Platform (GCP)

        Version Control:  
        - GitLab

        Development Environments:  
        - Jupyter Notebook  
        - Visual Studio Code

        Project Management:  
        - Jira

        Hardware Acceleration:  
        - GPU
        """)

        st.subheader("5. Results")
        st.write("Automatically detected marine mammals in videos with 85% accuracy using recent AI models deployed on Google Cloud Platform (GCP).")

    elif option == 'CEREMA Internship':
        st.header("1. Position and Organization")
        st.write("""
        **Organization**: CEREMA Normandie Centre  
        **Specialty**: 
        **Position**: Research Assistant  
        **Employment Period**: May 2021 - August 2021
        """)

        st.header("2. Context and Issue")
        st.write("""
        I completed my internship at CEREMA, a public institution under the Ministry of Ecological Transition and Territorial Cohesion. 

        Specifically, I worked within the ENDSUM team, composed of technicians and geoscience researchers, on the "TélédéTac" project. This project, supported by the Normandy Region, aims to develop remote sensing instruments to monitor, analyze, and assess coastal erosion, with the goal of improving the management and preservation of the Normandy coastline.

        My role within the team was to contribute to this project by studying the influence of soil and vegetation on the surface temperatures of the Vaches Noires cliffs.
        """)

        st.header("3. Tasks Completed")
        st.write("""
        **a) Data Acquisition Participation:**      
        Participated in data acquisition assisted by a team member who supervised a drone flight equipped with sensors over the Vaches Noires cliffs. This flight captured visible images as well as thermal images using LiDAR and a thermal camera. 
        
        These images were then used to perform photogrammetry, resulting in the creation of 3D models of the Vaches Noires, as well as visible and thermal orthophotos which I subsequently used.
        
        **b) Data Annotation:**          
        Annotated images using the Labelme annotation tool. This involved delimiting and annotating vegetation areas on images of the Vaches Noires cliffs.
        
        **c) State of the Art:**      
        Conducted a state-of-the-art review of thermal data analysis techniques and AI models for object segmentation.
        
        **d) Hot Spot Segmentation:**        
        Using the thermal orthophoto, I performed hot spot segmentation through thresholding with the help of QGIS. This step allowed me to identify areas with high temperatures compared to a set threshold. 
        
        Hot spots are generally associated with the presence of vegetation and sometimes water. Cold spots are mainly related to bare soil.
        
        **e) Vegetation Area Detection:**          
        Using a UNET neural network architecture, vegetation areas were segmented on visible images of the Vaches Noires cliffs. This detection allows for analysis of vegetation presence and distribution on the cliffs.

        """)

        st.subheader("4. Technologies Used")
        st.write("""
        Programming Language:
        - Python

        Deep Learning Frameworks:
        - Keras
        - Tensorflow
        
        Development Environment:
        - Jupyter Notebook
        
        Image Annotation:
        - Labelme
        
        Geographic Information System:
        - QGIS
        
        Hardware Acceleration:
        - GPU
        """)

        st.subheader("5. Results")
        st.write("""
        - Generated a temperature map using thresholding technique on thermal orthophotos. This map is black and white, where white areas indicate regions with temperatures exceeding a set threshold.
        - Segmented vegetation areas on visible images of the Vaches Noires cliffs using a neural network. The result is a black and white image where white areas indicate the presence of vegetation on the Vaches Noires cliffs. Subsequently, I conducted an analysis and comparison with the temperature map to identify hot areas not related to vegetation.
        """)
