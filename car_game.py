import time
import os
import msvcrt

class Car:
    def __init__(self):
        self.position = 10
        self.track_width = 20
        
    def move_left(self):
        if self.position > 0:
            self.position -= 1
            
    def move_right(self):
        if self.position < self.track_width - 1:
            self.position += 1
    
    def draw(self):
        road = [' '] * self.track_width
        road[self.position] = '>' # 使用 > 表示汽车
        return '|' + ''.join(road) + '|'

def main():
    car = Car()
    
    print("使用 'a' 向左移动，'d' 向右移动，按 'q' 退出游戏")
    
    while True:
        # 清屏
        os.system('cls')
        
        # 显示赛道和汽车
        print('\n' * 3)
        print(car.draw())
        
        # 检测按键
        if msvcrt.kbhit():
            key = msvcrt.getch()  # 不需要 lower()
            if key == b'a':
                car.move_left()
            elif key == b'd':
                car.move_right()
            elif key == b'q':
                print("游戏结束！")
                break
            
        time.sleep(0.1)

if __name__ == '__main__':
    main()