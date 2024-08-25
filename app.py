import streamlit as st

def main():
    # Titre de l'application
    #st.title("Dossier de Compétences Professionnelles")

    # Sélection de la langue
    st.sidebar.header("Langue")
    language = st.sidebar.radio("Choisissez la langue", ["Français", "English"])

    # Navigation entre les pages
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Choisissez une page", ["Présentation", "CV optimisé", "Expériences Professionnelles", "Formations"])

    if page == "Présentation":
        if language == "Français":
            import presentation_page_fr
            presentation_page_fr.show_presentation_page()
        else:
            import presentation_page_en
            presentation_page_en.show_presentation_page()
    elif page == "CV optimisé":
        if language == "Français":
            import premiere_page_fr
            premiere_page_fr.show_premiere_page()
        else:
            import premiere_page_en
            premiere_page_en.show_premiere_page()
    elif page == "Expériences Professionnelles":
        if language == "Français":
            import deuxieme_page_fr
            deuxieme_page_fr.show_deuxieme_page()
        else:
            import deuxieme_page_en
            deuxieme_page_en.show_deuxieme_page()
    elif page == "Formations":
        if language == "Français":
            import troisieme_page_fr
            troisieme_page_fr.show_troisieme_page()
        else:
            import troisieme_page_en
            troisieme_page_en.show_troisieme_page()

if __name__ == "__main__":
    main()
