from flask import Flask,jsonify
import qdrant_client
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Qdrant

from db.SearcherOfQdrant import SearcherOfQdrant

app = Flask(__name__)


@app.route('/query/labor_law/<q_content>', methods=['GET'])
def hello_world(q_content):  # put application's code here
    q_content = str(q_content)
    print(q_content)
    embeddings = HuggingFaceEmbeddings(
        model_name='../law_demo/GanymedeNil_text2vec-large-chinese'
    )
    # embeddings = HuggingFaceEmbeddings()

    client = qdrant_client.QdrantClient(
        url="127.0.0.1", prefer_grpc=False
    )
    qdrant = Qdrant(
        client=client, collection_name="labor_law",
        embeddings=embeddings
    )
    res = SearcherOfQdrant.search(q_content, qdrant)
    print(jsonify(res))
    return jsonify(res)


if __name__ == '__main__':
    app.run()
