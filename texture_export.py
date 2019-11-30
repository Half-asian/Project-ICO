#TM2 to bitmap
import sys
import os
import png

def exportColourMap(content, file_size, colour_bits, entry_point):
    colour_maps = []
    if colour_bits == '04':
        for i in range(64, 0, -4):
            current_colour = content[entry_point - i:entry_point - i + 4].hex()
            current_colour = current_colour[4:6] + current_colour[2:4] + current_colour[0:2] + '00'
            binary = bytearray.fromhex(current_colour)
            #f_write.write(binary)
            colour_maps.append(content[entry_point - i:entry_point - i + 4].hex())
    
    elif colour_bits == '08':
        for i in range(1024, 0, -128): #8 x 128 bit chunks
            block1 = content[entry_point - i:entry_point - i + 32].hex()
            block2 = content[entry_point - i + 32:entry_point - i + 64].hex()
            block3 = content[entry_point - i + 64:entry_point - i + 96].hex()
            block4 = content[entry_point - i + 96:entry_point - i + 128].hex()

            for colour in range(0, 64, 8): #block1
                binary = block1[colour + 4:colour + 6] + block1[colour + 2:colour + 4] + block1[colour:colour + 2] + '00'
                binary = bytearray.fromhex(binary)
                #f_write.write(binary)
                colour_maps.append(block1[colour: colour + 8])
            for colour in range(0, 64, 8): #block3
                binary = block3[colour + 4:colour + 6] + block3[colour + 2:colour + 4] + block3[colour:colour + 2] + '00'
                binary = bytearray.fromhex(binary)
                #f_write.write(binary)
                colour_maps.append(block3[colour: colour + 8])

            for colour in range(0, 64, 8): #block2
                binary = block2[colour + 4:colour + 6] + block2[colour + 2:colour + 4] + block2[colour:colour + 2] + '00'
                binary = bytearray.fromhex(binary)
                #f_write.write(binary)
                colour_maps.append(block2[colour: colour + 8])

            for colour in range(0, 64, 8): #block4
                binary = block4[colour + 4:colour + 6] + block4[colour + 2:colour + 4] + block4[colour:colour + 2] + '00'
                binary = bytearray.fromhex(binary)
                #f_write.write(binary)
                colour_maps.append(block4[colour: colour + 8])

    return colour_maps
             
def export4BitColours(content, file_size, y_count, x_count, entry_point):
    if y_count == 32 and x_count == 32:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 512]
        for x in range(16):
            offset = x * 32
            block_1 = buffer[offset: offset + 16].hex()
            block_2 = buffer[offset + 16: offset + 32].hex()
            blocks = [block_1, block_2]
            for i in blocks:    
                l = i
                l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices
    
    elif y_count == 64 and x_count == 64:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 2048]
        for x in range(32):
            offset = x * 64

            block_1 = buffer[offset: offset + 16].hex()
            block_2 = buffer[offset + 16: offset + 32].hex()
            block_3 = buffer[offset + 32: offset + 48].hex()
            block_4 = buffer[offset + 48: offset + 64].hex()
            blocks = [block_1, block_2, block_3, block_4]
            for i in blocks:    
                l = i
                l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices
    
    elif y_count == 64 and x_count == 128:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 4096]
        for x in range(64):
            offset = x * 64

            block_1 = buffer[offset: offset + 16].hex()
            block_2 = buffer[offset + 16: offset + 32].hex()
            block_3 = buffer[offset + 32: offset + 48].hex()
            block_4 = buffer[offset + 48: offset + 64].hex()
            blocks = [block_1, block_2, block_3, block_4]
            for i in blocks:    
                l = i
                l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices
        
    elif y_count == 128 and x_count == 128:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 8192]
        for x in range(128):
            offset = x * 64
            
            block_1 = buffer[offset:offset+16].hex()
            block_2 = buffer[offset+16:offset+32].hex()
            block_3 = buffer[offset+32:offset+48].hex()
            block_4 = buffer[offset+48:offset+64].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                l = l[1] + l[0] + l[3] + l[2] + l[5] + l[4] + l[7] + l[6] + l[9] + l[8] + l[11] + l[10] + l[13] + l[12] + l[15] + l[14] + l[17] + l[16] + l[19] + l[18] + l[21] + l[20] + l[23] + l[22] + l[25] + l[24] + l[27] + l[26] + l[29] + l[28] + l[31] + l[30]
                pixel_indices += l
                #f_write.write(bytearray.fromhex(l))
        return pixel_indices

    
    elif y_count == 128 and x_count == 256:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 16384]
        for x in range(128):
            offset = x * 128
            block_1 = buffer[offset: offset + 32].hex()
            block_2 = buffer[offset + 32: offset + 64].hex()
            block_3 = buffer[offset + 64: offset + 96].hex()
            block_4 = buffer[offset + 96: offset + 128].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                temp = ""
                for a in range(0, 64, 2):
                    temp += l[a + 1] + l[a]
                l = temp
                pixel_indices += l
                #f_write.write(bytearray.fromhex(l))
        return pixel_indices
                
    elif y_count == 256 and x_count == 256:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 32768]
        for x in range(256):
            offset = x * 128
            block_1 = buffer[offset: offset + 32].hex()
            block_2 = buffer[offset + 32: offset + 64].hex()
            block_3 = buffer[offset + 64: offset + 96].hex()
            block_4 = buffer[offset + 96: offset + 128].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                temp = ""
                for a in range(0, 64, 2):
                    temp += l[a + 1] + l[a]
                l = temp
                pixel_indices += l
                #f_write.write(bytearray.fromhex(l))
        return pixel_indices
    
    elif y_count == 512 and x_count == 512:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 65536]
        for x in range(512):
            offset = x * 256
            block_1 = buffer[offset: offset + 64].hex()
            block_2 = buffer[offset + 64: offset + 128].hex()
            block_3 = buffer[offset + 128: offset + 192].hex()
            block_4 = buffer[offset + 192: offset + 256].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                temp = ""
                for a in range(0, 128, 2):
                    temp += l[a + 1] + l[a]
                l = temp
                pixel_indices += l
                #f_write.write(bytearray.fromhex(l))
        return pixel_indices

    else:
        print("Unknown Y length:", y_count)
        print("Unknown X length:", x_count)


                
