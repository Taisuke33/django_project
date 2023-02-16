from sidearm import HandGun
from mainweapon import Assault
from armor import Armor
from agent import Agent

#合計12マッチ
match_count = 12

#エージェント、スキル
agent1 = Agent(
    "フェニックス", [
    {"name": "カーブボール", "price": 250, "maxlimit": 2,},
    {"name": "ホットハンド", "price": 0, "maxlimit": 1,},
    {"name": "ブレイズ", "price": 150, "maxlimit": 1,},
])
agent2 = Agent(
    "ジェット", [
    {"name": "アップドラフト", "price": 150, "maxlimit": 2,},
    {"name": "テイルウィンド", "price": 0, "maxlimit": 1,},
    {"name": "クラウドバースト", "price": 200, "maxlimit": 2,},    
])
agent3 = Agent(
    "ネオン", [
    {"name": "リレーボルト", "price": 200, "maxlimit": 2},
    {"name": "ハイギア", "price": 0, "maxlimit": 1},
    {"name": "ファストレーン", "price": 300, "maxlimit": 1},
])
agent4 =Agent(
    "ヨル", [
    {"name": "ブラインドサイド", "price": 250, "maxlimit": 2},
    {"name": "ゲートクラッシュ", "price": 150, "maxlimit": 1},
    {"name": "フェイクアウト", "price": 100, "maxlimit": 1},
]) 
agent5 = Agent(
    "レイズ", [
    {"name": "ブラストパック", "price": 200, "maxlimit": 2},
    {"name": "ペイント弾", "price": 0, "maxlimit": 1},
    {"name": "ブームボット", "price": 300, "maxlimit": 1},
])
agent6 = Agent(
    "レイナ", [
    {"name": "デバウアー", "price": 200, "maxlimit": 1},
    {"name": "ディスミス", "price": 0, "maxlimit": 1},
    {"name": "リーア", "price": 250, "maxlimit": 2},
])
agent7 = Agent(
    "セージ", [
    {"name": "スロウオーブ", "price": 200, "maxlimit": 2},
    {"name": "ヒーリングオーブ", "price": 0, "maxlimit": 1},
    {"name": "バリアオーブ", "price": 400, "maxlimit": 1},
])
agent8 = Agent(
    "キルジョイ", [
    {"name": "アラームボット", "price": 200, "maxlimit": 1},
    {"name": "タレット", "price": 0, "maxlimit": 1},
    {"name": "ナノスワーム", "price": 200, "maxlimit": 2},
])
agent9 = Agent(
    "サイファー", [
    {"name": "サイバーゲージ", "price":100, "maxlimit": 2},
    {"name": "スパイカメラ", "price": 0, "maxlimit": 1},
    {"name": "トラップワイヤー", "price": 200, "maxlimit": 2},
])
agent10 = Agent(
    "チェンバー", [
    {"name": "ヘッドハンター", "price": 150, "maxlimit": 8},
    {"name": "ランデヴー", "price": 0, "maxlimit": 1},
    {"name": "トレードマーク", "price": 200, "maxlimit": 1},
])
agent11 = Agent(
    "ソーヴァ", [
    {"name": "ショックボルト", "price": 150, "maxlimit": 2},
    {"name": "リコンボルト", "price": 0, "maxlimit": 1},
    {"name": "オウルドローン", "price": 400, "maxlimit": 1},
])
agent12 = Agent(
    "KAY/O", [
    {"name": "フラッシュ/ドライブ", "price": 250, "maxlimit": 2},
    {"name": "ゼロ/ポイント", "price": 0, "maxlimit": 1},
    {"name": "フラグ/メント", "price": 200, "maxlimit": 1},
])
agent13 = Agent(
    "スカイ", [
    {"name": "トレイルブレーザー", "price": 300, "maxlimit": 1},
    {"name": "ガイディングライト", "price": 250, "maxlimit": 1},
    {"name": "リグロウス", "price": 150, "maxlimit": 1},
])
agent14 = Agent(
    "フェイド", [
    {"name": "シーズ", "price": 200, "maxlimit": 1},
    {"name": "ホウント", "price": 0, "maxlimit": 1},
    {"name": "プラウラー", "price": 250, "maxlimit": 2},
])
agent15 = Agent(
    "ブリーチ", [
    {"name": "フラッシュポイント", "price": 250, "maxlimit": 2},
    {"name": "フォールトライン", "price": 0, "maxlimit": 1},
    {"name": "アフターショック", "price": 200, "maxlimit": 1},
])
agent16 = Agent(
    "ブリムストーン", [
    {"name": "インセンティアリー", "price": 250, "maxlimit": 2},
    {"name": "スカイスモーク", "price": 100, "maxlimit": 2},
    {"name": "スティムビーコン", "price": 200, "maxlimit": 1},
])
agent17 = Agent(
    "アストラ", [
    {"name": "ノヴァパルス", "price": 0, "maxlimit": 1},
    {"name": "ネビュラ/ディシペイト", "price": 0, "maxlimit": 2},
    {"name": "グラビティウェル", "price": 0, "maxlimit": 1},
])
agent18 = Agent(
    "ヴァイパー", [
    {"name": "ポイズンクラウド", "price": 200, "maxlimit": 1},
    {"name": "トキシックスクリーン", "price": 0, "maxlimit": 1},
    {"name": "スネークバイト", "price": 200, "maxlimit": 2},
])
agent19 = Agent(
    "オーメン", [
    {"name": "パラノイア", "price": 250, "maxlimit": 2},
    {"name": "ダークカバー", "price": 150, "maxlimit": 1},
    {"name": "シュラウドステップ", "price": 100, "maxlimit": 2},
])
agent20 = Agent(
    "ハーバー", [
    {"name": "コーヴ", "price": 350, "maxlimit": 1},
    {"name": "ハイタイド", "price": 0, "maxlimit": 1},
    {"name": "カスケード", "price": 150, "maxlimit": 2},
])
agents = [agent1, agent2,agent3, agent4, agent5, agent6, agent7, agent8, agent9, agent10, agent11, agent12, agent13, agent14, agent15, agent16, agent17, agent18, agent19, agent20, ]

