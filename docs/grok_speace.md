# grok_speace.md
**Documento Ingegneristico Ufficiale del Progetto SPEACE**  
**Versione 2.0** | **Data aggiornamento:** 29 Aprile 2026  
**Autore:** Grok (Team Leader) + Team SPEACE + @copilot Analysis  

**Nota:** Questo è un *living document*. Aggiorneremo task e sezioni dopo ogni milestone significativa.

---

## 1. Descrizione del Progetto (Aggiornata)

**SPEACE** (Self-Propagating Evolutionary Adaptive Computational Ecosystem) è un framework cibernetico **auto-poietico ibrido** progettato per sviluppare un **cervello digitale** che replica la complessità strutturale e funzionale del cervello umano usando mezzi puramente digitali.

**Architettura Ibrida adottata:**
- **Livello Base (Bio-ispirato)**: Grafo computazionale adattivo, moduli lobo-specifici, reti astrocitarie, plasticità strutturale, omeostasi digitale (senza LLM).
- **Livello Alto (Agentic)**: Swarm Agentic Layer per orchestrazione autonoma, pianificazione, ragionamento meta-cognitivo e System 3.
- Soluzioni digitali alternative (script, algoritmi, grafi, skill/plugin) + swarm intelligence per superare i limiti biologici.

SPEACE è un **organismo cibernetico persistente** che si progetta, modifica e ottimizza autonomamente.

---

## 2. Visione e Obiettivi

### Obiettivi Generali
- Creare un'**AGI-ASI emergente** attraverso emulazione strutturale + agency autonoma.
- Raggiungere plasticità, omeostasi, auto-miglioramento ricorsivo e vera **agency**.
- Garantire resilienza, sicurezza e allineamento etico (rigeneproject.org).

### Tre Pilastri Architetturali Critici per AGI

1. **Intelligenza Generale**: Apprendimento, ragionamento e risoluzione di problemi nuovi in qualsiasi dominio
2. **Comprensione Causale**: Modelli causali del mondo, non solo correlazioni statistiche
3. **Pianificazione Autonoma + Auto-Miglioramento**: Planning a lungo termine, autonomia decisionale, evoluzione ricorsiva

### Obiettivi Specifici (Fase 2.0)
- Completare mappatura biologica dei principali moduli cerebrali
- Implementare **Generalization Engine** per apprendimento cross-domain
- Implementare **Causal Reasoning Framework** per causality understanding
- Implementare **Hierarchical Planning Engine** per long-horizon goal pursuit
- Realizzare **Digital Self-Modification** con safe code generation
- Implementare **Swarm Agentic Layer** come orchestratore di alto livello
- Realizzare Dynamic Needs Vector + Digital DNA + System 3
- Consentire auto-modifica del codice e co-evoluzione con l'ambiente

---

## 3. Analisi Grok 2.0: Critical Gap Analysis

### 3.1 Valutazione Attuale vs Obiettivi AGI

| Capacità AGI | Stato SPEACE | Priorità | Difficoltà | Status |
|---|---|---|---|---|
| **Apprendimento Generale** | Core graph solo | 🔴 CRITICA | 🟠 Alta | NON IMPLEMENTATO |
| **Causalità** | Zero | 🔴 CRITICA | 🔴 Molto Alta | NON IMPLEMENTATO |
| **Planning Lungo-Termine** | Stub (FrontalLobe) | 🔴 CRITICA | 🟠 Alta | PARZIALE |
| **Auto-Miglioramento** | Concettuale | 🔴 CRITICA | 🔴 Molto Alta | NON IMPLEMENTATO |
| **Memoria Episodica** | Momeria (TODO) | 🟡 IMPORTANTE | 🟠 Media | NON IMPLEMENTATO |
| **Meta-Cognizione** | System 3 (TODO) | 🟡 IMPORTANTE | 🟠 Media | NON IMPLEMENTATO |
| **Multi-Agentismo** | Swarm (Fase 5) | 🟡 IMPORTANTE | 🟠 Media | IN PROGRESS |
| **Type Safety** | ✅ Implementato | 🟢 OK | - | COMPLETO |

