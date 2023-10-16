import networkx as nx

G = nx.Graph()
G.add_node(1, name="User1")
G.add_node(2, name="User2")
G.add_node(3, name="User3")

G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

G[1][2]["relation"] = "Friends"
G[2][3]["relation"] = "Friends"
G[1][3]["relation"] = "Friends"


# Знайти друзі користувача "User1"
user1_friends = list(G.neighbors(1))

# Знайти зв'язки (дружби) між користувачем "User1" і його друзями
user1_friendships = G.edges(1)
