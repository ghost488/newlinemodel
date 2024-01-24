import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(
    "test-newline-510ed-firebase-adminsdk-3t96t-5f3f87e90a.json"
)
firebase_admin.initialize_app(cred)


db = firestore.client()


# 모델 추가 함수
def addModel(data):
    doc_ref = db.collection("model").document(data["name"]).set(data)
    print(f'새로운 모델 추가 완료 {data["name"]}')


# 모델 정보를 가져오는 함수
def getModels():
    models = []
    docAll = db.collection("model").stream()

    for doc in docAll:
        data = doc.to_dict()
        modelInstance = Model(
            name=data.get("name"),
            number=data.get("number"),
            council=data.get("council"),
            operator=data.get("operator"),
            operation=data.get("operation"),
            opDate=data.get("opDate"),
        )
        models.append(modelInstance)
    return models


# 모델 클래스->인스턴스 생성용
class Model:
    def __init__(self, name, number, council, operator, operation, opDate):
        self.name = name
        self.number = number
        self.council = council
        self.operator = operator
        self.operation = operation
        self.opDate = opDate
