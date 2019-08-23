#TM2 to bitmap
import sys
import os

def exportColourMap(content, file_size, colour_bits, f_write, entry_point):
    if colour_bits == '04':
        for i in range(64, 0, -4):
            current_colour = content[entry_point - i:entry_point - i + 4].hex()
            current_colour = current_colour[4:6] + current_colour[2:4] + current_colour[0:2] + '00'
            binary = bytearray.fromhex(current_colour)
            f_write.write(binary)
    elif colour_bits == '08':
        for chunk in range(1024, 0, -128): #8 x 128 bit chunks
            block1 = content[file_size - chunk:file_size - chunk + 32].hex()
            block2 = content[file_size - chunk + 32:file_size - chunk + 64].hex()
            block3 = content[file_size - chunk + 64:file_size - chunk + 96].hex()
            block4 = content[file_size - chunk + 96:file_size - chunk + 128].hex()

            for colour in range(0, 64, 8): #block1
                binary = block1[colour + 4:colour + 6] + block1[colour + 2:colour + 4] + block1[colour:colour + 2] + '00'
                binary = bytearray.fromhex(binary)
                f_write.write(binary)
            for colour in range(0, 64, 8): #block3
                binary = block3[colour + 4:colour + 6] + block3[colour + 2:colour + 4] + block3[colour:colour + 2] + '00'
                binary = bytearray.fromhex(binary)
                f_write.write(binary)
            for colour in range(0, 64, 8): #block2
                binary = block2[colour + 4:colour + 6] + block2[colour + 2:colour + 4] + block2[colour:colour + 2] + '00'
                binary = bytearray.fromhex(binary)
                f_write.write(binary)
            for colour in range(0, 64, 8): #block4
                binary = block4[colour + 4:colour + 6] + block4[colour + 2:colour + 4] + block4[colour:colour + 2] + '00'
                binary = bytearray.fromhex(binary)
                f_write.write(binary)             
             
def export4BitColours(content, file_size, f_write, y_count, x_count, entry_point):
    if y_count == 32 and x_count == 64:
        for y in range(file_size - 64, 88, -32):
            l = content[(y - 16): y].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
            l = content[(y - 32):y + 16].hex()
            l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
            f_write.write(bytearray.fromhex(l))
    if y_count == 64 and x_count == 64:
        for y in range(file_size - 64, 88, -64):
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
            
    elif y_count == 64 and x_count == 128:
        print(entry_point)
        buffer = content[entry_point:entry_point + 4096]
        print(len(buffer))
        for x in range(32):
            offset = len(buffer) - 128 - (x * 128)
            block_1 = buffer[offset + 64: offset + 80].hex()
            block_2 = buffer[offset + 80: offset + 96].hex()
            block_3 = buffer[offset + 96: offset + 112].hex()
            block_4 = buffer[offset + 112: offset + 128].hex()
            block_5 = buffer[offset: offset + 16].hex()
            block_6 = buffer[offset + 16: offset + 32].hex()
            block_7 = buffer[offset + 32: offset + 48].hex()
            block_8 = buffer[offset + 48: offset + 64].hex()
            blocks = [block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8]

            for i in blocks:    
                l = i
                l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
                f_write.write(bytearray.fromhex(l))
        
    elif y_count == 128 and x_count == 128:
        buffer = content[96:8288]
        print(len(buffer))
        for x in range(64):
            offset = 8064 - (x * 128)
            block_1 = buffer[offset + 64: offset + 80].hex()
            block_2 = buffer[offset + 80: offset + 96].hex()
            block_3 = buffer[offset + 96: offset + 112].hex()
            block_4 = buffer[offset + 112: offset + 128].hex()
            block_5 = buffer[offset: offset + 16].hex()
            block_6 = buffer[offset + 16: offset + 32].hex()
            block_7 = buffer[offset + 32: offset + 48].hex()
            block_8 = buffer[offset + 48: offset + 64].hex()
            blocks = [block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8]

            for i in blocks:    
                l = i
                l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
                f_write.write(bytearray.fromhex(l))
                
    elif y_count == 256 and x_count == 256:
        print(entry_point)
        buffer = content[entry_point:32768 + entry_point]
        print(len(buffer))
        #if len(buffer) != 32768:
            #buffer = content[1buffer28:32896]
        for x in range(128):
            offset = 32512 - (x * 256)
            block_13 = buffer[offset + 64: offset + 80].hex()
            block_14 = buffer[offset + 80: offset + 96].hex()
            block_15 = buffer[offset + 96: offset + 112].hex()
            block_16 = buffer[offset + 112: offset + 128].hex()
            
            block_1 = buffer[offset + 128: offset + 144].hex()
            block_2 = buffer[offset + 144: offset + 160].hex()
            block_3 = buffer[offset + 160: offset + 176].hex()
            block_4 = buffer[offset + 176: offset + 192].hex()
            
            block_9 = buffer[offset: offset + 16].hex()
            block_10 = buffer[offset + 16: offset + 32].hex()
            block_11 = buffer[offset + 32: offset + 48].hex()
            block_12 = buffer[offset + 48: offset + 64].hex()
            
            block_5 = buffer[offset + 192: offset + 208].hex()
            block_6 = buffer[offset + 208: offset + 224].hex()
            block_7 = buffer[offset + 224: offset + 240].hex()
            block_8 = buffer[offset + 240: offset + 256].hex()

            blocks = [block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9, block_10, block_11, block_12, block_13, block_14, block_15, block_16]

            for i in blocks:    
                l = i
                l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
                f_write.write(bytearray.fromhex(l))
                
    elif y_count == 128 and x_count == 256:
        print(entry_point)
        buffer = content[entry_point:entry_point + 16384]
        print(len(buffer))
        for x in range(64):
            offset = len(buffer) - 256 - (x * 256)
            block_13 = buffer[offset + 64: offset + 80].hex()
            block_14 = buffer[offset + 80: offset + 96].hex()
            block_15 = buffer[offset + 96: offset + 112].hex()
            block_16 = buffer[offset + 112: offset + 128].hex()
            
            block_1 = buffer[offset + 128: offset + 144].hex()
            block_2 = buffer[offset + 144: offset + 160].hex()
            block_3 = buffer[offset + 160: offset + 176].hex()
            block_4 = buffer[offset + 176: offset + 192].hex()
            
            block_9 = buffer[offset: offset + 16].hex()
            block_10 = buffer[offset + 16: offset + 32].hex()
            block_11 = buffer[offset + 32: offset + 48].hex()
            block_12 = buffer[offset + 48: offset + 64].hex()
            
            block_5 = buffer[offset + 192: offset + 208].hex()
            block_6 = buffer[offset + 208: offset + 224].hex()
            block_7 = buffer[offset + 224: offset + 240].hex()
            block_8 = buffer[offset + 240: offset + 256].hex()

            blocks = [block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9, block_10, block_11, block_12, block_13, block_14, block_15, block_16]

            for i in blocks:    
                l = i
                l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
                f_write.write(bytearray.fromhex(l))
        

    else:
        print("Y length:", y_count)
        print("X length:", x_count)


                
