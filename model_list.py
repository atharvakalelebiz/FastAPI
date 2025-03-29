import openai
from openai import OpenAI

# Setup the client
client = OpenAI(
    base_url="https://beta.sree.shop/v1",
    api_key="ddc-beta-bnsvvfd1nx-OpH3p78LEiLmJRbTnylkWEazAn0Pwnrqt1L"
)

# Try to get the list of models
try:
    models = client.models.list()
    print("Available models:")
    for model in models.data:
        print(f"- {model.id}")
except Exception as e:
    print(f"Error getting models: {e}")
    print("This API might not support listing models. Using default model.")
    
# Create a completion with the specified model
try:
    # Use a fully-qualified model name from the list
    response = client.chat.completions.create(
        model="Provider-7/gpt-4o-mini",  # Notice the provider prefix
        messages=[
            {"role": "user", "content": "Hello!"}
        ]
    )
    print("\nResponse:")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error creating completion: {e}")
    
    # If the first attempt fails, try another model
    try:
        print("\nTrying with a different model...")
        response = client.chat.completions.create(
            model="Provider-5/deepseek-r1",
            messages=[
                {"role": "user", "content": "Hello!"}
            ]
        )
        print("Response:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error with second model: {e}")