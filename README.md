# Yamlify Me

Yamlify Me is a document generation tool and python library, which combines yaml and Jinja2.

It includes:

* Read data from multiple files in a folder.
* Read data recursively from subfolders.
* Manipulate data after reading and before rendering.
* Render data with a jinja template file to generate a document.
* Render data with multiple jinja template files to generate multiple documents

## Usage

```bash
> yamlify --help
```

## I a nutshell

### Scenario 1: Creating multiple doc files from multiple data files

Define data in a file ```data/cars/00001.yaml``` and ```data/cars/00002.yaml```:

``` yaml
make: Toyota
model: Corolla
year: 2020
owner: persons/john
```

``` yaml
make: Honda
model: Civic
year: 2019
owner: persons/jane
```

Define a template file ```templates/template_multi.j2```:

```
{{ make }} {{ model }} {{ year }} {{ filename }}
```

The command ```yamlify data/cars/ templates/template_multi.j2 -f {make}.txt```generates the file ```Toyota.txt``` and ```Honda.txt```:

``` txt
Toyota Corolla 2020 00001.yaml
```

``` txt
Honda Civic 2019 00002.yaml
```

_To test this scenario, please check the tests folder._

### Scenario 2: Creating a single doc file from multiple data files

Define data in a file ```data/cars/00001.yaml``` and ```data/cars/00002.yaml``` as above.

Define a template file ```templates/template_single.j2```:

```
{% for car in data %}{{ car.make }} {{ car.model }} {{ car.year }} {{ car.filename }}
{% endfor %}
```

The command ```yamlify data/cars/ templates/template_single.j2 -o output.txt``` generates the file ```output.txt```:

``` txt
Toyota Corolla 2020 00001.yaml
Honda Civic 2019 00002.yaml

```

_To test this scenario, please check the tests folder._

### Scenario 3: Creating a single doc file from multiple data files with recursive subfolders

Define data in a file ```data/cars/00001.yaml``` and ```data/cars/00002.yaml``` as above.

Define a template file ```templates/template_single.j2```:

```
{% for car in data.children.cars.elements %}{{ car.model }}
{% endfor %}
```

The command ```yamlify data/ templates/template_single.j2 -o output.txt -r``` generates the file ```output.txt```:

``` txt
Corolla
Civic

```

_To test this scenario, please check the tests folder._

## License

MIT - see LICENSE file
