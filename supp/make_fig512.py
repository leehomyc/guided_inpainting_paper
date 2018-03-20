import os


ids = [245764, 343706, 334977, 417876, 278749, 464251, 458992, 90155, 197022, 139684,
       170739, 374545, 46497, 418281, 360951, 172547, 549390, 565778, 344611, 516677]


def make_fig():
    f = open('random_512.tex', 'w')
    f.write('\\begin{longtable}{cc}\n')
    for i in ids:
        f.write(
            '\\includegraphics[width=.5\\textwidth]{figures/random_512/test_latest/images/%012d_input_image.png}&\n' % i)
        f.write(
            '\\includegraphics[width=.5\\textwidth]{figures/random_512/test_latest/images/%012d_synthesized_image.png}\\\\ \n' % i)
    f.write('\\end{longtable}\n')
    f.close()


if __name__ == '__main__':
    make_fig()
