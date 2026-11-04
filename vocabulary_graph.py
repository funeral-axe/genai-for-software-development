import matplotlib.pyplot as plt
import networkx as nx


# GenAI use cases from research.md
use_cases = [
    "Meeting\nAssistant",
    "Health Records\nOrganizer",
    "Document & Knowledge\nAssistant",
    "Software Maintenance\nAssistant",
    "Customer Ticket\nProcessing",
]

# Terms from vocabulary.md
terms = [
    "LLM",
    "Hallucination",
    "Prompt",
    "Context Window",
    "Speech-to-Text",
    "Speaker Diarization",
    "OCR",
    "RAG",
    "Embedding",
    "Vector Search",
    "Inference",
    "Local AI Model",
    "Data Normalization",
    "Structured Output",
    "Human-in-the-Loop",
]


# Connections between vocabulary and use cases.
# Third value:
# "explicit" = term is directly mentioned in the research
# "implicit" = concept is used, but the exact term is not written
connections = [
    ("Speech-to-Text", "Meeting\nAssistant", "explicit"),
    ("Speaker Diarization", "Meeting\nAssistant", "explicit"),
    ("Local AI Model", "Meeting\nAssistant", "implicit"),
    ("Hallucination", "Meeting\nAssistant", "explicit"),
    ("Inference", "Meeting\nAssistant", "implicit"),

    ("OCR", "Health Records\nOrganizer", "explicit"),
    ("Data Normalization", "Health Records\nOrganizer", "explicit"),
    ("Hallucination", "Health Records\nOrganizer", "implicit"),
    ("Structured Output", "Health Records\nOrganizer", "implicit"),
    ("LLM", "Health Records\nOrganizer", "implicit"),

    ("OCR", "Document & Knowledge\nAssistant", "explicit"),
    ("RAG", "Document & Knowledge\nAssistant", "explicit"),
    ("Embedding", "Document & Knowledge\nAssistant", "explicit"),
    ("Vector Search", "Document & Knowledge\nAssistant", "explicit"),
    ("LLM", "Document & Knowledge\nAssistant", "implicit"),
    ("Hallucination", "Document & Knowledge\nAssistant", "implicit"),

    ("Context Window", "Software Maintenance\nAssistant", "explicit"),
    ("LLM", "Software Maintenance\nAssistant", "implicit"),
    ("Prompt", "Software Maintenance\nAssistant", "implicit"),
    ("Hallucination", "Software Maintenance\nAssistant", "explicit"),
    ("RAG", "Software Maintenance\nAssistant", "implicit"),

    ("RAG", "Customer Ticket\nProcessing", "explicit"),
    ("Structured Output", "Customer Ticket\nProcessing", "implicit"),
    ("Human-in-the-Loop", "Customer Ticket\nProcessing", "implicit"),
    ("Hallucination", "Customer Ticket\nProcessing", "implicit"),
    ("LLM", "Customer Ticket\nProcessing", "implicit"),
]


# Create graph
graph = nx.Graph()

for use_case in use_cases:
    graph.add_node(use_case, node_type="use_case")

for term in terms:
    graph.add_node(term, node_type="term")

for term, use_case, usage_type in connections:
    graph.add_edge(term, use_case, usage_type=usage_type)


# Layout
plt.figure(figsize=(18, 12))

pos = nx.spring_layout(
    graph,
    seed=42,
    k=1.5
)


# Separate nodes
use_case_nodes = [
    node
    for node, data in graph.nodes(data=True)
    if data["node_type"] == "use_case"
]

term_nodes = [
    node
    for node, data in graph.nodes(data=True)
    if data["node_type"] == "term"
]


# Draw nodes
nx.draw_networkx_nodes(
    graph,
    pos,
    nodelist=use_case_nodes,
    node_size=5000,
    node_shape="s",
    node_color="lightblue"
)

nx.draw_networkx_nodes(
    graph,
    pos,
    nodelist=term_nodes,
    node_size=2500,
    node_color="lightgreen"
)


# Separate explicit and implicit edges
explicit_edges = [
    (u, v)
    for u, v, data in graph.edges(data=True)
    if data["usage_type"] == "explicit"
]

implicit_edges = [
    (u, v)
    for u, v, data in graph.edges(data=True)
    if data["usage_type"] == "implicit"
]


# Explicit = solid line
nx.draw_networkx_edges(
    graph,
    pos,
    edgelist=explicit_edges,
    width=2,
    style="solid",
)

# Implicit = dashed line
nx.draw_networkx_edges(
    graph,
    pos,
    edgelist=implicit_edges,
    width=1.5,
    style="dashed",
)


# Labels
nx.draw_networkx_labels(
    graph,
    pos,
    font_size=9,
)


# Legend
plt.plot([], [], linestyle="solid", label="Explicit usage")
plt.plot([], [], linestyle="dashed", label="Implicit usage")
plt.scatter([], [], s=150, marker="s",
            color="lightblue", label="GenAI use case")

plt.scatter([], [], s=100, marker="o",
            color="lightgreen", label="Vocabulary term")

plt.legend(loc="upper left")

plt.title(
    "Generative AI Vocabulary Relationship Graph",
    fontsize=18
)

plt.axis("off")
plt.tight_layout()

# Save PNG
plt.savefig(
    "vocabulary-graph.png",
    dpi=300,
    bbox_inches="tight"
)

print("Graph successfully saved as vocabulary-graph.png")

plt.show()