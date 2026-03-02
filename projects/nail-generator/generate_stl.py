import struct
import math

def write_stl(filename, vertices_list):
    """写入二进制STL文件"""
    with open(filename, 'wb') as f:
        # 80字节头部
        f.write(b' ' * 80)
        # 三角面数量
        f.write(struct.pack('I', len(vertices_list)))
        # 写入每个三角面
        for verts in vertices_list:
            # 法向量（简化计算）
            normal = [0.0, 0.0, 1.0]
            f.write(struct.pack('3f', *normal))
            # 3个顶点
            for v in verts:
                f.write(struct.pack('3f', *v))
            # 属性字节计数
            f.write(struct.pack('H', 0))

def create_cylinder_triangles(radius, height, z_offset, segments=32):
    """创建圆柱体的三角面"""
    triangles = []
    
    # 顶面和底面中心点
    top_center = [0, 0, z_offset + height]
    bottom_center = [0, 0, z_offset]
    
    for i in range(segments):
        angle1 = 2 * math.pi * i / segments
        angle2 = 2 * math.pi * (i + 1) / segments
        
        x1 = radius * math.cos(angle1)
        y1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        y2 = radius * math.sin(angle2)
        
        # 顶面三角
        triangles.append([top_center, [x1, y1, z_offset + height], [x2, y2, z_offset + height]])
        # 底面三角
        triangles.append([bottom_center, [x2, y2, z_offset], [x1, y1, z_offset]])
        
        # 侧面（两个三角）
        v1 = [x1, y1, z_offset + height]
        v2 = [x2, y2, z_offset + height]
        v3 = [x1, y1, z_offset]
        v4 = [x2, y2, z_offset]
        
        triangles.append([v1, v2, v3])
        triangles.append([v2, v4, v3])
    
    return triangles

# 参数（单位：mm）
head_radius = 5.0      # 钉头半径10mm直径
head_height = 10.0     # 钉头高度
neck_radius = 4.0      # 环槽处半径8mm直径
shank_radius = 4.0     # 钉体半径8mm直径
shank_length = 3.0     # 钉体长度（用户指定3mm）

all_triangles = []

# 钉头（顶部圆盘，z: 0 到 10）
all_triangles.extend(create_cylinder_triangles(head_radius, head_height, 0))

# 环槽（收腰部分，z: -2 到 0）
all_triangles.extend(create_cylinder_triangles(neck_radius, 2, -2))

# 钉体（底部短圆柱，z: -5 到 -2，高度3mm）
all_triangles.extend(create_cylinder_triangles(shank_radius, shank_length, -shank_length-2))

# 写入文件
write_stl('/root/.openclaw/workspace/小钉子.stl', all_triangles)

print("✅ STL文件已生成：小钉子.stl")
print(f"📐 规格：")
print(f"   钉头：Ø10mm × 10mm高")
print(f"   环槽：Ø8mm（收腰）")
print(f"   钉体：Ø8mm × 3mm长")
print(f"   总高：15mm")
