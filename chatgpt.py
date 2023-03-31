from revChatGPT.V1 import Chatbot
import copy, os

class ChatGPT:
    d = {
    "access_token": os.environ.get('ACCESS_TOKEN'),
# "model": "gpt-4",
}
    chatbot3 = Chatbot(d)
    d4 = copy.deepcopy(d)
    d4['model'] = "gpt-4"
    chatbot4 = Chatbot(d4)
        
    @classmethod
    def chat_with_gpt3(cls, prompt):
        # prompt = "Python的垃圾回收算法有用到标记清除法吗？"
        response = ""
        for data in cls.chatbot3.ask(
          prompt
        ):
            response = data["message"]
    
        # print("\n\n\n仲谦：\n")
        # print(response)
        return response

    @classmethod
    def chat_with_gpt4(cls, prompt):
        # prompt = "Python的垃圾回收算法有用到标记清除法吗？"
        response = ""
        for data in cls.chatbot4.ask(
          prompt
        ):
            response = data["message"]
    
        # print("\n\n\n仲谦：\n")
        # print(response)
        return response

def chat_with_gpt3(prompt):
    return ChatGPT.chat_with_gpt3(prompt)

def chat_with_gpt4(prompt):
    return ChatGPT.chat_with_gpt4(prompt)

if __name__ == "__main__":
    ChatGPT = ChatGPT()
    ChatGPT.chat_with_gpt3("Python的垃圾回收算法有用到标记清除法吗？直接答是或者否即可")
    ChatGPT.chat_with_gpt4("Python的垃圾回收算法有用到标记清除法吗？直接答是或者否即可")
    # print("Chatbot: ")
    # prev_text = ""
    # for data in chatbot.ask(
    #     "说一下Python的垃圾回收机制",
    # ):
    #     message = data["message"][len(prev_text) :]
    #     print(message, end="", flush=True)
    #     prev_text = data["message"]
    # prompt = "Python的垃圾回收算法有用到标记清除法吗？"
    # response = ""
    # for data in chatbot.ask(
    #   prompt
    # ):
    #     response = data["message"]

    # print("\n\n\n仲谦：\n")
    # print(response)