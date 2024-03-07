import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

#default_model='gpt-3.5-turbo-0613'
default_model='gpt-3.5-turbo'
#default_model='gpt-4-0613'
#default_model='gpt-4-turbo-preview'

client = OpenAI()

def code_interpreter():
    # my_assistant = client.beta.assistants.create(
    #     instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    #     name="Math Tutor",
    #     tools=[{"type": "code_interpreter"}],
    #     model=default_model,
    # )
    # print(my_assistant)
    #asst_pKktLaY5uTOx3uYG8Xkg0XYG
    assistant_id='asst_pKktLaY5uTOx3uYG8Xkg0XYG'

    # metadata={
    #     "user": "abc123"
    #   }
    # thread = client.beta.threads.create(metadata=metadata)
    # print(thread)
    # print(thread.id)
    # thread_id='thread_JPpwtxEAmgRy5QzH1GI3McV1'

    # response = client.beta.threads.delete(thread_id)
    # print(response)

    # message = client.beta.threads.messages.create(
    #     thread_id=thread_id,
    #     role="user",
    #     content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
    # )
    # print(message)

    # run = client.beta.threads.runs.create(
    #   thread_id=thread_id,
    #   assistant_id=assistant_id,
    # )
    # print(run)

    # while True:
    #     run = client.beta.threads.runs.retrieve(
    #         thread_id=thread_id,
    #         run_id=run.id
    #     )
    #     print(run)

    #     if run.status=='completed':
    #         break

    #     time.sleep(2)

    # messages = client.beta.threads.messages.list(
    #   thread_id=thread_id
    # )
    # print(messages)

def retrieval():
    # my_assistant = client.beta.assistants.create(
    #     instructions="You are a personal assistant that will help me finding answers based on the files that i provide to you. If you don't find an answer in those files, you can check in your own knowledge but always tell me about the fact that you are doing this",
    #     name="Content Knowledge Helper",
    #     tools=[{"type": "retrieval"}],
    #     model=default_model,
    # )
    # print(my_assistant)
    assistant_id='asst_6LXZUS6CtBUP3oJ0XJz8Mw38'

    # file=client.files.create(
    #     file=open("../files/Attention is all you need - 1706.03762.pdf", "rb"),
    #     purpose="assistants"
    # )
    # print(file)
    file_id='file-3TO4Z87Ax50oF70hioGVQ1Zr'

    # assistant = client.beta.assistants.update(
    #     assistant_id=assistant_id,
    #     file_ids=[file_id],
    # )
    # print(assistant)

    # metadata={
    #     "user": "test_user"
    #   }
    # thread = client.beta.threads.create(metadata=metadata)
    # print(thread)
    thread_id='thread_VcbVHfUzmFZgqRwvin2tHcG3'
    # response = client.beta.threads.delete(thread_id)
    # print(response)

    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content="this is my 1st question: what is attention in the document?"
    )
    #print(message)

    run = client.beta.threads.runs.create(
      thread_id=thread_id,
      assistant_id=assistant_id,
    )
    # print(run)

    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

        if run.status=='completed':
            print(run)
            break

        time.sleep(1)

    messages = client.beta.threads.messages.list(
      thread_id=thread_id,
      limit=1
    )
    print(messages.data)

    #print("hello world")

def function_call():
    my_assistant = client.beta.assistants.create(
        instructions="You are a personal assistant that will help me finding answers based on the files that i provide to you. If you don't find an answer in those files, you can check in your own knowledge but always tell me about the fact that you are doing this",
        name="Content Knowledge Helper",
        tools=[{"type": "retrieval"}],
        model=default_model,
    )
    print(my_assistant)
    assistant_id='asst_6LXZUS6CtBUP3oJ0XJz8Mw38'

    # file=client.files.create(
    #     file=open("../files/Attention is all you need - 1706.03762.pdf", "rb"),
    #     purpose="assistants"
    # )
    # print(file)
    file_id='file-3TO4Z87Ax50oF70hioGVQ1Zr'

    # assistant = client.beta.assistants.update(
    #     assistant_id=assistant_id,
    #     file_ids=[file_id],
    # )
    # print(assistant)

    # metadata={
    #     "user": "test_user"
    #   }
    # thread = client.beta.threads.create(metadata=metadata)
    # print(thread)
    thread_id='thread_VcbVHfUzmFZgqRwvin2tHcG3'
    # response = client.beta.threads.delete(thread_id)
    # print(response)

    # message = client.beta.threads.messages.create(
    #     thread_id=thread_id,
    #     role="user",
    #     content="this is my 1st question: what is attention in the document?"
    # )
    # #print(message)

    # run = client.beta.threads.runs.create(
    #   thread_id=thread_id,
    #   assistant_id=assistant_id,
    # )
    # # print(run)

    # while True:
    #     run = client.beta.threads.runs.retrieve(
    #         thread_id=thread_id,
    #         run_id=run.id
    #     )

    #     if run.status=='completed':
    #         print(run)
    #         break

    #     time.sleep(1)

    # messages = client.beta.threads.messages.list(
    #   thread_id=thread_id,
    #   limit=1
    # )
    # print(messages.data)

    print("hello world")

#retrieval()