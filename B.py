# H, 2B, 3B, HRのリストを作成する。
sList = [
    'H',
    '2B',
    '3B',
    'HR',
]

inputList = []

# 標準入力を受け付ける。
inputList.append(input())
inputList.append(input())
inputList.append(input())
inputList.append(input())

for i in range(0, len(inputList)):
    # 上記で作成したリスト内に含まれるか確かめる。
    if inputList[i] in sList:
        # リスト内にsiが含まれれば、リストからsiを削除する。
        # remove関数参考 : https://note.nkmk.me/python-list-clear-pop-remove-del/
        sList.remove(inputList[i])

# リスト内に値が残っている場合、Yes, そうでない場合Noとする。
if len(sList) == 0:
    print('Yes')
else:
    print('No')
