import streamlit as st
from document_loader import read_uploaded_file

st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("AI Teaching Assistant")
st.write("Upload course content, ask questions, and generate learning support materials.")

with st.sidebar:
    st.header("Settings")

    mode = st.selectbox(
        "Choose a mode",
        [
            "Ask a Question",
            "Explain a Concept",
            "Generate Study Guide",
            "Generate Practice Quiz"
        ]
    )

    audience = st.selectbox(
        "Audience level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

st.subheader("Upload Course Material")

uploaded_file = st.file_uploader(
    "Upload course files",
    type=["txt", "md"],
    accept_multiple_files=True
)

course_text = ""

if uploaded_file:
    
    st.subheader("Course Library")
    
    # Display uploaded Files
    for file in uploaded_file:
        st.success(file.name)
    
    #Create the list of Filenames    
    file_names = [file.name for file in uploaded_file]

    #Let the user select a file to preview
    selected_filename = st.selectbox(
        "Select a file to preview",
        file_names
    )

    #Get the actual uploaded file object 
    selected_file = next(
        file for file in uploaded_file
        if file.name == selected_filename
    )

    #Read the file contents
    course_text = read_uploaded_file(selected_file)

    with st.expander("Preview Uploaded Content"):
        st.write(course_text[:2000])

st.subheader("Student Request")

user_prompt = st.text_area(
    "What would you like help with?",
    placeholder="Example: Explain this topic in simple terms."
)

submit_button = st.button("Generate Response")

if submit_button:
    if not user_prompt:
        st.warning("Please enter a question or request first.")
    elif not uploaded_file:
        st.warning("Please upload course material first.")
    else:
        st.subheader("AI Response")

        st.markdown("### Response Preview")
        st.write(
            f"""
            **Mode:** {mode}  
            **Audience Level:** {audience}  
            **Student Request:** {user_prompt}  
            **Source File:** {uploaded_file.name}
            """
        )

        st.markdown("### Course Content Used")
        st.write(course_text[:1000])