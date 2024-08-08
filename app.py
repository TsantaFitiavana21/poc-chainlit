import chainlit as cl
from llm import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    messages.append({"role": "user", "content": message.content})
    response = ask_order(messages)
    messages.append({"role": "assistant", "content": response})

    await cl.Message(
        content=response,
    ).send()

# @cl.on_chat_start
# async def start():
#     await cl.Message(
#         content="Hello, I am virtual assistant to add information about company to a recruitment online searching job",
#     ).send()