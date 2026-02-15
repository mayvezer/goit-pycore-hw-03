import re


def normalize_phone(phone_number: str) -> str:



    cleaned_number = re.sub(r"\D", "", phone_number)


    if cleaned_number.startswith("380"):
        return f"+{cleaned_number}"


    if cleaned_number.startswith("0"):
        return f"+38{cleaned_number}"


    if cleaned_number.startswith("38"):
        return f"+{cleaned_number}"

    return f"+{cleaned_number}"