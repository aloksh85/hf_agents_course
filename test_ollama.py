"""
This is a test script to test the Ollama model.

It uses the LiteLLMModel class from the smolagents library to interact with the Ollama model.

It uses the qwen2:7b model, which is a 7B parameter model.

It uses the http://127.0.0.1:11434 API base, which is the default Ollama local server.
"""

from smolagents import LiteLLMModel

model = LiteLLMModel(
    model_id="ollama/qwen2:7b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "You are a expert haiku writer. Write a beautiful emotional haiku about babies",
            }
        ],
    }
]

response = model.generate(messages, response_format={"type": "text"})

print("================")
print(response.content)
