from __future__ import annotations
import os 
import time 
from time import localtime, strftime
from datetime import datetime as PyDateTime
from models import PDFDocument
import google.generativeai as genai 
import re 
import fitz  # PyMuPDF
import re 
import pymupdf4llm
import pathlib

BOOK = "pythonmath"
pathlib.Path('test books/output/'+ BOOK + '/chapters/').mkdir(parents=True, exist_ok=True) 
pathlib.Path('test books/output/'+BOOK+ '/markdown_chapters/').mkdir(parents=True, exist_ok=True) 

class PDFSummarizer:
    PATH = os.getcwd()
    notes_path = PATH + "\\output\\pdfchapters"
    model_name ="gemini-pro"
    client =  genai.GenerativeModel(model_name)
    user_prompt = """
    Please summarize this text.
    Text:
    \"""{text}\"""
    """

    def __init__(self,  pdfdocument: PDFDocument):
        self.pdfdocument = pdfdocument
        self.toc = ""

    def start(self):
        self.set_api_key()
        self.summarize(self.pdfdocument)

    def set_api_key(self):
        with open('gemini-api-key.txt', 'r') as f:
            api_key = f.read().strip()
            self.api_key = api_key
            genai.configure(api_key=api_key)
    
   
    def sanitize_filename(self, filename):
        return re.sub(r'[^a-zA-Z0-9_]', '_', filename)

    def get_table_of_contents(self, pdf_path):
        doc = fitz.open(pdf_path)
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

    def extract_chapters_from_toc(self, pdf_path, level1_toc):
        doc = fitz.open(pdf_path)
        chapters = []  
        print(self.toc)

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
            # Create a new PDF document for the chapter
            chapter_doc = fitz.open()

            chapter_text = ""
            for page_num in range(chapter_start_page - 1, chapter_end_page - 1) if chapter_page_count != 0 else range(chapter_start_page -1, chapter_end_page): 
                page = doc[page_num]
                chapter_text += page.get_text("text") + "\n"
                chapter_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
            chapter_filename = self.sanitize_filename(title) + ".pdf"
            chapter_path = f"test books/output/{BOOK}/chapters/"
            chapter_doc.save(chapter_path + chapter_filename)
            chapter_doc.close()  
            print(f"{title} chapter saved as '{chapter_filename}'")

            chapters.append({
                "title": title,
                "text": chapter_text.strip(),
                "path": chapter_filename
            })
        doc.close()
        return chapters

    def chapter_doc_to_markdown(filename):
        path = f"test books/output/{BOOK}/chapters/"
        md_text = pymupdf4llm.to_markdown(path + filename + ".pdf")
        pathlib.Path(f"test books/output/{BOOK}/markdown_chapters/{filename}.md").write_bytes(md_text.encode())


    def summarize(self, pdfdocument: PDFDocument):
        start_time = time.time()
        prompt = self.user_prompt.format(title=pdfdocument.title, transcript=pdfdocument.text)
        response = self.client.generate_content(prompt)
        summary = ""
        try:
            if hasattr(response, 'text') and response.text is not None:
                summary = response.text
                print(f"Summary for {pdfdocument.title}: {summary}")
            else:
                finish_reason = getattr(response, 'finish_reason', 'Unknown')
                print(f"No valid summary returned for {pdfdocument.title}. Reason: {finish_reason}")
                summary = f"No valid summary returned for {pdfdocument.title}. Reason: {finish_reason}"
        except ValueError as e:
            summary = f"ValueError encountered for {pdfdocument.title}: {e}"
            print(f"ValueError encountered for {pdfdocument.title}: {e}")
        except Exception as e:
            summary = f"Unexpected error for {pdfdocument.title}: {e}"
            print(f"Unexpected error for {pdfdocument.title}: {e}")
 
        end_time = time.time()
        summary_time = end_time - start_time 
        note_filename = self.notes_path + "\\" + pdfdocument.title + ".txt" 
        self.save_summary(summary, note_filename)
                
        return summary

    def save_summary(self, summary_text, note_filename):
        with open(note_filename, "w", encoding="utf-8") as file: 
            file.write(summary_text) 

        print(f"Note saved to {note_filename}")
