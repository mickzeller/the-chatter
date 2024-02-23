import pprint
from ollama import chat
from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
)


class ChatMessage(BaseModel):
    model: str = "llama2"
    role: str = "user"
    prompt: str = Field(..., min_length=1, max_length=50)
    stream: bool = False


pp = pprint.PrettyPrinter(indent=4)


def print_message_data(msg: ChatMessage):
    print_message = ChatMessage(**msg.dict())
    pp.pprint(print_message)


@router.get(
    "/",
    tags=["messages"],
    summary="Get all messages",
    description="Get all messages for a user",
)
async def get_all_messages():
    return "Hello World!"


@router.post("/")
async def create_message(msg: ChatMessage):
    print_message_data(msg)
    chat_data = {
        "model": msg.model,
        "role": msg.role,
        "stream": msg.stream,
        "content": msg.prompt,
    }
    message = chat(chat_data)
    chat_response = "".join(chunk["message"]["content"] for chunk in message)
    print(chat_response, end="", flush=True)
    return chat_response
