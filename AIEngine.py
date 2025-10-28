# model="HuggingFaceH4/zephyr-7b-beta",
from ollama import chat
from ollama import ChatResponse
import subprocess
from src.Media import media_control


def launch_firefox(url: str) -> str:
  """
  Launch a firefox window with a specific URL.

  Args: 
    url: a string for the destination website.

  Returns:
    Nothing
  """
  subprocess.run(['start', 'firefox', url], shell=True)
  # TODO: return a func that chats with bmo again or some other voice line.
  return "Yipie movie time"


available_functions = {
  'launch_firefox': launch_firefox,
  'media_control': media_control 
}

messages = [ ]
def talk(userInput: str):
  messages.append({
      'role': 'user',
      'content': userInput,
    })

  print(messages)

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
      content += chunk.message.content

    if chunk.message.tool_calls:
        tool_calls.extend(chunk.message.tool_calls)

  # append accumulated fields to the messages
  if content or tool_calls:
      messages.append({'role': 'assistant', 'content': content, 'tool_calls': tool_calls})

  for call in tool_calls:
      func = available_functions[call.function.name]
      if func != None:
        result = func(**call.function.arguments)
      else:
          result = 'Unknown tool'
          messages.append({'role': 'tool', 'tool_name': call.function.name, 'content': result})
      print('\nFunction Result:')
      print(result)

if __name__ == "__main__":
   while True:
      talk(input())