from pyvis.network import Network
import vk_api
import networkx as nx

g = nx.Graph()


new_token = 'vk1.a.cahpljxwFA-ZxoYFpedjUhpDYY6rFtx7yHJZwQP0dqgUKwGG_TmFdf73hrhO7_uQ3HlIzUc-BCOlNJ0Q2gtBDzZXxT02j8oZ1_xYHceR6QvJsgxYOIq73Yo7w2IpqGYO8uxewxvRWy2pVL9BzV9ZpJJxAugBcDxsZkW6ToGum9luD42ANLE7IU-Du1uU2M2ljIz47KmFl9WtgonvZCAEcQ'

session = vk_api.VkApi(token=new_token)
vk = session.get_api()

d = {}


def get_friends(user_id, d):
    friends1 = session.method("friends.get", {"user_id": user_id,
                                              "fields": "bdate, city, sex"})
    for i in friends1["items"]:
        d[i["id"]] = []
        if i["is_closed"]:
            d[i["id"]] = 'private account'
        elif 'deactivated' in i:
            d[i["id"]] = 'banned account'
        else:
            d[i["id"]] = session.method("friends.get", {"user_id": i["id"],
                                                        "fields": "bdate, city, sex"})
    print(d.keys())
    return d


def draw_friends(user_id, dict):
    for i in dict:
        g.add_node(i, label=i, color='blue')
        g.add_edge(user_id, i)


def draw(user_id, d):
    for t in d:
        if d[t] != 'private account' and d[t] != 'banned account':
            for q in d[t]["items"]:
                g.add_node(q["id"], label=q["first_name"], color='gray')
                g.add_edge(t, q["id"])
                friends2 = q["id"].count()
                # m = session.method("friends.getMutual", {"target_uid": user_id,
                #                                          "target_uids": q["id"]})
                # g.add_nodes_from(m, label='com_fri', color='green')


get_friends(633714088, d)
draw_friends(633714088, d)
draw(633714088, d)
nt = Network(notebook=True, cdn_resources='remote')
nt.from_nx(g)
nt.show('graph of friends.html')
