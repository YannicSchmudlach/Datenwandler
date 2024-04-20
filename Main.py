import re


def read_file(file_path) -> None:
    first_time = True
    front_lin_x = 0
    front_lin_y = 0
    front_lin_z = 0
    with open(file_path) as f:
        for line in f:
            if line.startswith('LIN'):
                coordinates = re.findall(r'[-+]?(?:\d*\.*\d+)', line)
                x = float(coordinates[0])
                y = float(coordinates[1])
                z = float(coordinates[2])
                if first_time:
                    write_to_file_with_LIN(x, y, z)
                    first_time = False
                else:
                    write_to_file_with_LIN(round(front_lin_x - x, 3), round(front_lin_y - y, 3),
                                           round(front_lin_z - z, 3))
                front_lin_x = x
                front_lin_y = y
                front_lin_z = z
            else:
                write_to_file(line)


def write_to_file(line) -> None:
    with open('newFile', 'a') as file_to_write:
        file_to_write.write(line)


def write_to_file_with_LIN(x: float, y: float, z: float) -> None:
    x_str = '%.3f' % (x)
    y_str = '%.3f' % (y)
    z_str = '%.3f' % (z)
    with open('newFile', 'a') as file_to_write:
        file_to_write.write(
            "LIN {X " + x_str + ",Y " + y_str + ",Z " +
            z_str + "} C_DIS\n")


if __name__ == "__main__":
    read_file("input.txt")
