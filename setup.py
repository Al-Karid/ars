import setuptools

setuptools.setup(
    name="ars",
    version="0.0.1",
    author="Gren CISSE Al-Karid",
    author_email="grencisse@gmail.com",
    description="AlloCine.fr scrapping and recommander system toolkits",
    packages=setuptools.find_packages(),
    include_package_data = True,
    install_requires=[
        "click==7.0",
        "pandas==1.0.1",
        "beautifulsoup4==4.8.2",
        "requests==2.21.0",
        "flask==1.1.1",
        "scikit-learn==0.22.2.post1"
        ],
    entry_points='''
    [console_scripts]
    ars=ars.cli:ars
    '''
)