import requests
import json
import tiktoken
import os   
from testembed import cosinsim
def get_embeddings(text):
    url="http://localhost:11434/api/embeddings"
    data={"model":"nomic-embed-text",
           "prompt":f"{text}"}
    post=requests.post(url,json=data,stream=False)  
    response=json.loads(post.text)
    return response
def build_embedding_index(file_path):
    with open(file_path,'r',encoding="utf-8")as f:
        content=f.read()
        mainvetor=[]

        paragraphs=[p.strip()for p in content.split("\n\n") if p.strip()]
        for q in paragraphs:
            embeddingvector=get_embeddings(q)
            newr={"text":q,"embedding":embeddingvector["embedding"]}
            mainvetor.append(newr)
        
        return mainvetor


    
    

    return best_para
    
def trim_memory(histroy,maxtokens=1000):
    while True:
        total_tokens = sum(counttoken(message["content"]) for message in histroy)
        while total_tokens > maxtokens and len(histroy) > 3:
            total_tokens -= counttoken(histroy.pop(1)["content"])
            total_tokens -= counttoken(histroy.pop(1)["content"])
        return histroy
def counttoken(text):
    encoder=tiktoken.get_encoding("cl100k_base")
    tokens=encoder.encode(text)
    return len(tokens)

    
if __name__ == "__main__":
    
    number_of_questions = 3
    question_number = 0
    conversation_history = [{ "role": "system", "content": "You are smart and helpful assistant with knowledge in every fieild. Explain everything in detail and provide examples when possible."}]

    while True:
        file_path = input("Enter the file path (or leave blank to skip): ").strip()
        if not file_path:
            print("Skipping file...")
            break
        
        # ... (your os.path.exists checks go here) ...
        break
    while question_number < number_of_questions:
        question = str(input("Question: "))
        conversation_history.append({
            "role": "user",
            "content": question
        })
        if file_path!="":
            context=build_embedding_index(file_path)
            qn=get_embeddings(question)
            max_similarity=0
            best_para=None
            for _ in range(len(context)):
                similarity=cosinsim(qn["embedding"],context[_]["embedding"])
                if similarity>max_similarity:
                    max_similarity=similarity
                    best_para=context[_]["text"]

            if best_para:
                conversation_history.append({
                "role": "system",
                "content": f"Context from the file: {best_para}"
                })
                conversation_history.append({
                    "role": "user",
                    "content": question
                })
            else:
                conversation_history.append({
                    "role": "user",
                    "content": question
                })

        conversation_history = trim_memory(conversation_history)
        data = {
            "model": "phi3",
            "messages": conversation_history,
            "stream": True}
                    
                    
        url="http://localhost:11434/api/chat"
        response = requests.post(url, json=data, stream=True)
        aireply = ""
        for line in response.iter_lines():
        
            if line:
                response_json = json.loads(line.decode("utf-8"))
                ai_reply = response_json["message"]["content"]
                aireply += ai_reply
                print(ai_reply, end="", flush=True)
        print("\n")


            
        question_number += 1
        conversation_history.append({"role": "assistant", "content": aireply})
