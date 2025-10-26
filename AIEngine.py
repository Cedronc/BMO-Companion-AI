# model="HuggingFaceH4/zephyr-7b-beta",
from ollama import chat
from ollama import ChatResponse

def get_temperature(city: str) -> str:
  """Get the current temperature for a city
  
  Args:
    city: The name of the city

  Returns:
    The current temperature for the city
  """
  temperatures = {
    'New York': '22°C',
    'London': '15°C',
    'Mechelen': '11°C',
  }
  return temperatures.get(city, 'Unknown')

available_functions = {
  'get_temperature': get_temperature,
}

while True:
  print("\n")
  userInput = input("Enter Prompt...")
  messages = [
      {
          'role': 'user',
          'content': userInput,
      },
  ]

  response: ChatResponse = chat(model='BMO', tools=available_functions.values(), stream=True, messages=messages, think=True)


  content = ''
  tool_calls = []
  in_thinking = False
  for chunk in response:
    if chunk.message.thinking and not in_thinking:
      in_thinking = True
      print('Thinking:\n', end='')

    if chunk.message.thinking:
      print(chunk.message.thinking, end='')
    elif chunk.message.content:
      if in_thinking:
        print('\nAnswer:\n', end='')
        in_thinking = False
      print(chunk.message.content, end='')

      # Old
    if chunk.message.content:
        print(chunk.message.content, end='', flush=True)
        # accumulate the partial content
        content += chunk.message.content
    if chunk.message.tool_calls:
        tool_calls.extend(chunk.message.tool_calls)


  # append accumulated fields to the messages
  if content or tool_calls:
      messages.append({'role': 'assistant', 'content': content, 'tool_calls': tool_calls})

  for call in tool_calls:
      if call.function.name == 'get_temperature':
          result = get_temperature(**call.function.arguments)
      else:
          result = 'Unknown tool'
          messages.append({'role': 'tool', 'tool_name': call.function.name, 'content': result})
      print('\nFunction Result:')
      print(result)

# new_messages = [{ 'role': 'assistant', thinking: thinking, content: content }]
# response = chat(model='BMO', stream=True, messages=new_messages)

# for chunk in response:
#   if chunk.message.content:
#     print(chunk.message.content, end='', flush=True)
#     # accumulate the partial content
#     content += chunk.message.content