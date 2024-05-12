n = int(input())
s = input().split(' ')

class TrieNode:
    def __init__(self, char: str):
        # assert len(char) <= 1
        self.char = char
        self.weight = 1
        self.children = dict()
    
    def __str__(self):
        base = f"char: {self.char}, weight: {self.weight}"
        children_description = f"\n Children are..."
        for k, v in self.children.items():
            children_description += "\n\t" + k + ":" + str(v)
        return base + children_description
    
    def increment_weight(self):
        self.weight += 1
    
    def add(self, strings: str):
        incremented_node = self
        for c in strings:
            if c in incremented_node.children:
                incremented_node.children[c].increment_weight()
            else:
                child = TrieNode(c)
                incremented_node.children[c] = child
            incremented_node = incremented_node.children[c]
    
    def calculate_answer(self):
        ans = 0

        def dfs(start_node):
            nonlocal ans
            for _, child in start_node.children.items():
                if child.weight > 1:
                    dfs(child)
            ans += ((start_node.weight - 1) * start_node.weight ) // 2

        dfs(self)
        return ans

trie_tree = TrieNode('')

for strings in s:
    trie_tree.add(strings)

print(trie_tree.calculate_answer())
