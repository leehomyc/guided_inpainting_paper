import os


ids = [385029, 532493, 475150, 8211, 188439, 434204, 409630, 372349, 314034,
       122962, 8277, 324614, 532575, 90208, 311394, 163951, 49269, 16502, 32887, 434297]


def make_fig():
    f = open('dh.tex', 'w')
    f.write('\\begin{longtable}{ccc}\n')
    for i in ids:
        f.write(
            '\\includegraphics[width=.33\\textwidth]{figures/coco_inpainting_256_harm_all/test_latest/images/%012d_input_image.jpg}&\n' % i)
        f.write(
            '\\includegraphics[width=.33\\textwidth]{figures/deep_harmonization_test/test_latest/images/%012d_synthesized_image.jpg}&\n' % i)
        f.write(
            '\\includegraphics[width=.33\\textwidth]{figures/coco_inpainting_256_harm_all/test_latest/images/%012d_synthesized_image.jpg}\\\\ \n' % i)
    f.write('\\end{longtable}\n')
    f.close()


if __name__ == '__main__':
    make_fig()
