# 標準入力を受け付ける。
N, M = map(int, input().split())

# 都市から都市への移動の情報を格納する。
G = [[] for _ in range(N)]
for _ in range(M):
    # 標準入力を受け付ける。
    A, B = map(int,input().split())
    # 配列のindexが0から始めることに合わせて、都市の番号を-1する。
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

# 初期化
# 次に移動する都市の情報を格納する。
que = [0]
# 0番目の都市からある都市へ移動する時間を格納する。
dist = [None] * N
# 0番目の都市からある都市へ移動する最短経路の道路数を格納する。
cnt = [0] * N
# 0番目の都市の移動時間を0とする。
dist[0] = 0
cnt[0] = 1

for v in que:
    for vv in G[v]:
        # まだ行ったことのない都市に関する計算
        if dist[vv] is None:
            # 初めて訪れた都市に、+1の時間を設定する。
            dist[vv] = dist[v] + 1
            # 初めて訪れた都市から、次の都市へ移動するための情報を格納する。
            que.append(vv)
            # 初めて訪れた都市へ移動できる道路の本数をメモしておく。一つ前の都市へ最短で行ける、道路数を参照できるようにするため。(動的計画法)
            cnt[vv] = cnt[v]
        # 都市と都市の間が1時間の時、常に最短経路であるため、その道路の本数を数える。
        # 1 -> 0のような方向に向かう経路は演算しない。
        elif dist[vv] == dist[v] + 1:
            cnt[vv] += cnt[v]
            # 10の9乗 + 7で割ることを忘れない。
            # 10の9乗 + 7以上の数値を答えとして扱わない。
            # 10の9乗 + 7は素数である。 ⏩ 10の9乗 + 7は、1と10の9乗 + 7以外で割り切れることのない値。 ⏩ 0 ~ 10の9乗 + 7以内に関して、あまりを計算しても答えに影響しない。
            cnt[vv] %= 10 ** 9 + 7

print(cnt[N - 1])
