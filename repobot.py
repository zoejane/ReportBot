# -*- coding: utf-8 -*-
#!/usr/bin/env python

VERSION = "repobot v18.4.6."
__author__ = 'zoejane'

from github import Github
from datetime import datetime, timedelta
from urllib import request
from base64 import b64decode

author_name = input("Input the people you are interested in: ")
while True:
    try:
        check_days = int(input("Input the days you want to check out: "))
        break
    except ValueError:
        print("Please input a valid number.")

access = request.urlopen("https://gist.githubusercontent.com/zoejane/e5a57407061c88914ecad532855f0248/raw/eeb6b8cd7cbc4c3329661e0fbfebcb376fae120f/reportbot.txt").read()
github_obj = Github(b64decode(access).decode())
repo_obj = github_obj.get_organization("DebugUself").get_repo("du4proto")

def create_summary(count_sign, summary_kind):
    days = 'days'
    if check_days == 0 or check_days == 1:
        days = 'day'

    if count_sign  == 0 or count_sign  == 1:
        return f'\nThere is {count_sign} {summary_kind} in the past {check_days} {days}.'
    else:
        return f'\nThere is {count_sign} {summary_kind}s in the past {check_days} {days}.'

def create_md(export_kind):
    filename = author_name.lower() + '-' + export_kind + 's-report.md'
    f = open(filename, "w+")
    f.write(f'# {author_name.lower().capitalize()}\'s {export_kind.capitalize()}s Report\n')
    return filename

# Generate Commits Report
f = open(create_md("commit"), "a+")

print(f'Creating report for commits now......')
f.write("\n## Commits\n\n")

i = 0
for branch in repo_obj.get_branches():
    print(f'Searching {branch.name} now......')

    all_commits = repo_obj.get_commits(sha = branch.name, since = datetime.now() - timedelta(days = check_days), until = datetime.now())  

    for a_commit in all_commits:
        if a_commit.author is not None:
            if a_commit.author.login.lower() == author_name.lower():
                print(f'Grabbing Commit - {a_commit.commit.message} now......')
                f.write(f'### {i+1}. {a_commit.commit.message}\n') 
                f.write(f'{a_commit.commit.html_url}\n')
                f.write(f'\n{a_commit.author.login} updated at {a_commit.raw_headers["last-modified"]}\n')
                f.write(f'Branch: {branch.name} \n\n')
                i += 1 

f.write("\n## Summary\n")
f.write(create_summary(i, "commit"))
f.close()
print("Commits Report Done......")

# Generate Issues & Issue Comments Report
f = open(create_md("issue"), "a+")

print(f'Creating report for issues now......')
f.write("\n## Issues\n\n")

all_issues = repo_obj.get_issues(state = 'all', since = datetime.now() - timedelta(days = check_days), creator = author_name)

k = 0
for an_issue in all_issues:
    timedelta_of_issue = datetime.now() - an_issue.created_at
    if timedelta_of_issue.days <= check_days:
        print(f'Grabbing {an_issue.title} now......')
        f.write(f'### {k+1}. {an_issue.title}\n')
        f.write(f'{an_issue.html_url}')
        f.write(f'\n{an_issue.user.login} created at {str(an_issue.created_at)}\n')
        f.write(f'\n``````\n{an_issue.body}\n``````\n')
        k += 1

print(f'Creating report for issues comments now......')
f.write("\n## Issues Comments\n\n")

all_issue_comments = repo_obj.get_issues_comments(sort = 'created', direction = 'desc', since = datetime.now() - timedelta(days = check_days))

j = 0
for an_issue_comment in all_issue_comments:
    if an_issue_comment.user.login.lower() == author_name.lower():
        print(f'Grabbing comment at {an_issue_comment.updated_at} now......')
        f.write(f'### {j+1}. {an_issue_comment.user.login} commented at {an_issue_comment.updated_at}\n')
        f.write(f'{an_issue_comment.html_url}\n')
        f.write(f'\n``````\n{an_issue_comment.body}\n``````\n')
        j += 1

f.write("\n## Summary\n")
f.write(create_summary(k, "issue"))
f.write(create_summary(j, "issue comment")) 
f.close()
print("Issues Report Done......")

# Generate Commit Comments Report
f = open(create_md("commit-comment"), "a+")

print(f'Creating report for commit comments now......')
f.write("\n## Commit Comments\n\n")

all_commit_comments = repo_obj.get_comments()

m = 0
for a_commit_comment in all_commit_comments:
    timedelta_of_commit_comment = datetime.now() - a_commit_comment.created_at
    if timedelta_of_commit_comment.days <= check_days and a_commit_comment.user.login.lower() == author_name.lower():
        print(f'Grabbing commit comment at {a_commit_comment.created_at} now......')
        f.write(f'### {m+1}. {a_commit_comment.user.login} commented at {a_commit_comment.updated_at}\n')
        f.write(f'{a_commit_comment.html_url}\n')
        f.write(f'\n``````\n{a_commit_comment.body}\n``````\n')
        m += 1

f.write("\n## Summary\n")
f.write(create_summary(m, "commit comment"))
f.close()
print("Commit Comments Report Done......")

print("All Done......")
