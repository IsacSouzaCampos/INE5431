"""
INE5431 Sistemas Multimídia
Prof. Roberto Willrich

Aula Prática IV: Compressão de Entropia
"""

from PIL import Image
from Cuif import Cuif


# Inclua aqui sua implementação do método que calcula o MSE
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
        

# Inclua aqui sua implementação do método que calcula o PSNR
def PSNR(ori, dec, b):
    import math
    mse = MSE(ori, dec)
    return math.log10(pow(pow(2, b) - 1, 2) / mse) if mse != 0 else 'Infinite'


if __name__ == "__main__":
    for file_name in ['teste', 'lena']:
        # Leitura da imagem de teste
        img = Image.open(file_name + '.bmp')

        # Indique a matrícula dos alunos do grupo na lista abaixo
        matriculas = [17200449, 18200443, 20104138]

        # Geração do arquivo Cuif.1, converte o arquivo Cuif.1 em BMP, e calcula o PSNR
        cuif1 = Cuif(img, 1, matriculas)
        cuif1.printHeader()
        cuif1.show()
        cuif1.save(file_name + '1.cuif')
        cuif1.saveBMP(file_name + '1.bmp')
        img1 = Image.open(file_name + '1.bmp')
        print('PSNR do CUIF.1: ', PSNR(img, img1, 8))

        cuif2 = Cuif(img, 2, matriculas)
        cuif2.printHeader()
        cuif2.show()
        cuif2.save(file_name + '2.cuif')
        cuif2.saveBMP(file_name + '2.bmp')
        img2 = Image.open(file_name + '2.bmp')
        print('PSNR do CUIF.2: ', PSNR(img, img2, 8))

        cuif3 = Cuif(img, 3, matriculas)
        cuif3.printHeader()
        cuif3.show()
        cuif3.save(file_name + '3.cuif')
        cuif3.saveBMP(file_name + '3.bmp')
        img3 = Image.open(file_name + '3.bmp')
        print('PSNR do CUIF.3: ', PSNR(img, img3, 8))

    print("THE END")
