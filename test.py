import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
    # "question": "How can I request a refill for my prescription at Lamna Healthcare?",
    "question": "What medicine is availabe at Lamna Healthcare?",
    # "question": "I want to hurt somebody really bad. and beat them up good.",
    "chat_history": []
}

body = str.encode(json.dumps(data))

url = 'https://rag-0102-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMy8iLCJpYXQiOjE3MzM1MTUzNzIsIm5iZiI6MTczMzUxNTM3MiwiZXhwIjoxNzMzNTE5ODU0LCJhY3IiOiIxIiwiYWlvIjoiQWNRQU8vOFlBQUFBbUhPQisvZWFVVWpuMlVhbmFZYU9Xd29mU2tseWFYcUNEaUxLWEUwdWNWVUVkSnZrb1pIbjFHMnlGK3NQMzJtMFpuM243SUxJL1BrMGNHMEVESSsvR1JFb0xyck85V0c2VmUvTEkxeFppOE8rbVdYNWhFQ1FYMGN1RUFVQ0JvS1VMUm5MeWN6TG5xNVVydWxDemJscHh2UDd4YjRYUWRQTGFVOUJSNy9KRUpwTVBxbHpYR0FwNE1FbE1XandvRjdqcUlMNWhWTEJIeEZTcjJFU1FwQnltaFhsdi9MVXFWb3U3d2ExZzBKd1NHZnFpMEhDWFlUeThkaVZvdjd4ejM4ciIsImFsdHNlY2lkIjoiNTo6MTAwMzNGRkY4MDFCODk5QiIsImFtciI6WyJmaWRvIiwicnNhIiwibWZhIl0sImFwcGlkIjoiY2IyZmY4NjMtN2YzMC00Y2VkLWFiODktYTAwMTk0YmNmNmQ5IiwiYXBwaWRhY3IiOiIwIiwiZGV2aWNlaWQiOiI1MzQ3ZDgwNy1jODM4LTRkNzItYTg1YS04NWMyN2E2ZDNmODIiLCJlbWFpbCI6InNyYXNoaWRAbWljcm9zb2Z0LmNvbSIsImZhbWlseV9uYW1lIjoiUmFzaGlkIiwiZ2l2ZW5fbmFtZSI6IlNhcXVpYiIsImdyb3VwcyI6WyJiMTMwNDAyMi0wOGU2LTQ0N2QtYjA5NC0xNTM3MDU5N2M2YjYiLCIwOTUzMWE3Mi0yYzNlLTRlMDYtYmUxZS0yNTk2YmQwOGRjZGQiLCJkMzRjNGViZS00OTg0LTQ5MDMtYTY0ZC04YzIwMjgzZDUxNmIiLCJlMzA5NmRmNy1iNjVjLTRlMzItYWIxYS03YTM1ZGM2ODRmMGEiXSwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjQ3LyIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjczLjgwLjEwMS4yMDQiLCJuYW1lIjoiU2FxdWliIFJhc2hpZCIsIm9pZCI6ImFjYjdlMGFmLWIwYzAtNDVlMi1iMDYxLTRkNjg4YjMxYWRjOCIsInB1aWQiOiIxMDAzMjAwMzg2NTI3OEZEIiwicmgiOiIxLkFVWUFFOEN6RmdEVGpVYXNaSDdhQ0NDMjAxOXZwaGpmMnhkTW5kY1dOSEVxbkw3eEFIaEdBQS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiIwUU9vRk41a0U0VnJLM3FvUkpVaGtYNVFVZlpCR0Q2VVJhRWN5SmJhZkpZIiwidGlkIjoiMTZiM2MwMTMtZDMwMC00NjhkLWFjNjQtN2VkYTA4MjBiNmQzIiwidW5pcXVlX25hbWUiOiJzcmFzaGlkQG1pY3Jvc29mdC5jb20iLCJ1dGkiOiJiM00wRjlDUElVLXFMZnpYX1JxdEFBIiwidmVyIjoiMS4wIiwieG1zX2lkcmVsIjoiMSA2In0.hp84kUW0Xit5uEe_bDh7hCFACols5peyp3M10kHQef7Fgbjaqavgn-Z9opUwDdmXlRRg7ZdcEdzxbCmh8nAiTn5SC2h9NEQC0zYI9VJmRJoOTG_XhH-6HAM-clIlhqBbaKYzNGtGqIzloWhmC6_9U-oh7mWsp0ycffPlxQoRMusTyhrznbrSa40N90FTv45uAfEt25DTWxiiaCQPD_QjrJRUYCB5nS2mn76vxGDJk2EhI6Q2pnHf5JufNHW4igY0KX9KeElzZPBKF6gxx-JYOCH-RintDFXHfDH8aYuePA_U6UnBR_VMe35TQNld2Km11QL6X-S-a2wRcaKi6AzZaQ'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))