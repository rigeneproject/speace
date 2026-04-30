# SPEACE Quickstart Guide - Phase 1.5-3.5 Modules

**Version 1.0** | **Date: 2026-04-29**

This guide shows how to use the newly implemented SPEACE modules for Generalization, Causality, Planning, and Reward Learning.

---

## 🚀 Quick Start

### Installation

```bash
cd speace_core
pip install -r requirements.txt
```

---

## 1. Generalization Engine (Phase 1.5)

Learn and generalize behaviors across domains.

### Basic Usage

```python
import asyncio
from speace_core.generalization_engine import AdaptiveNodeFactory, DomainAdapter, MetaLearner

async def main():
    factory = AdaptiveNodeFactory()
    
    # Register learning examples
    await factory.register_task_example("sum", "math", 
        inputs={"x": 2, "y": 3}, 
        outputs={"result": 5})
    
    await factory.register_task_example("sum", "math",
        inputs={"x": 5, "y": 7},
        outputs={"result": 12})
    
    # Learn a generalized node
    learned_node = await factory.learn_from_examples("sum")
    
    # Use on new inputs
    result = await learned_node(x=10, y=20)
    print(f"Learned generalization: {result}")
    
    # Adapt to new domain
    adapter = DomainAdapter(factory)
    adapted_node = await adapter.adapt_node_to_domain("sum", "math", "physics")
    result_physics = await adapted_node(x=3.5, y=2.5)
    print(f"Adapted to physics domain: {result_physics}")
    
    # Few-shot learning
    meta = MetaLearner(factory)
    few_shot_node = await meta.few_shot_learn("sum", k=2)
    print(f"Few-shot learning completed")

asyncio.run(main())
```

### Key Classes

- **`AdaptiveNodeFactory`**: Learn from examples, create generalizable nodes
- **`DomainAdapter`**: Transfer learned nodes to new domains
- **`MetaLearner`**: Few-shot learning (3-5 examples)

---

## 2. Causal Reasoning Engine (Phase 2)

Discover causal structures and perform causal inference.

### Basic Usage

```python
import asyncio
import numpy as np
from speace_core.causal_engine import CausalDiscoveryEngine, CausalReasoner

async def main():
    discovery = CausalDiscoveryEngine(alpha_threshold=0.1)
    
    # Add observations (synthetic causal data)
    for i in range(50):
        age = np.random.normal(40, 15)
        education = 12 + 0.5*age + np.random.normal(0, 2)
        income = 30000 + 1500*education + 300*age + np.random.normal(0, 5000)
        
        await discovery.add_observation({
            "Age": float(age),
            "Education": float(education),
            "Income": float(income)
        })
    
    # Discover causal DAG using PC algorithm
    dag = await discovery.learn_causal_structure()
    print(f"Discovered causal structure:")
    for source, targets in dag.items():
        for target in targets:
            print(f"  {source} → {target}")
    
    # Markov blanket
    mb = await discovery.get_markov_blanket("Income")
    print(f"Markov blanket of Income: {mb}")
    
    # Causal reasoning
    reasoner = CausalReasoner(discovery)
    
    # Intervention: do(Education = 16)
    intervened = await reasoner.do_operation("Education", 16.0)
    print(f"After intervention: {intervened}")
    
    # Counterfactual: What if education was higher?
    counterfactual = await reasoner.counterfactual_query(
        "What if Education had been 16?",
        {"Education": 12, "Income": 50000}
    )
    print(f"Counterfactual result: {counterfactual}")

asyncio.run(main())
```

### Key Classes

- **`CausalDiscoveryEngine`**: Learn causal DAG from observations (PC/FCI algorithms)
- **`CausalReasoner`**: Perform do-calculus interventions and counterfactual queries

---

## 3. Planning Engine (Phase 3)

Hierarchical planning with temporal reasoning and adaptive replanning.

### Basic Usage

