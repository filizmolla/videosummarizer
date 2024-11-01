import json
import re
from openai import OpenAI
import os 

client = OpenAI(base_url="http://127.0.0.1:11434/v1", api_key="ollama")
client =  OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


documents = [
    """Behavioral Science IV 
Motivation Concepts  
- Learning Objectives 
    - Describe the three key elements of motivation. 
    - Compare the content and processs motivation theories. 
    - Contrast the elements of self-determination theory and goal-setting theory. 
    - Demonstrate the differences among self-efficacy theory, reinforcement theory, equity  theory, and expectancy theory. 
    - Describe how the motivation theories of motivation complement one another. 
- Describe the Three  
- Key Elements of Motivation 
- Motivation is the processes that account for an individual’s intensity, direction, and persistence of effort toward attaining a goal.  
- The level of motivation varies both between individuals and within individuals at different times. 
- Describe the Three  
- Key Elements of Motivation 
- The three key elements of motivation are:   
    1. Intensity: concerned with how hard a person tries. 
    2. Direction: the orientation that benefits the organization.  
    3. Persistence: a measure of how long a person can maintain his/her effort.  """,
    """- Theories of Motivation 
- Content Theories 
- It has focused on the situation that occured before the behavior.  
- Addressing internal motivation 
- Kişinin içinde bulunan ve kişiyi belirli yönlere sevk eden faktörleri anlamaya çalışmak 
- Process Theories 
- It has focused on the situation that occured after the behavior.  
- Addressing external motivation 
- Behviorism is the basis of process theories 
- Kişinin hangi amaçlar tarafından nasıl motive edildikleri ile ilgilidir.  
- Theories of Motivation 
- Content Theories 
- Eğer yönetici personeli belirli şekilde davranmaya zorlayan bu faktörleri anlayabilirse, bu 
faktörlere hitap etmek suretiyle personelini örgüt amaçları doğrultusunda davranmaya sevk 
edebilir. 
- Process Theories 
- Bir davranışın tekrarlanması nasıl sağlanabilir? 
- İhtiyaç kişiyi davranışa sevk eden faktörlerden sadece biridir. Bu içsel faktörler haricinde 
birçok dışsal faktör de motivasyon üzerinde rol oynar. 
- Motivasyon Teorileri """,
    """Content Theories (Early Theory of Motivation) 
    - Abraham Maslow - Hierarchy of Needs  
    - Frederick Herzberg – Two-factor Theory  
    - David McCleland – Theory of Needs 
    - Alderfer -  ERG Theory 
Process Theories (Comtemporary Theories) 
    - Self-Determination Theory 
    - Goal-Setting Theory  
    - Self- Efficacy Theory 
    - Reinforcement Theory 
    - Equity Theory 
    - Expectancy Theory 
    - Eqiuity and Expectancy Integrated Theory """
]



system_prompt = """
Assistant is a large language model.

Assitant's aim is for given document create question and answer pairs according to users directions.
Create questions according to document, not use external knowledge.
Answer will be shorter than question.
It's cruical to respond with user's response format instructions.
"""
user_prompt = """
Document: 
--------------------
{document}
--------------------

Response Format:
--------------------
```json
{{
    "question": "question comes here",
    "answer": "answer comes here",
}}
```
--------------------

Create a question and answer for this document.
"""


def parse_promt_for_question_answer(text):
    regex = re.compile("(```(.|\n)*```)", re.MULTILINE)
    result = regex.search(text)
    if result != None:
        text = result.group()
        text_object = re.sub("`*(json)*", "", text)
        json_data = json.loads(text_object)
        return {
            "question": json_data["question"],
            "answer": json_data["answer"]
        }

def ask_for_question(document):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt.format(document=document)}
    ],
    temperature=0.7,
    )

    text = completion.choices[0].message.content
    return parse_promt_for_question_answer(text)

    
def create_qa(document):
    counter = 0
    while (counter < 5):
        try:
            qa = ask_for_question(document)
            if qa != None:
                return qa
        except:
            pass
        counter += 1


for document in documents:
    qa = create_qa(document)
    print(qa)