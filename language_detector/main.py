# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
  results = {}
  for language in languages:
    count = 0
    for word in text.split():
        if word in language['common_words']:
            count += 1
    results[language['name']] = count
  return max(results, key=results.get)
