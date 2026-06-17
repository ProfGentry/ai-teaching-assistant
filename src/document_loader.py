def read_uploaded_file(uploaded_file):
    # uploaded text-based course files.
    
    file_text = uploaded_file.read().decode("utf-8")

    return file_text