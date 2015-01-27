'A Makefile replacement'

from fabric.api import local

build_cmd = 'sphinx-build -b {0} {1} . _output/{0}'
clean_cmd = 'rm -rf _output/{}'
# This redirection failed to suppress output. Dont't know why
# show_cmd = 'xdg-open _output/{} >& /dev/null &'
show_cmd = 'xdg-open _output/{} > /dev/null  2>&1 &'


def build(builder='html', options=''):
    outdir = '_output/{}'.format(builder)
    build_cmd = 'sphinx-build -b {builder} {options} . {outdir}'
    local(build_cmd.format(**vars()))


def latex(pdf='contents', options=''):
    outdir = '_output/latex'
    build('latex', options)
    if pdf:
        local('cd {} && xelatex {}.tex'.format(outdir, pdf))
        show(file='latex/{}.pdf'.format(pdf))


def showpdf(pdf='contents'):
    show(file='latex/{}.pdf'.format(pdf))


def clean(builder='html'):
    local(clean_cmd.format(builder))


def show(file='html/contents.html'):
    local(show_cmd.format(file))
