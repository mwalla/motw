import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='character_tracker',
    version='0.13',
    packages=setuptools.find_packages(),
    url='https://github.com/llpk79/motw',
    license='MIT',
    author='Paul Kutrich',
    author_email='pkutrich@gmail.com',
    description='Tracker for Monster of the Week characters',
    long_description=long_description,
    include_package_data=True,
    package_data={
        "character_tracker": ["pickle/*.pkl", "archetypes/*.json"]
    }
)
