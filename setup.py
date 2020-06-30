import setuptools

setuptools.setup(
    name='mkcache',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/mkcache']
)
