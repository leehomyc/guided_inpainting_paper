import os


ids = [5037, 95843, 423617, 255965, 98839,
       300276, 309467, 190007, 355905, 29393]


def make_fig():
    f = open('guided.tex', 'w')
    f.write('\\begin{longtable}{cccc}\n')

    for i in ids:
        f.write(
            '\\includegraphics[width=.25\\textwidth]{figures/gi/images/%012d_input.jpg}&\n' % i)
        f.write(
            '\\includegraphics[width=.25\\textwidth]{figures/gi/images/%012d_mask.jpg}&\n' % i)
        f.write(
            '\\includegraphics[width=.25\\textwidth]{figures/gi/images/%012d_inpainting.jpg}&\n' % i)
        f.write(
            '\\includegraphics[width=.25\\textwidth]{figures/gi/images/%012d_inpainting_harmonization.jpg}\\\\ \n' % i)
    f.write('\\end{longtable}\n')
    f.close()


if __name__ == '__main__':
    make_fig()
