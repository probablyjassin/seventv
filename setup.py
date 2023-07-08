from setuptools import setup

setup(
    name='seventv',
    version='1.2.1',
    author='Jässin Aouani',
    author_email='jassin@aouani.de',
    description='An asynchronous API-wrapper for 7tv.app',
    long_description = """
        An asynchronous Python API-wrapper for 7tv.app. 
        It makes use of the 7tv API (v3) to make it possible to get emotes, details about them, and soon some more things the API supports.
        To get emotes by search query, the wrapper uses the GraphQL endpoint 
        https://7tv.io/v3/gql because it seems to currently be the only working one for searching emotes.
    """,
    packages=['seventv'],
    install_requires=['aiohttp'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
