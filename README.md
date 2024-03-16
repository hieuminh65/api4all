# api4all
Easy-to-use LLM API from a state-of-the-art provider and comparison.

## Features
- **Easy-to-use**: A simple and easy-to-use API for state-of-the-art language models from different providers but in a same way.
- **Comparison**: Compare the cost and performance of different providers and models.
- **Log**: Log the response and cost of the request in a log file.
- **Providers**: Support for all of providers both open-source and closed-source.
- **Result**: See the actual time taken by the request, especially when you dont't trust the benchmark.

## Installation
1. Install the package
```bash
pip3 install api4all
```

2. Create and activate a virtual environment (optional but recommended)
- Unix / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
- Windows
```bash
python3 -m venv venv
.\venv\Scripts\activate
```

## Quick Start
1. Wrap the API key in a `.env` file of the provider you want to test.
```bash
TOGETHER_API_KEY=xxx
OPENAI_API_KEY=xxx
MISTRAL_API_KEY=xxx
ANTHROPIC_API_KEY=xxx
```

or set the environment variable directly.
```bash
export TOGETHER_API_KEY=xxx
export OPENAI_API_KEY=xxx
```

2. Run the code
```python
from api4all import EngineFactory

messages = [
    {"role": "system",
    "content": "You are a helpful assistent for the my Calculus class."},
    {"role": "user",
    "content": "What is the current status of the economy?"}
]


engine = EngineFactory.create_engine(provider="together", 
                                    model="google/gemma-7b-it", 
                                    messages=messages, 
                                    temperature=0.5, 
                                    max_tokens=256, 
                                    )

response = engine.generate_response()

print(response)
```

3. Check the [log file](logfile.log) for the response and the cost of the request.
```bash
Request ID - fa8cebd0-265a-44b2-95d7-6ff1588d2c87
	create at: 2024-03-15 16:38:18,129
	INFO - SUCCESS
	
    Response:
		I am not able to provide information about the current status of the economy, as I do not have access to real-time information. Therefore, I recommend checking a reliable source for the latest economic news and data.
	
    Cost: $0.0000154    # Cost of this provider for this request
    Provider: together  # Provider used for this request
    Execution-time: Execution time not provided by the provider
    Actual-time: 0.9448428153991699 # Actual time taken by the request
    Input-token: 33     # Number of tokens used for the input
    Output-token: 44    # Number of tokens used for the output
```

## Providers and Models

### Providers

