x
trigger FFAApprovalRequestTrigger on Case (after insert, after update) {
    List<Messaging.SingleEmailMessage> emails = new List<Messaging.SingleEmailMessage>();
    List<Case> casesToUpdate = new List<Case>();

    for (Case c : Trigger.new) {
        if (c.Status == 'New' && c.Owner.Profile.Name == 'Location State Owner') {
            c.Status = 'F&F Approval Pending with QC2';
            casesToUpdate.add(c);

            Messaging.SingleEmailMessage email = new Messaging.SingleEmailMessage();
            email.setToAddresses(new String[] { 'qc2@example.com' });
            email.setSubject('F&F Approval Request');
            email.setPlainTextBody('Case ' + c.CaseNumber + ' requires your approval. Remarks: ' + c.Remarks__c);
            emails.add(email);
        }
    }

    if (!casesToUpdate.isEmpty()) {
        update casesToUpdate;
        Messaging.sendEmail(emails);
    }
}

trigger QC2ApprovalTrigger on Case (after update) {
    for (Case c : Trigger.new) {
        Case oldCase = Trigger.oldMap.get(c.Id);
        if (oldCase.Status == 'F&F Approval Pending with QC2' && c.Status == 'Approved by QC2') {
            c.Status = 'Approved';
        } else if (oldCase.Status == 'F&F Approval Pending with QC2' && c.Status == 'Rejected by QC2') {
            c.Status = 'Rejected';
        }
    }
}
