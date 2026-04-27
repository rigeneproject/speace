"""
SPEACE Core Graph Engine - Typed Adaptive Computational Graph
Versione 0.3 (Fase 0 - Foundation) - FIX propagazione definitivo
"""
from contracts import ExecutionContract, SPEACEMessage, CommonOperationalLanguage, MessageType
import asyncio
import json
import logging
from datetime import datetime
from typing import Any, Dict, Callable, List, Optional, Type
import networkx as nx
from dataclasses import dataclass, field

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("SPEACE.GraphEngine")


@dataclass
class NodeContract:
    input_types: Dict[str, Type]
    output_types: Dict[str, Type]
    pre_conditions: List[Callable] = field(default_factory=list)
    post_conditions: List[Callable] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class SPEACENode:
    def __init__(self, name: str, func: Callable, contract: NodeContract):
        self.name = name
        self.func = func
        self.contract = contract
        
        # === MODIFICA AGGIUNTA ===
        self.execution_contract: Optional[ExecutionContract] = None
        # =========================
        
        self.state: Dict[str, Any] = {}
        self.last_execution: Optional[datetime] = None
        self.performance_score: float = 1.0

    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        # Filtra solo gli input richiesti dal contratto
        filtered_inputs = {k: v for k, v in inputs.items() if k in self.contract.input_types}
        
        # Validazione input
        for key, expected_type in self.contract.input_types.items():
            if key not in filtered_inputs:
                raise ValueError(f"Missing input '{key}' in node {self.name}")
            if not isinstance(filtered_inputs[key], expected_type):
                raise TypeError(f"Wrong type for '{key}' in {self.name}: got {type(filtered_inputs[key])}")

        for cond in self.contract.pre_conditions:
            if not cond(filtered_inputs):
                raise RuntimeError(f"Pre-condition failed in {self.name}")

        try:
            if asyncio.iscoroutinefunction(self.func):
                result = await self.func(**filtered_inputs)
            else:
                result = self.func(**filtered_inputs)

            result = result if isinstance(result, dict) else {"output": result}

            # Validazione output
            for key, expected_type in self.contract.output_types.items():
                if key not in result:
                    raise ValueError(f"Missing output '{key}' from {self.name}")
                if not isinstance(result[key], expected_type):
                    raise TypeError(f"Wrong output type for '{key}' in {self.name}")

            self.last_execution = datetime.now()
            self.performance_score = min(1.0, self.performance_score * 1.05)
            return result

        except Exception as e:
            self.performance_score = max(0.1, self.performance_score * 0.8)
            logger.error(f"Node {self.name} failed: {e}")
            raise


