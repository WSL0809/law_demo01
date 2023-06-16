from typing import List

from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Qdrant


class UploaderOfQdrant:
    @staticmethod
    def __documentsLoader(markdown_path):
        # markdown_path = "../law_data/law.md"
        loader = UnstructuredHTMLLoader(markdown_path)
        documents = loader.load()
        return documents

    # @staticmethod
    # def documentsTokenizer():
    #     tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    #     return tokenizer

    @staticmethod
    def __documentsSpliter(documents):
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=100, chunk_overlap=10)
        documents = text_splitter.split_documents(documents)
        texts = []
        for i in documents:
            texts.append(i.page_content)
        return texts

    @staticmethod
    def __documentsEmbedding(model_name="GanymedeNil/text2vec-large-chinese"):
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        return embeddings

    @staticmethod
    def __UploadToQdrant(texts: List[str], embeddings):
        qdrant = Qdrant.from_texts(
            texts, embeddings,
            host="127.0.0.1",
            port=6333,
            collection_name="labor_law",
        )
        return qdrant

    def Upload(self, filePath="../law_data/law.md"):
        loader = self.__documentsLoader(filePath)
        texts = self.__documentsSpliter(loader)
        embeddings = self.__documentsEmbedding()
        qdrant = self.__UploadToQdrant(texts, embeddings)
        return qdrant
