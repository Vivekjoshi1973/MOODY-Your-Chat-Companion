from dotenv import load_dotenv # important always load this to access  api keys 
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
)
model = ChatHuggingFace(llm=llm)

response=model.invoke("naruto uzumaki")
print(response.content) 
 # it is a limited service with limit because it is runnging on the servers of huging face 