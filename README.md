## 🧪 Sample Usage

**Endpoint**: `POST /classify-email`  
**Request Body**:
```json
{
  "email": "Hi, I’m Neha CK. My phone is 9876543210 and email is neha@example.com. I need help logging into my account."
}
```

**Response**:
```json
{
  "input_email_body": "Hi, I’m Neha CK. My phone is 9876543210 and email is neha@example.com. I need help logging into my account.",
  "list_of_masked_entities": [
    {
      "position": [53, 69],
      "classification": "email",
      "entity": "neha@example.com"
    },
    {
      "position": [29, 39],
      "classification": "phone_number",
      "entity": "9876543210"
    }
  ],
  "masked_email": "Hi, I’m Neha CK. My phone is [phone_number] and email is [email]. I need help logging into my account.",
  "category_of_the_email": "Incident"
}
```
