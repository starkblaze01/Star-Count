# [Star-Count](https://github.com/starkblaze01/Star-Count)
[![PyPI version](https://badge.fury.io/py/starcount.svg)](https://badge.fury.io/py/starcount)

Python Command Line tool to get total stargazers count of GitHub Repository of any user.

# How to Install
`pip install starcount`

# How to Use
- Open Terminal
- Run `starcount -h` for help
#### Usage:
`starcount -u <user_name> -t <stars_count_threshold_per_repo> -n <num_repo_to_show> -a <auth_token>`
#### Example Usage:
`starcount -u starkblaze01 -t 10 -n 12`

#### Optional arguements:
```
- t: to get repositories having num stars above threshold
- n: to show limited number of repository
- a: GitHub OAuth token
```
##### Note:
- Number of API calls request is limited to 60/hr without auth token. With OAuth token it is 5000/hr. Know more about it [here](https://developer.github.com/v3/#rate-limiting).
- Authentication using password is not used for this package because it will be depricated soon and not recommended. You can get your OAuth token from [here](https://github.com/settings/tokens) in case you hit your request limit.

#### GIF
Click [here](https://github.com/starkblaze01/Star-Count/blob/master/starcount.gif)

![](https://github.com/starkblaze01/Star-Count/blob/master/starcount.gif)
