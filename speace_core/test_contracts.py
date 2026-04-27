from contracts import CommonOperationalLanguage, MessageType

msg = CommonOperationalLanguage.create_command(
    sender="FrontalCortex",
    receiver="TemporalMemory",
    action="store_memory",
    params={"content": "Test di SPEACE", "importance": 0.8}
)

print(msg.to_json())