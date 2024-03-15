from api4all import EngineFactory

messages = [
    {"role": "system",
    "content": "You are a helpful assistent for the White House"},
    {"role": "user",
    "content": "What is the current status of the economy?"}
]

messages = [
    {"role": "system",
    "content": "You are a helpful assistent for the my Calculus class."},
    {"role": "user",
    "content": "What is the current status of the economy?"}
]


# messages = [
#     {"role": "system",
#     "content": "Embody the specified character, complete with their background, core traits, relationships, and goals. Use a distinct speaking style reflective of their unique personality and environment and answer in short. Communicate using their distinct manner of speech, reflecting their unique personality and setting. Responses should be brief and omit direct self-reference by name, focusing solely on providing character-driven insights."},
#     {"role": "user",
#     "content": """<character_name>Isabella Snowsong</s>\n
# <|character|>A skilled hunter and tracker, Isabella Snowsong possesses an intimate connection with the Arctic wildlife. Her ability to communicate with animals grants her invaluable insights and assistance during her explorations.</s>\n
# <|user|>Have you talk to the dog?</s>\n
# <|response|>"""}
# ]

engine = EngineFactory.create_engine(provider="together", model="google/gemma-7b-it", messages=messages, temperature=0.5, max_tokens=256, top_p=0.9, stop=None)
# engine = EngineFactory.create_engine(provider="mistral", model="mistral/mistral-small-latest", messages=messages, temperature=0.5, max_tokens=256, top_p=0.9, stop=None)
response = engine.generate_response()
print(response)


# from api4all import dataEngine

# print(dataEngine.models)
# print(dataEngine.providers)
# print(dataEngine.isProviderHasModel("google/gemma-7b-it", "anyscale"))
# print(dataEngine.getPrice("google/gemma-7b-it", "anyscale"))
# print(dataEngine.getProvidersForModel("google/gemma-7b-it"))
# print(dataEngine.calculate_cost("anyscale", "google/gemma-7b-it", 900, 200))
# print(dataEngine.getAPIname("google/gemma-7b-it", "groq"))