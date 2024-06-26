# Translator API Documentation

## Description
This API allows you to translate text using Google Translate.

## API Request Methods
- GET
- POST

## API Endpoint
Base URL: `https://translator.eg-mgn.com/`

## Parameters
| Name                   | Description                                     | Required | Options                               |
|------------------------|-------------------------------------------------|----------|---------------------------------------|
| `query`                | The text to be translated.                      | Yes      | N/A                                   |
| `query.target_language`| The target language for translation.            | Yes      | N/A                                   |
| `query.source_language`| The source language of the text (optional).     | No       | Auto-detection or specific language code |

## Usage
```python
import requests

url = "https://translator.eg-mgn.com/translator"
data = {
    "query": "Hello, world!",
    "query.target_language": "es",
    "query.source_language": "en"
}

response = requests.post(url, json=data)
print(response.json())
```

<a href="https://heroku.com/deploy?template=https://github.com/dev-virous/TranslateAPI">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku">
</a>
