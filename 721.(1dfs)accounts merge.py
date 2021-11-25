import collections
class Solution:
    def accountsMerge(self,accounts):
        belongs = collections.defaultdict(list)
        for i,j in enumerate(acounts):
            for email in j[1:]:
                belongs[email].append(i)
        email_visited = set()
        id_visited = set()
        def dfs(id):
            if id in id_visited:
                return
            id_visited.add(id)
            for email in accounts[id][1:]:
                if email in email_visited:
                    continue
                email_visited.add(email)
                ans[-1].append(email)
                for i in belongs[email]:
                    dfs(i)
        ans = []
        for i in range(len(accounts)):
            if i not in id_visited:
                ans.append(accounts[i][:1])
                dfs(i)
        for i in range(len(ans)):
            ans[i] = ans[i][:1] + sorted(ans[i][1:])
        return ans
