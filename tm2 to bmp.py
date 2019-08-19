#TM2 to bitmap
import sys
import os

def exportColourMap(content, file_size, colour_bits, f_write):
    print(colour_bits)
    if colour_bits == '04':
        for i in range(64, 0, -4):
            current_colour = content[file_size - i:file_size - i + 4].hex()
            current_colour = current_colour[4:6] + current_colour[2:4] + current_colour[0:2] + '00'
            binary = bytearray.fromhex(current_colour)
            f_write.write(binary)
    elif colour_bits == '08':
        print('ya')
        for i in range(1024, 0, -4):
            current_colour = content[file_size - i:file_size - i + 4].hex()
            current_colour = current_colour[4:6] + current_colour[2:4] + current_colour[0:2] + '00'
            binary = bytearray.fromhex(current_colour)
            f_write.write(binary)
            
def export4BitColours(content, file_size, f_write, y_count):
    print("y",y_count)
    #for y in range(int(file_size / 16) - 16, -1, -1):
    #    print(hex(y * 16 + 64))
     #   l = content[(y * 16 + 64):(y * 16 + 80)].hex()
        #l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
         #   f_write.write(bytearray.fromhex(l))
    if y_count == 64:
        for y in range(file_size - 64, 104, -64):
            l = content[(y - 32): y + 16].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 16):y].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 64):y + 48].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 48):y + 32].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
        
    elif y_count == 128:
        for y in range(file_size - 64, 104, -128):
            l = content[(y - 64): y + 48].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 48): y + 32].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 32): y + 16].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 16): y + 0].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 128): y + 112].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 112): y + 96].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 96): y + 80].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 80): y + 64].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
    
def export8BitColours(content, file_size, f_write, y_count):
    for y in range(file_size - 1024, 104, -16):
        l = content[(y - 2):y].hex()
        #f_write.write(bytearray.fromhex(l))

if (len(sys.argv) != 2):
    print("Please provide a tm2 file")
    sys.exit()

file = sys.argv[1]
with open(file, mode='rb') as file: # b is important -> binary
    content = file.read()
file_size = os.path.getsize(sys.argv[1])



tex_name = sys.argv[1][:-4]

tex_width = content[int('24', 16):int('26', 16)].hex()
print(tex_width)
tex_width = tex_width[2:4] + tex_width[0:2]

tex_height = content[int('26', 16):int('28', 16)].hex()
tex_height = tex_height[2:4] + tex_height[0:2]



if content[int('1e', 16):int('20', 16)].hex() == '0001' and content[int('28', 16):int('2c', 16)].hex() == '000030dd':
    bits_per_pixel = '8'
    bits_per_pixel = ('00' + bits_per_pixel)[-2:]
    f_write = open(tex_name + '.bmp', mode='wb')
    f_write.write(b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x28\x00')
    line_2 = '0000' + tex_width[2:4] + tex_width[0:2] + '0000' + tex_width[2:4] + tex_width[0:2]  + '00000100' + bits_per_pixel + '000000'
    f_write.write(bytearray.fromhex(line_2))
    f_write.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f_write.write(b'\x00\x00\x00\x00\x00\x00')

    exportColourMap(content, file_size, bits_per_pixel, f_write)
    export8BitColours(content, file_size, f_write, int(tex_height, 16))
    
    f_write.flush()
    with open(tex_name + '.bmp', mode='rb') as file: # b is important -> binary
        content_2 = file.read()
    file_length = ("0000" + (hex(len(content_2))[2:]))[-4:]
    print("f_length", file_length)
    #f_write = open(tex_name + '.bmp', mode='wb')
    f_write.seek(2)
    f_write.write(bytearray.fromhex(file_length[2:] + file_length[:2]))
    

elif content[int('1e', 16):int('20', 16)].hex() == '1000' and content[int('2a', 16):int('2b', 16)].hex() == '40':
    bits_per_pixel = '4'
    bits_per_pixel = ('00' + bits_per_pixel)[-2:]
    f_write = open(tex_name + '.bmp', mode='wb')
    f_write.write(b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00\x76\x00\x00\x00\x28\x00')
    line_2 = '0000' + tex_width[2:4] + tex_width[0:2] + '0000' + tex_width[2:4] + tex_width[0:2]  + '00000100' + bits_per_pixel + '000000'
    f_write.write(bytearray.fromhex(line_2))
    f_write.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00')
    f_write.write(b'\x00\x00\x10\x00\x00\x00')
    exportColourMap(content, file_size, bits_per_pixel, f_write)
    export4BitColours(content, file_size, f_write, int(tex_height, 16))
    #f_write.close()
    f_write.flush()
    with open(tex_name + '.bmp', mode='rb') as file: # b is important -> binary
        content_2 = file.read()
    file_length = ("0000" + (hex(len(content_2))[2:]))[-4:]
    print("f_length", file_length)
    #f_write = open(tex_name + '.bmp', mode='wb')
    f_write.seek(2)
    f_write.write(bytearray.fromhex(file_length[2:] + file_length[:2]))
    
else:
    print("unknown bits per pixel")
    sys.exit()
    

