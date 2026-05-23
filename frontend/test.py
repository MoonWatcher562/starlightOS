import requests


def main() -> None:
    print(requests.get(
        "http://127.0.0.1:8000/health"
    ).content)
    
    print(requests.post(
        "http://127.0.0.1:8000/ai/send_request",
        json={
            "status": True, 
            "data": input("message to send to server: ")
        }
    ).content)


if __name__ == "__main__":
    main()