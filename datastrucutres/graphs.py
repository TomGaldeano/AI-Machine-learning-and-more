import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

class Vertex:
    def __init__(self, vertexId, x, y, label):
        self.vertexId = vertexId
        self.x = x
        self.y = y
        self.label = label
        self.adjacent = []
        self.previous = None

    def __repr__(self):
        return f"Vertex({self.vertexId}, label={self.label})"

class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def getVertices(self):
        return (self.v1, self.v2)

    def __repr__(self):
        return f"Edge({self.v1.vertexId} -> {self.v2.vertexId}, weight={self.weight})"
    
    def __contains__(self, item):
        if item == self.v1 or item == self.v2:
            return True
        return False

class Graph:
    def __init__(self, directed=True):
        self.vertices = {}   # vertexId -> Vertex
        self.edges = []      # list of Edge objects
        self.directed = directed

    def add_vertex(self, vertexId, x=0, y=0, label=None):
        """Add a vertex; label defaults to str(vertexId)."""
        if label is None:
            label = str(vertexId)
        v = Vertex(vertexId, x, y, label)
        self.vertices[vertexId] = v
        return v

    def add_edge(self, id1, id2, weight=0):
        """
        Add a directed edge from vertex id1 to vertex id2.
        For undirected graphs the reverse edge is added automatically.
        Raises KeyError if either vertex does not exist.
        """
        v1 = self.vertices[id1]
        v2 = self.vertices[id2]
        edge = Edge(v1, v2, weight)
        self.edges.append(edge)
        v1.adjacent.append(edge)
        if not self.directed:
            rev = Edge(v2, v1, weight)
            self.edges.append(rev)
            v2.adjacent.append(rev)
        return edge

    def get_vertex(self, vertexId):
        return self.vertices.get(vertexId)
    
    def getVertices(self):
        return self.vertices
    
    def getEdges(self, v = None):
        if v == None:
            return self.edges
        else:
            edges = []
            for i in self.edges:
                if v in i:
                    edges.append(i)
            return edges

    def view(self, title="Graph", figsize=(14, 10)):
        """
        Render the graph using matplotlib.

        Vertex positions are taken from each Vertex's (x, y) attributes.
        Edge weights are drawn near the midpoint of each edge.
        Directed graphs show arrowheads; undirected graphs show plain lines.
        """
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
        ax.set_aspect("equal")
        ax.axis("off")

        # --- draw edges ---
        drawn_pairs = set()   # avoid drawing both directions for display
        for edge in self.edges:
            x1, y1 = edge.v1.x, edge.v1.y
            x2, y2 = edge.v2.x, edge.v2.y
            pair = (min(edge.v1.vertexId, edge.v2.vertexId),
                    max(edge.v1.vertexId, edge.v2.vertexId))

            if self.directed:
                ax.annotate(
                    "",
                    xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(
                        arrowstyle="-|>",
                        color="#555555",
                        lw=1.2,
                        shrinkA=14,
                        shrinkB=14,
                    ),
                )
            else:
                if pair in drawn_pairs:
                    continue
                drawn_pairs.add(pair)
                ax.plot([x1, x2], [y1, y2], color="#888888", lw=1.4, zorder=1)
            # weight label near the midpoint, offset slightly
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            dx, dy = x2 - x1, y2 - y1
            length = math.hypot(dx, dy) or 1
            nx, ny = -dy / length, dx / length   # perpendicular unit vector
            offset = 0.35
            ax.text(
                mx + nx * offset, my + ny * offset,
                str(edge.weight),
                fontsize=7.5,
                ha="center", va="center",
                color="#333333",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.7),
                zorder=3,
            )
        # --- draw vertices ---
        node_radius = 0.55
        for vid, v in self.vertices.items():
            circle = plt.Circle(
                (v.x, v.y), node_radius,
                color="#90EE90",   # light green
                ec="#3a7a3a",
                lw=1.8,
                zorder=4,
            )
            ax.add_patch(circle)
            ax.text(
                v.x, v.y, v.label,
                ha="center", va="center",
                fontsize=8, fontweight="bold",
                color="#1a4a1a",
                zorder=5,
            )

        # fit the axes around all vertex positions
        if self.vertices:
            xs = [v.x for v in self.vertices.values()]
            ys = [v.y for v in self.vertices.values()]
            pad = 1.5
            ax.set_xlim(min(xs) - pad, max(xs) + pad)
            ax.set_ylim(min(ys) - pad, max(ys) + pad)

        fig.tight_layout()
        plt.show()
        return fig

