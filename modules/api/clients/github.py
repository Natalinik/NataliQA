import requests


class GitHub:

    def get_user(self, username):
        url = "https://api.github.com/users/" + username
        response = requests.get(url)
        body = response.json()

        return body
    
    def search_repo(self, name):
        url = f"https://api.github.com/search/repositories?q={name}"
        response = requests.get(url)
        body = response.json()

        return body
    
    def list_releases(self, owner, repository):
        url = f"https://api.github.com/repos/{owner}/{repository}/releases"
        response = requests.get(url)
        body = response.json()

        return body
    
    def list_commits_on_pull_request(self, owner, repository, pull_number):
        url = f"https://api.github.com/repos/{owner}/{repository}/pulls/{pull_number}/commits"
        response = requests.get(url)
        body = response.json()

        return body