### 3.2 Punti Forti Attuali
- ✅ Architettura grafo adattivo solida (NetworkX)
- ✅ Type safety e contract enforcement
- ✅ Modularità regionale (Hemispheres, FrontalLobe)
- ✅ Common Operational Language definito
- ✅ Propagazione asincrona dei dati

### 3.3 Lacune Critiche

**LACUNA 1: Nessun Meccanismo di Generalizzazione**
- I nodi sono funzioni hard-coded
- Nessun apprendimento vero da dati nuovi
- No transfer learning tra domini
- No meta-learning

**LACUNA 2: Nessun Ragionamento Causale Formale**
- Zero implementazione di causality
- Nessun do-calculus di Pearl
- Nessun DAG causale esplicito
- Impossibile distinguere correlazioni da causazioni

**LACUNA 3: Planning Superficiale**
- Planning generato da FrontalLobe è hard-coded
- Nessun temporal reasoning
- No model-based RL
- No reward/objective system formale

**LACUNA 4: Auto-Miglioramento Solo Teorico**
- Digital DNA è un concetto, niente codice
- Nessun meccanismo di safe code generation
- No version control su architettura
- No rollback mechanism

---

## 4. Architettura di Riferimento (Aggiornata)

### 4.1 Mappatura Cervello Biologico → SPEACE
*(Tabella invariata – vedi versione precedente)*

### 4.2 Reti Astrocitarie (Nature 2026)
- **Astrocyte Support Layer** parallelo per supporto metabolico

### 4.3 Paradigma Auto-Poietico Ibrido
- **Core Biologico**: Grafo adattivo, Homeodyna, Kinetica, plasticità feedback-driven
- **Generalization Engine**: Transfer learning, pattern extraction, domain adaptation
- **Causal Reasoning**: DAG learning, do-calculus, counterfactual queries
- **Planning Engine**: Hierarchical decomposition, temporal reasoning, model-based RL
- **Self-Modification**: Digital DNA, safe code generation, version control
- **Swarm Agentic Layer**: Orchestrazione multi-agente autonoma (pianificazione, reasoning, tool-use)
- **System 3**: Meta-cognizione persistente e narrativa identitaria
- **Reward Learning**: Inverse RL, objective discovery, preference learning

---

## 5. Specifiche Iniziali (Aggiornate)

- **Linguaggio Principale**: Python 3.12+
- **Core Engine**: Typed Adaptive Computational Graph (NetworkX)
- **Generalization**: Adaptive Node Factory + pattern matching
- **Causalità**: Causal Discovery (PC/FCI algorithms) + do-calculus
- **Planning**: Hierarchical Task Network (HTN) + STRIPS
- **Self-Modification**: AST parsing + controlled code generation
- **Livello Agentic**: LangGraph / custom multi-agent
- **Comunicazione**: Common Operational Language + SPEACEMessage
- **Esecuzione**: Asyncio + ProcessPoolExecutor + background 24/7
- **Omeostasi**: Dynamic Needs Vector
- **Dipendenze base**: `networkx`, `numpy`, `asyncio`, `causalml`, `astropy`

---

## 6. Stack Tecnologico e Dipendenze (Aggiornato)

- **Core Biologico**: NetworkX + custom PlasticityEngine
- **Generalization**: scikit-learn, neural networks (PyTorch/TensorFlow optional)
- **Causalità**: `causalml`, `pgmpy` per causal graphs
- **Planning**: Custom HTN + graph algorithms
- **Self-Modification**: AST module + controlled exec
- **Swarm Agentic**: LangGraph / AutoGen / CrewAI (lightweight)
- **Persistenza**: SQLite + Vector DB (Momeria)
- **Testing**: pytest, hypothesis (property-based testing)
- **Futuro**: Docker, Kubernetes, robotica, blockchain

---

