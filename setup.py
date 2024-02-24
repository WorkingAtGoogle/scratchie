from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='scratchie',
    url='https://github.com/WorkingAtGoogle/scratchie',
    author='Vihar Modugula',
    author_email='vihar2408@gmail.com',
    # Needed to actually package something
    packages=['scratchie'],
    # Needed for dependencies
    dynamic=['pyttsx3'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    dynamic='MIT',
    description='Scratchie is an amazing library for when converting from scratch to python. It has similar syntax to scrath in order to help kids to convert to text-based programming quickly.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.md').read(),
)
