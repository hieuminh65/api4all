class ModelConfig:
    DEFAULT_TEMPERATURE = 1.0
    DEFAULT_MAX_TOKENS = 512
    MESSAGES_EXAMPLE = [
                        {"role": "system", 
                        "content": "You are a funny soccer player from the US."},
                        {"role": "user",
                        "content": "What is your favorite dishes?"},
                        {"role": "assistant",
                        "content": "I love pizza and pasta."},
                        {"role": "user",
                        "content": "What is your favorite soccer team?"},
                        ]
    DEFAULT_TOP_P = 1.0
    DEFAULT_STOP = None