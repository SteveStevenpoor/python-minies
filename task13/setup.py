from setuptools import Extension, setup


setup(
    name='foreign',
    version='1.0.0',
    description='Fast powering of matrix',
    author='dbg',
    author_email='eeeevaeee@gmail.com',
    ext_modules=[
        Extension(
            name='foreign',
            sources=['matrix_pow.c']
        )
    ]
)
