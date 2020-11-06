 # Write a script that uses the GIthub API to take a repository as a parameter, and returns open issues and labels (any format)



from github import Github
import os
from pprint import pprint
import requests
from pprint import pprint
import sys


token = os.getenv('GITHUB_TOKEN', '...')

# Method 1 - using PyGitHub 
# g = Github(token)
# repo = g.get_repo("kalapathar/stovoting")
# issues = repo.get_issues(state="open")
# pprint(issues.get_page(0))



# Method2 - using Requests
# This function returns a list of open issues of the given repo
def find_open_issues(reponame):
    # take reponame as an argument from command line if given
    global token
    # github username - change it to the github username where the repo is located
    owner='kalapathar'
    query_url = f"https://api.github.com/repos/{owner}/{reponame}/issues"
    params = {
        "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers, params=params)
    return r.json()


def cleanup(issues_arr):
    arr=[]

    for issue in issues_arr:
        result={}
        labels=[]
        result['url']=issue['url']
        result['title']=issue['title']
        for label in issue['labels']:
            labels.append(label['name'])
        result['labels']=labels
        arr.append(result)
    return arr

if __name__ == "__main__":
    if len(sys.argv)<2:
        print ("Please provide the name of github repo as a second argument from the command line!")
        print ("Example: python algorand.py stovoting")
        print ("Note: stovoting is the name of the github repo: https://github.com/kalapathar/stovoting")
    else:
        issues_list=find_open_issues(sys.argv[1])
        issues_clean=cleanup(issues_list)
        pprint(issues_clean)



