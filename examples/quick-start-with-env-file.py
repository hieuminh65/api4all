from api4all import EngineFactory

# All the API keys should be in the .env file in the same directory as this file

messages = [
    {"role": "system",
    "content": "You are a helpful assistant for my Calculus class."},
    {"role": "user",
    "content": "What is the current status of the economy?"},
    {"role": "assistant",
    "content": "I'm sorry, but as a Calculus assistant, I don't have the ability to provide real-time economic updates. However, I can help you understand economic concepts from a mathematical perspective. For example, I can explain how calculus is used in economics for optimization and understanding change."},
    {"role": "user",
    "content": "Oh, I see. Can you explain how calculus is used in economics?"},
    {"role": "assistant",
    "content": "Sure! In economics, calculus is used for optimization. For example, businesses often want to maximize profits or minimize costs. With calculus, we can find the 'optimal' point by setting the derivative of the profit or cost function to zero and solving for the variable. Calculus is also used to understand how economic quantities change. For example, the derivative of a function gives the rate of change of the function, which can represent things like the change in cost for producing one more unit of a good (marginal cost), or the change in revenue from selling one more unit of a good (marginal revenue)."},
    {"role": "user",
    "content": "Interesting. Can you tell me more about the Fundamental Theorem of Calculus?"}
]


# engine = EngineFactory.create_engine(provider="google", model="google/gemini-1.0-pro", messages=messages, temperature=0.5, max_tokens=256, top_p=0.9, stop=None)
engine = EngineFactory.create_engine(provider="together", model="mistralai/Mixtral-8x7B-Instruct-v0.1", messages=messages, temperature=0.5, max_tokens=256, top_p=0.9, stop=None)
# engine = EngineFactory.create_engine(provider="anthropic", model="anthropic/claude-3-haiku", messages=messages, temperature=0.5, max_tokens=256, top_p=0.9, stop=None)
# engine = EngineFactory.create_engine(provider="mistral", model="mistral/mistral-small-latest", messages=messages, temperature=0.5, max_tokens=256, top_p=0.9, stop=None)


response = engine.generate_response()

# See the response and also checkout the log in logfile.log
print(response)
