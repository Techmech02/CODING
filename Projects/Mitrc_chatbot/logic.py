import json

def load_faq():
    with open("faq_data.json", "r") as f:
        return json.load(f)

def find_answer(user_question):
    user_question = user_question.lower()
    faqs = load_faq()
    
    for faq in faqs:
        if faq["question"].lower() in user_question:
            return faq["answer"]

    # Keyword-based fallback match
    for faq in faqs:
        if any(word in user_question for word in faq["question"].lower().split()):
            return faq["answer"]
    
    return "Sorry, I couldn't find an answer to that. Please contact the admissions office for more help."
