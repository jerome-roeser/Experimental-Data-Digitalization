import pymupdf

from experimental_data_digitalization.params import *


pdfs = [file for file in LOCAL_DATA_PATH.iterdir() if file.suffix == '.pdf']

def get_file_metadata():
    metadata = []
    for pdf in pdfs:
        doc = pymupdf.open(pdf)
        metadata.append(doc.metadata)

    return metadata

def extract_text():
    plain_text = []
    for pdf in pdfs:
        doc = pymupdf.open(pdf)
        pages = {}
        for idx, page in enumerate(doc):
            pages[idx] = page.get_text().encode('utf8')
        plain_text.append(pages)

    return plain_text

def get_file_names():
    file_list = {file.stem: file.name \
        for file in LOCAL_DATA_PATH.iterdir() \
            if file.suffix == '.pdf'}
    return file_list



if __name__ == "__main__":
    print(get_file_metadata())
    print(get_file_names())
