from g4f.client import Client

def generate_logline(show_name):
    client = Client()
    q = f"Just generate log line of the '''{show_name}''' show with around 30 words, in Persian (Farsi) language without any explanation about the response before and after generated log line."
    print(q)
    is_valid_response = False
    while not is_valid_response:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": q,
                }
            ],
        )
        content = response.choices[0].message.content
        if 10 < len(content.split()) < 50:
            return content
        else:
            print(content)
