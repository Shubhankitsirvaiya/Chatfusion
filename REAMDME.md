# Chat Fusion

**Chat Fusion** is a contextual chatbot project designed to maintain conversation history and provide coherent, context-aware responses using advanced natural language processing techniques. The project leverages OpenAI's GPT model and is implemented using Python and FastAPI for robust backend support.

This project is created in accordance with the **Grow Data Skills NLP Course**.

---

## Features
- Maintains a history of up to 10 recent messages for contextual awareness.
- Implements OpenAI's GPT-4 model for generating conversational responses.
- FastAPI integration for efficient REST API handling.
- Error handling for robust interaction.

---

## Folder Structure
```
chat_fusion/
├── app/
│   ├── main.py          # FastAPI application and chatbot integration
│   └── index.html       # Frontend for user interaction
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Prerequisites
- Python 3.8+
- An OpenAI API key with access to GPT models
- Basic understanding of Python and FastAPI

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/chat-fusion.git
   cd chat-fusion
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Usage
- **Frontend:** Interact with the chatbot via the provided HTML interface.
- **API:**
  Send a POST request to the `/chat` endpoint with user input to receive a response.

Example:
```bash
curl -X POST http://127.0.0.1:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"user_input": "Hello!"}'
```
Response:
```json
{
    "response": "Hi! How can I assist you today?"
}
```

---

## Future Enhancements
- Integration with a database for persistent conversation storage.
- Improved error handling and logging.
- Support for multiple GPT model versions.

---

## Credits
This project was developed as part of the **Grow Data Skills NLP Course** to demonstrate practical applications of NLP in chatbot development.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
