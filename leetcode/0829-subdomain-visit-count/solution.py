class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            parts = domain.split(".")
            subdomain = ""

            for i in range(len(parts)-1, -1, -1):
                if subdomain:
                    subdomain = parts[i] + "." + subdomain
                else:
                    subdomain = parts[i]
                
                counts[subdomain] += count
        
        ans = []

        for domain, count in counts.items():
            ans.append(str(count) + " " + domain)
        
        return ans
