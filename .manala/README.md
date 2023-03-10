---
title: Lazy - Ansible
tableOfContent: 3
---

## Requirements

* [Manala CLI](https://manala.github.io/manala/installation/) to update the recipe
* Make
* Docker Desktop 2.2.0+ or Docker Engine + Docker Compose

## Usage

### Shell

Open a shell to container
```shell
make sh
```

Run commands through container shell
```shell
# From file
make sh < file
# Multilines, using heredoc
make sh << 'EOF'
command 1
command 2
...
EOF
# Single line
make sh <<< command
```

Specify working dir
```shell
make sh DIR=/etc <<< pwd
/etc
```

Expose a container port 4321 on localhost:1234
```shell
make sh PORT=1234:4321
```

### Makefile

One of the first directive of your project's Makefile should be to include manala recipe `Makefile`
```makefile
include .manala/Makefile
```

Or, if you're not sure manala recipe directory will be present, make it optional. If you do make it optionnal, you'll have to ensure that every parts of you project's Makefile using manala recipe tools could fallback to another solution.
```makefile
-include .manala/Makefile
```

Note: it's a good practise to have a `.SILENT:` as the first line of your project's Makefile. Not only does it globally silence make targets echoing, but it also offers a lowcost debugging system by just commenting it on demand.
```makefile
.SILENT:
```
```makefile
#.SILENT:
```

A `MANALA_DOCKER` variable is available to check whether you're inside the container or not
```makefile
foo:
ifdef MANALA_DOCKER
	echo Inside container
else
	echo Outside container
endif
```

A `MANALA_DIR` variable is available to get your project's directory *inside* container
```makefile
foo:
	echo Project directory is $(MANALA_DIR)
```

There are three ways to force your project's Makefile target execution inside container:

1. Function `manala_docker_shell`

```makefile
foo:
	echo Can be run *inside* or *outside* container
	$(call manala_docker_shell, echo Always run *inside* container)
```

2. Shell substitution with `MANALA_DOCKER_SHELL`

```makefile
foo: SHELL := $(MANALA_DOCKER_SHELL)
foo:
	echo Always run *inside* container

# Or, if you're not sure manala recipe "Makefile" will be included
foo: SHELL := $(or $(MANALA_DOCKER_SHELL),$(SHELL))
foo:
	echo Can be run *inside* or *outside* container, \
		but always *inside* if manala recipe "Makefile" is included
```

3. Make substitution with `MANALA_DOCKER_MAKE`

```makefile
foo:
	$(MANALA_DOCKER_MAKE) bar

bar:
	echo Run *outside* container if called directly \
		or *inside* container if called from "foo"
```

An automagic target help system is included out-of-the-box. You can list all available documented commands with `make help` (or just `make`,  as the help command is the default one)

```shell
$ make

Usage: make [command]

Help:
  help This help

System:
  sh    Open a local system shell
  clean Clean local system
```

You can add your own documented commands, by adding double dashed comments in your projects's Makefile
```makefile
## This is foo
foo:
	...

## Bar - Use the "Bar" help section
bar.baz:
	...
```

```shell
$ make

Usage: make [command]

Help:
  help This help

System:
  sh    Open a local system shell
  clean Clean local system

Commands:
  foo This is foo

Bar:
  bar.baz Use the "Bar" help section
```