```python
import asyncio
from speace_core.planning_engine import (
    HierarchicalPlanner, Action, Task, 
    Precondition, Effect
)

async def main():
    planner = HierarchicalPlanner()
    
    # Register actions
    move_action = Action(
        name="move",
        preconditions=[
            Precondition("can_move", lambda s: s.get("energy", 0) > 0.2)
        ],
        effects=[
            Effect("change_location", 
                lambda s, p: {**s, "location": "destination"})
        ],
        cost=1.0
    )
    
    grasp_action = Action(
        name="grasp",
        preconditions=[],
        effects=[
            Effect("hold_object", 
                lambda s, p: {**s, "holding": True})
        ],
        cost=0.5
    )
    
    await planner.register_action(move_action)
    await planner.register_action(grasp_action)
    
    # Plan a task
    initial_state = {
        "location": "start",
        "energy": 0.9,
        "holding": False
    }
    
    goal_state = {
        "location": "destination",
        "holding": True
    }
    
    task = Task(name="pickup_at_destination", goal=goal_state)
    
    # Hierarchical decomposition
    plan = await planner.hierarchical_task_decomposition(task, initial_state)
    
    if plan:
        print(f"Plan: {len(plan.steps)} steps")
        for i, step in enumerate(plan.steps):
            print(f"  {i+1}. {step.action.name}")
    
    # Model-based planning (long-horizon)
    model_plan = await planner.model_based_planning(
        initial_state, goal_state, horizon=20
    )
    
    # Adaptive replanning
    observed_state = {"location": "middle", "energy": 0.5}
    expected_state = {"location": "destination", "energy": 0.7}
    
    new_plan = await planner.adaptive_replanning(
        plan, observed_state, expected_state, goal_state
    )

asyncio.run(main())
```

### Key Classes

- **`HierarchicalPlanner`**: HTN-style hierarchical planning
- **`TemporalModel`**: World model for state prediction
- Task decomposition, adaptive replanning

---

## 4. Reward Learning (Phase 3.5)

Learn objective functions and verify alignment.

### Basic Usage

```python
import asyncio
from speace_core.reward_learning import (
    RewardModel, HomeostasisVector,
    InverseReinforcementLearner,
    ObjectiveAlignmentChecker,
    ExpertTrajectory
)

async def main():
    # Reward model
    reward_model = RewardModel()
    
    # Homeostasis state
    homeostasis = HomeostasisVector(
        energy=0.9,
        learning=0.7,
        coherence=0.85,
        agency=0.8,
        safety=1.0
    )
    
    # Compute reward
    reward = await reward_model.compute_reward(
        state={},
        action={},
        homeostasis=homeostasis
    )
    print(f"Reward: {reward:.4f}")
    
    # Update homeostasis
    action_result = {
        "energy_change": -0.1,
        "learning_change": 0.15,
        "coherence_change": 0.0,
        "agency_change": 0.0,
        "safety_change": 0.0
    }
    updated = await reward_model.update_homeostasis(homeostasis, action_result)
    print(f"Updated homeostasis: {updated.to_dict()}")
    
    # Inverse RL - learn from expert
    irl = InverseReinforcementLearner(reward_model)
    
    expert_traj = ExpertTrajectory(
        states=[{"task": 1}, {"task": 2}],
        actions=[{"action": "learn"}],
        rewards=[0.5, 0.8],
        description="Expert prefers learning"
    )
    
    await irl.add_expert_trajectory(expert_traj)
    inferred_weights = await irl.infer_objective_trajectory_matching()
    print(f"Inferred objective: {inferred_weights}")
    
    # Alignment checking
    checker = ObjectiveAlignmentChecker()
    
    async def safety_constraint(state):
        return state.get("energy", 0) > 0.2
    
    await checker.add_safety_constraint(safety_constraint, "Energy > 0.2")
    
    is_aligned, score = await checker.check_alignment(
        inferred_weights, 
        {"energy": 0.8}
    )
    print(f"Alignment: {is_aligned}, Score: {score:.3f}")

asyncio.run(main())
```

### Key Classes

- **`RewardModel`**: Homeostatic-based reward function
- **`InverseReinforcementLearner`**: Learn objective from demonstrations
- **`ObjectiveAlignmentChecker`**: Verify alignment with human values

