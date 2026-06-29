from dotenv import load_dotenv
# in chatbot we can send continuous prompts again and again 

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model = init_chat_model("google_genai:gemini-2.5-flash-lite")
print(" welcome type 0 to exit the chatbot")
messages= [
    SystemMessage(content="you are a funny ai agent ")
    ]

while True:
    
    prompt=input("you : ")
    messages.append(HumanMessage(content=prompt))
    if prompt ==0:
        break
    # give your question 
    response = model.invoke(messages)
    # model gives a response 
    messages.append(AIMessage(content=response.content))

    print("BOT:" ,response.content)


    # currently our model dont have any memory to give answers according to he prevoius response
    # make a list to save this 

    # we are creating a message history to give contex to the answes 

    # our current chatbots doesnot have 
    # no role seperation ( no system/ user/ assistant distinction )
    # just raw strings weak conversation structure
    # memory keeeps growing infinitely 
    # will hit token limit
    # api cost increases over time 
    # slower respomse as history grows 
    # no trimming, summarization of old chats 
    # no production scalable 
    # no control over context window 


    # now to fix the assigning of role you need to use messages 
    # langchan_core.messages it divides messafges into three parts 
    # syste,ai,human meassages 
