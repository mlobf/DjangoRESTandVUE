import requests

def main():
    response = requests.get("http://www.uol.com.br")
    print("Status Code: ", response.status_code)
    print("Headhes: ", response.headers)
    print(" --------------- ")
    print("Content-Type: ", response.headers['Content-Type'])
    print(" --------------- ")
    print("Content: ", response.text)

    print(" --------------- ")


if __name__ == "__main__":
    main()
