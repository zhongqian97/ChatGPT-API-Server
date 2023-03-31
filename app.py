import chatgpt

from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST'])
def translate():
    def extract_content(input_data):
        contents = [message["content"] for message in input_data["messages"]]
        return "\n".join(contents)
    
    def wrap_output_content(output_str):
        return {
            "id": "chatcmpl-70D64JgXAOgjbkLBbOWahCWVszGd5",
            "object": "chat.completion",
            "created": 1680284700,
            "model": "gpt-3.5-turbo-0301",
            "usage": {
                "prompt_tokens": 46,
                "completion_tokens": 11,
                "total_tokens": 57
            },
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": output_str
                    },
                    "finish_reason": "stop",
                    "index": 0
                }
            ]
        }
    
    def chat_with_gpt(input_data):
        # # 示例输入
        # input_data = {
        #     'messages': [
        #         {
        #             'content': 'You are a translation engine that can only translate text and cannot interpret it.',
        #             'role': 'system'
        #         },
        #         {
        #             'content': 'translate from en to zh-CN:\n\n"status code" =>',
        #             'role': 'user'
        #         }
        #     ],
        #     'frequency_penalty': 1,
        #     'model': 'gpt-3.5-turbo',
        #     'temperature': 0,
        #     'presence_penalty': 1,
        #     'top_p': 1,
        #     'max_tokens': 1000
        # }
        
        # 从输入中提取内容并合并
        content_to_translate = extract_content(input_data)
        
        # 将内容传递给 chat_with_gpt 函数（此处需要实现与 GPT 交互的逻辑）
        translated_content = chatgpt.chat_with_gpt3(content_to_translate)
        
        # 对输出的字符串进行封装
        output_data = wrap_output_content(translated_content)
        output_json = output_data
        # 将输出数据转换为 JSON 格式
        # output_json = json.dumps(output_data, ensure_ascii=False, indent=4)
        # print(output_json)
        return output_json

    data = request.get_json(force=True)
    print("Received data:", data)  # Temporary print statement to debug the received data

    if not data:
        return jsonify({"error": {"type": "param", "message": "缺少必要的输入数据"}}), 400

    option = data

    # Check if the required keys are present in the data
    required_keys = ['model', 'messages']
    if not all(key in option for key in required_keys):
        return jsonify({"error": {"type": "param", "message": "缺少必要的输入数据"}}), 400

    # Extract the query data from the messages
    # Extract the query data from the messages
    user_messages = [message for message in option['messages'] if message['role'] == 'user']
    if not user_messages or len(user_messages) < 1:
        return jsonify({"error": {"type": "param", "message": "缺少必要的输入数据"}}), 400
    
    query = {
        'text': user_messages[-1]['content'].split('=>')[1].strip(' "'),
        'detectFrom': user_messages[-1]['content'].split()[2],
        'detectTo': user_messages[-1]['content'].split()[4]
    }
    print("Query data:", query)  # Temporary print statement to debug the extracted query data
    

    # Add the text to be translated as an additional user message
    data['messages'].append({'role': 'user', 'content': query['text']})

    # Extract the API key from the request headers
    authorization = request.headers.get('Authorization')
    if not authorization:
        return jsonify({"error": {"type": "param", "message": "缺少API密钥"}}), 400
    api_key = authorization.replace('Bearer ', '')

    # Set the default API URL and path if they are not present in the data
    # api_url = option.get('api_url', 'https://api.openai.com')
    # api_url_path = option.get('api_url_path', '/v1/chat/completions')

    # headers = {
    #     'Content-Type': 'application/json',
    #     'Authorization': f'Bearer {api_key}'
    # }
    
    # response = requests.post(
    #     api_url + api_url_path,
    #     headers=headers,
    #     json=data
    # )

    # print("zhongqian: \n" + str(response.json()))
    # return jsonify(response.json())
    return jsonify(chat_with_gpt(data))

if __name__ == '__main__':
    app.run('0.0.0.0',port='5000')