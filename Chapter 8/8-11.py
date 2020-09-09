def send_messages_func(messages, send_messages=[]):
    while messages:
        print(messages[0])
        send_messages.append(messages[0])
        messages.pop(0)
    
messages=['green', 'yellow','pink']
send_messages=[]
send_messages_func(messages[:], send_messages)
print(f"messages:{messages}")
print(f"send_messages:{send_messages}")
