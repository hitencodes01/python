import requests
def call_function():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    try:
        response = requests.get(url)
        data = response.json()
        if data['success'] == False:
            print("API call failed")
            return None, None
        author = data['data']['author']
        thought = data['data']['content']
        return author , thought
    except Exception as e:
        print(f"Error: API call failed {e}")
        return None, None

def main():
    author , thought = call_function()
    print(f"Author: {author} \nThought : {thought}")

if __name__ == "__main__":
    main()
