# Take a set of nodes on a plane and move each such that its distance to its neighbors is minimized
# inspired by one of Tom7's videos: https://www.youtube.com/user/suckerpinch

import matplotlib
matplotlib.use('agg')


import random

import seaborn as sns
import matplotlib.pyplot as plt


sns.set_style('white')


node_count = 1000
edge_count = 5
digraph = False  # graph is undirected
step_count = 30 * 20  # 30 fps for 20 seconds

nodes=[]

for i in range(node_count):
    nodes.append({'i': i, 'x': random.random(), 'y': random.random(), 'edges': []})

for i in range(node_count):
    node = nodes[i]

    edges = random.sample(range(node_count), edge_count)
    node['edges'] = node['edges'] + edges

    if not digraph:  # make other node point back to this one as well
        for edge in edges:
            nodes[edge]['edges'].append(i)


for i in range(step_count):
    if i % 30 == 0:
        print('{} steps'.format(i))

    node = random.choice(nodes)
    x_avg = sum(nodes[other]['x'] for other in node['edges']) / len(node['edges'])
    y_avg = sum(nodes[other]['y'] for other in node['edges']) / len(node['edges'])

    node['x'] = x_avg
    node['y'] = y_avg

    ax = sns.lineplot(x=[node['x'] for node in nodes],
                      y=[node['y'] for node in nodes],
                      hue=[node['i'] // 2 for node in nodes],
                      sort=False,
                      lw=.5,
                      palette=sns.color_palette('viridis', n_colors=len(nodes) // 2))

    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend_.remove()
    sns.despine(top=True, bottom=True, left=True, right=True)
    plt.tight_layout()

    fig = ax.get_figure()
    fig.savefig('graph/graph{}.png'.format(i))
    plt.clf()

# to generate video
# ffmpeg -i graph/graph%03d.png -framerate 30 -vf format=yuv420p output.mp4
