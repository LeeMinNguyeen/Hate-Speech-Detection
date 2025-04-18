# Gemma 2 9B Instruct

"""

Using the above output, format into the following json schema because we require processing before replying to the user.

```json
{
"stop_interview": { "type": "boolean" },
"ask": { 
    "question": "string",
    "answers": {
      "1": <Option 1>,
      "2": <Option 2>,
      ...
    }
  }
}
```

Requirements:
- Only output json objects and do not prefix or suffix the message with irrelevant text.
"""