import os


ids = [159311, 319696, 426241, 90155, 213255, 269113, 369503, 330369, 146489, 312192, 90284, 243626, 122962, 417876, 442456,
       491613, 490171, 360564, 385205, 128372, 435081, 4395, 41888, 478393, 443303, 33707, 213935, 266400, 484296, 205776, 230362]


def make_fig():
    f = open('random.txt', 'w')
    f.write('\\begin{longtable}{ccc}\n')
    for i in ids:
        f.write(
            '\\includegraphics[width=.33\\textwidth]{figures/random_256/test_latest/images/%012d_input_image.png}&\n' % i)
        f.write(
            '\\includegraphics[width=.33\\textwidth]{figures/random_256_sig/%012d_siggraph2017.png}&\n' % i)
        f.write(
            '\\includegraphics[width=.33\\textwidth]{figures/random_256/test_latest/images/%012d_synthesized_image.png}\\\\ \n' % i)
    f.write('\\end{longtable}\n')
    f.close()


if __name__ == '__main__':
    make_fig()
