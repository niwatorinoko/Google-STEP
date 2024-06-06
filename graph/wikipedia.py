import sys
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

        #key->id,value->リンクもとのid
        self.incoming_links = defaultdict(list)
        
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
                self.incoming_links[dst].append(src)
        print("Finished reading %s" % links_file)
        print()


    # Find the longest titles. This is not related to a graph algorithm at all
    # though :)
    def find_longest_titles(self):
        titles = sorted(self.id_to_titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()


    # Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.id_to_titles.keys():
            link_count[id] = 0

        for id in self.id_to_titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.id_to_titles[dst], link_count_max)
        print()


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
                print(node[1])
                return True
            for child in self.links[node[0]]:
                if not child in visited:
                    visited[child] = True
                    queue.append((child, node[1]+1))
        print("Not found")
        return False


    def find_words_id(self, start, goal):
        return self.title_to_id[start], self.title_to_id[goal]


    # Calculate the page ranks and print the most popular pages.
    def find_most_popular_pages(self):
        d = 0.85  # ダンピングファクター（リンクをたどる確率）
        num_iterations = 100  # 最大反復回数
        tolerance = 0.01  # 収束基準の許容誤差
        total = 0
        for iteration in range(100):
            new_ranks = {page: 0 for page in self.id_to_titles}  # 各ページの新しいPageRankを初期化
            for key, value in self.links.items():
                for id in value:
                    new_ranks[id] += self.ranks[key]/len(value)
                # total += 1.0*self.ranks[key]
            # for l in new_ranks:
            #     new_ranks[l] += total
            self.ranks = new_ranks
            #∑(new[i] - old[i])^2 < 0.01　収束の条件
        print(self.ranks)
        pass


    # Do something more interesting!!
    def find_something_more_interesting(self):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    # wikipedia.find_longest_titles()
    # wikipedia.find_most_linked_pages()
    # wikipedia.find_shortest_path("渋谷", "パレートの法則")
    wikipedia.find_most_popular_pages()