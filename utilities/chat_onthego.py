import os
from dotenv import load_dotenv
import json
import time
from openai import OpenAI

class TextColors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"

system_message=""

assistant_id='asst_MNxKvaLKAJuSDba9DtaZYyv6'
thread_id=''

script_assistant_id='asst_E8DMkLHqCXwDMIsJ8O7OiDvs'

load_dotenv()

def do_chat():

    print(TextColors.RESET)

    client=OpenAI()

    metadata={"user": "test_user"}
    thread = client.beta.threads.create(metadata=metadata)
    print(thread)
    thread_id=thread.id

    try:
        print("\n***WELCOME***\n")
        while True:
            print(TextColors.BLUE)
            user_message = input("\nUser: ")
            print(TextColors.RESET)   
            
            message = client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_message
            )
        
            run = client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant_id,
            )
            # print(TextColors.CYAN)
            # print(run)
            # print(TextColors.RESET)

            while True:
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread_id,
                    run_id=run.id
                )

                if run.status=='completed':
                    print(TextColors.CYAN)
                    print("COMPLETED")
                    #print(run)
                    print(TextColors.RESET)
                    break

                if run.status=='requires_action':
                    print(TextColors.CYAN)
                    print("REQUIRES_ACTION")
                    print(run)
                    print(TextColors.RESET)

                    tool_calls = run.required_action.submit_tool_outputs.tool_calls
                    for tool_call in tool_calls:
                        tool_call_id = tool_call.id
                        function_arguments = tool_call.function.arguments                        
                        print("Tool Call ID:", tool_call_id)
                        print("Function Arguments:", function_arguments)

                    user_message="Please generate the script for the final configuration of the "\
                        "GoGo server "\
                        "based on the following arguments: "+function_arguments

                    print(TextColors.CYAN)
                    print("USER_MESSAGE: "+user_message)
                    print(TextColors.RESET)

                    thread_action = client.beta.threads.create(metadata=metadata)
                    print(thread)

                    message = client.beta.threads.messages.create(
                        thread_id=thread_action.id,
                        role="user",
                        content=user_message
                    )
                
                    run_script = client.beta.threads.runs.create(
                        thread_id=thread_action.id,
                        assistant_id=script_assistant_id,
                    )

                    while True:
                        run_script = client.beta.threads.runs.retrieve(
                            thread_id=thread_action.id,
                            run_id=run_script.id
                        )

                        if run_script.status=='completed':
                            print(TextColors.CYAN)
                            print("COMPLETED")
                            #print(run)
                            print(TextColors.RESET)
                            break

                        time.sleep(1)

                    messages = client.beta.threads.messages.list(
                        thread_id=thread_action.id,
                        limit=1
                    )
                    
                    print(TextColors.CYAN)
                    print(messages.data)
                    print(TextColors.RESET)   

                    print(TextColors.RED)
                    print(messages.data[0].content[0].text.value)
                    print(TextColors.RESET)   

                    response = client.beta.threads.delete(thread_action.id)
                    print(TextColors.CYAN)
                    print(response)
                    print(TextColors.RESET)

                    run = client.beta.threads.runs.submit_tool_outputs(
                        thread_id=thread_id,
                        run_id=run.id,
                        tool_outputs=[
                            {
                            "tool_call_id": tool_call_id,
                            "output": messages.data[0].content[0].text.value
                            }
                        ]
                    )

                    while True:
                        run = client.beta.threads.runs.retrieve(
                            thread_id=thread_id,
                            run_id=run.id
                        )

                        if run.status=='completed':
                            print(TextColors.CYAN)
                            print("COMPLETED")
                            #print(run)
                            print(TextColors.RESET)
                            break

                    break

                time.sleep(1)

            messages = client.beta.threads.messages.list(
                thread_id=thread_id,
                limit=1
            )
            
            print(TextColors.CYAN)
            print(messages.data)
            print(TextColors.RESET)   

            print(TextColors.RED)
            print(messages.data[0].content[0].text.value)
            print(TextColors.RESET)   


    except KeyboardInterrupt:
        if thread_id!="":
            response = client.beta.threads.delete(thread_id)
            print(TextColors.CYAN)
            print(response)
            print(TextColors.RESET)

        print("BYE BYE!!!")

do_chat()        