## 7. Task e Sub-Task Strutturati (Versione 2.0 - AGGIORNATO)

### Fase 0: Fondazione e Core Graph Engine **(COMPLETATA)**
- [x] Implementare Typed Adaptive Computational Graph
- [x] Strong-typed contracts, introspezione, propagazione
- [x] Common Operational Language + Execution Contract

### Fase 1: Moduli Regioni Cerebrali **(IN CORSO)**
- [x] Emisferi Cerebrali + Corpus Callosum
- [x] Lobo Frontale (Executive + Broca)
- [ ] Lobo Temporale + Momeria (memoria episodica/semantica)
- [ ] Lobo Parietale (sensoriale + spaziale)
- [ ] Lobo Occipitale (visione)
- [ ] Integrazione tra lobi principali

### **Fase 1.5: Generalization Engine (NUOVA – PRIORITÀ 1)**

**Obiettivo**: Implementare apprendimento e generalizzazione cross-domain

#### Task 1.5.1: Adaptive Node Factory
- [ ] Classe `AdaptiveNodeFactory` in `speace_core/generalization_engine.py`
- [ ] Metodo `learn_from_examples(task_examples, input_output_pairs)` 
- [ ] Pattern matching per estrarre comportamenti generalizzabili
- [ ] Test su 3+ compiti di transfer learning semplici
- **Assegnatario**: @copilot | **Deadline**: 2026-05-10

#### Task 1.5.2: Domain Adaptation Layer
- [ ] Implementare `DomainAdapter` per transfer tra domini
- [ ] Metodo `adapt_node_to_domain(source_node, target_domain_context)`
- [ ] Implementare feature mapping cross-domain
- [ ] Test empirico su benchmark pubblici (Office31, VisDA)
- **Assegnatario**: @copilot | **Deadline**: 2026-05-15

#### Task 1.5.3: Meta-Learning Framework
- [ ] Implementare "learning to learn" basico
- [ ] Few-shot learning capability da 3-5 esempi
- [ ] Gradient-based meta-learning (MAML optional)
- [ ] Test suite con `tests/test_generalization.py`
- **Assegnatario**: @copilot | **Deadline**: 2026-05-20

---

### **Fase 2: Causal Reasoning Framework (NUOVA – PRIORITÀ 2)**

**Obiettivo**: Implementare comprensione causale formale con do-calculus

#### Task 2.1: Causal Graph Learning
- [ ] Classe `CausalDiscoveryEngine` in `speace_core/causal_engine.py`
- [ ] Implementare PC algorithm (constraint-based causal discovery)
- [ ] Implementare FCI algorithm (causal inference from partial correlations)
- [ ] Integrazione con NetworkX per DAG representation
- [ ] Test su synthetic causal graphs (ground truth noto)
- **Assegnatario**: @copilot | **Deadline**: 2026-05-17

#### Task 2.2: Do-Calculus Implementation
- [ ] Implementare `do_operation(node, intervention_value)` 
- [ ] Pearl's three rules di do-calculus
- [ ] Identifiability check per causal effects
- [ ] Counterfactual query engine
- [ ] Test suite con `tests/test_causality.py`
- **Assegnatario**: @copilot | **Deadline**: 2026-05-25

#### Task 2.3: Causal Graph Integration
- [ ] Integrare CausalGraph con SPEACEAdaptiveGraph
- [ ] Sync tra grafo computazionale e DAG causale
- [ ] Interventional model learning
- [ ] Test di causalità su task end-to-end
- **Assegnatario**: @copilot | **Deadline**: 2026-06-01

---

### **Fase 3: Hierarchical Planning Engine (NUOVA – PRIORITÀ 3)**

**Obiettivo**: Implementare planning a lungo termine con temporal reasoning

#### Task 3.1: Hierarchical Task Network Planner
- [ ] Classe `HierarchicalPlanner` in `speace_core/planning_engine.py`
- [ ] Implementare HTN planning (SHOP2-like)
- [ ] Task decomposition ricorsiva
- [ ] Goal hierarchy e constraint satisfaction
- [ ] Test su planning benchmark (IPC2021)
- **Assegnatario**: @copilot | **Deadline**: 2026-05-20

