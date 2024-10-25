import pymupdf

from experimental_data_digitalization.params import *



def get_file_metadata():
    pdfs = [file for file in LOCAL_DATA_PATH.iterdir() if file.suffix == '.pdf']
    metadata = []
    for pdf in pdfs:
        doc = pymupdf.open(pdf)
        metadata.append(doc.metadata)

    return metadata

if __name__ == "__main__":
    print(get_file_metadata())