def build_screenshot_graph():
    """Return a Graph that matches the weighted directed graph in the image."""
    g = Graph(directed=False)
    vertex_positions = [
        (0,  9.5, 18.0),
        (1, 11.5, 18.0),
        (2,  5.0, 17.5),
        (3,  7.5, 17.5),
        (4, 13.5, 18.5),
        (5, 15.0, 17.5),
        (6,  5.5, 15.5),
        (7, 18.5, 17.0),
        (8,  3.0, 18.0),
        (9,  9.0, 15.5),
        (10, 12.0, 15.5),
        (11, 14.0, 15.5),
        (12, 16.0, 15.5),
        (13,  0.5, 13.5),
        (14,  3.5, 13.5),
        (15,  3.5, 12.0),
        (16,  3.5, 10.5),
        (17,  9.0, 11.5),
        (18, 12.0, 13.0),
        (19, 13.0, 11.5),
        (20, 13.5, 10.0),
        (21, 17.0, 10.0),
        (22, 19.5, 10.0),
        (23,  6.5,  8.5),
        (24,  8.5,  7.5),
        (25, 11.0,  8.0),
        (26, 13.5,  8.0),
        (27,  9.5,  6.0),
        (28, 17.0,  7.0),
        (29, 17.5,  5.0),
    ]

    for vid, x, y in vertex_positions:
        g.add_vertex(vid, x, y)

    # Edges: (from, to, weight) — read from the screenshot
    edges = [
        # top cluster
        (8,  2,  4.64),
        (2,  3,  5.53),
        (3,  0,  4.45),
        (0,  1,  2.02),
        (1,  4,  1.7),
        (4,  5,  3.28),
        (5,  7,  4.28),
        (5, 12,  3.3),
        (1, 10,  6.2),  # 0->9 or 1->10 area
        (10, 11, 1.67),
        (11, 12, 2.16),
        (9, 10,  2.32),
        (2,  6,  3.41),
        (3,  9,  5.02),
        (8, 13,  8.45),
        (10, 0, 6.2),
        (7, 22, 16.43),
        # mid-left cluster
        (13, 14, 4.61),
        (13, 16, 7.32),
        (14, 15, 4.07),
        (15, 16, 1.24),
        (15, 17, 8.81),
        (16, 17, 9.01),
        # hub vertex 17
        (3,  17, 11.6),   # approximate; 3.41 label near 2-6, 11.6 near 3-17
        (9,  17, 7.1),
        (9,  17, 8.65),   # two edges shown from 9-area to 17
        (6,  17, 13.47),
        (14, 17, 7.32),
        (10, 17, 10.81),
        # right-mid cluster
        (17, 18, 4.07),
        (18, 19, 1.54),
        (19, 20, 1.53),
        (20, 21, 6.17),
        (21, 22, 4.66),
        (18, 25, 6.17),
        (20, 26, 4.72),
        (21, 28, 9.32),
        # bottom cluster
        (17, 23, 11.76),
        (17, 24,  8.42),
        (23, 24,  2.18),
        (20, 28, 9.32),
        (24, 27,  4.67),
        (25, 26,  1.86),
        (25, 27,  3.51),
        (27, 29, 11.6),
        (28, 29,  4.24),
    ]

    for v1, v2, w in edges:
        g.add_edge(v1, v2, w)

    return g

def pathfinder():
    g = build_screenshot_graph(directed = False)
    path = []
    start = g.get

if __name__ == "__main__":
    g = build_screenshot_graph()
