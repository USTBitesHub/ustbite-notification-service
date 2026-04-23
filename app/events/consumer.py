import json
import aio_pika
from app.config import settings
from app.services.email_service import send_email
from app.templates.emails import order_confirmed_email, order_delivered_email, payment_failed_email

class LogChannel:
    async def send(self, user_id, message, routing_key):
        print(f"LogChannel [{routing_key}] to {user_id}: {message}")

channel = LogChannel()

async def process_message(message: aio_pika.abc.AbstractIncomingMessage):
    async with message.process():
        event = json.loads(message.body.decode())
        routing_key = message.routing_key
        
        if routing_key == "order.placed":
            await channel.send(event.get("user_id"), "Your order has been placed! We'll confirm shortly.", routing_key)
        elif routing_key == "order.confirmed":
            await channel.send(event.get("user_id"), "Your order is confirmed and being prepared.", routing_key)
        elif routing_key == "order.cancelled":
            await channel.send(event.get("user_id"), "Your order has been cancelled.", routing_key)
        elif routing_key == "payment.success":
            template = order_confirmed_email(
                user_name=event.get("user_name", "User"),
                restaurant_name=event.get("restaurant_name", "Restaurant"),
                order_id=event.get("order_id", "N/A"),
                items=event.get("items", []),
                total=event.get("total", event.get("amount", 0)),
                floor=event.get("delivery_floor", ""),
                wing=event.get("delivery_wing", ""),
                estimated_minutes=event.get("estimated_minutes", 0),
                frontend_url=settings.frontend_url
            )
            await send_email(event.get("user_email", ""), template["subject"], template["html"])
        elif routing_key == "payment.failed":
            template = payment_failed_email(
                user_name=event.get("user_name", "User"),
                amount=event.get("amount", 0),
                order_id=event.get("order_id", "N/A"),
                frontend_url=settings.frontend_url
            )
            await send_email(event.get("user_email", ""), template["subject"], template["html"])
        elif routing_key == "delivery.status_updated":
            if event.get("status") == "PICKED_UP":
                await channel.send(event.get("user_id", "unknown"), "Your order is on its way!", routing_key)
            elif event.get("status") == "DELIVERED":
                template = order_delivered_email(
                    user_name=event.get("user_name", "User"),
                    restaurant_name=event.get("restaurant_name", "Restaurant"),
                    order_id=event.get("order_id", "N/A"),
                    floor=event.get("delivery_floor", ""),
                    wing=event.get("delivery_wing", "")
                )
                await send_email(event.get("user_email", ""), template["subject"], template["html"])

async def start_consumer():
    if not settings.rabbitmq_url:
        return
    connection = await aio_pika.connect_robust(settings.rabbitmq_url)
    mq_channel = await connection.channel()
    exchange = await mq_channel.declare_exchange("ustbite_events", aio_pika.ExchangeType.TOPIC)
    queue = await mq_channel.declare_queue("notification_queue", durable=True)
    await queue.bind(exchange, routing_key="*.*")
    await queue.consume(process_message)
    print("Notification consumer started")
