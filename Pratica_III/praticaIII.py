from PIL import Image
# from Cuif import Cuif


def PSNR(ori, dec):
    import math
    return math.log10(pow(pow(2, 8) - 1, 2) / MSE(ori, dec))


def MSE(ori, dec):
    sum = 0
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))

            diff_r = pow((ori_r - dec_r), 2)
            diff_g = pow((ori_g - dec_g), 2)
            diff_b = pow((ori_b - dec_b), 2)

            sum += (diff_r + diff_g + diff_b)

    return sum / (ori.width * ori.height * 3)


if __name__ == "__main__":
    # img = Image.open("mandril.bmp")
    # matriculas = [17200449, 18200443, 20104138]
    
    # instancia objeto Cuif, convertendo imagem em CUIF.1
    # cuif = Cuif(img, 1, matriculas)
    
    # imprime cabeçalho Cuif
    # cuif.printHeader()
    
    # mostra imagem Cuif
    # cuif.show()
    
    #gera o arquivo Cuif.1
    # cuif.save('mandril1.cuif')
    
    #Abre um arquivo Cuif e gera o objeto Cuif
    # cuif2 = Cuif.openCUIF('mandril1.cuif')
    
    # Converte arquivo Cuif em BMP e mostra
    # cuif2.saveBMP('mandril1.bmp')
    #cuif2.show()

    ori = Image.open("mandril.bmp")
    dec = Image.open("mandril1.bmp")

    result = PSNR(ori, dec)
    
    print("THE END")

