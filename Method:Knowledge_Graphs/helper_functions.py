import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

class EmptyGraphError(Exception):
    """Custom exception for empty graphs."""
    pass

def make_graph(triplets):
    G = nx.MultiDiGraph()
    for triplet in triplets:
        head = triplet[0]
        h_ent = triplet[1]
        tail = triplet[2]
        t_ent = triplet[3]
        rel = triplet[4]
        head_node = (head, h_ent)
        tail_node = (tail, t_ent)
        if head_node not in G.nodes:
            G.add_node(head_node, type=h_ent)
        if tail_node not in G.nodes:
            G.add_node(tail_node, type=t_ent)
        G.add_edge(head_node, tail_node, key=rel, relation=rel)
    return G

def prune_graph_by_depth(G, root, max_depth, direction='bidirectional'):

    if len(G.nodes()) == 0 or len(G.edges()) == 0:
        raise EmptyGraphError

    if max_depth < 0:
        return G

    G = G.copy()

    G_reversed = G.reverse()

    forward_lengths = nx.single_source_shortest_path_length(G, root)
    backward_lengths = nx.single_source_shortest_path_length(G_reversed, root)


    if direction == 'bidirectional':
        nodes_to_remove = [
            node for node in G.nodes()
            if min(forward_lengths.get(node, float('inf')), backward_lengths.get(node, float('inf'))) > max_depth
        ]
    elif direction == 'bidirectional_and':
        nodes_to_remove = [
            node for node in G.nodes()
            if forward_lengths.get(node, float('inf')) > max_depth and backward_lengths.get(node, float('inf')) > max_depth
        ]
    elif direction == 'bidirectional_or':
        nodes_to_remove = [
            node for node in G.nodes()
            if forward_lengths.get(node, float('inf')) > max_depth or backward_lengths.get(node, float('inf')) > max_depth
        ]
    elif direction == 'forward':
        nodes_to_remove = [
            node for node in G.nodes()
            if forward_lengths.get(node, float('inf')) > max_depth
        ]
    elif direction == 'backward':
        nodes_to_remove = [
            node for node in G.nodes()
            if backward_lengths.get(node, float('inf')) > max_depth
        ]
    else:
        raise EmptyGraphError('Unknown direction of pruning (options: forward, backward, bidirectional, bidirectional_and, bidirectional_or)')

    G.remove_nodes_from(nodes_to_remove)
    
    return G

def view_graph(G, root, max_depth, direction, num_nodes):

    max_depth_message = max_depth
    if max_depth < 0:
        max_depth_message = '(Unpruned)'
    
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.01)
    pos = nx.spring_layout(G, k=2, iterations=200)

    entity_colors = {
        'LOC': '#ffb347',  # orange
        'ORG': '#87ceeb',  # light blue
        'PER': '#90ee90',  # light green
        'MISC': '#dda0dd',  # plum
    }

    node_colors = []
    node_sizes = []
    labels = {}

    for node in G.nodes():
        entity_name, entity_type = node
        labels[node] = entity_name
        node_sizes.append(200)
        if node == root:
            node_colors.append('#d90000')  # Root node color (red)
        else:
            node_colors.append(entity_colors.get(entity_type, '#c08aed'))  # purple for any undefined types

    if max_depth == -1 or max_depth > 3:
        nx.draw(G, pos, node_size=[s * 0.5 for s in node_sizes], node_color=node_colors,
                font_size=0, arrows=True, arrowsize=5, edge_color='gray', width=0.4, ax=ax)
    else:
        nx.draw(G, pos, labels=labels, with_labels=True, node_size=node_sizes, node_color=node_colors,
                font_size=10, font_weight='normal', arrowsize=5, edge_color='gray', width=0.4, ax=ax)
        edge_labels = nx.get_edge_attributes(G, 'relation')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='gray', font_size=5, ax=ax)
    
    num_edges = G.number_of_edges()  # Get the number of edges
    plt.title(f"Knowledge Graph for {root[0]}, {direction.capitalize()} Prune After Depth {max_depth_message} (N={num_nodes}, E={num_edges})", fontsize=14)
    
    legend_patches = [mpatches.Patch(color=color, label=entity) for entity, color in entity_colors.items()]
    legend_patches.append(mpatches.Patch(color='#d90000', label=root[0]))
    plt.legend(handles=legend_patches, loc='best', fontsize=10)

    return fig, ax