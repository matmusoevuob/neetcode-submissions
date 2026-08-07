class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        num = 0
        set_emails = set()

        for email in emails:
            a = ""
            email = email.split("@")
            for ch in email[0]:
                if ch == "+":
                    break
                if ch == ".":
                    continue
                a += ch
            
            a = a + "@" + email[1]

            if a not in set_emails:
                set_emails.add(a)
                num += 1            

        return num
