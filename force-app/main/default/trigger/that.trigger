
trigger LoanApprovalTrigger on Loan_Application__c (after insert, after update) {
    List<Loan_Approval_Letter__c> approvalLetters = new List<Loan_Approval_Letter__c>();
    
    for (Loan_Application__c loan : Trigger.new) {
        if (loan.Status__c == 'Approved') {
            Loan_Approval_Letter__c approvalLetter = new Loan_Approval_Letter__c();
            approvalLetter.Loan_Application__c = loan.Id;
            approvalLetter.Approved_Amount__c = loan.Approved_Amount__c;
            approvalLetter.Interest_Rate__c = loan.Interest_Rate__c;
            approvalLetter.Repayment_Period__c = loan.Repayment_Period__c;
            approvalLetter.Requirements__c = loan.Requirements__c;
            // Add any additional fields required by the bank
            
            approvalLetters.add(approvalLetter);
        }
    }
    
    if (!approvalLetters.isEmpty()) {
        insert approvalLetters;
    }
}
