import qdrant_client
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Qdrant


def query(q: str):
    embeddings = HuggingFaceEmbeddings(
        model_name='../GanymedeNil_text2vec-large-chinese',
        model_kwargs={'device': 'cpu'}
    )
    # embeddings = HuggingFaceEmbeddings()

    client = qdrant_client.QdrantClient(
        url="127.0.0.1", prefer_grpc=False
    )
    qdrant = Qdrant(
        client=client, collection_name="labor_law",
        embeddings=embeddings
    )
    res = []
    found_docs = qdrant.max_marginal_relevance_search(q)
    for i in found_docs:
        res.append(i.page_content)
    return res


if __name__ == '__main__':
    print(query('怀孕'))
    print('')
