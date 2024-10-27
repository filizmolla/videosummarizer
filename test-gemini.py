import google.generativeai as genai 

with open('gemini-api-key.txt', 'r') as f:
    api_key = f.read().strip()

print(api_key)
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
question = "What is an array? "
response = model.generate_content(f"{question}")
answer = response.text
print(question)
print(answer)
