import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown("test books/linuxbook.pdf")
pathlib.Path("test books/output/linux-book.md").write_bytes(md_text.encode())
