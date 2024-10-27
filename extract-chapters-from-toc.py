import fitz  # PyMuPDF


def extract_chapters_from_toc(pdf_path):
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()  # İçindekiler tablosunu al
    chapters = []  # Bölümleri saklamak için liste

    for i, entry in enumerate(toc):
        level, title, start_page = entry
        end_page = toc[i + 1][2] - 1 if i + 1 < len(toc) else doc.page_count - 1
        print("start#################")
        print(f"Level: {level}, Title: {title}, start_page: {start_page}, end_page: {end_page}")
        print("end###################\n")
        

        chapter_text = ""
        for page_num in range(start_page - 1, end_page):
            page = doc[page_num]
            chapter_text += page.get_text("text") + "\n"
        
        chapters.append({
            "title": title,
            "text": chapter_text.strip()
        })
    
    return chapters


# Kullanım
pdf_path = "test books/linuxbook.pdf"
chapters = extract_chapters_from_toc(pdf_path)

# Bölümleri yazdır
#for i, chapter in enumerate(chapters):
#    print(f"Bölüm {i + 1}: {chapter['title']}\n{'=' * 40}\n{chapter['text'][:500]}...\n")
