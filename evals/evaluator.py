from langsmith.evaluation import evaluate
from app.graph import build_graph
from evals.dataset import dataset

from dotenv import load_dotenv
load_dotenv()

graph = build_graph()

def app_fn(example):
    result = graph.invoke({"input": example["input"]})
    return {"output": result["output"]}

# def simple_eval(example, prediction):
#     return {
#         "score": 1 if example["expected"].lower() in prediction["output"].lower() else 0
#     }
    
    
def simple_eval( prediction,example):
    expected = example.outputs.get("output", "")
    actual = prediction.outputs.get("output", "")
    return {
        "score": 1 if expected.lower() in actual.lower() else 0
    }

if __name__ == "__main__":
    results = evaluate(
        app_fn,
        data=dataset,
        evaluators=[simple_eval],
        experiment_prefix="chatbot-eval"
    )

    print(results)