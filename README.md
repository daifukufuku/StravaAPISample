
# Strava OAuth Flow Guide
This guide provides instructions and sample code for fetching your activity data and split data using the Strava API.

## Python Version
Python 3.6 or newer

## Modules
pip install requests

## Preparation
First, confirm your client id and secret from the following page:
[Strava API Settings](https://www.strava.com/settings/api)

## Authorize Your Application
Use the URL below to authorize your application. Make sure to replace `<YOUR_CLIENT_ID>` with your actual client ID:

```
https://www.strava.com/oauth/authorize?client_id=<YOUR_CLIENT_ID>&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all
```

## **Capture the Authorization Code**
Once you've authorized the application, you will be redirected to the given `redirect_uri`. Capture the value after `code=` from the URL.

## **Exchange Authorization Code for an Access Token**
Using `curl`, replace the placeholders with the appropriate values to get your access token:

```
curl -X POST https://www.strava.com/oauth/token \
    -F client_id=YOUR_CLIENT_ID \
    -F client_secret=YOUR_CLIENT_SECRET \
    -F code=YOUR_COPIED_CODE \
    -F grant_type=authorization_code
```

## Verify the Access Token

```
curl -X GET \
https://www.strava.com/api/v3/athlete/activities \
-H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

## API Reference
https://developers.strava.com/docs/reference/