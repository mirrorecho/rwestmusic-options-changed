from distutils.core import setup

install_requires = [
    'calliope[development]'
    ]

def main():
    setup(
        author='Randall West',
        author_email='info@randallwest.com',
        install_requires=install_requires,
        name='closely',
        packages=('closely',),
        url='https://github.com/mirrorecho/rwestmusic-options-changed/',
        version='2.0',
        zip_safe=False,
        )

if __name__ == '__main__':
    main()