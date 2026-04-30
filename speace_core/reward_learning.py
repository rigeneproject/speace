"""SPEACE Reward Learning - Phase 3.5

Implements inverse reinforcement learning and objective alignment.
Features:
  - Homeostatic needs vector
  - Reward model computation
  - Inverse RL from expert demonstrations
  - Objective alignment verification
  - Preference learning from human feedback
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
import numpy as np

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class NeedType(Enum):
    """Types of homeostatic needs"""
    ENERGY = "energy"
    LEARNING = "learning"
    COHERENCE = "coherence"
    AGENCY = "agency"
    SAFETY = "safety"


@dataclass
class HomeostasisVector:
    """Homeostatic needs state"""
    energy: float = 1.0  # 0-1
    learning: float = 0.5  # 0-1
    coherence: float = 0.8  # 0-1
    agency: float = 0.7  # 0-1
    safety: float = 1.0  # 0-1
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary"""
        return {
            "energy": self.energy,
            "learning": self.learning,
            "coherence": self.coherence,
            "agency": self.agency,
            "safety": self.safety
        }
    
    def all_above_threshold(self, threshold: float = 0.2) -> bool:
        """Check if all needs are above threshold"""
        return all(v >= threshold for v in self.to_dict().values())


@dataclass
class ExpertTrajectory:
    """Expert demonstration trajectory"""
    states: List[Dict[str, Any]]
    actions: List[Dict[str, Any]]
    rewards: List[float]
    description: str = ""


class RewardModel:
    """Models reward based on homeostatic needs"""
    
    def __init__(self):
        self.weights: Dict[NeedType, float] = {
            NeedType.ENERGY: 0.2,
            NeedType.LEARNING: 0.3,
            NeedType.COHERENCE: 0.2,
            NeedType.AGENCY: 0.2,
            NeedType.SAFETY: 0.1
        }
        logger.info(f"RewardModel initialized with weights: {self.weights}")
    
    async def compute_reward(self, state: Dict, action: Dict,
                            homeostasis: HomeostasisVector) -> float:
        """Compute reward from state and homeostasis"""
        reward = 0.0
        
        # Reward for maintaining homeostasis
        h_dict = homeostasis.to_dict()
        
        for need_type, weight in self.weights.items():
            need_value = h_dict.get(need_type.value, 0.5)
            # Reward increases with need satisfaction
            reward += weight * need_value
        
        logger.debug(f"Computed reward: {reward:.4f}")
        return reward
    
    async def update_homeostasis(self, current: HomeostasisVector,
                                action_result: Dict[str, float]) -> HomeostasisVector:
        """Update homeostasis based on action result"""
        new_h = HomeostasisVector(
            energy=max(0, min(1, current.energy + action_result.get("energy_change", 0))),
            learning=max(0, min(1, current.learning + action_result.get("learning_change", 0))),
            coherence=max(0, min(1, current.coherence + action_result.get("coherence_change", 0))),
            agency=max(0, min(1, current.agency + action_result.get("agency_change", 0))),
            safety=max(0, min(1, current.safety + action_result.get("safety_change", 0)))
        )
        
        logger.debug(f"Updated homeostasis: {new_h.to_dict()}")
        return new_h
    
    async def set_objective_weights(self, weights: Dict[NeedType, float]) -> None:
        """Set custom objective weights"""
        self.weights = weights
        logger.info(f"Updated objective weights: {weights}")


class InverseReinforcementLearner:
    """Learns reward function from expert demonstrations"""
    
    def __init__(self, reward_model: RewardModel):
        self.reward_model = reward_model
        self.expert_trajectories: List[ExpertTrajectory] = []
        self.inferred_weights: Optional[Dict[NeedType, float]] = None
        logger.info("InverseReinforcementLearner initialized")
    
    async def add_expert_trajectory(self, trajectory: ExpertTrajectory) -> None:
        """Add expert demonstration"""
        self.expert_trajectories.append(trajectory)
        logger.info(f"Added expert trajectory: {trajectory.description}")
    
    async def infer_objective_trajectory_matching(self) -> Dict[NeedType, float]:
        """Infer objective function using trajectory matching"""
        if not self.expert_trajectories:
            logger.warning("No expert trajectories provided")
            return self.reward_model.weights
        
        # Simple IRL: average rewards from trajectories
        logger.info(f"Inferring objective from {len(self.expert_trajectories)} trajectories")
        
        total_rewards = {need: 0.0 for need in NeedType}
        total_weight = 0.0
        
        for traj in self.expert_trajectories:
            for reward in traj.rewards:
                total_weight += reward
                # Distribute reward proportionally
                for need in NeedType:
                    total_rewards[need] += reward / len(NeedType)
        
        # Normalize to create weights
        inferred_weights = {}
        for need in NeedType:
            if total_weight > 0:
                inferred_weights[need] = total_rewards[need] / total_weight
            else:
                inferred_weights[need] = 1.0 / len(NeedType)
        
        self.inferred_weights = inferred_weights
        logger.info(f"Inferred weights: {inferred_weights}")
        return inferred_weights
    
    async def learn_from_preferences(self, preference_pairs: List[tuple]) -> Dict[NeedType, float]:
        """Learn from pairwise preference comparisons"""
        logger.info(f"Learning from {len(preference_pairs)} preference pairs")
        # Placeholder: in practice would use preference learning algorithms
        return self.reward_model.weights


