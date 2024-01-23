import os
import requests
import json

class Issues:
    def __init__(self, repo_owner,repo_name , access_token):
        self.repo_owner = repo_owner
        self.repo_name =repo_name
        self.access_token = access_token
        self.api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
        self. headers = {
        "Authorization": f"Bearer {self.access_token}",
        "Accept": "application/vnd.github.v3+json"
        }

    # ***All get requests don't require a token***
    # Get a list of all open issues and print the number of returned issues
    def get_open_issues_count(self):
        
        response = requests.get(self.api_url, params={"state": "open"})
        open_issues = response.json()
        if response.status_code == 200:
            return len(open_issues)
        else:
            print("Exception request")
    


    # 2. Get a list of issues with label "practice1" and print the number of returned issues
    def get_issues_by_label(self):
      
        response = requests.get(self.api_url, params={"state": "open", "labels": "practice1"})
        practice1_issues = response.json()
        return len(practice1_issues)

    # 3. Create a new issue
    def create_new_issue(self, title, body, labels, assignees):
        new_issue_data = {
            "title": title,
            "body": body,
            "labels": labels,
            "assignees": assignees
        }
        response = requests.post(self.api_url, headers=self.headers, json=new_issue_data)

        if response.status_code == 201:
            print("New issue created successfully!")
            return response.status_code 
        else:
            print(f"Failed to create a new issue. Status code: {response.status_code}")
            print(f"Error response: {response.status_code}")
            return response.status_code





