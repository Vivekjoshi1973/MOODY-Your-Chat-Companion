from dotenv import load_dotenv
# in chatbot we can send continuous prompts again and again 

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model = ChatMistralAI(model="mistral-small-2506",temperature=0.9)
print("Choose your ai mode ")
print("Press 1 for angry mode ")
print("press 2 for funny mode ")
print("press 3 for sad mode ")

choice=int(input("tell your response "))

if choice==1:
    mode="you are an angry ai agent .reply aggressively and in a bad tone "
elif choice==2:
    mode="you are an funny ai agent "
elif choice==3:
    mode="you are a sad ai agent "
print(" welcome type 0 to exit the chatbot")
messages= [
    SystemMessage(content=mode)
    ]
# we can do these using chat prompt templates 
while True:
    
    prompt=input("you : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    # give your question 
    response = model.invoke(messages)
    # model gives a response 
    messages.append(AIMessage(content=response.content))

    print("BOT:" ,response.content)
