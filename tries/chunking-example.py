import google.generativeai as genai  

with open('gemini-api-key.txt', 'r') as f:
    api_key = f.read().strip()
genai.configure(api_key=api_key)
model_name ="gemini-pro"
model = genai.GenerativeModel(model_name)

path = "C:\\workdir\\PDFsummarizer\\test books\\output\\linux2\\markdown_chapters\\Chapter_2__The_Linux_Kernel.md"
path = "test books\\output\\linux-book.md"
path = "test videos\\output\\transcripts\\build your own cloud.txt"
with open(path, 'r',  encoding="utf-8") as f: 
    long_text = f.read().strip()

def get_token_count(text):
    ct = model.count_tokens(text)
    token_count = ct.total_tokens
    return token_count

print(len(long_text)) # 38160 
print(get_token_count(long_text))

def get_word_count(text):
    words = text.split()
    return len(words)

words_per_chunk = 800  # Approximately 450 words is around 300 tokens

# Function to split text by word limit
def split_text_by_words(text, words_per_chunk):
    words = text.split()
    chunks = [" ".join(words[i:i + words_per_chunk]) for i in range(0, len(words), words_per_chunk)]
    return chunks

# Split the text into chunks
text_chunks = split_text_by_words(long_text, words_per_chunk)

for chunk in text_chunks: 
    print(chunk[:100])
    print("\n")
print("###########################################\n")

# Define a function to get a summary for each chunk using Google GenAI
def get_summary(text):
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
    response = model.generate_content(prompt)
    summary = response.text
    print(f"Summary-----------------------\n")
    print(summary)
    return summary

print("###########################################\n")
summaries = [get_summary(chunk) for chunk in text_chunks]
final_summary = " ".join(summaries)
print(final_summary)
