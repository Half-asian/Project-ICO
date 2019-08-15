import os
import sys

def open_file(file):
    with open(file, mode='rb') as file: # b is important -> binary
        content = file.read()
    return content
    
def get_file_size(file):
    st = os.stat(file)
    return st.st_size

def convert_to_big_endian(little_endian):
    return little_endian[6:8] + little_endian[4:6] + little_endian[2:4] + little_endian[0:2]

def convert_to_float32(byte4):
    mantissa_bits = byte4[9:]
    byte4 = int(byte4, 2)
    sign = (byte4 >> 31) & 0x01
    exponent = (byte4 >> 23) & 0xff
    mantissa = 1
    for i in range(23):
        if mantissa_bits[i] == '1':
            mantissa += 2 ** (-(i + 1))
    if sign == 1:
        decimal = -1 * mantissa * (2 ** (exponent - 127))
    else:
        decimal = mantissa * (2 ** (exponent - 127))
    return decimal

def convert_hex_to_binary32(hex32):
    binary32 = '00000000000000000000000000000000' + str(bin(int(hex32, 16)))[2:]
    return binary32[-32:]

def get_objectListEntryPointer(content):
    pointer = int(convert_to_big_endian(content[4:8].hex()), 16)
    return int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)

def getObjectList(content, pointer):
    pointer += 144
    objects = {}
    toVertexCoords = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    objects['ToVertexCoords'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 4
    objects['NumberofVertexCoords'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 12
    objects['ToNormalMappingList'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 4
    objects['NumberofNormalMappingEntries'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 12
    objects['ToTextureMappingList'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 4
    objects['NumberofTextureMappingEntries'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 12
    objects['ToColorMappingList'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 4
    objects['NumberofColorMappingEntries'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 12
    objects['ToTintMappingList'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 4
    objects['NumberofTintMappingEntries'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 12
    objects['ToTextureList'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 4
    objects['NumberofTextureEntries'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 28
    ToObjectFormationListSubPointer = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    objects['ToObjectFormationList'] = int(convert_to_big_endian(content[ToObjectFormationListSubPointer:ToObjectFormationListSubPointer + 4].hex()), 16)
    pointer += 4
    objects['NumberofObjectsToForm'] = int(convert_to_big_endian(content[pointer:pointer + 4].hex()), 16)
    pointer += 12
    return objects

def exportVertices(content, pointer, vertex_amount, vertex_type, size):
    for i in range(pointer, pointer + 16 * vertex_amount, 16):
        line_output = ""
        current_line = content[i:i+16].hex()
        current_line = [current_line[0:8], current_line[8:16], current_line[16:24], current_line[24:32]]
        for little_endian in current_line:
            decimal = convert_to_float32(convert_hex_to_binary32(convert_to_big_endian(little_endian)))
            line_output += str('{0:.5f}'.format(decimal / -10)) + " "
        if (size == 4):
            print(vertex_type, line_output[:-1])
        elif (size == 3):
            print(vertex_type, line_output[:-9])
        elif (size == 2):
            print(vertex_type, line_output[:-17])

def exportColorMaps(content, pointer, colour_amount):
    for i in range(pointer, pointer + 4 * colour_amount, 4):
        print('colour', int(content[i]), int(content[i + 1]), int(content[i + 2]))

def exportTintMaps(content, pointer, colour_amount):
    for i in range(pointer, pointer + 4 * colour_amount, 4):
        tint_red = 'tint_red ' + str(int(content[i])) + " " + str(int(content[i + 1])) + " " + str(int(content[i + 2]))
        tint_green = 'tint_green ' + str(int(content[i + 4])) + " " + str(int(content[i + 5])) + " " + str(int(content[i + 6]))
        tint_blue = 'tint_blue ' + str(int(content[i + 8])) + " " + str(int(content[i + 9])) + " " + str(int(content[i + 10]))
        floating_point_weight = convert_to_float32(convert_hex_to_binary32(convert_to_big_endian(content[i+12:i+16].hex())))
        print('tint', tint_red, tint_green, tint_blue, 'fpw', str('{0:.5f}'.format(floating_point_weight)))

def exportTextures(content, pointer, texture_amount):
    for i in range(pointer, pointer + 144 * texture_amount, 144):
        texture = content[i:i + 128]
        texture = str(texture.strip('\x00'.encode()))[2:]
        print('texture', texture)

def exportObjectFormations(content, pointer, objects_to_form, extra_vertex_count):
    size_of_sub_object = int(convert_to_big_endian(content[pointer:pointer + 1].hex()), 16)
    sub_object_pointer = pointer + 16
    while size_of_sub_object != 0:
        #print("subobject")
        object_vertexes = []
        for i in range(size_of_sub_object):
            #print(content[sub_object_pointer + 4:sub_object_pointer + 6].hex())
            vertex = int(convert_to_big_endian(content[sub_object_pointer + 4:sub_object_pointer + 6].hex()), 16)
            normal = int(convert_to_big_endian(content[sub_object_pointer + 6:sub_object_pointer + 7].hex()), 16)
            texturemap = int(convert_to_big_endian(content[sub_object_pointer + 8:sub_object_pointer + 9].hex()), 16)
            colour = int(convert_to_big_endian(content[sub_object_pointer + 10:sub_object_pointer + 11].hex()), 16)
            tint = int(convert_to_big_endian(content[sub_object_pointer + 12:sub_object_pointer + 13].hex()), 16)
            texture = int(convert_to_big_endian(content[sub_object_pointer + 14:sub_object_pointer + 15].hex()), 16)
            object_vertexes.append(vertex + 1 + extra_vertex_count)
            #print('f vertex', vertex, 'normal', normal, 'texturemap', texturemap, 'colour', colour, 'tint', tint, 'texture', texture)
            sub_object_pointer += 16
        #print(object_vertexes)
        while len(object_vertexes) != 3:
            print('f', object_vertexes[0], object_vertexes[1], object_vertexes[2])
            object_vertexes = object_vertexes[1:]
        print('f', object_vertexes[0], object_vertexes[1], object_vertexes[2])
        size_of_sub_object = int(convert_to_big_endian(content[sub_object_pointer:sub_object_pointer + 1].hex()), 16)
        sub_object_pointer += 16


file = sys.argv[1]
print(file)
file_size = get_file_size(file)
content = open_file(file)
objectListEntryPointer = get_objectListEntryPointer(content)
model_counter = 0
extra_vertex_count = 0
while objectListEntryPointer != 0:
    objects = getObjectList(content, objectListEntryPointer)
    exportVertices(content, objects['ToVertexCoords'], objects['NumberofVertexCoords'], 'v', 3)
    #exportVertices(content, objects['ToNormalMappingList'], objects['NumberofNormalMappingEntries'], 'vn', 3)
    exportVertices(content, objects['ToTextureMappingList'], objects['NumberofTextureMappingEntries'], 'vt', 2)
    #exportColorMaps(content, objects['ToColorMappingList'], objects['NumberofColorMappingEntries'])
    #exportTintMaps(content, objects['ToTintMappingList'], objects['NumberofTintMappingEntries'])
    #exportTextures(content, objects['ToTextureList'], objects['NumberofTextureEntries'])
    exportObjectFormations(content, objects['ToObjectFormationList'], objects['NumberofObjectsToForm'], extra_vertex_count)
    extra_vertex_count += objects['NumberofVertexCoords']
    model_counter += 1
    pointer = int(convert_to_big_endian(content[4:8].hex()), 16)
    objectListEntryPointer = int(convert_to_big_endian(content[pointer + (model_counter * 4):pointer + (model_counter * 4) + 4].hex()), 16)


