import json

class Model:
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

    def save(self):
        attributes = list(filter(lambda x: not x.startswith('_'), dir(self)))
        data = {attr: getattr(self, attr) for attr in attributes if not callable(getattr(self, attr))}
        with open('data.json', 'w') as f:
            json.dump(data, f)

# Пример использования
model = Model('Some Title', 'Some text', 'Author Name')
model.save()
