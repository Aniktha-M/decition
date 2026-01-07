def explainable_decision_maker(income, credit_score):
    income_threshold = 25000
    score_threshold = 700

    explanation = []

    if income >= income_threshold:
        explanation.append("Income is sufficient")
    else:
        explanation.append("Income is insufficient")

    if credit_score >= score_threshold:
        explanation.append("Credit score is good")
    else:
        explanation.append("Credit score is poor")

    if income >= income_threshold and credit_score >= score_threshold:
        decision = "Loan Approved"
    else:
        decision = "Loan Rejected"

    return decision, explanation


if __name__ == "__main__":
    decision, reasons = explainable_decision_maker(30000, 750)
    print("Decision:", decision)
    print("Explanation:", reasons)
