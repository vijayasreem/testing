
trigger CreditCheckPreQualificationTrigger on Applicant__c (after insert) {
    public void performCreditCheckAndPreQualification(List<Applicant__c> newApplicants) {
        List<Applicant__c> applicantsToUpdate = new List<Applicant__c>();
        List<PreQualification__c> preQualificationsToCreate = new List<PreQualification__c>();
        List<Messaging.SingleEmailMessage> emailNotificationsToSend = new List<Messaging.SingleEmailMessage>();
        
        for (Applicant__c applicant : newApplicants) {
            // Perform credit check by integrating with credit bureau
            Integer creditScore = CreditBureauIntegration.getCreditScore(applicant.SSN__c);
            
            // Calculate loan amount and interest rate range based on credit score and financial history
            Decimal loanAmount = LoanCalculator.calculateLoanAmount(creditScore, applicant.Income__c);
            Decimal interestRateLow = LoanCalculator.calculateInterestRateLow(creditScore);
            Decimal interestRateHigh = LoanCalculator.calculateInterestRateHigh(creditScore);
            
            // Display pre-qualified loan amount and interest rate range to the analyst
            System.debug('Pre-Qualified Loan Amount: ' + loanAmount);
            System.debug('Interest Rate Range: ' + interestRateLow + ' - ' + interestRateHigh);
            
            // Save pre-qualification results for further processing
            PreQualification__c preQualification = new PreQualification__c();
            preQualification.Applicant__c = applicant.Id;
            preQualification.Loan_Amount__c = loanAmount;
            preQualification.Interest_Rate_Low__c = interestRateLow;
            preQualification.Interest_Rate_High__c = interestRateHigh;
            preQualificationsToCreate.add(preQualification);
            
            // Send notification to the applicant about pre-qualification status, loan amount, and interest rate range
            Messaging.SingleEmailMessage emailNotification = new Messaging.SingleEmailMessage();
            emailNotification.setToAddresses(new List<String>{ applicant.Email__c });
            emailNotification.setSubject('Loan Pre-Qualification');
            emailNotification.setPlainTextBody('Congratulations! You have been pre-qualified for a loan.\n\nLoan Amount: ' + loanAmount + '\nInterest Rate Range: ' + interestRateLow + ' - ' + interestRateHigh);
            emailNotificationsToSend.add(emailNotification);
            
            // Update applicant record with pre-qualification status
            applicant.Pre_Qualified__c = true;
            applicantsToUpdate.add(applicant);
        }
        
        // Perform DML operations
        if (!preQualificationsToCreate.isEmpty()) {
            insert preQualificationsToCreate;
        }
        
        if (!emailNotificationsToSend.isEmpty()) {
            Messaging.sendEmail(emailNotificationsToSend);
        }
        
        if (!applicantsToUpdate.isEmpty()) {
            update applicantsToUpdate;
        }
    }
    
    // Trigger entry point
    public void afterInsert(List<Applicant__c> newApplicants, Map<Id, Applicant__c> oldApplicants) {
        performCreditCheckAndPreQualification(newApplicants);
    }
}
