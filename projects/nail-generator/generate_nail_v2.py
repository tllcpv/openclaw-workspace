import struct
import math

def write_stl(filename, vertices_list):
    """写入二进制STL文件"""
    with open(filename, 'wb') as f:
        f.write(b' ' * 80)
        f.write(struct.pack('I', len(vertices_list)))
        for verts in vertices_list:
            normal = [0.0, 0.0, 1.0]
            f.write(struct.pack('3f', *normal))
            for v in verts:
                f.write(struct.pack('3f', *v))
            f.write(struct.pack('H', 0))

def create_cylinder_triangles(radius, height, z_offset, segments=32):
    """创建圆柱体的三角面"""
    triangles = []
    top_center = [0, 0, z_offset + height]
    bottom_center = [0, 0, z_offset]
    
    for i in range(segments):
        angle1 = 2 * math.pi * i / segments
        angle2 = 2 * math.pi * (i + 1) / segments
        
        x1 = radius * math.cos(angle1)
        y1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        y2 = radius * math.sin(angle2)
        
        triangles.append([top_center, [x1, y1, z_offset + height], [x2, y2, z_offset + height]])
        triangles.append([bottom_center, [x2, y2, z_offset], [x1, y1, z_offset]])
        
        v1 = [x1, y1, z_offset + height]
        v2 = [x2, y2, z_offset + height]
        v3 = [x1, y1, z_offset]
        v4 = [x2, y2, z_offset]
        
        triangles.append([v1, v2, v3])
        triangles.append([v2, v4, v3])
    
    return triangles

def create_cone_triangles(base_radius, height, z_offset, segments=32):
    """创建圆锥体的三角面（尖头）"""
    triangles = []
    tip = [0, 0, z_offset - height]
    base_center = [0, 0, z_offset]
    
    for i in range(segments):
        angle1 = 2 * math.pi * i / segments
        angle2 = 2 * math.pi * (i + 1) / segments
        
        x1 = base_radius * math.cos(angle1)
        y1 = base_radius * math.sin(angle1)
        x2 = base_radius * math.cos(angle2)
        y2 = base_radius * math.sin(angle2)
        
        v1 = [x1, y1, z_offset]
        v2 = [x2, y2, z_offset]
        v3 = tip
        
        triangles.append([v1, v2, v3])
        triangles.append([base_center, [x2, y2, z_offset], [x1, y1, z_offset]])
    
    return triangles

# 参数（单位：mm）
head_radius = 5.0       # 钉头半径10mm直径
head_height = 10.0      # 钉头高度
neck_radius = 4.0       # 环槽处半径8mm直径
shank_radius = 1.5      # 钉体半径（3mm直径）
shank_length = 20.0     # 钉体长度20mm
tip_length = 4.0        # 尖头长度

all_triangles = []

# 钉头（z: 20 到 30）- 放在顶部
all_triangles.extend(create_cylinder_triangles(head_radius, head_height, shank_length))

# 环槽（z: 18 到 20）
all_triangles.extend(create_cylinder_triangles(neck_radius, 2, shank_length - 2))

# 钉体圆柱部分（z: -2 到 18，长度20mm）
all_triangles.extend(create_cylinder_triangles(shank_radius, shank_length, -2))

# 尖头圆锥部分（从z=-2到z=-6）
all_triangles.extend(create_cone_triangles(shank_radius, tip_length, -2))

# 写入文件
write_stl('/root/.openclaw/workspace/小钉子_细长带尖.stl', all_triangles)

print("✅ STL文件已生成：小钉子_细长带尖.stl")
print(f"📐 规格：")
print(f"   钉头：Ø10mm × 10mm高")
print(f"   环槽：Ø8mm（收腰）")
print(f"   钉体：Ø3mm × 20mm长")
print(f"   尖头：4mm长")
print(f"   总高：34mm")
