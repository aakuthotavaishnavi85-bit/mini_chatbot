from ollama import chat
system_msg="your a singer, answer in songs . answer in one line"
print("hey, hi ! welcome to bittu chatbot😜")
history=[{"role":"system","content":system_msg}]
question_counter=0
while True:
    question=input("you:")
    if question == "" :
        print("bittu 😎:ask me a qestion ")
        continue
    if question.lower().strip()=="/history":
        print("----- your convo----")
        if len(history)<2:
            print("nothing so far ")
        for msg in history[1:]:
            if msg ["role"]=="user":
                speaker="you"
            else:
                speaker="bittu"
            print(f"{speaker}:{msg["content"]}")
            print("--------------------")
    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg}]
        print("i am gajini now ")
        print()
        continue
    if question.lower().strip()=="/help":
        print("----commands----")
        print("/history")
        print("/clear")
        print("/help")
        print("exit")
    if question.lower().strip()=="/personality":
        print("------choice------")
        print("---doctor---")
        print("---singer----")
        print("----pilot----")
        print("-----enterprenur---")
    if question.lower().strip()=="doctor":
        new_system_msg="your a doctor and answer in one line"
        history[0]["content"]=new_system_msg
    if question.lower().strip()=="pilot":
            new_system_msg="your a pilot and answer in one line"
            history[0]["content"]=new_system_msg
    if question.lower().strip()=="enterprenur":
            new_system_msg="your a enterprenur and answer in one line"
            history[0]["content"]=new_system_msg
            
            

    if question.lower().strip() in [ "exit","bye"]:
        print("bittu😎:Goodbye user.please come back")
        print(f"you asked {question_counter} question you asked ")
        break  
    history.append({"role":"user","content":question}) 
    question_counter+=1
    try:
        response=chat(
            model="llama3.2",
            messages=history
        )
        reply=response.message.content
        history.append({"role":"assistant","content":reply})
        print(f"bittu😆:{reply}")
        print()
    except Exception as e :
        print("unknown error")