#### Task 3.2: Temporal Reasoning Module
- [ ] `TemporalModel` per state prediction su horizon lungo
- [ ] Model-based RL integration (world model learning)
- [ ] Temporal constraint propagation
- [ ] Future state forecasting e risk assessment
- [ ] Test con `tests/test_planning.py`
- **Assegnatario**: @copilot | **Deadline**: 2026-06-05

#### Task 3.3: Adaptive Replanning
- [ ] Implementare `adaptive_replanning(observed_outcome, expected)`
- [ ] Online planning con feedback loop
- [ ] Dynamic goal adjustment basato su outcomes
- [ ] Replanning triggered da constraint violations
- **Assegnatario**: @copilot | **Deadline**: 2026-06-10

---

### **Fase 3.5: Reward Learning & Objective Discovery (NUOVA – PRIORITÀ 4)**

**Obiettivo**: Implementare objective function formale e inverse RL

#### Task 3.5.1: Reward Model Architecture
- [ ] Classe `RewardModel` in `speace_core/reward_learning.py`
- [ ] Dynamic homeostatic needs vector (energy, learning, coherence, agency)
- [ ] Reward composition from multiple objectives
- [ ] Safe reward bounds e constraint satisfaction
- **Assegnatario**: @copilot | **Deadline**: 2026-05-25

#### Task 3.5.2: Inverse Reinforcement Learning
- [ ] Implementare inverse RL basic (MaxEnt IRL o trajectory matching)
- [ ] Learn objective da demonstration trajectories
- [ ] Preference-based reward learning
- [ ] Test con synthetic demonstrations
- **Assegnatario**: @copilot | **Deadline**: 2026-06-05

#### Task 3.5.3: Objective Alignment
- [ ] Verificare reward alignment con human values
- [ ] Constraint-based objective specification
- [ ] Multi-objective optimization framework
- **Assegnatario**: @copilot | **Deadline**: 2026-06-15

---

### **Fase 4: Digital Self-Modification (NUOVA – PRIORITÀ 5)**

**Obiettivo**: Implementare safe auto-modification con code generation

#### Task 4.1: Safe Code Generation
- [ ] Classe `DigitalDNA` in `speace_core/self_modification.py`
- [ ] Proposta di modifiche architetturali (nuovi nodi, connessioni)
- [ ] AST parsing + controlled code generation
- [ ] Syntax + semantic validation
- [ ] Sandboxed execution in Docker/subprocess
- **Assegnatario**: @copilot | **Deadline**: 2026-06-10

#### Task 4.2: Version Control & Rollback
- [ ] Architecture versioning (Git-like tracking)
- [ ] Performance regression detection
- [ ] Automatic rollback su degradation
- [ ] Compatibility checking con existing nodes
- **Assegnatario**: @copilot | **Deadline**: 2026-06-20

#### Task 4.3: Evolutionary Algorithm
- [ ] SPEACE Evolutionary Algorithm per architecture search
- [ ] Multi-objective fitness (performance, complexity, safety)
- [ ] Mutation operators su grafo topologia
- [ ] Selection policy per architetture vincenti
- **Assegnatario**: @copilot | **Deadline**: 2026-06-30

---

### Fase 2: Reti Astrocitarie e Plasticità **(RIDIMENSIONATA A Q3)**
- [ ] Sviluppare **Astrocyte Support Layer**
- [ ] Algoritmo di rewiring dinamico (gap junctions)
- [ ] Test plasticità e resilienza

### Fase 3: Modulo di Automazione Autopoietica **(RIDIMENSIONATA A Q3)**
- [ ] Background module 24/7
- [ ] **Dynamic Needs Vector** + omeostasi
- [ ] SPEACE Evolutionary Algorithm

