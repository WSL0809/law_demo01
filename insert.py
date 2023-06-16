from langchain.document_loaders import UnstructuredHTMLLoader, UnstructuredMarkdownLoader


def update():
    markdown_path = "law_data/law.md"
    loader = UnstructuredMarkdownLoader(markdown_path)
    documents = loader.load()
    # from transformers import GPT2TokenizerFast

    # tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

    from langchain.text_splitter import CharacterTextSplitter
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=25)
    from langchain.text_splitter import CharacterTextSplitter
    text_splitter = CharacterTextSplitter(
        separator=";",
        chunk_size=100,
        chunk_overlap=25,
    )
    documents = text_splitter.split_documents(documents)
    from langchain.embeddings import HuggingFaceEmbeddings

    embeddings = HuggingFaceEmbeddings(model_name="./GanymedeNil_text2vec-large-chinese")
    # embeddings = HuggingFaceEmbeddings()
    from langchain.vectorstores import Qdrant

    texts = []
    for i in documents:
        texts.append(i.page_content)
    from qdrant_client import models
    Qdrant.from_texts(
        texts, embeddings,
        host="127.0.0.1",
        port=6333,
        collection_name="labor_law",
        optimizers_config=models.OptimizersConfigDiff(default_segment_number=6)
    )


if __name__ == '__main__':
    update()
