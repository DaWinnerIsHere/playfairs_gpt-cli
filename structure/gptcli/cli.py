from prompt_toolkit import PromptSession
from gptcli.config import load_config
from gptcli.apis import openai
import random

def main():
    config = load_config()
    api_name = config["default_api"]
    api_conf = config["apis"][api_name]
    settings = config.get("settings", {})

    session = PromptSession()
    history = []

    while True:
        try:
            user_input = session.prompt("You: ")
            if user_input.strip().lower() in ("exit", "quit"):
                break

            history.append({"role": "user", "content": user_input})
            reply = openai.chat_openai(
                api_key=api_conf["api_key"],
                model=api_conf["model"],
                messages=history[-settings.get("history_limit", 5):],
                temperature=settings.get("temperature", round(random.randrange(50,100)/100,2)),
                max_tokens=settings.get("max_tokens", 1000),
                top_p=settings.get("top_p", 1.0)
            )
            print(f"\nAI: {reply}\n")
            history.append({"role": "assistant", "content": reply})

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\n[ERROR] {e}\n")

if __name__ == "__main__":
    main()
