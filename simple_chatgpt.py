import openai

# OpenAI API key
openai.api_key = open("openai_key.txt", "r").read().strip() # Read the API key from a file
mod = "gpt-3.5-turbo" # The model to use

def loop():
    while True:
        prompt = input(">> Input: ")

        response = openai.ChatCompletion.create(
            model=mod,
            messages=[
                {"role": "system", "content": open("model_description.txt", "r").read().strip()},
                {"role": "user", "content": f"{prompt}"},
            ],
            temperature=0.5,
            presence_penalty=1,
            frequency_penalty=1
        )
        print("\n<< ", end=" ")
        print(response["choices"][0]["message"]["content"].strip() + "\n") # type: ignore

    print(">> Starting chat...\n")
    loop()