import os
from github import Github
import config

g = Github(config.GITHUB_TOKEN)

repo = g.get_repo('username/repo-name')
license = repo.get_license_template('mit')
license_content = license.rendered_content

with open('LICENSE', 'w') as f:
    f.write(license_content)
