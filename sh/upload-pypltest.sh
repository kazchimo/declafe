rm -f -r declafe.egg-info/* dist/*

python setup.py sdist bdist_wheel

twine upload --repository testpypi dist/*
