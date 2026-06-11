#!/usr/bin/python3
"""
This module provides a function to indent text based on specific punctuation.
It adds two newlines after each '.', '?', and ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The string to be formatted and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # تنظيف النص من الفراغات في بدايته ونهايته المطلقة أولاً
    text = text.strip()

    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            # تخطي أي مسافات فارغة تلي مباشرة الحروف الثلاثة لمنع ظهورها أول السطر الجديد
            while i + 1 < length and text[i + 1] == " ":
                i += 1
        i += 1
