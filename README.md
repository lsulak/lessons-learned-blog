# lessons-learned-blog

[![Deploy Blog](https://github.com/lsulak/lessons-learned-blog/actions/workflows/cicd.yml/badge.svg)](https://github.com/lsulak/lessons-learned-blog/actions/workflows/cicd.yml)

This is a source code for my personal [blog](https://lsulak.github.io). It's a static
website powered by [Pelican](https://blog.getpelican.com) with slightly modified
[Flex](https://bit.ly/flex-pelican) theme.

I started this site as a way to capture and share my journey in tech. I blog about
various things I learned and experienced, mostly focusing on **software
engineering with some intersection of data science**.

## Build And Run Locally

If you want to build the blog locally, including installation
of all dependencies, please follow these steps:

1. Create and activate virtual env and install dependencies: `./setup.sh`
1. Run `make html && pelican --listen`
1. Visit [http://localhost:8000](http://localhost:8000)

*Note*: optionally also install `gem` and `mdl`
(details [here](https://github.com/markdownlint/markdownlint) for having
a full tooling around the CI. Please see file `.github/workflows/cicd.yml`
and `Makefile` for more details.
