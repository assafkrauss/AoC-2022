class SegmentCrusher:
    def __init__(self):
        self._segments = []

    def add_segment(self, a, b):
        self._segments.append((a, b))
        self._segments.sort(key=lambda segment: segment[0])
        i = 0
        while i < len(self._segments) - 1:
            if self._segments[i][1] >= self._segments[i + 1][0]:
                self._segments[i] = (self._segments[i][0], max(self._segments[i][1], self._segments[i + 1][1]))
                self._segments.remove(self._segments[i + 1])
            else:
                i += 1

    def remove_point(self, n):
        for i in range(len(self._segments)):
            if self._segments[i][0] > n:
                break
            if self._segments[i][1] < n:
                continue
            if self._segments[i][0] == n:
                self._segments[i] = (self._segments[i][0] + 1, self._segments[i][1])
                if self._segments[i][0] > self._segments[i][1]:
                    self._segments.remove(self._segments[i])
                break
            if self._segments[i][1] == n:
                self._segments[i] = (self._segments[i][0], self._segments[i][1] - 1)
                if self._segments[i][0] > self._segments[i][1]:
                    self._segments.remove(self._segments[i])
                break
            if self._segments[i][0] < n < self._segments[i][1]:
                temp = self._segments[i][1]
                self._segments[i] = (self._segments[i][0], n)
                self.add_segment(n, temp)
                break
            raise Exception("shouldn't have gotten this far")

    def count(self):
        total = 0
        for s in self._segments:
            total += s[1] - s[0] + 1
        return total


def distance(a, b):  # actually manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    f = open("day15.txt")
    lines = f.readlines()

    sensors_to_beacons = {}
    sensor_radius_dic = {}
    beacons = set()
    for line in lines:
        line_fragments = line.strip().split()
        sensor_x = int(line_fragments[2][2:-1])
        sensor_y = int(line_fragments[3][2:-1])
        beacon_x = int(line_fragments[8][2:-1])
        beacon_y = int(line_fragments[9][2:])
        beacons.add((beacon_x, beacon_y))
        sensors_to_beacons[(sensor_x, sensor_y)] = (beacon_x, beacon_y)

    for sensor in sensors_to_beacons:
        sensor_radius_dic[sensor] = distance(sensor, sensors_to_beacons[sensor])

    target_row = 2000000
    sc = SegmentCrusher()
    for sensor in sensor_radius_dic:
        move_on_x = sensor_radius_dic[sensor] - (abs(sensor[1] - target_row))
        if move_on_x < 0:
            continue
        min_x = sensor[0] - move_on_x
        max_x = sensor[0] + move_on_x
        sc.add_segment(min_x, max_x)
        for beacon in beacons:
            if beacon[1] == target_row and min_x <= beacon[0] <= max_x:
                sc.remove_point(beacon[0])

    print(sc.count())


if __name__ == '__main__':
    main()
