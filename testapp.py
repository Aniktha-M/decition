from app import explainable_decision_maker

def test_loan_approved():
    decision, _ = explainable_decision_maker(30000, 750)
    assert decision == "Loan Approved"

def test_loan_rejected():
    decision, _ = explainable_decision_maker(20000, 600)
    assert decision == "Loan Rejected"