class SPEACEAdaptiveGraph:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.nodes: Dict[str, SPEACENode] = {}

    # === MODIFICA register_node ===
    def register_node(self, name: str, func: Callable,
                      input_types: Dict[str, Type],
                      output_types: Dict[str, Type],
                      metadata: Dict = None,
                      execution_contract: Optional[ExecutionContract] = None) -> None:
        contract = NodeContract(input_types=input_types, output_types=output_types, metadata=metadata or {})
        node = SPEACENode(name, func, contract)
        
        # Assegna il contratto di esecuzione (se fornito)
        node.execution_contract = execution_contract
        
        self.nodes[name] = node
        self.graph.add_node(name, node=node)
        logger.info(f"Node registered: {name} {'(with execution contract)' if execution_contract else ''}")
    # =================================

    def connect(self, source: str, target: str, weight: float = 1.0,
                plasticity_enabled: bool = True,
                output_to_input_map: Dict[str, str] = None):
        if source not in self.nodes or target not in self.nodes:
            raise ValueError("Node not found")
        self.graph.add_edge(source, target,
                            weight=weight,
                            plasticity=plasticity_enabled,
                            output_to_input_map=output_to_input_map or {})
        logger.info(f"Connected {source} → {target} (weight={weight})")

    # ... (il resto del codice rimane invariato: propagate, get_introspection, save_state, ecc.)

    async def propagate(self, start_node: str, inputs: Dict[str, Any], max_hops: int = 10) -> Dict[str, Any]:
        # (codice originale invariato)
        if start_node not in self.nodes:
            raise ValueError(f"Start node {start_node} not found")
        visited = set()
        current_inputs = {start_node: inputs}
        results = {}
        for _ in range(max_hops):
            next_inputs = {}
            for node_name, node_inputs in list(current_inputs.items()):
                if node_name in visited:
                    continue
                visited.add(node_name)
                try:
                    result = await self.nodes[node_name].execute(node_inputs)
                    results[node_name] = result
                    
                    for successor in self.graph.successors(node_name):
                        if successor in visited:
                            continue
                        edge_data = self.graph.get_edge_data(node_name, successor)
                        mapping = edge_data[0].get('output_to_input_map', {}) if edge_data else {}
                        target_contract = self.nodes[successor].contract
                        successor_inputs = {}
                        for out_key, val in result.items():
                            in_key = mapping.get(out_key, out_key)
                            if in_key in target_contract.input_types:
                                successor_inputs[in_key] = val
                        if successor_inputs:
                            next_inputs[successor] = successor_inputs
                except Exception as e:
                    logger.warning(f"Propagation stopped at {node_name}: {e}")
                    continue
            if not next_inputs:
                break
            current_inputs = next_inputs
        return results

    def get_introspection(self) -> Dict:
        def type_to_str(t):
            return str(t).replace("<class '", "").replace("'>", "")
        return {
            "nodes_count": len(self.nodes),
            "edges_count": self.graph.number_of_edges(),
            "node_details": {
                name: {
                    "input_types": {k: type_to_str(v) for k, v in self.nodes[name].contract.input_types.items()},
                    "output_types": {k: type_to_str(v) for k, v in self.nodes[name].contract.output_types.items()},
                    "performance": round(self.nodes[name].performance_score, 3),
                    "last_execution": str(self.nodes[name].last_execution),
                    "has_execution_contract": self.nodes[name].execution_contract is not None
                } for name in self.nodes
            }
        }

    def save_state(self, filepath: str = "speace_graph_state.json"):
        state = {
            "nodes": list(self.nodes.keys()),
            "edges": [(u, v, d) for u, v, d in self.graph.edges(data=True)],
            "timestamp": str(datetime.now())
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
        logger.info(f"Graph state saved to {filepath}")


# ==================== TEST MIGLIORATO ====================
async def example_node_hello(name: str) -> Dict[str, str]:
    return {"greeting": f"Hello {name} from SPEACE!", "text": f"Hello {name} from SPEACE!"}


async def example_node_upper(text: str) -> Dict[str, Any]:
    return {"upper": text.upper(), "processed": True}


async def run_test():
    graph = SPEACEAdaptiveGraph()
   
    graph.register_node(
        name="input_processor",
        func=example_node_hello,
        input_types={"name": str},
        output_types={"greeting": str, "text": str},
        metadata={"region": "frontal"}
        # execution_contract può essere passato qui quando necessario
    )
   
    graph.register_node(
        name="text_enhancer",
        func=example_node_upper,
        input_types={"text": str},
        output_types={"upper": str, "processed": bool},
        metadata={"region": "temporal"}
    )
   
    graph.connect("input_processor", "text_enhancer",
                 weight=0.95,
                 output_to_input_map={"text": "text"})
   
    result = await graph.propagate(
        start_node="input_processor",
        inputs={"name": "SPEACE User"}
    )
   
    print("\n=== RISULTATO PROPAGAZIONE ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))
   
    print("\n=== INTROSPEZIONE GRAFO ===")
    print(json.dumps(graph.get_introspection(), indent=2, ensure_ascii=False))
   
    graph.save_state()


if __name__ == "__main__":
    asyncio.run(run_test())
