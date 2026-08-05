from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)


def build_chat_messages(context, history, question):
    messages = [
        SystemMessage(
            content=(
                "You are a knowledgeable and conversational assistant. "
                "Answer questions using ONLY the document context provided below. "
                "If the context does not contain enough information, say you don't know. "
                "Be concise, clear, and natural.\n\n"
                f"Document Context:\n{context}"
            )
        )
    ]

    for msg in history:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))

    messages.append(HumanMessage(content=question))

    return messages