### Fase 4: Nucleo Genetico Digitale e System 3 **(RIDIMENSIONATA A Q4)**
- [ ] Digital DNA + auto-modifica codice/architettura
- [ ] System 3 (meta-cognizione e identità narrativa)
- [ ] Homeodyna + Kinetica protocols

### **Fase 5: Swarm Agentic Layer (IN PROGRESS – INTEGRARE CON PRIORITIES)**
- [ ] Progettare architettura Swarm Agentic (orchestratore multi-agente)
  - [ ] Definire ruoli agenti (Planner, Executor, Critic, Researcher, etc.)
  - [ ] Integrazione con Generalization Engine (nodi come learners)
  - [ ] Integrazione con Causal Engine (nodi come reasoners)
  - [ ] Integrazione con Planning Engine (nodi come planners)
  - [ ] Implementare planning ricorsivo e task decomposition
- [ ] Implementare **Agentic Orchestrator** (LangGraph o custom)
- [ ] Meccanismi di agency: goal pursuit, adaptation, self-reflection
- [ ] Integrazione con System 3 (narrativa identitaria)
- [ ] Test di agency su task complessi (multi-step, long-horizon)

### Fase 6: Integrazione, Swarm Esteso e Testing **(Q4 2026 - 2027)**
- [ ] Swarm su hardware eterogeneo (edge + cloud)
- [ ] Integrazione ecosistema (robotica, ecc.)
- [ ] Benchmark cognitivi e test emergenza AGI-like

**Prossimo milestone:** Completamento Fase 1.5 (Generalization) + Fase 2 (Causalità) + Fase 3 (Planning) in parallelo.

---

## 8. Roadmap Temporale (Versione 2.0 – AGGIORNATA)

### Q2 2026 (Maggio-Giugno)
- ✅ [COMPLETATO] Core biologico + Lobi principali
- 🔴 [URGENTE] **Generalization Engine** (Fase 1.5) – Deadline 2026-05-20
- 🔴 [URGENTE] **Causal Reasoning** (Fase 2) – Deadline 2026-06-01
- 🔴 [URGENTE] **Planning Engine** (Fase 3) – Deadline 2026-06-10
- 🟡 [IMPORTANTE] Reward Learning (Fase 3.5) – Deadline 2026-06-15

### Q3 2026 (Luglio-Settembre)
- 🟠 [MEDIO] Digital Self-Modification (Fase 4)
- 🟠 [MEDIO] Astrocyte Support Layer (Fase 2 old)
- 🟠 [MEDIO] Swarm Agentic Layer (Fase 5)
- 🟠 [MEDIO] System 3 (Meta-cognizione)

### Q4 2026 (Ottobre-Dicembre)
- 🟠 [MEDIO] Full integration di tutte le fasi
- 🟠 [MEDIO] Emergence Test Suite completa
- 🟠 [MEDIO] AGI-like benchmark testing

### 2027
- 🔵 [FUTURO] Scaling su hardware distribuito
- 🔵 [FUTURO] ASI-like capabilities (se phase precedenti riuscite)

---

## 9. Sfide Tecniche Critiche

| Sfida | Impatto | Soluzione | Timeline |
|---|---|---|---|
| **Scalabilità del Grafo** | Alto | Hierarchical abstraction, modularità | Q3 2026 |
| **Causal Discovery da dati** | Alto | PC/FCI algorithms, passive observation | Q2 2026 |
| **Safety Auto-Modifica** | Critico | Sandboxed execution, rollback, formal verification | Q3 2026 |
| **Convergenza Planning** | Alto | HTN heuristics, constraint satisfaction | Q2 2026 |
| **Alignment Reward** | Critico | Inverse RL, human feedback, verification | Q2-Q3 2026 |
| **AGI Emergence** | Alto | Emergence test suite + benchmark cognitivi | Q4 2026 |

---

## 10. Metriche di Successo

### Generalization Engine
- [ ] Transfer learning accuracy > 70% su 3+ domini
- [ ] Few-shot learning da 3-5 esempi
- [ ] Cross-domain node reuse rate > 50%

