"""
SPEACE - Lobo Frontale (Funzioni Esecutive + Area di Broca)
Versione 0.2 - Fix input mapping
"""

import asyncio
import sys
from pathlib import Path
from typing import Dict, Any

# Fix percorso
current_dir = Path(__file__).resolve().parent.parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from graph_engine import SPEACEAdaptiveGraph


class FrontalLobeModule:
    """Lobo Frontale: Funzioni Esecutive, Decisione e Produzione Linguistica (Broca)"""
    
    def __init__(self, graph: SPEACEAdaptiveGraph):
        self.graph = graph
        self.executive_hub = "ExecutiveController"
        self.broca_area = "BrocaLanguage"
        
        self._register_frontal_lobe()
    
    def _register_frontal_lobe(self):
        # === Executive Controller ===
        async def executive_controller(goal: str, context: Dict = None) -> Dict[str, Any]:
            if context is None:
                context = {}
            return {
                "plan": f"Piano esecutivo per: {goal}",
                "steps": ["Analisi", "Prioritizzazione", "Assegnazione risorse", "Monitoraggio"],
                "priority_score": 0.89,
                "risk_assessment": "Basso rischio",
                "decision": f"APPROVATO → {goal}"
            }
        
        self.graph.register_node(
            name=self.executive_hub,
            func=executive_controller,
            input_types={"goal": str, "context": dict},
            output_types={"plan": str, "steps": list, "priority_score": float, 
                         "risk_assessment": str, "decision": str},
            metadata={"region": "frontal", "function": "executive"}
        )
        
        # === Area di Broca ===
        async def broca_language_production(concept: str, style: str = "formal") -> Dict[str, Any]:
            styles = {
                "formal": "Risposta strutturata e precisa.",
                "creative": "Risposta innovativa e metaforica.",
                "concise": "Risposta essenziale."
            }
            return {
                "verbal_output": f"{styles.get(style, styles['formal'])} {concept}",
                "grammatical_complexity": 0.87,
                "fluency_score": 0.95,
                "emotional_tone": "determinato-positivo"
            }
        
        self.graph.register_node(
            name=self.broca_area,
            func=broca_language_production,
            input_types={"concept": str, "style": str},
            output_types={"verbal_output": str, "grammatical_complexity": float, 
                         "fluency_score": float, "emotional_tone": str},
            metadata={"region": "frontal", "function": "broca"}
        )
        
        # Connessione con default style
        self.graph.connect(self.executive_hub, self.broca_area, weight=0.92,
                          output_to_input_map={"decision": "concept"})
    
    async def execute_task(self, goal: str, style: str = "creative", context: Dict = None) -> Dict:
        exec_result = await self.graph.propagate(
            self.executive_hub, 
            {"goal": goal, "context": context or {}}
        )
        
        exec_data = exec_result.get(self.executive_hub, {})
        
        broca_result = await self.graph.propagate(
            self.broca_area,
            {"concept": exec_data.get("decision", goal), "style": style}
        )
        
        return {
            "goal": goal,
            "executive": exec_data,
            "language": broca_result.get(self.broca_area, {}),
            "status": "EXECUTED"
        }


# ====================== TEST ======================
async def test_frontal_lobe():
    graph = SPEACEAdaptiveGraph()
    frontal = FrontalLobeModule(graph)
    
    result = await frontal.execute_task(
        goal="Integrare il modulo Astrocitario con gli emisferi cerebrali",
        style="creative"
    )
    
    print("=== TEST LOBO FRONTALE v0.2 (PULITO) ===")
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(test_frontal_lobe())
