import fitz  # PyMuPDF

def get_table_of_contents(pdf_path):
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()  # PDF'nin içindekiler tablosunu al

    if toc:
        for level, title, page in toc:
            if level == 1: 
                print(f"Seviye: {level}, Başlik: {title}, Sayfa: {page}")
    else:
        print("Bu PDF dosyasında yerleşik bir içindekiler tablosu bulunmuyor.")

# Kullanım
pdf_path = "test books/linuxbook.pdf"
get_table_of_contents(pdf_path)
