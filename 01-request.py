import requests


def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")

    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was a error!")

    data = response.json()
    print("JSON data: ", data)
#### masi um tests

if __name__ == "__main__":
    main()
