# To run the script:  streamlit run pdf_binder.py

import streamlit as st # To create the web interface
import PyPDF2 # to work with PDF files

output_pdf = "documents/pdf_final" # Define the file name for the combined PDF

def bind_pdfs(output_path, documents):
    # Makes an object PdfMerger to combine PDF files
    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document) # Adds each PDF file 
        pdf_final.write(output_path) # Saves the PDF in the given path

# FRONT

st.image("assets/combine-pdf.png") #Shows an image to the user interface
st.header("Bind PDF") # Adds a header to the user's interface
st.subheader("Add PDFs to bind")  # Adds a subheader

# Make an area for the user to upload several PDF files

pdf_combined = st.file_uploader(label="", accept_multiple_files=True)

bind = st.button(label="Bind PDFs") # Create a button 

if bind:
    # starts a conditional if the bind button is clicked
    if len(pdf_combined) <=1:
        st.warning("You have to add more than 1 PDF") # Shows a warning 
    else:
        # starts a the code if two or more PDF files were added
        bind_pdfs(output_pdf, pdf_combined) # Binds the PDFs uploaded and saves the result as output_pdf
        st.success("Click here to download Final PDF") #Shows a succes message
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()  # Reads the Final PDF
        st.download_button(label="Download Final PDF", data= pdf_data, file_name="final_PDF.pdf")
