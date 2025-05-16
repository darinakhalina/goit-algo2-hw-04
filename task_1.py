from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError(
                f"Illegal argument for pattern = {pattern} must be a string"
            )

        current, result, path = self.root, 0, ""
        result = self.count_suffixes(current, pattern, path, result)
        return result

    def count_suffixes(self, node, pattern, path, result):
        if node.value is not None:
            if path.endswith(pattern):
                result += 1
        for char, next_node in node.children.items():
            result = self.count_suffixes(next_node, pattern, path + char, result)
        return result

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument prefix = {prefix} must be a string")
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat
    print('count_words_with_suffix("e") =', trie.count_words_with_suffix("e"))
    print('count_words_with_suffix("ion") =', trie.count_words_with_suffix("ion"))
    print('count_words_with_suffix("a") =', trie.count_words_with_suffix("a"))
    print('count_words_with_suffix("at") =', trie.count_words_with_suffix("at"))

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
    print('has_prefix("app") =', trie.has_prefix("app"))
    print('has_prefix("bat") =', trie.has_prefix("bat"))
    print('has_prefix("ban") =', trie.has_prefix("ban"))
    print('has_prefix("ca") =', trie.has_prefix("ca"))
