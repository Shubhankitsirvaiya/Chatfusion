from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()



client = OpenAI()

class ContextualChatbot:

    def __init__(self):
        self.conversation_history = []
        self.max_history_length = 10  # Adjust as needed


    def update_conversation_history(self, role, content):
        self.conversation_history.append({"role": role, "content": content})
        if len(self.conversation_history) > self.max_history_length:
            self.conversation_history = self.conversation_history[-self.max_history_length:]

    def generate_response(self, user_input):
        self.update_conversation_history("user", user_input)
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    *self.conversation_history
                ]
            )
            assistant_response = response.choices[0].message.content.strip()
            self.update_conversation_history("assistant", assistant_response)
            return assistant_response
        except Exception as e:
            print(f"An error occurred: {e}")
            return "I'm sorry, but I encountered an error. Please try again."


app = FastAPI()
chatbot = ContextualChatbot()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Restrict for specific domains if needed.
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)

class UserInput(BaseModel):
    message: str


@app.post("/chat")
def chat(input: UserInput):
    user_message = input.message
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    response = chatbot.generate_response(user_message)
    return {"response": response}
