import requests

class GitHub:

    def get_user(self, username):
        address = "https://api.github.com/users/" + username
        response = requests.get(address)
        body = response.json()

        return body
    
    def search_repo(self, name):
        address = f"https://api.github.com/search/repositories?q={name}"
        response = requests.get(address)
        body = response.json()

        return body
    
    def list_releases(self, owner, repository):
        address = f"https://api.github.com/repos/{owner}/{repository}/releases"
        response = requests.get(address)
        body = response.json()

        return body