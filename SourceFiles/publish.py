from is_wire.core import Channel, Message

# Connect to the broker
channel = Channel("amqp://10.10.2.2:30000")

message = Message()
# Body is a binary field therefore we need to encode the string
message.body = "Hello!".encode('latin1')

# Broadcast message to anyone interested (subscribed)
channel.publish(message, topic="MyTopic.SubTopic")