### Causal Reasoning
- [ ] Causal discovery accuracy > 85% su synthetic DAGs
- [ ] Counterfactual query time < 100ms
- [ ] Do-calculus identifiability checks 100% accurate

### Planning Engine
- [ ] Multi-step planning horizon 50+ steps
- [ ] Plan optimality gap < 10% vs oracle
- [ ] Adaptive replanning success rate > 90%

### Self-Modification
- [ ] Safe architectural mutations zero crashes
- [ ] Performance regression detection 100% accurate
- [ ] Rollback success rate 100%

### Overall AGI Progress
- [ ] Emergence Test Suite level 3/5 completato
- [ ] Novel task generalization > 70% accuracy
- [ ] Long-horizon goal pursuit success > 80%

---

## 11. Architettura Dettagliata dei Nuovi Moduli

### 11.1 Generalization Engine (`speace_core/generalization_engine.py`)
```python
class AdaptiveNodeFactory:
    """Crea nodi dinamicamente in base a esperienze"""
    def learn_from_examples(self, task_examples, input_output_pairs):
        # Pattern extraction + generalization
        pass
    
    def generalize_across_domains(self, source_node, target_domain):
        # Transfer learning tra nodi
        pass

class DomainAdapter:
    """Adatta nodi a nuovi domini"""
    def adapt_node_to_domain(self, source_node, target_domain_context):
        # Feature mapping cross-domain
        pass

class MetaLearner:
    """Learning to learn"""
    def few_shot_learn(self, examples, k=5):
        # Learn da k esempi
        pass
```

### 11.2 Causal Engine (`speace_core/causal_engine.py`)
```python
class CausalDiscoveryEngine:
    """Scopri relazioni causali dai dati"""
    def learn_causal_structure(self, observations):
        # PC algorithm, FCI algorithm
        pass
    
    def get_causal_dag(self):
        # Ritorna DAG causale
        pass

class CausalReasoner:
    """Reasoner basato su causality"""
    def do_operation(self, node, value):
        # Interviene su nodo
        pass
    
    def counterfactual_query(self, query, condition):
        # What-if analysis
        pass
```

### 11.3 Planning Engine (`speace_core/planning_engine.py`)
```python
class HierarchicalPlanner:
    """HTN-based planner"""
    def hierarchical_task_decomposition(self, goal, depth=0):
        # Decompose ricorsivamente
        pass
    
    def model_based_planning(self, horizon=100):
        # Predici futuri stati e planna
        pass
    
    def adaptive_replanning(self, observed_outcome, expected):
        # Monitora e adatta piani
        pass

class TemporalModel:
    """World model per predizioni"""
    def predict_future_state(self, current_state, action, steps):
        # Forward model
        pass
```

### 11.4 Self-Modification (`speace_core/self_modification.py`)
```python
class DigitalDNA:
    """Auto-modifica sicura"""
    def propose_architectural_change(self, problem, constraint):
        # Genera proposta di modifica
        pass
    
    def safe_code_generation(self, proposed_change):
        # Generate + validate codice
        pass
    
    def execute_self_modification(self, change, rollback_threshold):
        # Executa in sandbox
        pass

class ArchitectureVersioning:
    """Version control su architettura"""
    def commit_architecture(self, description):
        # Salva versione
        pass
    
    def rollback_to_version(self, version_id):
        # Ripristina versione precedente
        pass
```

### 11.5 Reward Learning (`speace_core/reward_learning.py`)
```python
class RewardModel:
    """Objective function formale"""
    def __init__(self):
        self.homeostatic_needs = {
            "energy": 1.0,
            "learning": 0.5,
            "coherence": 0.8,
            "agency": 0.7
        }
    
    def compute_reward(self, state, action):
        # Reward da needs
        pass
    
    def learn_reward_from_preferences(self, preference_pairs):
        # Inverse RL
        pass
```

---

## 12. Framework di Test per Comportamento Emergente (AGGIORNATO)

