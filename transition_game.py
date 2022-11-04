import random
import math

# 定義部分
def generate_position(size):
    x = random.randrange(0, 5)
    y = random.randrange(0, 5)

    return (x, y)

def calculation_distance(position1, position2):
    # 二点間の距離を求める
    diff_x = position1[0] - position2[0]
    diff_y = position1[1] - position2[1]
    return math.sqrt(diff_x**2 + diff_y**2)

def move_position(direction, position):
    current_x, current_y = position

    match user_input:
        case "n":
            current_y = current_y - 1
        case "s":
            current_y = current_y + 1
        case "e":
            current_x = current_x - 1
        case "w":
            current_x = current_x + 1

    return (current_x, current_y)

BAORD_SIZE = 5

watermelon_position = generate_position(BAORD_SIZE)
print("スイカ初期位置：", watermelon_position)

player_position = generate_position(BAORD_SIZE)
print("プレイヤー初期位置：", player_position)

# 実装部分

while watermelon_position == player_position:
    player_position = generate_position(BAORD_SIZE)
    print("スイカと同じ位置だったので、プレイヤーの場所を変更しました：", watermelon_position)

while watermelon_position != player_position:
    distance = calculation_distance(player_position, watermelon_position)
    print("スイカまでの距離:", distance)

    user_input = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
    player_position = move_position(user_input, player_position)

print("スイカが割れました！！")