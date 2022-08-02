from typing_extensions import Self


class Trie:
    def __init__(self, is_end=False):
        self.tree: dict[str, Self] = {}
        self.is_end = is_end

    def insert(self, string: str):
        f, rest = string[:1], string[1:]

        if f not in self.tree:
            self.tree[f] = Trie()

        if not rest:
            self.tree[f].is_end = True
        else:
            self.tree[f].insert(rest)

    def search(self, term: str):
        f, rest = term[:1], term[1:]

        if f not in self.tree:
            return False

        if not rest and self.tree[f].is_end:
            return True

        return self.tree[f].search(rest)

    def contains(self, term: str):
        f, rest = term[:1], term[1:]

        if f not in self.tree:
            return False

        if not rest:
            return True

        return self.tree[f].contains(rest)

    def get_trie(self, term: str) -> Self:
        f, rest = term[:1], term[1:]

        if f not in self.tree:
            return None

        if not rest:
            return self.tree[f]

        return self.tree[f].get_trie(rest)

    def walk(self):
        res = []
        for k, trie in self.tree.items():
            word = k

            if trie.is_end:
                res.append(word)

            if trie.tree:
                for entry in trie.walk():
                    res.append(word+entry)

        return res

    def autocomplete(self, term: str):
        res = []
        if self.contains(term):
            base_trie = self.get_trie(term)

            if self.search(term):
                res.append(term)

            for entry in base_trie.walk():
                res.append(term+entry)

        return res

#


def main():
    trie = Trie()

    words = ["wakanda", "walk", "cat", "cap", "nigga", "wak"]

    for word in words:
        print(f"insert `{word}`")
        trie.insert(word)

    autoc = ["w", "wa", "wak", "g", "c", "ca", "cap"]
    for term in autoc:
        print(f"autocomplete `{term}`")
        res = trie.autocomplete(term)
        print(res)


if __name__ == "__main__":
    main()
