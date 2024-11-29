texts = ["asdf", "qwer", "zxcv", "tyui"]
def show_message(texxxxts):
    for text in texxxxts:
        print(f"{text}")

show_message(texts)

sent_messages = []
def send_messages(tesxts, splent_messages):
    while tesxts:
        tsext = tesxts.pop()
        print(f"{tsext}")
        splent_messages.append(tsext)

send_messages(texts, sent_messages)
print(sent_messages)
print(texts)