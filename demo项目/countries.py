import pygal
from pygal.maps import world as world

worldmap_chart = world.World()
worldmap_chart.title = "Some countries"
worldmap_chart.add("F countries", ['fr', 'fi'])
worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
                                   'mk', 'ml', 'mm', 'mn', 'mo',
                                   'mr', 'mt', 'mu', 'mv', 'mw',
                                   'mx', 'my', 'mz'])
worldmap_chart.render_to_file('bar_chart.svg')