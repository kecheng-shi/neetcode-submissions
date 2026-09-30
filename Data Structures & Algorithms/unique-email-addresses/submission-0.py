class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local = True
            skip = False
            current = ""
            for c in email:
                if c == '@':
                    local = False

                if c == '.' and local:
                    continue
                elif c == '+' and local:
                    skip = True
                    continue
                
                if skip and local:
                    continue
                current += c
            
            seen.add(current)

        return len(seen)
                