def export8BitColours(content, file_size, y_count, x_count, entry_point):
    
    if y_count == 64 and x_count == 64:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 4096]
        
        for x in range(64):
            offset = x * 64
            block_1 = buffer[offset: offset + 16].hex()
            block_2 = buffer[offset + 16: offset + 32].hex()
            block_3 = buffer[offset + 32: offset + 48].hex()
            block_4 = buffer[offset + 48: offset + 64].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices [:-2]

    elif y_count == 64 and x_count == 128:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 8192]
        for x in range(64):
            offset = x * 128
            block_1 = buffer[offset: offset + 32].hex()
            block_2 = buffer[offset + 32: offset + 64].hex()
            block_3 = buffer[offset + 64: offset + 96].hex()
            block_4 = buffer[offset + 96: offset + 128].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices [:-2]
    
    elif y_count == 64 and x_count == 256:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 16384]
        for x in range(64):
            offset = x * 256
            block_1 = buffer[offset: offset + 64].hex()
            block_2 = buffer[offset + 64: offset + 128].hex()
            block_3 = buffer[offset + 128: offset + 192].hex()
            block_4 = buffer[offset + 192: offset + 256].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices [:-2]
    
    elif y_count == 128 and x_count == 128:
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 16384]
        for x in range(128):
            offset = x * 128
            block_1 = buffer[offset: offset + 32].hex()
            block_2 = buffer[offset + 32: offset + 64].hex()
            block_3 = buffer[offset + 64: offset + 96].hex()
            block_4 = buffer[offset + 96: offset + 128].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices [:-2]
    
    
    elif y_count == 256 and x_count == 256: #WIP
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 65536]
        for x in range(256):
            offset = x * 256         
            block_1 = buffer[offset: offset + 64].hex()
            block_2 = buffer[offset + 64: offset + 128].hex()
            block_3 = buffer[offset + 128: offset + 192].hex()
            block_4 = buffer[offset + 192: offset + 256].hex()

            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices [:-2]
                
    elif y_count == 512 and x_count == 512: #WIP
        pixel_indices = ""
        buffer = content[entry_point:entry_point + 262144]
        for x in range(512):
            offset = x * 512           
            block_1 = buffer[offset: offset + 128].hex()
            block_2 = buffer[offset + 128: offset + 256].hex()
            block_3 = buffer[offset + 256: offset + 384].hex()
            block_4 = buffer[offset + 384: offset + 512].hex()
            
            blocks = [block_1, block_2, block_3, block_4]

            for i in blocks:    
                l = i
                #f_write.write(bytearray.fromhex(l))
                pixel_indices += l
        return pixel_indices [:-2]

