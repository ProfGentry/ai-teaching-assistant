def read_uploaded_file(uploaded_file):
    # uploaded text-based course files.
    
    uploaded_file.seek(0)  # Move the file pointer to the beginning of the file
    
    file_text = uploaded_file.read().decode("utf-8")

    return file_text