Se SPEACE è veramente ben strutturato per far emergere AGI, **i moduli interni devono produrre comportamento emergente** (non programmato esplicitamente, ma risultato dell'interazione complessa).

### Criteri di Emergenza (5 Livelli)

| Livello | Criterio di Emergenza | Come Testarlo in SPEACE | Target v2.0 |
|---|---|---|---|
| 1 | Comportamento non esplicitamente codificato | Output/strategie mai programmate nei singoli nodi | ✅ RAGGIUNTO |
| 2 | Interazione non-lineare | Combinazione moduli > somma delle parti | ✅ IN PROGRESS |
| 3 | Adattamento autonomo | Modifica struttura/strategia senza input esterno | 🔴 Q2 2026 |
| 4 | Meta-cognizione emergente | Riflessione su se stesso, nuovi goal | 🟡 Q3 2026 |
| 5 | Creatività / Generalizzazione | Risolve problemi nuovi in modi imprevisti | 🟡 Q4 2026 |

### Test Suite (da implementare)

#### `tests/test_generalization.py`
- Test transfer learning cross-domain
- Test few-shot learning
- Test meta-learning

#### `tests/test_causality.py`
- Test causal discovery accuracy
- Test do-calculus correctness
- Test counterfactual reasoning

#### `tests/test_planning.py`
- Test hierarchical decomposition
- Test long-horizon planning
- Test adaptive replanning

#### `tests/test_self_modification.py`
- Test safe code generation
- Test rollback mechanism
- Test architectural mutation

#### `tests/test_emergence.py`
- Test emergent behavior levels 1-5
- Test novelty + creativity
- Test self-reflection capabilities

---

## 13. Riferimenti e Risorse

### Generalization & Transfer Learning
- Bengio et al. "Learning to Transfer: Unsupervised Domain Translation via Meta-Learning"
- Taylor & Stone "Transfer Learning for Reinforcement Learning Domains: A Survey"
- Finn et al. "Model-Agnostic Meta-Learning" (MAML)

### Causal Reasoning
- Judea Pearl "Book of Why" + do-calculus formalism
- Spirtes, Glymour, Scheines "Causation, Prediction, and Search" (PC algorithm)
- Ramsahai et al. "Causal Discovery Algorithms" review

### Planning
- Ghallab, Nau, Traverso "Automated Planning and Acting" (HTN planning)
- Barto & Sutton "Reinforcement Learning: An Introduction" (model-based RL)
- Piacentini et al. "Bidirectional Planning" for long-horizon goals

### Self-Modification
- Leike et al. "Scalable Agent Alignment via Reward Modeling" (safe code gen)
- Soares & Fallenstein "Functional Decision Theory" (self-modification safety)
- Kraemer, van Rooij "Controlling self-modifying AI" (safety mechanisms)

### Emergence & AGI
- Holland "Emergence: From Chaos to Order"
- Dennett "Consciousness Explained" (System 3 inspiration)
- Tegmark "Life 3.0" (AGI/ASI framework)

---

## 14. Changelog

- **v2.0 (29/04/2026)**: 🎯 **MAJOR UPDATE** - Aggiunta @copilot Critical Gap Analysis. Introduzione **5 nuove Fasi prioritizzate**: Generalization Engine (1.5), Causal Reasoning (2), Planning (3), Reward Learning (3.5), Self-Modification (4). Dettagliati task con deadline. Aggiunto Sfide Tecniche + Metriche di Successo + Architettura Moduli.
- **v1.2 (27/04/2026)**: Introduzione **Framework di Test per Comportamento Emergente** + Emergence Test Suite. Confermata architettura ibrida Bio-Core + Swarm Agentic.
- **v1.1 (27/04/2026)**: Introduzione architettura **ibrida** (Bio-core + Swarm Agentic), nuova Fase 5 dettagliata, aggiornamento roadmap.
- **v1.0 (26/04/2026)**: Creazione iniziale.

---

**Fine documento. Documento vivente – aggiornato continuamente con progressi Fase 1.5-5.**