def main(f):
    #f = 'op_tsuta.tm2'
    with open(f, mode='rb') as file:
        content = file.read()
    file_size = os.path.getsize(f)
    tex_name = f[:-4]

    tex_width = content[int('24', 16):int('26', 16)].hex()
    tex_width = tex_width[2:4] + tex_width[0:2]

    tex_height = content[int('26', 16):int('28', 16)].hex()
    tex_height = tex_height[2:4] + tex_height[0:2]



    if content[int('1e', 16):int('20', 16)].hex() == '0001' and content[int('2a', 16):int('2b', 16)].hex() == '30':
        #print("8 bit")
        bits_per_pixel = '8'
        bits_per_pixel = ('00' + bits_per_pixel)[-2:]
        #f_write = open(tex_name + '.bmp', mode='wb')
        #f_write.write(b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00\x36\x04\x00\x00\x28\x00')
        line_2 = '0000' + tex_width[2:4] + tex_width[0:2] + '0000' + tex_height[2:4] + tex_height[0:2]  + '00000100' + bits_per_pixel + '000000'
        #f_write.write(bytearray.fromhex(line_2))
        #f_write.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        #f_write.write(b'\x00\x00\x00\x00\x00\x00')
        entry_point = content[int('1c', 16): int('1e', 16)].hex()
        entry_point = int(entry_point[2:4] + entry_point[0:2], 16) + 16
        colour_entry_point = content[int('10', 16): int('14', 16)].hex()
        colour_entry_point = int(colour_entry_point[6:8] + colour_entry_point[4:6] + colour_entry_point[2:4] + colour_entry_point[0:2] , 16) + 16
        colour_maps = exportColourMap(content, file_size, bits_per_pixel, colour_entry_point)
        pixel_indices = export8BitColours(content, file_size, int(tex_height, 16), int(tex_width, 16), entry_point)
        #f_write.flush()
        #with open(tex_name + '.bmp', mode='rb') as file: # b is important -> binary
        #    content_2 = file.read()
        #file_length = ("0000" + (hex(len(content_2))[2:]))[-4:]
        #f_write.seek(2)
        #f_write.write(bytearray.fromhex(file_length[2:] + file_length[:2]))
        pixels = []
        current_line = []
        new_pixel_indices = []
        for i in range(0, len(pixel_indices), 2):
            new_pixel_indices.append(pixel_indices[i:i+2])    
        
        
        
        for indice in new_pixel_indices:
            red = int(colour_maps[int(indice, 16)][0:2], 16)
            green = int(colour_maps[int(indice, 16)][2:4], 16)
            blue = int(colour_maps[int(indice, 16)][4:6], 16)
            alpha = int(colour_maps[int(indice, 16)][6:8], 16)
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            current_line.append(red)
            current_line.append(green)
            current_line.append(blue)
            alpha = alpha * 2 - 1
            if alpha > 255:
                alpha = 255
            if alpha < 0:
                alpha = 0
            current_line.append(alpha)
            if len(current_line) == int(tex_width, 16) * 4:
                pixels.append(current_line)
                current_line = []
        png.from_array(pixels, 'RGBA').save(tex_name + '.png')
        

    elif content[int('1e', 16):int('20', 16)].hex() == '1000' and content[int('2a', 16):int('2b', 16)].hex() == '40':
        #print("4 bit")
        bits_per_pixel = '4'
        bits_per_pixel = ('00' + bits_per_pixel)[-2:]
        #f_write = open(tex_name + '.bmp', mode='wb')
        #f_write.write(b'\x42\x4d\x00\x00\x00\x00\x00\x00\x00\x00\x76\x00\x00\x00\x28\x00')
        line_2 = '0000' + tex_width[2:4] + tex_width[0:2] + '0000' + tex_height[2:4] + tex_height[0:2]  + '00000100' + bits_per_pixel + '000000'
        #f_write.write(bytearray.fromhex(line_2))
        #f_write.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00')
        #f_write.write(b'\x00\x00\x10\x00\x00\x00')
        entry_point = content[int('1c', 16): int('1e', 16)].hex()
        entry_point = int(entry_point[2:4] + entry_point[0:2], 16) + 16
        colour_entry_point = content[int('10', 16): int('12', 16)].hex()
        colour_entry_point = int(colour_entry_point[2:4] + colour_entry_point[0:2], 16) + 16
        colour_maps = exportColourMap(content, file_size, bits_per_pixel, colour_entry_point)
        pixel_indices = export4BitColours(content, file_size, int(tex_height, 16), int(tex_width, 16), entry_point)
        #f_write.flush()
        #with open(tex_name + '.bmp', mode='rb') as file: # b is important -> binary
        #    content_2 = file.read()
        #file_length = ("0000" + (hex(len(content_2))[2:]))[-4:]
        #f_write.seek(2)
        #f_write.write(bytearray.fromhex(file_length[2:] + file_length[:2]))
        
        pixels = []
        current_line = []
        for indice in pixel_indices:
            red = int(colour_maps[int(indice, 16)][0:2], 16)
            green = int(colour_maps[int(indice, 16)][2:4], 16)
            blue = int(colour_maps[int(indice, 16)][4:6], 16)
            alpha = int(colour_maps[int(indice, 16)][6:8], 16)
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            current_line.append(red)
            current_line.append(green)
            current_line.append(blue)
            alpha = alpha * 2 - 1
            if alpha > 255:
                alpha = 255
            if alpha < 0:
                alpha = 0
            current_line.append(alpha)
            if len(current_line) == int(tex_width, 16) * 4:
                pixels.append(current_line)
                current_line = []
        png.from_array(pixels, 'RGBA').save(tex_name + '.png')
        
    
    else:
        print("File:", f, "unknown bits per pixel")
        return
    
#main()
