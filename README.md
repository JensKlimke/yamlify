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

Define data in the files ```data/cars/00001.yaml``` and ```data/cars/00002.yaml```:

``` yaml
make: Toyota
model: Corolla
year: 2020
```

``` yaml
make: Honda
model: Civic
year: 2019
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

Define data in the files ```data/cars/00001.yaml``` and ```data/cars/00002.yaml``` as above.

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

Define data in the files ```data/cars/00001.yaml``` and ```data/cars/00002.yaml``` as above and add data file ```data/persons/john.yaml``` and ```data/persons/jane.yaml```:

``` yaml
name: John Doe
```

``` yaml
name: Jane Smith
```

Define a template file ```templates/template_recursive.j2```:

```
{% for car in data.children.cars.elements %}{{ car.model }}
{% endfor %}
{% for person in data.children.persons.elements %}{{ person.name }}
{% endfor %}
```

The command ```yamlify data/ templates/template_single.j2 -o output.txt -r``` generates the file ```output.txt```:

``` txt
Corolla
Civic

Jane Smith
John Doe

```

**Explanation:** The data is merged from multiple files and added to a data structure with the following structure (and a few more fields):

``` python
{
    'children': {
        'cars': {
            'elements': [
                {'filename': '00001.yaml', 'make': 'Toyota', 'model': 'Corolla', 'year': 2020},
                {'filename': '00002.yaml', 'make': 'Honda', 'model': 'Civic', 'year': 2019}
            ]
        },
        'persons': {
            'elements': [
                {'filename': 'john.yaml', 'name': 'John Doe'},
                {'filename': 'jane.yaml', 'name': 'Jane Smith'}
            ]
        }
    }
}
```

### Scenario 4: Review the data structure

To see the complete data structure, create a template file ```templates/template_structure.j2```:

```
{{ data | json }}
```

Execute the command ```yamlify data/ templates/template_structure.j2 -o output.txt -r ```. This will generate the file ```output.txt``` with the complete data structure in JSON format.

### Scenario 5: Manipulate data before rendering (here: link data)

Create the files ```data/cars/00001.yaml``` and ```data/cars/00002.yaml``` and ```data/cars/00003.yaml```:

``` yaml
make: Toyota
model: Corolla
year: 2020
owner: john
```

``` yaml
make: Honda
model: Civic
year: 2019
owner: jane
```

``` yaml
make: Audi
model: A3
year: 2017
owner: john
```

Create the files ```data/persons/john.yaml``` and ```data/persons/jane.yaml```:

``` yaml
name: John Doe
email: john.doe@example.com
age: 30
```

``` yaml
name: Jane Smith
email: jane.smith@example.com
age: 25
```


Create a module file ```modules/link_refs.py```:

``` python

def process(data):
    # Create index of persons
    data['person_index'] = {}
    for person in data['children']['persons']['elements']:
        data['person_index'][person['key']] = person
    for car in data['children']['cars']['elements']:
        if 'owner' in car and data['person_index'][car['owner']]:
            car['owner'] = data['person_index'][car['owner']]
        else:
            car['owner'] = None
    return data
```

This code reads the persons from the merged data structure and creates a person index (dictionary) using the key field, which is generated from the file name.
Then it iterates over the cars and replaces the owner field with the person object from the index. Within the renderer, the owner is now available as a linked object.

Create a template file ```templates/template_linked.j2```:

```
| Vehicle | Owner |
|---|---|
{% for car in data.children.cars.elements %}|{{ car.make }} {{ car.model }}|{{ car.owner.name }}|
{% endfor %}
```

The command ```yamlify data/ templates/template_linked.j2 -o output.md -r --processor-path modules -p link_refs``` generates the file ```output.md```:

``` markdown
| Vehicle | Owner |
|---|---|
|Toyota Corolla|John Doe|
|Honda Civic|Jane Smith|
|Audi A3|John Doe|
```

The rendered version of the table looks like this:

| Vehicle        | Owner      |
|----------------|------------|
| Toyota Corolla | John Doe   |
| Honda Civic    | Jane Smith |
| Audi A3        | John Doe   |


_To test this scenario, please check the tests folder._

## License

MIT - see LICENSE file
