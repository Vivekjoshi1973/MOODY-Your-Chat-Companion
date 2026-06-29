from dotenv import load_dotenv

load_dotenv()

# now we can use all api keys inside environment file here


# to use any chat model use this  from lanchain docs models 
from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-2.5-flash-lite")
# print(model)

 # to print info about models like token limit s etc types of input and output types and info about tool calling and too outputs etc 

response = model.invoke("Why do parrots talk?")
# how to invoke a model to get response from it it will give output in a combined form like all data is not seperated 
# print(response)
print(response.content) # it will give output in oraganized form as well this process is fast as well 

# similarly we can use any api key to get reaponse 
# for grok models go to thier websites 
