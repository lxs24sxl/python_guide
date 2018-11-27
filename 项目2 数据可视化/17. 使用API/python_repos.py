import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
language = 'javascript'  # Python
url = "https://api.github.com/search/repositories?q={0}:javascript&sort=stars".format(language)
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

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
# configs = {
#     'x_label_rotation': 45,
#     'show_legend': False,
#     'title_font_size': 24,
#     'label_font_size': 14,
#     'major_label_font_size': 18,
#     'truncate_label': 15,
#     'show_y_guides': False,
#     'width': 1000
# }
# for key, value in configs.items():
#     my_config.key = value

print('my_config', my_config)
chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred {0} Project on GitHub.".format(language)
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file("{0}_repos.svg".format(language))