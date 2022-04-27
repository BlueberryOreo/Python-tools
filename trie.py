class Trie:
    def __init__(self):
        self.tree = {0: {}}
        self.store = {}
        self.size = 0
        self.root = 0

    def dfs(self, p):
        if not self.tree[p]:
            return [self.store[p]]
        ret = []
        for k in self.tree[p]:
            ret += self.dfs(self.tree[p][k])
        return ret

    def insert(self, word, target=None):
        p = self.root
        for c in word:
            tmp = self.tree[p].get(c)
            if tmp:
                p = tmp
            else:
                self.size += 1
                self.tree[p][c] = self.size
                p = self.tree[p][c]
                self.tree[p] = {}
        self.store[p] = word if not target else target

    def search(self, word):
        p = self.root
        for c in word:
            tmp = self.tree[p].get(c)
            if not tmp:
                return False
            p = tmp
        return True

    def get_sub_tree(self, word):
        p = self.root
        for c in word:
            tmp = self.tree[p].get(c)
            if not tmp:
                return []
            p = tmp
        return self.dfs(p)

    def get_size(self):
        return self.size

    def show_stored(self):
        for k in self.store:
            print(k, self.store[k])

    def clear(self):
        self.tree = {0: {}}
        self.store = {}
        self.size = 0
        self.root = 0


if __name__ == "__main__":
    tree = Trie()

    tree.insert("tree")
    tree.insert("air")
    tree.insert("train")
    print(tree.get_size())
    print(tree.search("apple"))
    print(tree.search("air"))
    tree.show_stored()
    print(tree.get_sub_tree(""))
