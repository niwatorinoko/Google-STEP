import sys

# Implement a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
#
# Note: Please do not use a library like collections.OrderedDict). The goal is
#       to implement the data structure yourself!
class Node:
    def __init__(self, url, contents):
        self.url = url
        self.contents = contents
        self.prev = None
        self.next = None

class HashTable:
    def __init__(self):
        self.bucket_size = 97
        self.buckets = [None] * self.bucket_size
        self.item_count = 0

    def put(self, key, value):
        assert type(key) == str
        self.check_size()
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]
        while item:
            if item.key == key:
                item.value = value
                return False
            item = item.next
        new_item = Item(key, value, self.buckets[bucket_index])
        self.buckets[bucket_index] = new_item
        self.item_count += 1
        return True

    def get(self, key):
        assert type(key) == str
        self.check_size()
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]
        while item:
            if item.key == key:
                return (item.value, True)
            item = item.next
        return (None, False)

    def delete(self, key):
        assert type(key) == str
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]
        prev_item = None
        while item:
            if item.key == key:
                if prev_item:
                    prev_item.next = item.next
                else:
                    self.buckets[bucket_index] = item.next
                self.item_count -= 1
                return True
            prev_item = item
            item = item.next
        return False

    def size(self):
        return self.item_count

    def check_size(self):
        assert (self.bucket_size < 100 or self.item_count >= self.bucket_size * 0.3)

class Item:
    def __init__(self, key, value, next_item=None):
        self.key = key
        self.value = value
        self.next = next_item

def calculate_hash(key):
    hash_value = 0
    for char in key:
        hash_value = hash_value * 31 + ord(char)
    return hash_value


class Cache:
    # Initialize the cache.
    # |n|: The size of the cache.
    def __init__(self, n):
        #------------------------#
        self.capacity = n
        self.size = 0
        self.head = Node(None, None)  # ダミーヘッド
        self.tail = Node(None, None)  # ダミーテール
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_table = HashTable()
        #------------------------#


    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


    def _add_node_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


    # Access a page and update the cache so that it stores the most recently
    # accessed N pages. This needs to be done with mostly O(1).
    # |url|: The accessed URL
    # |contents|: The contents of the URL
    def access_page(self, url, contents):
        #------------------------#
        #valueはnodeの情報が全て入ってる？
        value, found = self.hash_table.get(url)
        if found:
            #Hash tableにurlが保存されてた場合、linked listから削除
            node = value
            self._remove_node(node)
            node.contents = contents
        else:
            #保存されてない場合
            if self.size >= self.capacity:
                #もし、キャッシュの容量がキャパシティ以上だったら
                #ダミーテールのひとつ前
                tail_node = self.tail.prev
                #ダミーテールのひとつ前のNodeを削除
                self._remove_node(tail_node)
                #nextの参照を変える
                self.hash_table.delete(tail_node.url)
                self.size -= 1

            node = Node(url, contents)
            self.size += 1

        self._add_node_to_head(node)
        self.hash_table.put(url, node)
        #------------------------#

    # Return the URLs stored in the cache. The URLs are ordered in the order
    # in which the URLs are mostly recently accessed.
    def get_pages(self):
        #------------------------#
        pages = []
        current = self.head.next
        while current != self.tail:
            pages.append(current.url)
            current = current.next
        return pages        
        #------------------------#


    def get(self, key):
        assert type(key) == str
        self.check_size() # Note: Don't remove this code.
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]
        while item:
            if item.key == key:
                return (item.value, True)
            item = item.next
        return (None, False)

    


def cache_test():
    # Set the size of the cache to 4.
    cache = Cache(4)

    # Initially, no page is cached.
    assert cache.get_pages() == []

    # Access "a.com".
    cache.access_page("a.com", "AAA")
    # "a.com" is cached.
    assert cache.get_pages() == ["a.com"]

    # Access "b.com".
    cache.access_page("b.com", "BBB")
    # The cache is updated to:
    #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
    assert cache.get_pages() == ["b.com", "a.com"]

    # Access "c.com".
    cache.access_page("c.com", "CCC")
    # The cache is updated to:
    #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
    assert cache.get_pages() == ["c.com", "b.com", "a.com"]

    # Access "d.com".
    cache.access_page("d.com", "DDD")
    # The cache is updated to:
    #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
    assert cache.get_pages() == ["d.com", "c.com", "b.com", "a.com"]

    # Access "d.com" again.
    cache.access_page("d.com", "DDD")
    # The cache is updated to:
    #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
    assert cache.get_pages() == ["d.com", "c.com", "b.com", "a.com"]

    # Access "a.com" again.
    cache.access_page("a.com", "AAA")
    # The cache is updated to:
    #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
    assert cache.get_pages() == ["a.com", "d.com", "c.com", "b.com"]

    cache.access_page("c.com", "CCC")
    assert cache.get_pages() == ["c.com", "a.com", "d.com", "b.com"]
    cache.access_page("a.com", "AAA")
    assert cache.get_pages() == ["a.com", "c.com", "d.com", "b.com"]
    cache.access_page("a.com", "AAA")
    assert cache.get_pages() == ["a.com", "c.com", "d.com", "b.com"]

    # Access "e.com".
    cache.access_page("e.com", "EEE")
    # The cache is full, so we need to remove the least recently accessed page "b.com".
    # The cache is updated to:
    #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
    assert cache.get_pages() == ["e.com", "a.com", "c.com", "d.com"]

    # Access "f.com".
    cache.access_page("f.com", "FFF")
    # The cache is full, so we need to remove the least recently accessed page "c.com".
    # The cache is updated to:
    #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
    assert cache.get_pages() == ["f.com", "e.com", "a.com", "c.com"]

    # Access "e.com".
    cache.access_page("e.com", "EEE")
    # The cache is updated to:
    #   (most recently accessed)<-- "e.com", "f.com", "a.com", "c.com" -->(least recently accessed)
    assert cache.get_pages() == ["e.com", "f.com", "a.com", "c.com"]

    # Access "a.com".
    cache.access_page("a.com", "AAA")
    # The cache is updated to:
    #   (most recently accessed)<-- "a.com", "e.com", "f.com", "c.com" -->(least recently accessed)
    assert cache.get_pages() == ["a.com", "e.com", "f.com", "c.com"]

    print("Tests passed!")


if __name__ == "__main__":
    cache_test()