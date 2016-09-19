import click
from moviepy.editor import *

@click.group()
def cli():
    pass

@cli.command()
@click.option('-i', '--inputfile', type=click.Path(exists=True))
@click.option('-o', '--outputfile',  type=click.Path(exists=False))
@click.option('--fps', type=int, default=24, prompt="Frames per second...")
@click.option('--resize', type=float, default=1, prompt="Reduce size by...")
@click.option('--fuzz', type=int, default=0, prompt="Optimize [0-100]")
def convert(inputfile, outputfile, fps, resize, fuzz):
    clip = (VideoFileClip(inputfile).resize(resize))
    clip.write_gif(outputfile, fps=fps, fuzz=fuzz)


@cli.command()
@click.option('-i', '--inputfile', type=click.Path(exists=True))
@click.option('-o', '--outputfile',  type=click.Path(exists=False))
@click.option('--fps', type=int, default=5, prompt="Frames per second...")
@click.option('--resize', type=float, default=1, prompt="Reduce size by...")
@click.option('--speed', type=float, default=1, prompt="Reduce speed by...")
def loop(inputfile, outputfile, fps, resize, speed):
    clip = (VideoFileClip(inputfile, audio=False).resize(resize).speedx(speed))
    d = clip.duration
    clip = clip.crossfadein(d/2)
    composition = (CompositeVideoClip([clip,
                                       clip.set_start(d/2),
                                       clip.set_start(d)])
                   .subclip(d/2, 3*d/2))
    composition.write_gif(outputfile, fps=fps, fuzz=fuzz)

@cli.command()
@click.option('-i', '--inputfile', type=click.Path(exists=True))
@click.option('-o', '--outputfile',  type=click.Path(exists=False))
@click.option('--fps', type=int, default=12, prompt="Frames per second...")
@click.option('--fuzz', type=int, default=2, prompt="Fuzz...")
@click.option('--resize', type=float, default=1, prompt="Reduce size by...")
def symetrize(inputfile, outputfile, fps, fuzz, resize):
    clip = (VideoFileClip(inputfile, audio=False).resize(resize).fx(time_symetrize))
    clip.write_gif(outputfile, fps=fps, fuzz=fuzz)

def time_symetrize(clip):
    return concatenate([clip, clip.fx( vfx.time_mirror )])
