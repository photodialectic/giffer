import click
from moviepy.editor import *

@click.group()
def cli():
    pass

@cli.command()
@click.option('-i', '--inputfile', type=click.Path(exists=True))
@click.option('-o', '--outputfile',  type=click.Path(exists=False))
@click.option('--fps', type=int, default=12, prompt="Frames per second")
@click.option('--resize', type=float, default=1, prompt="Resize, 1 for none")
def convert(inputfile, outputfile, fps, resize):
    clip = (VideoFileClip(inputfile).resize(resize))
    clip.write_gif(outputfile, fps=fps)


#def main(argv):
#    inputfile = ''
#    outputfile= ''
#    fps=12
#    resize=.5
#    helpmsg = 'giffer.py -i <inputfile> -o <outputfile>'
#    try:
#        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile"])
#    except getopt.GetoptError:
#        print helpmsg
#        sys.exit(2)
#    for opt, arg in opts:
#        if opt == '-h':
#            print helpmsg
#            sys.exit()
#        if opt in ("-i", "--ifile"):
#            inputfile = arg
#        elif opt in ("-o", "--ofile"):
#            outputfile = arg
#
#    clip = (VideoFileClip(inputfile).resize(resize))
#    clip.write_gif(outputfile, fps=fps)
#
#if __name__ == "__main__":
#    if len(sys.argv) == 1:
#        print "WTF"
#        sys.exit(2)
#    main(sys.argv[1:])