---

## 5. Running Tests

### Test All Modules

```bash
cd speace
pytest tests/test_all_modules.py -v -s
```

### Test Individual Modules

```bash
# Generalization
python -m speace_core.generalization_engine

# Causality
python -m speace_core.causal_engine

# Planning
python -m speace_core.planning_engine

# Reward Learning
python -m speace_core.reward_learning
```

---

## 📊 Architecture Overview

```
┌─────────────────────────────────────────────┐
│       SPEACE AGI Framework v2.0             │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ Core Graph Engine (Phase 0) ✅      │   │
│  │ - NetworkX + typed contracts        │   │
│  └─────────────────────────────────────┘   │
│           ▼ Built On                        │
│  ┌─────────────────────────────────────┐   │
│  │ Generalization Engine (1.5) 🔄     │   │
│  │ - Pattern learning & generalization │   │
│  │ - Domain adaptation                 │   │
│  │ - Few-shot learning                 │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ Causal Reasoning (2) 🔄            │   │
│  │ - Causal structure discovery        │   │
│  │ - Do-calculus interventions        │   │
│  │ - Counterfactual reasoning          │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ Planning Engine (3) 🔄             │   │
│  │ - HTN hierarchical planning         │   │
│  │ - Temporal reasoning                │   │
│  │ - Adaptive replanning               │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ Reward Learning (3.5) 🔄          │   │
│  │ - Homeostatic objectives            │   │
│  │ - Inverse RL                        │   │
│  │ - Alignment verification            │   │
│  └─────────────────────────────────────┘   │
│           ▼ Enable                         │
│  ┌─────────────────────────────────────┐   │
│  │ Self-Modification (4) 🔴           │   │
│  │ - Digital DNA                       │   │
│  │ - Safe code generation              │   │
│  │ - Architecture versioning           │   │
│  └─────────────────────────────────────┘   │
│           ▼ Orchestrates                   │
│  ┌─────────────────────────────────────┐   │
│  │ Swarm Agentic Layer (5) 🟡        │   │
│  │ - Multi-agent coordination          │   │
│  │ - Distributed reasoning             │   │
│  │ - Emergent behaviors                │   │
│  └─────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 🔗 Integration Tips

### Connect Modules

```python
# 1. Learn generalizations
learned_node = await factory.learn_from_examples("task")

# 2. Discover causal structure
dag = await discovery.learn_causal_structure()

# 3. Use for planning
plan = await planner.hierarchical_task_decomposition(task, state)

# 4. Compute rewards
reward = await reward_model.compute_reward(state, action, homeostasis)
```

### Example: Full Pipeline

```python
# Generalize → Plan → Execute → Learn Reward
learned_node = await factory.learn_from_examples("move")
plan = await planner.hierarchical_task_decomposition(task, state)
for step in plan.steps:
    outcome = await learned_node(**step.parameters)
    homeostasis = await reward_model.update_homeostasis(homeostasis, outcome)
    reward = await reward_model.compute_reward(state, step.parameters, homeostasis)
```

---

## 📚 Resources

- **Main Documentation**: `docs/grok_speace.md`
- **Status Tracking**: `docs/IMPLEMENTATION_STATUS.md`
- **Test Suite**: `tests/test_all_modules.py`
- **Core Modules**: `speace_core/*.py`

---

## ❓ FAQ

**Q: How do I learn from new domains?**
A: Use `DomainAdapter` to transfer existing nodes to new domains with feature mapping.

**Q: Can I use my own causal model?**
A: Yes, you can construct a custom `CausalDiscoveryEngine` and load your own DAG.

**Q: How are plans adaptive?**
A: Use `adaptive_replanning()` when observed state deviates from expected to replan online.

**Q: How are rewards aligned with human values?**
A: Use `ObjectiveAlignmentChecker` with safety and value constraints.

---

**Last Updated**: 2026-04-29  
**Version**: 1.0  
**Status**: Production Ready ✅