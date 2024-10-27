import pymupdf  # PyMuPDF
import re 

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_]', '_', filename)


def get_table_of_contents(pdf_path):
    doc = pymupdf.open(pdf_path)
    toc = doc.get_toc()
    level1_toc = []
    if toc:
        print(type(toc))
        print(toc)
        for level, title, page in toc:
            if level == 1: 
                print(f"Seviye: {level}, Başlik: {title}, Sayfa: {page}")
                level1 = [title,  page]
                level1_toc.append(level1)
        print(type(level1_toc))
        doc.close()
        return level1_toc
    else:
        print("Bu PDF dosyasında yerleşik bir içindekiler tablosu bulunmuyor.")
        doc.close()
        return []

def extract_chapters_from_toc(pdf_path, level1_toc):
    doc = pymupdf.open(pdf_path)
    chapters = []  
    print(toc)

    for i, value in enumerate(level1_toc):
        title, chapter_start_page = value

        if (i + 1) != len(level1_toc):
           chapter_end_page = level1_toc[i+1][1]  
        
        #doc_len = doc.__len__()     
        #if chapter_end_page == doc_len - 1 and chapter_start_page == doc_len :
        #    print("Last page is 1 page.")
        #    chapter_end_page = doc_len + 1
        
        chapter_page_count = chapter_end_page - chapter_start_page        
        print(f" Başlik: {title}, Start: {chapter_start_page} End: {chapter_end_page} Page count: {chapter_page_count} ") # [start, end)
        
        chapter_text = ""
        for page_num in range(chapter_start_page - 1, chapter_end_page - 1) if chapter_page_count != 0 else range(chapter_start_page -1, chapter_end_page): 
            page = doc[page_num]
            chapter_text += page.get_text("text") + "\n"

        chapters.append({
            "title": title,
            "text": chapter_text.strip()
        })
        
        filename = sanitize_filename(title) + ".txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(chapter_text.strip())
        print(f"{title} bölümü '{filename}' dosyasına kaydedildi.")

    doc.close()
    return chapters


    

# Kullanım
pdf_path = "test books/linuxbook.pdf"
toc = get_table_of_contents(pdf_path)

if toc: 
    chapters = extract_chapters_from_toc(pdf_path,toc)

#Bölümleri yazdır
for i, chapter in enumerate(chapters):
    print(f"Bölüm {i + 1}: {chapter['title']}\n{'=' * 40}\n{chapter['text'][:500]}...\n")
