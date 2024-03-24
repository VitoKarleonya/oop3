import json

class Model:
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

    def save(self):
        attributes = {attr: getattr(self, attr) for attr in dir(self) if not attr.startswith('__') and not callable(getattr(self, attr))}
        with open('model.json', 'w') as file:
            json.dump(attributes, file)

# Example usage
model = Model('Some title', 'Some text', 'Some author')
model.save()
