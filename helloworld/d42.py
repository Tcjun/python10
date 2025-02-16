class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name} 占地 {self.area: .2f} 平方米."

    def __del__(self):
        print(f"{self.name} is being removed from the house.")


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 初始化房屋剩余面积
        self.remaining_area = area

        # 初始化房屋内的物品列表
        self.items_list = []

    def add_item(self, item: HouseItem):
        if item.area <= self.remaining_area:
            self.items_list.append(item)
            self.remaining_area -= item.area
            print(f"{item.name} has been added to the house.")
        else:
            print(f"房屋剩余面积不足，无法添加 {item.name}。")

    def remove_item(self, item_name):
        for item in self.items_list:
            if item.name == item_name:
                self.items_list.remove(item)
                self.remaining_area += item.area
                print(f"{item_name} has been removed from the house.")
                return
        print(f"{item_name} 不在房屋内。")

    def __str__(self):
        items_str = "\n".join([str(item) for item in self.items_list])
        return (
            f"房屋类型：{self.house_type}\n"
            f"房屋面积：{self.area: .2f} 平方米\n"
            f"房屋剩余面积：{self.remaining_area: .2f} 平方米\n"
            f"房屋内物品：\n"
            f"{items_str}"
        )

    def __del__(self):
        print(f"{self.house_type} 房屋已被销毁。")


house = House("平房", 100)
print(house)

bed = HouseItem("床", 20)
table = HouseItem("桌子", 10)

house.add_item(bed)
house.add_item(table)
print(house)
