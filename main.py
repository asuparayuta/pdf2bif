# 2024/01/03改定
import base64
import tempfile

import streamlit as st
from pdf2image import convert_from_path
import json

from pathlib import Path

def show_pdf(file_path:str):
    """Show the PDF in Streamlit
    That returns as html component

    Parameters
    ----------
    file_path : [str]
        Uploaded PDF file path
    """

    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)


def main():
    """Streamlit application
    """

    st.title("BIF extractor from PDF file")
    uploaded_file = st.file_uploader("Choose your .pdf file (local)", type="pdf")



    if uploaded_file is not None:
        # Make temp file path from uploaded file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            st.markdown("Extraction from PDF(convert json)")
            fp = Path(tmp_file.name)
            fp.write_bytes(uploaded_file.getvalue())
            #st.write(show_pdf(tmp_file.name))

            imgs = convert_from_path(tmp_file.name)
            with open('connection.json') as f:
                di = json.load(f)
                print(f)
            st.json(di)
            st.markdown(f"Converted images from PDF")            
            st.image(imgs)


if __name__ == "__main__":
    main()
