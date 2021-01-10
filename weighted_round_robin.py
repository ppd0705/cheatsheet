from typing import List


class ServerConfig:
    def __init__(self, addr: str, weight: int):
        self.addr: str = addr
        self.weight: int = weight
        self.cur_weight: int = 0

    def __repr__(self):
        return f"\n    [Server]addr:{self.addr}, weigh:{self.weight}, cur_weight:{self.cur_weight}"


class WeightedRoundRobin:
    def __init__(self):
        self.server_list: List[ServerConfig] = []

    def load_config(self, config):
        for addr, weight in config:
            self.server_list.append(
                ServerConfig(addr, weight)
            )

    def next_item(self) -> str:
        index = -1
        total = 0
        size = len(self.server_list)

        for i in range(size):
            self.server_list[i].cur_weight += self.server_list[i].weight
            total += self.server_list[i].weight

            if index == -1 or self.server_list[index].cur_weight < self.server_list[i].cur_weight:
                index = i
        self.server_list[index].cur_weight -= total
        print(self.server_list)
        return self.server_list[index].addr


def test():
    config = [
        ("192.168.0.1", 1),
        ("192.168.0.2", 2),
        ("192.168.0.3", 1),
    ]

    robin = WeightedRoundRobin()
    robin.load_config(config)

    for i in range(12):
        print(i, robin.next_item())


if __name__ == "__main__":
    test()
