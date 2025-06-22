# auth
This app is a fork from the [OAuth2-Integration-with-OAuthlib-and-GitHub](https://github.com/mchesler613/OAuth2-Integration-with-OAuthlib-and-GitHub) 
repo. This is a sample Django app to authenticate with an IDP as a third-party OAuth2 provider.

## Deployment
This app contains a secret page whose secret content can only be viewed after authenticating with the IDP.

Before authentication, the [secret page](https://aws.djangodemo.com/auth/page/) looks like this:

![Before Authentication](https://i.postimg.cc/T3Lx89gD/2021-04-21-14-13-13.jpg "Before Authentication")

After authentication:

![After Authentication](https://i.postimg.cc/GhSRSN8R/2021-04-21-14-12-03.jpg "After Authentication")

## Dependencies
This app uses the following Python packages
+ [python-dotenv](https://pypi.org/project/python-dotenv/), to store sensitive information
+ [oauthlib](https://github.com/oauthlib/oauthlib), to integrate with third-party OAuth2 providers, such as GitHub
+ [requests](https://github.com/psf/requests), to send HTTP GET and POST requests

To learn more about OAuth2 flow, refer to this [doc](https://datatracker.ietf.org/doc/html/rfc6749).
