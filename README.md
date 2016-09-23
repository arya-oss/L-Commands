# Powerful L Commands

Implementation of [L Commands](https://github.com/vicky002/L-Commands)

### Requirements

* Linux Operating System
* Python 2.7
* libgnome2-bin ( for opening file explorer with command )

```
   sudo apt-get install libgnome2-bin
```

### HOW TO SETUP

It is recommended to install this package in [virtualenv](https://virtualenv.pypa.io/en/stable/)
```
	# Install virtualenv
	sudo apt-get install python-virtualenv
	or
	sudo pip install virtualenv

	# create and activate virtualenv

	virtualenv ~/env
	source ~/env/bin/activate

	# To install this package
	git clone https://github.com/rajmani1995/L-Commands.git
	cd L-Commands
	python setup.py install

```

### Contributing

* Fork this repository and create a new branch and commit your changes and send pull request

```
	git clone https://github.com/<username>/L-Commands.git
	git remote add upstream https://github.com/<username>/L-Commands

	# stay updated with master branch
	git pull upstream master
	# create branch, add changes and send PR
	git checkout -b SomeNewFeature
	git commit -m "made some changes"
	git push origin SomeNewFeature
	# Go to repository url and create Pull request
```

## open command
To open any file or directory in Ubuntu

| Command Name | Use | status|
|--------------|:-----:|------:|
|`open filename`| Open a given filename in any editor| done
|`open folder foldername`|Open a given directory in file manager| done

## search command

| Command Name | Uses | status|
|------------|:-------:|-----:|
|`search keyword filename`|Search if the given keyword exist in the filename|done
|`search filename foldername`|Search if the file exists in the given directory|done

## code Command
Working with codes in Shell

| Command Name | use | status|
|--------------|:------:|-----:|
|`code lang filename`| To run any language codes in terminal| pending
|`code c filename`|To run C files | done
|`code cpp filename` | To run cpp files| done
|`code js filename`| To run JavaScript in terminal| done
|`code py filename`| To run python codes in terminal| done
|`code rb filename`| To run ruby codes | done
|`code sh filename`| To run shell scripts | done
|`code go filename`| To run GO codes in terminal| done



## math Command 
| Command Name | Use | Status|
|-------------|:------:|------:|
|math | To perform mathematical operations.| done
|`math add A B`| Addition of Two numbers | done
|`math sub A B`| Subtract two numbers| done
|`math pow A B`| Output A^B | done
|`math bin A` | Converts integer A into Binary number| done
|`math hex A`| Converts Decimal integer to Hex| done
|`math mul A B`|Multiply A * B | done
|`math div A B`| divide A/B | done

## Tests

Pending 

### License

[The MIT License](/LICENSE)