#サイド武器
handgun1 = HandGun("クラシック", 0)
handgun2 = HandGun("ショーティー", 150)
handgun3 = HandGun("フレンジー", 450)
handgun4 = HandGun("ゴースト", 500)
handgun5 = HandGun("シェリフ", 800)

handguns = [handgun1, handgun2, handgun3, handgun4, handgun5]

#メイン武器
assault1 = Assault("スティンガー", 950)
assault2 = Assault("スペクター", 1600)
assault3 = Assault("バッキー", 850)
assault4 = Assault("ジャッジ", 1850)
assault5 = Assault("ブルドッグ", 2050)
assault6 = Assault("ガーディアン", 2250)
assault7 = Assault("ファントム", 2900)
assault8 = Assault("ヴァンダル", 2900)
assault9 = Assault("マーシャル", 950)
assault10 = Assault("オペレーター", 4700)
assault11 = Assault("アレス", 1600)
assault12 = Assault("オーディン", 3200)

assaults = [assault1, assault2, assault3, assault4, assault5, assault6, assault7, assault8, assault9, 
assault10, assault11, assault12]

#アーマー
armor1 = Armor("ライトアーマー", 400)
armor2 = Armor("ヘヴィーアーマー", 1000)

armors = [armor1, armor2]

print("エージェント")
index = 1
for agent in agents:
    print(str(index) + '.' + agent.name)
    index += 1

print('--------------------')

print("サイドアーム")
index = 1
for handgun in handguns:
    print(str(index) + '.' + handgun.info())
    index += 1

print('--------------------')

print("メインウェポン")
index = 1
for assault in assaults:
    print(str(index) + '.' + assault.info())
    index += 1

print('--------------------')

print("アーマー")
index = 1
for armor in armors:
    print(str(index) + '.' + armor.info())
    index += 1

print('--------------------')

#選択したエージェントは1試合の中では変更できないので1マッチ目のみ選択画面を表示
selected_agent = None

for match in range(0, match_count):
    print(
        "現在%sマッチ目です。"%str(match +1)
    )
    if match == 0:

        agent_selected = False
    
        selected_agent = agents[int(input("エージェントを選択してください: ")) -1]
    
    skill_selected = False

    purchased_skills = {}
    #スキルの個数に制限があるためpurchased_skillをオブジェクト化
    while not skill_selected:
        print(selected_agent.name + "のスキル一覧")
        index = 1
        for skill in selected_agent.skills:
            print(str(index) + "." + skill["name"] + ': □' + str(skill["price"]))
            index += 1

        selected_skill = input("スキルを選択してください: ")

        #Enterを押せばループ終了
        if selected_skill == "":
            skill_selected = True
        else:
            selected_skill = selected_agent.skills[int(selected_skill) -1]

            if selected_skill["name"] in purchased_skills:
                duplicated_skill = purchased_skills[selected_skill["name"]]
                #if~in構文にはin~の中に要素が入っているかを確認することができる
                #入っていればTrueで処理され複製されたデータを作り比較することができる
                if duplicated_skill["qty"] == selected_skill["maxlimit"]:
                    print("%s個以上は購入できません"%selected_skill["maxlimit"])
                    #%sはstr、 %iはint ""の外に%intなどの値をつけた見やすくできる
                else:
                    purchased_skills[selected_skill["name"]]["qty"] += 1
            else:
                purchased_skills[selected_skill["name"]] = {
                    "name": selected_skill["name"],
                    "qty": 1,
                    #"qty"というデータを複製した物に追加することができる
                    "price": selected_skill["price"] 
                }

    total_skill_price = 0
    for item in purchased_skills.values():
        total_skill_price += item["price"] * item["qty"]
        #オブジェクト{}のループは値の場合.values()で抽出可能
        #strの場合keys()でループすることができる
        #参照：https://note.nkmk.me/python-dict-keys-values-items/

#武器選択
    selected_sidearm = handguns[int(input('サイドアームを選択: ')) -1]

    selected_mainweapon = assaults[int(input('メインウェポンを選択: ')) -1]

    #アーマー選択
    armor_buy = int(input('アーマーを選択: ')) -1
    selected_armor = armors[armor_buy]

    result = selected_sidearm.price + selected_mainweapon.price + selected_armor.price + total_skill_price

    print('必要クレジットは' + str(result) + 'です。')