import sys, time
from collections import deque, defaultdict


class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.id_to_titles = {}
        # A mapping from the page title to a page ID (integer).
        self.title_to_id = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # pageのidとpagerank初期値1を割り当てる辞書
        self.ranks = {}
        
        # Read the pages file into self.titles.
        with open(pages_file) as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.id_to_titles, id
                self.id_to_titles[id] = title
                self.title_to_id[title] = id
                self.links[id] = []
                self.ranks[id] = 1.0
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.id_to_titles, src
                assert dst in self.id_to_titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()

        # 初期化の際コピーする辞書
        self.copy_ranks = {page: 0 for page in self.id_to_titles}


    def find_words_id(self, start, goal):
        assert start in self.title_to_id
        assert goal in self.title_to_id
        return self.title_to_id[start], self.title_to_id[goal]
    

    # Do something more interesting!!
    def find_most_longest_path(self, start, goal):
        # 開始ノードとゴールノードのIDを取得
        start_id, goal_id = self.find_words_id(start, goal)

        def dfs(current_id, goal_id, visited, path_length):
            # ベースケース: ゴールに到達したら、パスの長さを返す
            if current_id == goal_id:
                return path_length

            # 現在のノードを訪問済みとしてマーク
            visited.add(current_id)

            max_path_length = 0
            # 隣接ノードをすべて探索
            for neighbor in self.links[current_id]:
                if neighbor not in visited:
                    current_path_length = dfs(neighbor, goal_id, visited, path_length + 1)
                    if current_path_length > max_path_length:
                        max_path_length = current_path_length

            # 現在のノードを未訪問に戻す（バックトラック）
            visited.remove(current_id)
            return max_path_length

        # 訪問済みノードのセットを初期化し、DFSを開始
        visited = set()
        longest_path_length = dfs(start_id, goal_id, visited, 0)

        # 結果を表示
        if longest_path_length == 0:
            print("Not found")
        else:
            print(longest_path_length)
        print()

        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    wikipedia.find_most_longest_path("A", "F")