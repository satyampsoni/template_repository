import os
from github import Github
import config

g = Github(config.GITHUB_TOKEN)

repo = g.get_repo('username/repo-name')
contributor = repo.get_contributor('contributor-name')
repo.add_to_collaborators(contributor, permission='push')
