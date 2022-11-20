def sanitize_text(text: str) -> str:
    """
    Sanitize the text of a caption
    :param text: text of caption
    :return: sanitized text
    """
    return text.replace(chr(34), "").replace("\n", " ").replace(chr(160), " ")
