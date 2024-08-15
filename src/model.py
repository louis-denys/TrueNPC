import requests
import json

class chat_handler:
    def __init__(self, id) -> None:
        self.url = "http://localhost:11434/api/chat"
        self.chat_id = id

    def save(self, history):
        with open('./chats/' + self.chat_id + '.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)

    def read(self):
        with open('./chats/' + self.chat_id + '.json', 'r', encoding='utf-8') as f:
            return json.loads(f.read())

    def prompt(self, prompt: str):
        """
        The prompt method adds a new interaction to the conversation and saves it.
        """
        history = self.read()
        history.append({
                "role": "user",
                "content": prompt
                })
        data = {
            "model": "llama3",
            "messages": history,
            "stream": False
        }
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(self.url, headers=headers, json=data)
        response = response.json()['message']
        history.append(response)
        self.save(history)
        return(response['content'])
    