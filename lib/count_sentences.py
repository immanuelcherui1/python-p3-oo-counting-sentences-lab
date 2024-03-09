#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str) or value == '':
            print('The value must be a string.')
        else:
            self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = 0
        for word in self.value.split():
            if word.endswith('.') or word.endswith('?') or word.endswith('!'):
                sentences += 1
        return sentences
