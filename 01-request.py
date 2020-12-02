import requests

def main():
    response = requests.get("https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01 HTTP/1.1")
    print("Status Code: ", response.status_code)
    print("Headhes: ", response.headers)

if __name__ == "__main__":
    main()