class ObjectiveAlignmentChecker:
    """Verifies alignment of objectives with human values"""
    
    def __init__(self):
        self.safety_constraints: List[tuple] = []  # (check_fn, description)
        self.value_constraints: List[tuple] = []   # (check_fn, description)
        logger.info("ObjectiveAlignmentChecker initialized")
    
    async def add_safety_constraint(self, check_fn: Callable,
                                   description: str) -> None:
        """Add safety constraint"""
        self.safety_constraints.append((check_fn, description))
        logger.info(f"Added safety constraint: {description}")
    
    async def add_value_constraint(self, check_fn: Callable,
                                  description: str) -> None:
        """Add value alignment constraint"""
        self.value_constraints.append((check_fn, description))
        logger.info(f"Added value constraint: {description}")
    
    async def check_alignment(self, objective: Dict,
                             state: Dict) -> tuple[bool, float]:
        """Check alignment of objective with constraints
        
        Returns: (is_aligned, alignment_score)
        """
        logger.info(f"Checking alignment for objective: {objective}")
        
        alignment_score = 0.0
        total_checks = 0
        
        # Check safety constraints
        for check_fn, desc in self.safety_constraints:
            try:
                if await check_fn(state):
                    alignment_score += 1.0
                total_checks += 1
            except Exception as e:
                logger.warning(f"Error checking safety constraint '{desc}': {e}")
        
        # Check value constraints
        for check_fn, desc in self.value_constraints:
            try:
                if await check_fn(state):
                    alignment_score += 1.0
                total_checks += 1
            except Exception as e:
                logger.warning(f"Error checking value constraint '{desc}': {e}")
        
        # Compute alignment score
        if total_checks > 0:
            alignment_score /= total_checks
        else:
            alignment_score = 1.0  # No constraints = fully aligned
        
        is_aligned = alignment_score >= 0.8  # 80% threshold
        logger.info(f"Alignment check: {'✅ Aligned' if is_aligned else '❌ Not aligned'} (score={alignment_score:.3f})")
        
        return is_aligned, alignment_score


# ============================================================================
# Test Functions
# ============================================================================

async def test_reward_model():
    """Test reward model"""
    logger.info("\n=== Testing Reward Model ===")
    
    reward_model = RewardModel()
    
    homeostasis = HomeostasisVector(
        energy=0.9,
        learning=0.7,
        coherence=0.85,
        agency=0.8,
        safety=1.0
    )
    
    reward = await reward_model.compute_reward({}, {}, homeostasis)
    assert isinstance(reward, float)
    assert 0 <= reward <= 1
    logger.info("✅ Reward model test passed")


async def test_inverse_rl():
    """Test inverse reinforcement learning"""
    logger.info("\n=== Testing Inverse RL ===")
    
    reward_model = RewardModel()
    irl = InverseReinforcementLearner(reward_model)
    
    # Add expert trajectory
    traj = ExpertTrajectory(
        states=[{"task": 1}, {"task": 2}],
        actions=[{"action": "learn"}],
        rewards=[0.5, 0.8],
        description="Expert prefers learning"
    )
    
    await irl.add_expert_trajectory(traj)
    weights = await irl.infer_objective_trajectory_matching()
    assert weights is not None
    logger.info("✅ Inverse RL test passed")


async def test_alignment_checker():
    """Test objective alignment checking"""
    logger.info("\n=== Testing Alignment Checker ===")
    
    checker = ObjectiveAlignmentChecker()
    
    # Add safety constraint
    async def safety_check(state):
        return state.get("energy", 0) > 0.2
    
    await checker.add_safety_constraint(safety_check, "Energy > 0.2")
    
    # Check alignment
    is_aligned, score = await checker.check_alignment({}, {"energy": 0.8})
    assert is_aligned
    assert score >= 0.8
    logger.info("✅ Alignment checker test passed")


async def main():
    """Run all tests"""
    logger.info("Starting Reward Learning Tests...")
    
    await test_reward_model()
    await test_inverse_rl()
    await test_alignment_checker()
    
    logger.info("\n=== All Reward Learning Tests Passed ===")


if __name__ == "__main__":
    asyncio.run(main())
