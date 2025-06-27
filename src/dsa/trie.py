class TrieNode: 
  def __init__(self):
    self.children = {}
    self.isEndOfWord = False
    self.value = None  # Optional: can be used to store the character or value of the node

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str):
    current = self.root
    for c in word:
      # If the character doesn't exist as a child node, create a new TrieNode for it
      if not c in current.children:
        newNode = TrieNode()
        newNode.value = c  # Optional: store the character in the node
        current.children[c] = newNode
        print(f"Creating new TrieNode for character: {c} - children: {list(current.children.keys())}")

      # Move to next TrieNode
      current = current.children.get(c)

    current.isEndOfWord = True
    print(f"current: {current} - value: {current.value}, isEndOfWord: {current.isEndOfWord}, children: {list(current.children.keys())}")

  def __traverse(self, word: str):
    current = self.root
    found_nodes: list[TrieNode] = [current]

    for c in word:
      # If the character doesn't exist as a child node, return empty list
      if not c in current.children:
        return []
      
      # Move to next TrieNode
      current = current.children.get(c)

      found_nodes.append(current)

    return found_nodes

  def search(self, word: str):
    print(f"Searching for word: {word}")
    found_nodes = self.__traverse(word)
    # debug found nodes to see if the word exists in trie
    for node in found_nodes:
      print(f"Node: {node} - value: ${node.value}, Is End of Word: {node.isEndOfWord}, children: {list(node.children.keys())}")
    print("-------------------------End of traverse-------------------------")
    last_node = found_nodes[-1] if found_nodes else None
    print(f"Last node: {last_node} - value: {last_node.value if last_node else None}, Is End of Word: {last_node.isEndOfWord if last_node else None}")
    # If the last node (last character) marked as end of word, it means the word exist in trie
    return last_node != None and last_node.isEndOfWord
  
  def starts_with(self, word: str):
    found_nodes = self.__traverse(word)

    return len(found_nodes) > 0
  
  def delete(self, word: str):
    found_nodes: list[(str, TrieNode)] = []
    current = self.root

    for c in word:
      if not c in current.children:
        return

      current = current.children.get(c)
      found_nodes.append((c, current))
      continue      
    
    # If the last node (last character) is not marked as end of word, it means the word doesn't exist in trie
    if not current.isEndOfWord:
      return

    # Reverse to delete from the end of word
    found_nodes.reverse()

    for index, item in enumerate(found_nodes):
      c = item [0]
      node = item[1]
      if not node.children and index + 1 < len(found_nodes):
        # Safe to delete this node
        prev_item = found_nodes[index + 1]
        prev_node = prev_item[1]
        prev_node.children.pop(c)
      elif node.isEndOfWord:
        # If this is the last character of the word, just mark it as not end of word
        node.isEndOfWord = False
      
    return



  