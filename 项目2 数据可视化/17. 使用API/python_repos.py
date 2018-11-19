import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)

response_dict = r.json()

# print(response_dict.keys())
print("Total repositories: ", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# # print("\nKeys: ", len(repo_dict))
# # for key in sorted(repo_dict.keys()):
# #   print(key)
# print("\nSelected information about first repository: ")
# print("Name: {0}".format(repo_dict['name']))
# print("Owner: {0}".format(repo_dict['owner']['login']))
# print("Stars: {0}".format(repo_dict['stargazers_count']))
# print("Repository: {0}".format(repo_dict['html_url']))
# print("Created: {0}".format(repo_dict['created_at']))
# print("Updated: {0}".format(repo_dict['updated_at']))
# print("Description: {0}".format(repo_dict['description']))

# print("\nSelected information about each repository: ")
# for repo_dict in repo_dicts:
#   print("\nName: {0}".format(repo_dict['name']))
#   print("Owner: {0}".format(repo_dict['owner']['login']))
#   print("Stars: {0}".format(repo_dict['stargazers_count']))
#   print("Repository: {0}".format(repo_dict['html_url']))
#   # print("Created: {0}".format(repo_dict['created_at']))
#   # print("Updated: {0}".format(repo_dict['updated_at']))
#   print("Description: {0}".format(repo_dict['description']))

names, stars = [], []
for repo_dict in repo_dicts:
  names.append(repo_dict['name'])
  stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starred JavaScript Project on GitHub."
chart.x_labels = names

chart.add('', stars)
chart.render_to_file("javascript_repos.svg")