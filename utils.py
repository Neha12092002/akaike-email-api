
import re

patterns = {
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "phone_number": r"\b(?:\+91[\-\s]?|0)?[6-9]\d{9}\b",
    "dob": r"\b(?:\d{1,2}[/-]){2}\d{2,4}\b",
    "aadhar_num": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d{4}[\s-]?){4}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])/?([0-9]{2}|[0-9]{4})\b",
    "full_name": r"\b([A-Z][a-z]+\s[A-Z][a-z]+)\b"
}

def mask_pii(email_text):
    masked_text = email_text
    masked_entities = []

    for entity, pattern in patterns.items():
        for match in re.finditer(pattern, masked_text):
            start, end = match.span()
            value = match.group()

            masked_entities.append({
                "position": [start, end],
                "classification": entity,
                "entity": value
            })

            masked_text = masked_text[:start] + f"[{entity}]" + masked_text[end:]
            break

    return masked_text, masked_entities
