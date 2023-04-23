# OSINT-compass Engine - API Documentation

## Overview

OSINT-compass Engine is an API that provides open-source intelligence (OSINT) information by aggregating data from various sources such as term searches, domain information, email data, and social media. It is part of the open source tool OSINT-compass.

The main project can be found [here](https://github.com/elpato-dev/OSINT-compass).

## Getting Started

In order to use the API, you will need a valid API key. The API key is passed as a query parameter in every request.

## API Endpoints

### Home

- URL: `/`
- Method: `GET`

This endpoint returns a welcome message for the OSINT-compass API.

### Term

- URL: `/term`
- Method: `GET`
- Parameters:
  - `apikey`: string (required) - Your API key.
  - `term`: string (required) - The search term.
  - `news_count`: integer (optional, default: 10) - The number of news articles to retrieve.
  - `tweet_count`: integer (optional, default: 10) - The number of tweets to retrieve.

The news endpoint returns information about news articles and tweets related to a specific topic. The structure of the response is as follows:
```javascript
{
  "news": {
    "articles": [
      {
        "content": string,
        "source": string,
        "title": string,
        "url": string
      },
      ...
    ],
    "count": integer,
    "sentiment": float
  },
  "tweets": {
    "sentiment": float,
    "tweets_text": [string, ...]
  }
  "wikipedia": [
    {"<title of article>": "<link to article>"}, ...
    ]
    ...
  }
}
```
### Domain

- URL: `/domain`
- Method: `GET`
- Parameters:
  - `apikey`: string (required) - Your API key.
  - `domain`: string (required) - The domain to get information about.

The domain endpoint returns information about a specific domain, including its robots.txt content, subdomains, and archived snapshots from the Wayback Machine. The structure of the response is as follows:
```javascript
{
"sources": [
    {
        "title": "robots_txt",
        "content": string
    },
    {
        "title": "wayback_machine",
        "content": {
            "archived_snapshots": {
                "closest": {
                    "available": boolean,
                    "status": string,
                    "timestamp": string,
                    "url": string
                }
            },
            "url": string
        }
    },
    {
        "title": "subdomains",
        "content": [string, ...
        ]
    }
]
}
```

### Email

- URL: `/email`
- Method: `GET`
- Parameters:
  - `apikey`: string (required) - Your API key.
  - `email`: string (required) - The email to get information about.

The email endpoint returns information about an email address, including its deliverability, whether it's disposable or spam, and associated company and executive data. The structure of the response is as follows:
```javascript
{
"sources":[
  "pingutil": {
    "data": {
      "catch_all": boolean,
      "deliverable": boolean,
      "disposable": boolean,
      "domain": string,
      "email_address": string,
      "gibberish": boolean,
      "spam": boolean,
      "valid_syntax": boolean,
      "webmail": boolean
    },
    "status": string
  },
  "spycloud": {
    "company": {
      "discovered": integer,
      "discovered_unit": string,
      "name": string,
      "records": integer
     },
     "executives": {
      "count": integer
     },
     "you": {
      "discovered": integer,
      "discovered_unit": string,
      "records": integer
    }
  ]
}
```

### Alert

- URL: `/alert`
- Method: `POST`
- Parameters:
  - `apikey`: string (required) - Your API key.
  - `term`: string (required) - The search term.
  - `channel`: string (required) - The communication channel for alerts (currently only Telegram).
  - `contact`: string (required) - The contact information for the channel (the Telegram chat id).
  - `scoregt`: float (optional) - The minimum score for an alert to be triggered.
  - `scorelt`: float (optional) - The maximum score for an alert to be triggered.

This endpoint sets an alert based on the given term and specified conditions.

### Snscrape

- URL: `/snscrape`
- Method: `GET`
- Parameters:
  - `apikey`: string (required) - Your API key.
  - `term`: string (optional) - The search term.
  - `user`: string (optional) - Representing the name of the Reddit user whose submissions and comments you want to retrieve.
  - `subreddit`: string (optional) - Representing the name of the subreddit whose submissions and comments you want to retrieve.
  - `entries`: integer (optional) - Representing the number of entries to retrieve. Default is 10.
  - `reddit`: boolean (required) - Indicating whether to retrieve data from Reddit. Must be set to true.
  - `submissions`: boolean (optional) - Indicating whether to retrieve submissions. Default is true.
  - `comments`: boolean (optional) - Indicating whether to retrieve comments. Default is true.

This endpoint searches the specified social media platforms (Instagram and/or Facebook) for the given term and returns the results. To search on Reddit, you must set at least one of the following to true: `term`, `user`, or `subreddit`.
```javascript
{
    "reddit": {
        "results": [
            {
                "author": string,
                "body": string,
                "created": date,
                "id": number,
                "parentId": number,
                "subreddit": string,
                "type": "comment",
                "url": string
            },
            {
                "author": string,
                "created": date,
                "id": number,
                "link": string,
                "selftext": string,
                "subreddit": string,
                "title": string,
                "type": "submission",
                "url": string
            }
        ],
        "sentiment": number
    }
}

```

## Error Handling

When an error occurs, the API will return a JSON object with an `error` key containing the error message. The HTTP status code will also be set accordingly to indicate the error type (e.g., 400 for bad request, 403 for forbidden).

## Example

To get term data using the OSINT-compass API:

```plaintext
GET /term?apikey=<your-api-key>&term=brazil
