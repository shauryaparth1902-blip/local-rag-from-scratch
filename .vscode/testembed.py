import json
import requests
import math
def cosinsim(vec1,vec2):
    dot_product=(sum(a*b for a,b in zip(vec1,vec2)))
    magnitude1=math.sqrt(sum(a*a for a in vec1))
    magnitude2=math.sqrt(sum(b*b for b in vec2))
    if magnitude1==0 or magnitude2==0:
        return 0
    else:
        return dot_product/(magnitude1*magnitude2)

if __name__ =="__main__":
    tnqns=10
    last_embeding= None
    for i in range(tnqns):
        question=input("Enter your question: ")
        url="http://localhost:11434/api/embeddings"
        data={"model":"nomic-embed-text",
               "prompt":f"{question}"}
        post=requests.post(url,json=data,stream=False)  
        response=json.loads(post.text)
        if last_embeding is None:
            last_embeding=response["embedding"]
            continue
        else:

            similarity=cosinsim(last_embeding,response["embedding"])    
            print(f"Cosine similarity between last embedding and current embedding: {similarity}")
            last_embeding=response["embedding"]
        

       