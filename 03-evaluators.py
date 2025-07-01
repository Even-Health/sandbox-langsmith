import os
from langsmith.schemas import Example, Run

os.environ["OPENAI_API_KEY"] = ""

def correct_label(inputs: dict, reference_outputs: dict, outputs: dict) -> dict:
  score = outputs.get("output") == reference_outputs.get("label")
  return {"score": int(score), "key": "correct_label"}


from openai import OpenAI
from pydantic import BaseModel, Field

client = OpenAI()

class Similarity_Score(BaseModel):
    similarity_score: int = Field(description="Semantic similarity score between 1 and 10, where 1 means unrelated and 10 means identical.")

# NOTE: This is our evaluator
def compare_semantic_similarity(inputs: dict, reference_outputs: dict, outputs: dict):
    input_question = inputs["question"]
    reference_response = reference_outputs["output"]
    run_response = outputs["output"]
    
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {   
                "role": "system",
                "content": (
                    "You are a semantic similarity evaluator. Compare the meanings of two responses to a question, "
                    "Reference Response and New Response, where the reference is the correct answer, and we are trying to judge if the new response is similar. "
                    "Provide a score between 1 and 10, where 1 means completely unrelated, and 10 means identical in meaning."
                ),
            },
            {"role": "user", "content": f"Question: {input_question}\n Reference Response: {reference_response}\n Run Response: {run_response}"}
        ],
        response_format=Similarity_Score,
    )

    similarity_score = completion.choices[0].message.parsed
    return {"score": similarity_score.similarity_score, "key": "similarity"}

# inputs = {
#   "question": "Is LangSmith natively integrated with LangChain?"
# }
# reference_outputs = {
#   "output": "Yes, LangSmith is natively integrated with LangChain, as well as LangGraph."
# }


# # From Run
# outputs = {
#   "output": "No, LangSmith is NOT integrated with LangChain."
# }

# similarity_score = compare_semantic_similarity(inputs, reference_outputs, outputs)
# print(f"Semantic similarity score: {similarity_score}")    