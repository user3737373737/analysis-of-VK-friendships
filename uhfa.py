import networkx as nx
import matplotlib.pyplot as plt

"""
https://oauth.vk.com/authorize?client_id=51865430&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,groups,status,offline&response_type=token&v=5.131&state=123456


https://oauth.vk.com/blank.html#access_token=vk1.a.cahpljxwFA-ZxoYFpedjUhpDYY6rFtx7yHJZwQP0dqgUKwGG_TmFdf73hrhO7_uQ3HlIzUc-BCOlNJ0Q2gtBDzZXxT02j8oZ1_xYHceR6QvJsgxYOIq73Yo7w2IpqGYO8uxewxvRWy2pVL9BzV9ZpJJxAugBcDxsZkW6ToGum9luD42ANLE7IU-Du1uU2M2ljIz47KmFl9WtgonvZCAEcQ&expires_in=0&user_id=633714088&state=123456
"""

list_of_friends = [824396, 1348699, 1401510, 1533218, 1560904, 2064491, 2071315, 3058444, 3071114, 5650356, 8601947, 12468098, 12855720, 16509270, 21627962, 35210665, 40417202, 47545356, 48022991, 51055712, 52456786, 54840077, 55802691, 59710901, 61497046, 76372692, 90806426, 150133105, 180732340, 189178679, 217435224, 227307459, 518577454, 633714088, 710300646]
g = nx.Graph()
g.add_node(6185342)
g.add_nodes_from(list_of_friends, color='blue')
for i in range(len(list_of_friends)):
    g.add_edge(6185342, list_of_friends[i])

s = plt.subplot(121)
nx.draw(g, with_labels=True)
plt.show()