import random
import math

# 定義部分
def random_int(min, max):
    return random.randrange(min, max)

def calculation_distance(x1, y1, x2, y2):
    # 二点間の距離を求める
    diff_x = x1 - x2
    diff_y = y1 - y2
    return math.sqrt(diff_x**2 + diff_y**2)

min = 0
max = 5

waterMelon_x = random_int(min, max)
waterMelon_y = random_int(min, max)

player_x = random_int(min, max)
player_y = random_int(min, max)

# 実装部分

while (waterMelon_x, waterMelon_y) == (player_x, player_y):
    player_x = random_int(min, max)
    player_y = random_int(min, max)

while (waterMelon_x != player_x) or (waterMelon_y != player_y):
    distance = calculation_distance(player_x, player_y, waterMelon_x, waterMelon_y)
    print("スイカまでの距離:", distance)

    user_input = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
    match user_input:
        case "n":
            player_y = player_y - 1
        case "s":
            player_y = player_y + 1
        case "e":
            player_x = player_x - 1
        case "w":
            player_x = player_x + 1

print("スイカが割れました！！")