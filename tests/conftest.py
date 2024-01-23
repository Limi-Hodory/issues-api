import pytest
import os
import requests
import json
from issues import *

# GitHub repository information 
repo_owner = "topq-practice"
repo_name = "api-practice"
access_token = "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"
# api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"

@pytest.fixture()
def my_issues():
    return Issues(repo_owner, repo_name, access_token)