def export8BitColours(content, file_size, f_write, y_count, x_count):
    print("Y length:", y_count)
    print("X length:", x_count)

    for y in range(file_size - 1088, 0, -64): #128 x 128 renders correctly, everything else needs buffers
        l = content[y:y + 16].hex()
        f_write.write(bytearray.fromhex(l))
        l = content[y + 16:y + 32].hex()
        f_write.write(bytearray.fromhex(l))
        l = content[y + 32:y + 48].hex()
        f_write.write(bytearray.fromhex(l))
        l = content[y + 48:y + 64].hex()
        f_write.write(bytearray.fromhex(l))


def main():
    f = 'op_tsuta.tm2'
    with open(f, mode='rb') as file:
        content = file.read()
    file_size = os.path.getsize(f)
    tex_name = f[:-4]


    tex_width = content[int('24', 16):int('26', 16)].hex()
    tex_width = tex_width[2:4] + tex_width[0:2]

    tex_height = content[int('26', 16):int('28', 16)].hex()
    tex_height = tex_height[2:4] + tex_height[0:2]



    if content[int('1e', 16):int('20', 16)].hex() == '0001' and content[int('2a', 16):int('2b', 16)].hex() == '30':
        bits_per_pixel = '8'
        print("8 bit")
        bits_per_pixel = ('00' + bits_per_pixel)[-2:]
        f_write = open(tex_name + '.bmp', mode='wb')
        f_write.write(b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00\x36\x04\x00\x00\x28\x00')
        line_2 = '0000' + tex_width[2:4] + tex_width[0:2] + '0000' + tex_height[2:4] + tex_height[0:2]  + '00000100' + bits_per_pixel + '000000'
        f_write.write(bytearray.fromhex(line_2))
        f_write.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        f_write.write(b'\x00\x00\x00\x00\x00\x00')

        exportColourMap(content, file_size, bits_per_pixel, f_write)
        export8BitColours(content, file_size, f_write, int(tex_height, 16), int(tex_width, 16))
        
        f_write.flush()
        with open(tex_name + '.bmp', mode='rb') as file: # b is important -> binary
            content_2 = file.read()
        file_length = ("0000" + (hex(len(content_2))[2:]))[-4:]
        f_write.seek(2)
        f_write.write(bytearray.fromhex(file_length[2:] + file_length[:2]))
        

    elif content[int('1e', 16):int('20', 16)].hex() == '1000' and content[int('2a', 16):int('2b', 16)].hex() == '40':
        print("4 bit")
        bits_per_pixel = '4'
        bits_per_pixel = ('00' + bits_per_pixel)[-2:]
        f_write = open(tex_name + '.bmp', mode='wb')
        f_write.write(b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00\x76\x00\x00\x00\x28\x00')
        line_2 = '0000' + tex_width[2:4] + tex_width[0:2] + '0000' + tex_height[2:4] + tex_height[0:2]  + '00000100' + bits_per_pixel + '000000'
        f_write.write(bytearray.fromhex(line_2))
        f_write.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00')
        f_write.write(b'\x00\x00\x10\x00\x00\x00')
        entry_point = content[int('1c', 16): int('1e', 16)].hex()
        entry_point = int(entry_point[2:4] + entry_point[0:2], 16) + 16
        colour_entry_point = content[int('10', 16): int('12', 16)].hex()
        colour_entry_point = int(colour_entry_point[2:4] + colour_entry_point[0:2], 16) + 16
        exportColourMap(content, file_size, bits_per_pixel, f_write, colour_entry_point)
        export4BitColours(content, file_size, f_write, int(tex_height, 16), int(tex_width, 16), entry_point)
        #f_write.close()
        f_write.flush()
        with open(tex_name + '.bmp', mode='rb') as file: # b is important -> binary
            content_2 = file.read()
        file_length = ("0000" + (hex(len(content_2))[2:]))[-4:]
        #f_write = open(tex_name + '.bmp', mode='wb')
        f_write.seek(2)
        f_write.write(bytearray.fromhex(file_length[2:] + file_length[:2]))
        
    
    else:
        print("File:", f, "unknown bits per pixel")
        return
    
main()