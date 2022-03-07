# lessons-learned-blog

[![Deploy Blog](https://github.com/lsulak/lessons-learned-blog/actions/workflows/cicd.yml/badge.svg)](https://github.com/lsulak/lessons-learned-blog/actions/workflows/cicd.yml)

This is a source code for my personal [blog](https://lsulak.github.io). It's a static
website powered by [Pelican](https://blog.getpelican.com) with slightly modified
[Flex](https://bit.ly/flex-pelican) theme.

I started this site as a way to capture and share my journey in tech. I blog about
various things I learned, and I'm continuously learning, in tech. I focus on software
engineering with some intersection of data science.

## Build and run locally

Follow these steps if you want to build the blog locally, including installation
of all dependencies:

    # Create and activate virtual env and install dependencies: `./setup.sh`
    # Run `make html && pelican --listen`
    # Visit [http://localhost:8000](http://localhost:8000)

*Note*: optionally also install `gem` and `mdl`
(details [here](https://github.com/markdownlint/markdownlint) for having
a full tooling around the CI. Please see file `.github/workflows/cicd.yml`
and `Makefile` for more details.
