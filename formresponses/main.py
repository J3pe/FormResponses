import requests
import re

responses = []
questions = []

def url(url):
    global form_url
    global questions
    form_url = url
    r = requests.get(form_url)
    entry = r.text.split('"')
    for n in entry:
        if "entry" in n:
            if not "data" in n:
                questions.append(n.replace("_sentinel", ""))
    form_url = re.sub(r"\?.*|viewform|edit", "", form_url)

    if not form_url.endswith("/"):
        form_url += "/"

    form_url += "formResponse"


def response(question, response):
    global responses
    if form_url:
        try:
            responses[question-1] = response
        except:
            responses.append(response)

def send():
    data = {}
    qr = dict(zip(questions, responses))
    data.update(qr)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    r = requests.post(url=form_url, data=data, headers=headers)
    if r.status_code != 200:
        print("[404] FormResponses: Something went wrong. Check the documentation for more information. https://github.com/J3pe/FormResponses")