"""Core data structures for Meta-Graph Research."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class Node:
    """A knowledge element in the Meta-Graph."""

    node_id: str
    kind: str
    content: str
    status: str = "proposed"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Edge:
    """A directed relationship between two knowledge nodes."""

    source_id: str
    target_id: str
    relation: str


@dataclass
class StateEvent:
    """A recorded state transition."""

    event_type: str
    description: str
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class MetaGraph:
    """Minimal directed graph for reasoning dependencies."""

    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []
        self.history: list[StateEvent] = []

    def add_node(self, node: Node) -> None:
        """Add a knowledge node."""

        if node.node_id in self.nodes:
            raise ValueError(f"Node already exists: {node.node_id}")

        self.nodes[node.node_id] = node

        self.history.append(
            StateEvent(
                event_type="node_added",
                description=f"Added node {node.node_id}",
            )
        )

    def add_dependency(
        self,
        prerequisite_id: str,
        dependent_id: str,
    ) -> None:
        """
        Record that one node may affect another.

        Direction:
        prerequisite -> dependent
        """

        if prerequisite_id not in self.nodes:
            raise KeyError(f"Unknown prerequisite: {prerequisite_id}")

        if dependent_id not in self.nodes:
            raise KeyError(f"Unknown dependent: {dependent_id}")

        edge = Edge(
            source_id=prerequisite_id,
            target_id=dependent_id,
            relation="AFFECTS",
        )

        if edge in self.edges:
            raise ValueError("Dependency already exists")

        self.edges.append(edge)

        self.history.append(
            StateEvent(
                event_type="dependency_added",
                description=f"{prerequisite_id} affects {dependent_id}",
            )
        )

    def get_affected_nodes(self, node_id: str) -> set[str]:
        """Find all downstream nodes affected by a changed node."""

        if node_id not in self.nodes:
            raise KeyError(f"Unknown node: {node_id}")

        affected = set()
        visited = {node_id}
        queue = [node_id]

        while queue:
            current = queue.pop(0)

            for edge in self.edges:
                if edge.source_id == current:
                    target = edge.target_id

                    if target not in visited:
                        visited.add(target)
                        affected.add(target)
                        queue.append(target)

        return affected

    def record_perturbation(
        self,
        node_id: str,
        description: str,
    ) -> None:
        """Record an external perturbation affecting a node."""

        if node_id not in self.nodes:
            raise KeyError(f"Unknown node: {node_id}")

        self.history.append(
            StateEvent(
                event_type="perturbation",
                description=f"{node_id}: {description}",
            )
        )

    def get_history(self) -> list[StateEvent]:
        """Return the recorded state transitions."""
