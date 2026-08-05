from dotenv import load_dotenv

load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

from backend.config import LLM_MODEL
from backend.prompts import format_docs, build_chat_messages


def build_rag_chain(retriever):

    llm = ChatGroq(
        model=LLM_MODEL,
        temperature=0.3
    )

    parser = StrOutputParser()

    parallel_chain = RunnableParallel(
        {
            "context": (
                lambda x: x["question"]
            )
            | retriever
            | RunnableLambda(format_docs),

            "question": lambda x: x["question"],

            "history": lambda x: x["history"],
        }
    )

    def assemble_messages(inputs):
        return build_chat_messages(
            context=inputs["context"],
            history=inputs["history"],
            question=inputs["question"],
        )

    return (
        parallel_chain
        | RunnableLambda(assemble_messages)
        | llm
        | parser
    )