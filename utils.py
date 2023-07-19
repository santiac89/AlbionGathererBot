class Utils:
    @staticmethod
    def calculate_closest_point(p1, points):
        closest_distance = 9999

        for point in points:
            tmp = Utils.distance_between_points((p1[0], p1[1]), (point[0], point[1]))

            if tmp < closest_distance:
                closest_distance = tmp
                closest_x, closest_y = point[0], point[1]

        return closest_x, closest_y

    @staticmethod
    def distance_between_points(p1, p2):
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
