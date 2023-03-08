import tkinter as tk

# Define the graph
graph_data = {
    '0': {'1': 2},
    '1': {'2': 3},
    '2': {'3': 2, '5': 2},
    '3': {'4': 1, '8': 2, '5': 1},
    '4': {'1': 4},
    '5': {'6': 3},
    '6': {'3': 2, '7': 3},
    '7': {'9': 2},
    '8': {'4': 1, '6': 3},
    '9': {'6': 2}
}

# Create a networkx graph from the data
graph = nx.Graph(graph_data)

# Create the GUI window
root = tk.Tk()
root.title('Dijkstra Graph')
root.geometry('500x500')

# Create a Canvas widget to display the graph
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw the graph on the Canvas
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos, with_labels=True, node_size=500,
                 font_size=16, font_weight='bold')
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=12)

# Add a button to close the window
close_button = tk.Button(root, text='Close', command=root.destroy)
close_button.pack(pady=10)

# Display the GUI
root.mainloop()
