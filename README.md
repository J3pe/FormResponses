# FormResponses

FormResponses is a python library for automating  the sending of Google Forms responses. Made to be as easy to understand and use as possible! This removes all the annoying parts and makes it as simple as you could imagine.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install formresponses to start using this package for your project.

```bash
pip install formresponses
```
Note: If the installed version is lower than 0.1.0, the package wont work!

## Usage

```python
import formresponses as forms

#Setting the form url
forms.url("https://docs.google.com/forms/d/IDgoeshere/viewform")

#Choosing what to respond with to each question.
# Note: If the answer is a multiple choice question, this wont work with more than one answer chosen. 
# Note again: If the answer is choice question, you have to write the answer exactly like it says on the form.
forms.response(question=1, response="Wow, I can't believe this works!")

# the response may also be written like this!
forms.response(2, "Wow, I can't believe this works!")

# Sending the response
forms.send()
```


## If you want to be extra

If you want to be extra and send a little more responses.. include this at the end of your project

```python
while True:
    forms.send()
```
Or use threads, it's faster but more complicated, only use this if you are experienced with Python!

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
