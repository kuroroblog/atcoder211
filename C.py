# 検証用文字列
# 番兵用に先頭文字列へ空白を挿入する。 ⏩ リストのエラー防止にもつながる。
# 番兵とは? : https://www.weblio.jp/content/%E7%95%AA%E5%85%B5
inspectionStr = ' chokudai'

# 標準入力を受け付ける。
S = input()
# 番兵用に先頭文字列へ空白を挿入する。 ⏩ リストのエラー防止にもつながる。
# 番兵とは? : https://www.weblio.jp/content/%E7%95%AA%E5%85%B5
S = ' ' + S

Slen = len(S)
inspectionStrLen = len(inspectionStr)

# 動的計画法を利用するための、配列の初期化を行う。
# 動的計画法とは? : https://www.momoyama-usagi.com/entry/info-algo-dp
dp = [[0 for _ in range(0, Slen)] for _ in range(0, inspectionStrLen)]
for j in range(0, Slen):
    # 番兵行の値を設定する。
    dp[0][j] = 1

# 参考 : https://www.youtube.com/watch?v=Zu9S_kJ-7tk
for i in range(0, inspectionStrLen):
    for j in range(0, Slen):
        if S[j] == inspectionStr[i]:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i][j - 1]

# 10の9乗 + 7で割ることを忘れない。
# 10の9乗 + 7以上の数値を答えとして扱わない。
# 10の9乗 + 7は素数である。 ⏩ 10の9乗 + 7は、1と10の9乗 + 7以外で割り切れることのない値。 ⏩ 0 ~ 10の9乗 + 7以内に関して、あまりを計算しても答えに影響しない。
print(dp[inspectionStrLen - 1][Slen - 1] % (10 ** 9 + 7))
