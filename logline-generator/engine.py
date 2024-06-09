from g4f.client import Client

def generate_logline(show_name):
    client = Client()
    q = f"Generate Only log line of the '''{show_name}''' show with around 30 words, in Persian (Farsi) language without any explanation about the response before and after generated log line."
    print(q)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": q,
            }
        ],
    )
    return response.choices[0].message.content
