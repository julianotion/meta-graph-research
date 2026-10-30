"""Unit tests for the MetaGraph core module."""

import sys
import unittest
from pathlib import Path

# Allow tests to run from the repository root without an installed package.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from meta_graph.core import MetaGraph, Node


class TestMetaGraph(unittest.TestCase):
    def setUp(self):
        self.graph = MetaGraph()

    def add_nodes(self, *node_ids):
        for node_id in node_ids:
            self.graph.add_node(
                Node(node_id=node_id, kind="claim", content=f"Content for {node_id}")
            )

    def test_add_node_stores_node_and_records_transition(self):
        node = Node(node_id="A", kind="claim", content="A claim")

        self.graph.add_node(node)

        self.assertIs(self.graph.nodes["A"], node)
        history = self.graph.get_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].event_type, "node_added")

    def test_duplicate_node_is_rejected(self):
        self.add_nodes("A")

        with self.assertRaises(ValueError):
            self.graph.add_node(Node(node_id="A", kind="claim", content="Duplicate"))

    def test_add_dependency_records_directed_edge(self):
        self.add_nodes("A", "B")

        self.graph.add_dependency("A", "B")

        self.assertEqual(len(self.graph.edges), 1)
        edge = self.graph.edges[0]
        self.assertEqual(edge.source_id, "A")
        self.assertEqual(edge.target_id, "B")
        self.assertEqual(edge.relation, "AFFECTS")

    def test_dependency_requires_both_nodes_to_exist(self):
        self.add_nodes("A")

        with self.assertRaises(KeyError):
            self.graph.add_dependency("missing", "A")

        with self.assertRaises(KeyError):
            self.graph.add_dependency("A", "missing")

    def test_duplicate_dependency_is_rejected(self):
        self.add_nodes("A", "B")
        self.graph.add_dependency("A", "B")

        with self.assertRaises(ValueError):
            self.graph.add_dependency("A", "B")

    def test_affected_nodes_follows_a_dependency_chain(self):
        self.add_nodes("A", "B", "C", "D")
        self.graph.add_dependency("A", "B")
        self.graph.add_dependency("B", "C")
        self.graph.add_dependency("C", "D")

        self.assertEqual(self.graph.get_affected_nodes("A"), {"B", "C", "D"})
        self.assertEqual(self.graph.get_affected_nodes("C"), {"D"})

    def test_affected_nodes_handles_cycles_without_infinite_loop(self):
        self.add_nodes("A", "B", "C")
        self.graph.add_dependency("A", "B")
        self.graph.add_dependency("B", "C")
        self.graph.add_dependency("C", "A")

        self.assertEqual(self.graph.get_affected_nodes("A"), {"B", "C"})

    def test_affected_nodes_rejects_unknown_node(self):
        with self.assertRaises(KeyError):
            self.graph.get_affected_nodes("missing")

    def test_record_perturbation_adds_history_event(self):
        self.add_nodes("A")

        self.graph.record_perturbation("A", "New evidence arrived")

        history = self.graph.get_history()
        self.assertEqual(history[-1].event_type, "perturbation")
        self.assertEqual(history[-1].description, "A: New evidence arrived")

    def test_perturbation_rejects_unknown_node(self):
        with self.assertRaises(KeyError):
            self.graph.record_perturbation("missing", "Change")

    def test_get_history_returns_a_copy(self):
        self.add_nodes("A")

        history = self.graph.get_history()
        history.clear()

        self.assertEqual(len(self.graph.get_history()), 1)


if __name__ == "__main__":
    unittest.main()
