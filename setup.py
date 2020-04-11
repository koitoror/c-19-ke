from setuptools import setup, find_packages


# setup(name="covid19-estimator-py", packages='requirements.txt')
setup(
    name="covid19-estimator-py", 
    packages=find_packages(),  
    install_requires=[
        'flask', 
        'flask-restplus',
        'dicttoxml',
        'werkzeug==0.16.1'
        ])