| Provider | Free Credit | Rate Limit | API Key name | Provider string name |
|:------:|:------:|:------:|:------:|:------:|
|  [Groq](https://wow.groq.com)          |     Unlimited | 30 Requests / Minute  | GROQ_API_KEY | "groq"  |
|  [Anyscale](https://www.anyscale.com)  |     $10      | 30 Requests / Second  |  ANYSCALE_API_KEY | "anyscale"  |
|  [Together AI](https://www.together.ai)|     $25      | 1 Requests / Second  | TOGETHER_API_KEY | "together"  | 
|  [Replicate](https://replicate.com)    |     Free to try  | 50 Requests / Second    | REPLICATE_API_KEY | "replicate"  |
|  [Fireworks](https://fireworks.ai)     |     $1      | 600 Requests / Minute  |  FIREWORKS_API_KEY | "fireworks"  |  
|  [Deepinfra](https://deepinfra.com)    |     Free to try     | 200 Concurrent request |  DEEPINFRA_API_KEY | "deepinfra"  |
|  [Google AI (Vertex AI)](https://ai.google.dev)    |     Unlimited     | 60 Requests / Minute | GOOGLE_API_KEY | "google"  |
|  [OpenAI](http://openai.com)    |     &#x2715;     | 60 Requests / Minute | OPENAI_API_KEY | "openai"  |
|  [Mistral AI](https://mistral.ai)    |     Free to try     | 5 Requests / Second | MISTRAL_API_KEY | "mistral"  |
|  [Anthropic](https://www.anthropic.com)    |     Free to try     | 5 Requests / Minute | ANTHROPIC_API_KEY | "anthropic"  |


- **Free to try**: Free to try, no credit card required but limited to a certain number of tokens.

### Open-source models
  -- |Mixtral-8x7b-Instruct-v0.1 | Gemma 7B it |  Mistral-7B-Instruct-v0.1 | LLaMA2-70b |
|:------:|:------:|:------:|:------:|:------:|
|  API string name          |     "mistralai/Mixtral-8x7B-Instruct-v0.1"    | "google/gemma-7b-it"    | &#x2715;  | "meta/Llama-2-70b-chat-hf" |
|  Context Length          |     32,768    | 8.192    |  4,096 | 4,096
|  Developer          |     Mistral AI    | Google    |  Mistral AI | Meta
|  Cost (Input - Output / MTokens)          |     -----    | ------    | ------ | -----
|  [Groq](https://wow.groq.com)          |     $0-$0    | $0-$0    | &#x2715; | $0-$0
|  [Anyscale](https://www.anyscale.com)  |     $0.5-$0.5       | $0.15-$0.15       |  $0.15-$0.15 | $1.0-$1.0
|  [Together AI](https://www.together.ai)|     $0.6-$0.6        | $0.2-$0.2        | $0.2-$0.2 | $0.9-$0.9
|  [Replicate](https://replicate.com)    |     $0.3-$1       | &#x2715;       |  $0.05-$0.25 | $0.65-$2.75
|  [Fireworks](https://fireworks.ai)     |     $0.5-$0.5        | $0.2-$0.2        |  $0.2-$0.2  | $0.9-$0.9
|  [Deepinfra](https://deepinfra.com)    |     $0.27-$0.27    | &#x2715;    |   &#x2715; | $0.7-$0.9

### Closed-source models
#### 1. Mistral AI

| Model | Input Pricing ($/1M Tokens) | Output Pricing ($/1M Tokens) | Context Length | API string name |
|:------:|:------:|:------:|:------:|:------:|
|  Mistral-7B-Instruct-v0.1          |     $0.25        | $0.25    |  8,192 | "mistral/open-mistral-7b" |
|  Mixtral-8x7b-Instruct-v0.1          |     $0.7        | $0.7    |  8,192 | "mistral/open-mixtral-8x7b" |
|  Mixtral Small          |     $2        | $6    |  &#x2715; | "mistral/mistral-small-latest" |
|  Mixtral Medium          |     $2.7        | $8.1    |  &#x2715; | "mistral/mistral-medium-latest" |
|  Mixtral Large          |     $8        | $24    |  &#x2715; | "mistral/mistral-large-latest" |


#### 2. OpenAI

| Model | Input Pricing ($/1M Tokens) | Output Pricing ($/1M Tokens) | Context Length | API string name |
|:------:|:------:|:------:|:------:|:------:|
|  GPT-3.5-0125          |     $0.5        | $1.5    |  16,385 | "openai/gpt-3.5-turbo-0125" |
|  GPT-3.5          |     $0.5        | $1.5    |  16,385 | "openai/gpt-3.5-turbo" |
|  GPT-4          |     $30        | $60    |  8,192 | "openai/gpt-4" |
|  GPT-4          |     $60        | $120    |  32,768 | "openai/gpt-4-32k" |


#### 3. Anthropic
| Model | Input Pricing ($/1M Tokens) | Output Pricing ($/1M Tokens) | Context Length | API string name |
|:------:|:------:|:------:|:------:|:------:|
|  Claude 3 Opus  |     $15        | $75    |  200,000 | "anthropic/claude-3-opus" |
|  Claude 3 Sonnet  |     $3        | $15    |  200,000 | "anthropic/claude-3-sonnet" |
|  Claude 3 Haiku  |     $0.25        | $1.25    |  200,000 | "anthropic/claude-3-haiku" |
|  Claude 2.1  |     $8        | $24    |  200,000 | "anthropic/claude-2.1" |
|  Claude 2.0  |     $8        | $24    |  100,000 | "anthropic/claude-2.0" |
|  Claude 2.0  |     $0.8        | $2.4    |  100,000 | "anthropic/claude-instant-1.2" |


#### 4. Google
| Model | Input Pricing ($/1M Tokens) | Output Pricing ($/1M Tokens) | Context Length | API string name |
|:------:|:------:|:------:|:------:|:------:|
|  Google Gemini 1.0 Pro  |     $0        | $0    |  32,768 | "google/gemini-1.0-pro" |


## Contributing
Welcome to contribute to the project. If you see any updated pricing, new models, new providers, or any other changes, feel free to open an issue or a pull request.