import json

def main():
    with open("./modules/example_data_response.json", mode="r") as file:
        data_processed =json.load(file)
        return data_processed

if __name__ == "__main__":
    main()