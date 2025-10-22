# model="HuggingFaceH4/zephyr-7b-beta",
from ollama import chat
from ollama import ChatResponse

while True:
    userInput = input("Enter Prompt...")
    response: ChatResponse = chat(model='BMO',  stream=True, messages=[
    {
        'role': 'user',
        'content': userInput,
    },
    ])

    content = ''
    thinking = ''
    for chunk in response:
        if chunk.message.content:
            print(chunk.message.content, end='', flush=True)
            # accumulate the partial content
            content += chunk.message.content

    print("\n")
    print("\n")

  # append the accumulated fields to the messages for the next request

# new_messages = [{ 'role': 'assistant', thinking: thinking, content: content }]
# response = chat(model='BMO', stream=True, messages=new_messages)

# for chunk in response:
#   if chunk.message.content:
#     print(chunk.message.content, end='', flush=True)
#     # accumulate the partial content
#     content += chunk.message.content