import sys
import ntpath
import os
import shutil

from pdf2image import convert_from_path;


IMAGE_EXT = '.png'
IMAGE_ID = 'PNG'

def strip_name(path):
    base = ntpath.basename(path)
    return os.path.splitext(base)[0]


def get_paths():
    if (len(sys.argv) == 1):
        print("Please pass input pdf and outdir")
        sys.exit()

    path = sys.argv[1]

    if type == 0 and not os.path.isfile(path):
        print("Valid pdf path is required")
        sys.exit()

    return (path, os.path.dirname(path))


def make_op_dir(path, stripped):
    # Never change this line, if you do you run the risk of
    # wiping the wrong directory === not good
    full = os.path.join(path, stripped)

    if os.path.isdir(full):
        shutil.rmtree(full)

    try:
        os.mkdir(full)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    return full


def num_lpad(i):
    return str(i).zfill(3)


def main():
    (input, output) = get_paths()
    print('Input PDF: ', input)
    input_stripped = strip_name(input)
    full_out_dir = make_op_dir(output, input_stripped)
    print('Output Dir: ', full_out_dir)
    pages = convert_from_path(input, 500)

    for k, page in enumerate(pages, start=1):
        out_file = "{index}_{base}{ext}".format(base=input_stripped,
                                                index=num_lpad(k),
                                                ext=IMAGE_EXT)

        out_path = os.path.join(full_out_dir, out_file)
        page.save(out_path, IMAGE_ID)


if __name__ == '__main__':
    main()
