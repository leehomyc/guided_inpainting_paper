import os


ids = [3, 5, 7, 8, 12, 14, 19, 23, 27, 31,
       38, 39, 40, 42, 46, 47, 48, 50, 51, 54]


def make_fig():
    f = open('face.tex', 'w')
    f.write('\\begin{longtable}{cccc}\n')
    cnt = 0
    for i in ids:

        f.write(
            '\\includegraphics[width=.25\\textwidth]{figures/face/test_latest/images/%06d_input_image.png}&\n' % i)
        if cnt % 2 == 0:
            f.write(
                '\\includegraphics[width=.25\\textwidth]{figures/face/test_latest/images/%06d_synthesized_image.png}&\n' % i)
        else:
            f.write(
                '\\includegraphics[width=.25\\textwidth]{figures/face/test_latest/images/%06d_synthesized_image.png}\\\\ \n' % i)

        cnt += 1
    f.write('\\end{longtable}\n')
    f.close()


if __name__ == '__main__':
    make_fig()
