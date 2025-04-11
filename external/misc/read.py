import struct

ENTRY_SIZE = (
    1 +  # requirements (1 byte)
    1 +  # padding (1 byte)
    2 +  # angle (2 bytes)
    4 * 3 +  # pos (3 floats)
    4 * 3 +  # cam pos (3 floats)
    4 * 3 +  # cam target (3 floats)
    4 +  # counter (4 bytes)
    32 +  # filename (32 bytes, ASCII)
    4  # padding (4 bytes)
)

def read_entries(path):
    with open(path, 'rb') as f:
        while True:
            data = f.read(ENTRY_SIZE)
            if not data:
                break

            # Unpack the binary data
            requirements = struct.unpack('>B', data[0:1])[0]
            angle = struct.unpack('>H', data[2:4])[0]
            pos = struct.unpack('>fff', data[4:16])
            cam_pos = struct.unpack('>fff', data[16:28])
            cam_target = struct.unpack('>fff', data[28:40])
            counter = struct.unpack('>I', data[40:44])[0]
            filename = struct.unpack('>32s', data[44:76])[0].decode('ascii').strip('\x00')

            print(f"{filename}:")
            print(f"  Requirements: {requirements}")
            print(f"  Angle: {angle}")
            print(f"  Position: {pos}")
            print(f"  Camera Pos: {cam_pos}")
            print(f"  Camera Target: {cam_target}")
            print(f"  Counter: {counter}")
            print()

read_entries('any_bite.bin')