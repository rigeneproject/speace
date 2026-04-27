"""
SPEACE Common Operational Language + Execution Contract
Versione 0.1
"""

import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Callable, Optional, Type
from enum import Enum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SPEACE.Contracts")


class MessageType(Enum):
    """Tipi di messaggio nel Common Operational Language"""
    COMMAND = "command"          # Richiesta azione
    QUERY = "query"              # Richiesta informazione
    EVENT = "event"              # Notifica di evento avvenuto
    RESPONSE = "response"        # Risposta a command/query
    STATE_UPDATE = "state_update"  # Aggiornamento stato
    ERROR = "error"              # Errore


@dataclass
class SPEACEMessage:
    """Messaggio standardizzato del Common Operational Language"""
    msg_type: MessageType
    sender: str
    receiver: str
    payload: Dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.now)
    message_id: str = field(default_factory=lambda: f"msg_{datetime.now().timestamp()}")
    correlation_id: Optional[str] = None  # Per tracciare conversazioni

    def to_dict(self) -> Dict:
        return {
            "msg_type": self.msg_type.value,
            "sender": self.sender,
            "receiver": self.receiver,
            "payload": self.payload,
            "timestamp": self.timestamp.isoformat(),
            "message_id": self.message_id,
            "correlation_id": self.correlation_id
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, default=str)


@dataclass
class ExecutionContract:
    """Contratto di esecuzione forte tra nodi/moduli"""
    pre_conditions: List[Callable] = field(default_factory=list)
    post_conditions: List[Callable] = field(default_factory=list)
    invariants: List[Callable] = field(default_factory=list)  # Devono essere sempre veri
    timeout_seconds: float = 30.0
    required_capabilities: List[str] = field(default_factory=list)
    priority: int = 50  # 0-100

    def validate_pre(self, context: Dict) -> bool:
        for cond in self.pre_conditions:
            if not cond(context):
                logger.warning(f"Pre-condition failed: {cond.__name__}")
                return False
        return True

    def validate_post(self, result: Dict, context: Dict) -> bool:
        for cond in self.post_conditions:
            if not cond(result, context):
                logger.warning(f"Post-condition failed: {cond.__name__}")
                return False
        return True

    def validate_invariants(self, state: Dict) -> bool:
        for inv in self.invariants:
            if not inv(state):
                logger.error(f"Invariant broken: {inv.__name__}")
                return False
        return True


class CommonOperationalLanguage:
    """Linguaggio operativo condiviso"""
    
    @staticmethod
    def create_command(sender: str, receiver: str, action: str, params: Dict) -> SPEACEMessage:
        return SPEACEMessage(
            msg_type=MessageType.COMMAND,
            sender=sender,
            receiver=receiver,
            payload={"action": action, "params": params}
        )
    
    @staticmethod
    def create_query(sender: str, receiver: str, query_type: str, params: Dict) -> SPEACEMessage:
        return SPEACEMessage(
            msg_type=MessageType.QUERY,
            sender=sender,
            receiver=receiver,
            payload={"query": query_type, "params": params}
        )
    
    @staticmethod
    def create_event(sender: str, event_type: str, data: Dict) -> SPEACEMessage:
        return SPEACEMessage(
            msg_type=MessageType.EVENT,
            sender=sender,
            receiver="broadcast",  # o specifico
            payload={"event_type": event_type, "data": data}
        )


# ==================== ESEMPI DI USO ====================

def example_pre_condition(context: Dict) -> bool:
    """Esempio: input deve contenere 'text'"""
    return "text" in context or "name" in context

def example_post_condition(result: Dict, context: Dict) -> bool:
    """Esempio: output deve contenere 'upper' o 'greeting'"""
    return bool(result)

# Contratto di esempio
example_contract = ExecutionContract(
    pre_conditions=[example_pre_condition],
    post_conditions=[example_post_condition],
    timeout_seconds=10.0,
    required_capabilities=["text_processing"]
)