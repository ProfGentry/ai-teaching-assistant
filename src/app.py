import streamlit as st
from document_loader import read_uploaded_file
from text_chunker import chunk_text

st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="🎓",
    layout="wide"
)

if "course_doucments" not in st.session_state:
    st.session_state.course_documents = {}
    
if "document_chunks" not in st.session_state:
    st.session_state.document_chunks = {}

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

if uploaded_file:
    
    for file in uploaded_file:
        if file.name not in st.session_state.course_documents:
            file_text = read_uploaded_file(file)

            st.session_state.course_documents[file.name] = file_text
            st.session_state.document_chunks[file.name] = chunk_text(file_text)
        
    st.subheader("Course Library")
    
    for filename in st.session_state.course_documents.keys():
        st.success(filename)
    
    selected_filename = st.selectbox(
        "Select a file to preview",
        list(st.session_state.course_documents.keys())
    )

    course_text = st.session_state.course_documents[selected_filename]
    chunks = st.session_state.document_chunks[selected_filename]

    #Read the file contents
    course_text = st.session_state.course_documents[selected_filename]
    chunks = st.session_state.document_chunks[selected_filename]

    with st.expander("Preview Uploaded Content"):
        st.write(course_text[:2000])
        
    with st.expander("Preview Content Chunks"):
        st.write(f"Total chunks created: {len(chunks)}")
        
        selected_chunk_index = st.selectbox(
            "Select a chunk to preview", 
            range(len(chunks))
        )

        st.write(chunks[selected_chunk_index])

st.subheader("Student Request")

user_prompt = st.text_area(
    "What would you like help with?",
    placeholder="Example: Explain this topic in simple terms."
)

submit_button = st.button("Generate Response")

if submit_button:
    if not user_prompt:
        st.warning("Please enter a question or request first.")
    elif not st.session_state.course_documents:
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