import sys, time
from collections import deque, defaultdict

#Wikipediaで47都道府県１週するにはどのくらいかかるか。
#1つの都道府県から1つの都道府県をたどったら、visitedはリセットする。

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


    # Find the shortest path.
    # |start|: The title of the start page.
    # |goal|: The title of the goal page.
    # 目標：最短経路で通るエッジの数を出力
    # 幅優先探索 (breadth first search)
    def find_shortest_path(self, start, goal):
        # txtファイルに単語が存在するか確認
        start_id, goal_id = self.find_words_id(start, goal)

        queue = deque() # dequeを使いキューを用意
        visited = {} # 訪問済みのノードを保存する
        visited[start_id] = True # 訪問済みかをTrueにする
        step = 0 # 親のstep数を記録
        queue.append((start_id, step)) # スタート地点のノードと現在のstep数を保存
        while queue:
            node = queue.popleft()
            if node[0] == goal_id:
                return node[1]
            for child in self.links[node[0]]:
                if not child in visited:
                    visited[child] = True
                    queue.append((child, node[1]+1))
        print("Not found")
        return False


    def find_words_id(self, start, goal):
        assert start in self.title_to_id
        assert goal in self.title_to_id
        return self.title_to_id[start], self.title_to_id[goal]

    def find_shortest_path_around_Japan(self, prefectures):
        total_path = 0
        start = prefectures[0] #北海道
        for goal in range(1, len(prefectures)):
            print(goal)
            path = self.find_shortest_path(start, prefectures[goal])
            total_path += path
            print(start + "から" + prefectures[goal] + "まで" + str(path) + "かかる。合計" + str(total_path))
            start = prefectures[goal]
        print(total_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    prefectures = [
        "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県",
        "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県",
        "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県",
        "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県",
        "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県",
        "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県",
        "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]
    wikipedia.find_shortest_path_around_Japan(prefectures)