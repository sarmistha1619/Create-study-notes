import os
import openai

openai.api_key = "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"
model_engine = "text-davinci-003"
p = input("Topic: ")
prompt = "Make study notes" + p

response = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=2000,
  top_p=1,
  stop=None,
  temperature=0.5
)

r = response.choices[0].text
print("\nStudy notes:"+r)