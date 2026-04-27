"""
SPEACE - Emisferi Cerebrali + Corpus Callosum
Versione 0.4 - Fix definitivo type mapping
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


class CerebralHemispheres:
    def __init__(self, graph: SPEACEAdaptiveGraph):
        self.graph = graph
        self.left_agent = "LeftCortex"
        self.right_agent = "RightCortex"
        self.corpus_callosum = "CorpusCallosum"
        
        self._register_hemispheres()
        self._register_corpus_callosum()
    
    def _register_hemispheres(self):
        async def left_cortex_process(query: str) -> Dict[str, Any]:
            return {
                "analysis": f"Analisi logica e sequenziale: {query}",
                "language_output": f"Risposta strutturata: {query.upper()}",
                "confidence": 0.93
            }
        
        self.graph.register_node(
            name=self.left_agent,
            func=left_cortex_process,
            input_types={"query": str},
            output_types={"analysis": str, "language_output": str, "confidence": float},
            metadata={"hemisphere": "left", "role": "logic"}
        )
        
        async def right_cortex_process(query: str) -> Dict[str, Any]:
            return {
                "creative_insight": f"Idea creativa su: {query}",
                "spatial_representation": f"Rappresentazione olistica di {query}",
                "emotional_valence": 0.78
            }
        
        self.graph.register_node(
            name=self.right_agent,
            func=right_cortex_process,
            input_types={"query": str},
            output_types={"creative_insight": str, "spatial_representation": str, "emotional_valence": float},
            metadata={"hemisphere": "right", "role": "creative"}
        )
    
    def _register_corpus_callosum(self):
        async def integrate_hemispheres(left_data: Dict[str, Any], right_data: Dict[str, Any]) -> Dict[str, Any]:
            return {
                "integrated_output": f"{left_data.get('analysis', '')} | Creativo: {right_data.get('creative_insight', '')}",
                "fusion_confidence": (left_data.get('confidence', 0) + right_data.get('emotional_valence', 0)) / 2,
                "coherence_score": 0.89,
                "final_synthesis": "Integrazione bilaterale completata con successo."
            }
        
        self.graph.register_node(
            name=self.corpus_callosum,
            func=integrate_hemispheres,
            input_types={"left_data": dict, "right_data": dict},
            output_types={"integrated_output": str, "fusion_confidence": float, "coherence_score": float, "final_synthesis": str},
            metadata={"role": "corpus_callosum"}
        )
        
        # Mapping preciso (solo dizionari completi)
        self.graph.connect(self.left_agent, self.corpus_callosum, weight=0.95,
                          output_to_input_map={})  # mapping vuoto → passa tutto l'output
        self.graph.connect(self.right_agent, self.corpus_callosum, weight=0.95,
                          output_to_input_map={})
    
    async def process_bilateral(self, query: str) -> Dict:
        left_result = await self.graph.propagate(self.left_agent, {"query": query})
        right_result = await self.graph.propagate(self.right_agent, {"query": query})
        
        left_data = left_result.get(self.left_agent, {})
        right_data = right_result.get(self.right_agent, {})
        
        integrated_result = await self.graph.propagate(
            self.corpus_callosum, 
            {"left_data": left_data, "right_data": right_data}
        )
        
        return {
            "query": query,
            "left": left_data,
            "right": right_data,
            "integrated": integrated_result.get(self.corpus_callosum, {})
        }


async def test_hemispheres():
    graph = SPEACEAdaptiveGraph()
    hemispheres = CerebralHemispheres(graph)
    
    result = await hemispheres.process_bilateral("Progetta l'evoluzione futura di SPEACE verso ASI")
    
    print("=== TEST EMISFERI + CORPUS CALLOSUM v0.4 (PULITO) ===")
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(test_hemispheres())
