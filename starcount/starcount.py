#!/usr/bin/env python
import sys
import requests
import getopt
import json
from collections import OrderedDict
from termcolor import colored

username = ''
stars_count_threshold = ''
num_repo = ''
auth_token = False


def final_result(output=''):
    global stars_count_threshold, num_repo
    unsorted_output = {}
    total_stars = 0
    max_repo_name_length = 0
    if len(output) > 0:
        for repo in output:
            unsorted_output[repo['name']] = repo['stargazers_count']
        unsorted_output = OrderedDict(unsorted_output)
        sorted_output = {k: v for k, v in sorted(
            unsorted_output.items(), key=lambda item: item[1], reverse=True)}
        for each_repo in sorted_output:
            total_stars = total_stars + sorted_output[each_repo]
            if len(each_repo) > max_repo_name_length:
                max_repo_name_length = len(each_repo)
        print(colored("*****", 'yellow'), 'Total Stars: ',
              colored(total_stars, 'green'), colored("*****", 'yellow'))

        result_dict = OrderedDict()

        if num_repo != '':
            for key, value in sorted_output.items():
                if num_repo > 0:
                    result_dict[key] = value
                    num_repo = num_repo - 1
                else:
                    break
            sorted_output = result_dict

        result_dict = OrderedDict()

        if stars_count_threshold != '':
            for key, value in sorted_output.items():
                if value >= stars_count_threshold:
                    result_dict[key] = value
                else:
                    break
            sorted_output = result_dict

        for each_repo in sorted_output:
            star = ''
            for i in range(0, (2*max_repo_name_length - len(each_repo))):
                star = star + "-"
            print(colored('>', 'green'), each_repo, star,
                  sorted_output[each_repo], colored('*', 'yellow'))
    else:
        print('No Repository Found')
        sys.exit()


def get_repo_data():
    global username, auth_token
    base_url = 'https://api.github.com/users/'
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Repositories Star Count',
               'Accept': 'application/vnd.github.v3+json'}
    if auth_token:
        headers['Authorization'] = 'token ' + auth_token
    repo_data = []

    num_repos = requests.get(base_url+username, headers=headers)
    if num_repos.status_code == 200:
        repo_count = num_repos.json()['public_repos']
    else:
        print('[!] HTTP {0} calling [{1}]'.format(
            num_repos.status_code, base_url+username))
        sys.exit()

    num_pages = (int(repo_count) // 100) + 1
    for i in range(0, num_pages):
        response = requests.get(base_url+username+'/repos?per_page=100&page='+str(i+1),
                                headers=headers)
        if response.status_code == 200:
            repo_data.extend(response.json())
        else:
            print('[!] HTTP {0} calling [{1}]'.format(
                response.status_code, base_url+username+'/repos?per_page=100&page='+str(i+1)))
            sys.exit()
    final_result(output=repo_data)


def main():
    argv = sys.argv[1:]
    global username, stars_count_threshold, num_repo, auth_token
    try:
        opts, args = getopt.getopt(
            argv, "hu:t:n:a:", ["user_name=", "stars_count_threshold=", "num_repo=", "auth_token="])
    except getopt.GetoptError:
        print('Usage: starcount -u <user_name> -t <stars_count_threshold_per_repo> -n <num_repo_to_show> -a <auth_token>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
                'Usage: starcount -u <user_name> -t <stars_count_threshold_per_repo> -n <num_repo_to_show> -a <auth_token>')
            sys.exit()
        elif opt in ('-u', '--user_name'):
            username = arg.strip()
        elif opt in ('-t', '--stars_count_threshold'):
            stars_count_threshold = int(arg.strip())
        elif opt in ('-n', '--num_repo'):
            num_repo = int(arg.strip())
        elif opt in ('-a', '--auth_token'):
            auth_token = arg.strip()

    if num_repo != '' and num_repo < 0:
        print('Number of repositories should be greater than 0')
        sys.exit()
    if stars_count_threshold != '' and stars_count_threshold < 0:
        print('Stars Count Threshold should be grater than 0')
        sys.exit()

    if username != '':
        get_repo_data()
    else:
        print("GitHub username is required! Run 'starcount -h' for help")


if __name__ == "__main__":
    main()
