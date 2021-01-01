import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='character_tracker',
    version='0.4',
    packages=['character_tracker'],
    url='https://github.com/llpk79/motw',
    license='MIT',
    author='Paul Kutrich',
    author_email='pkutrich@gmail.com',
    description='Tracker for Moster of the Week characters',
    long_description=long_description,
    include_package_data=True,
)
