from g4f.client import Client


def is_valid_logline(logline):
    chars = (
        'اآبپتسجچحخدذرزژسشصضطظعغفقکگلمنوهی1234567890ثءabcdefghijklmnopqrstuvwxyz۱۲۳۴۵۶۷۸۹۰."   -_!؟?:;,،«»\u200cABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )
    for c in logline:
        if c and (c not in chars):
            print(c.encode("utf8"))
            print(f"invalid*{c}*")
            return False
    return True


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
        if is_valid_logline(content):
            print("saved:", content)
            return content
        else:
            print(content)
