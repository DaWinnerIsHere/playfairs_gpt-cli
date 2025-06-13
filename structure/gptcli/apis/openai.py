import httpx

def chat_openai(api_key, model, messages, **params):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        **params
    }
    response = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
def chat_openai_stream(api_key, model, messages, **params):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        **params
    }
    response = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload,
        stream=True
    )
    response.raise_for_status()
    for chunk in response.iter_lines():
        if chunk:
            data = chunk.decode("utf-8")
            if data.startswith("data: "):
                data = data[6:]  # Remove the "data: " prefix
            if data == "[DONE]":
                break
            yield data
def chat_openai_stream_with_error_handling(api_key, model, messages, **params):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        **params
    }
    try:
        response = httpx.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            stream=True
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        raise RuntimeError(f"Request error occurred: {str(e)}")
    for chunk in response.iter_lines():
        if chunk:
            data = chunk.decode("utf-8")
            if data.startswith("data: "):
                data = data[6:]
            if data == "[DONE]":
                break
            try:
                yield data
            except Exception as e:
                raise RuntimeError(f"Error processing chunk: {str(e)}")
